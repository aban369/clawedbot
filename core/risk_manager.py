"""
Risk Management System
Handles position sizing, stop losses, and risk limits
"""

import logging
from typing import Dict, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class RiskManager:
    """Manage trading risk and position sizing"""
    
    def __init__(self, config):
        """
        Initialize risk manager
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.daily_pnl = 0.0
        self.daily_trades = 0
        self.open_positions = {}
        self.daily_reset_time = datetime.now().date()
        
        logger.info("✅ Risk Manager initialized")
    
    def calculate_position_size(self, account_balance: float, risk_per_trade: float,
                               entry_price: float, stop_loss_price: float) -> float:
        """
        Calculate position size based on risk
        
        Args:
            account_balance: Total account balance
            risk_per_trade: Risk percentage per trade (0.02 = 2%)
            entry_price: Entry price
            stop_loss_price: Stop loss price
            
        Returns:
            Position size in base currency
        """
        # Calculate risk amount in dollars
        risk_amount = account_balance * risk_per_trade
        
        # Calculate price difference (risk per unit)
        price_diff = abs(entry_price - stop_loss_price)
        
        if price_diff == 0:
            logger.warning("Stop loss price equals entry price")
            return 0
        
        # Calculate position size
        position_size = risk_amount / price_diff
        
        # Apply maximum position size limit
        max_position = self.config.MAX_POSITION_SIZE
        if position_size > max_position:
            logger.warning(f"Position size {position_size} exceeds max {max_position}")
            position_size = max_position
        
        logger.info(f"Calculated position size: {position_size:.4f}")
        return position_size
    
    def check_daily_loss_limit(self) -> bool:
        """
        Check if daily loss limit has been reached
        
        Returns:
            True if trading is allowed, False if limit reached
        """
        # Reset daily counters if new day
        current_date = datetime.now().date()
        if current_date > self.daily_reset_time:
            self.daily_pnl = 0.0
            self.daily_trades = 0
            self.daily_reset_time = current_date
            logger.info("Daily counters reset")
        
        # Check daily loss limit
        max_daily_loss = self.config.MAX_DAILY_LOSS
        if self.daily_pnl < -max_daily_loss:
            logger.warning(f"⚠️ Daily loss limit reached: {self.daily_pnl:.2%}")
            return False
        
        return True
    
    def check_max_positions(self) -> bool:
        """
        Check if maximum number of positions is reached
        
        Returns:
            True if can open new position, False otherwise
        """
        max_positions = self.config.MAX_OPEN_POSITIONS
        current_positions = len(self.open_positions)
        
        if current_positions >= max_positions:
            logger.warning(f"⚠️ Max positions reached: {current_positions}/{max_positions}")
            return False
        
        return True
    
    def can_open_position(self, symbol: str) -> bool:
        """
        Check if a new position can be opened
        
        Args:
            symbol: Trading pair
            
        Returns:
            True if position can be opened
        """
        # Check if already have position in this symbol
        if symbol in self.open_positions:
            logger.warning(f"Already have open position in {symbol}")
            return False
        
        # Check daily loss limit
        if not self.check_daily_loss_limit():
            return False
        
        # Check max positions
        if not self.check_max_positions():
            return False
        
        return True
    
    def calculate_stop_loss(self, entry_price: float, side: str, 
                           stop_loss_pct: float = None) -> float:
        """
        Calculate stop loss price
        
        Args:
            entry_price: Entry price
            side: 'buy' or 'sell'
            stop_loss_pct: Stop loss percentage (default from config)
            
        Returns:
            Stop loss price
        """
        if stop_loss_pct is None:
            stop_loss_pct = self.config.DEFAULT_STOP_LOSS
        
        if side.lower() == 'buy':
            stop_loss = entry_price * (1 - stop_loss_pct)
        else:
            stop_loss = entry_price * (1 + stop_loss_pct)
        
        return stop_loss
    
    def calculate_take_profit(self, entry_price: float, side: str,
                             take_profit_pct: float = None) -> float:
        """
        Calculate take profit price
        
        Args:
            entry_price: Entry price
            side: 'buy' or 'sell'
            take_profit_pct: Take profit percentage (default from config)
            
        Returns:
            Take profit price
        """
        if take_profit_pct is None:
            take_profit_pct = self.config.DEFAULT_TAKE_PROFIT
        
        if side.lower() == 'buy':
            take_profit = entry_price * (1 + take_profit_pct)
        else:
            take_profit = entry_price * (1 - take_profit_pct)
        
        return take_profit
    
    def add_position(self, symbol: str, side: str, entry_price: float,
                    size: float, stop_loss: float, take_profit: float):
        """Add a new position to tracking"""
        self.open_positions[symbol] = {
            'side': side,
            'entry_price': entry_price,
            'size': size,
            'stop_loss': stop_loss,
            'take_profit': take_profit,
            'entry_time': datetime.now(),
            'pnl': 0.0
        }
        
        logger.info(f"✅ Position added: {side} {size} {symbol} @ {entry_price}")
    
    def remove_position(self, symbol: str, exit_price: float):
        """Remove position and update PnL"""
        if symbol not in self.open_positions:
            logger.warning(f"Position {symbol} not found")
            return
        
        position = self.open_positions[symbol]
        
        # Calculate PnL
        if position['side'].lower() == 'buy':
            pnl = (exit_price - position['entry_price']) * position['size']
        else:
            pnl = (position['entry_price'] - exit_price) * position['size']
        
        # Update daily PnL
        self.daily_pnl += pnl
        self.daily_trades += 1
        
        logger.info(f"✅ Position closed: {symbol} | PnL: ${pnl:.2f}")
        
        del self.open_positions[symbol]
    
    def update_trailing_stop(self, symbol: str, current_price: float) -> Optional[float]:
        """
        Update trailing stop loss
        
        Args:
            symbol: Trading pair
            current_price: Current market price
            
        Returns:
            New stop loss price or None
        """
        if symbol not in self.open_positions:
            return None
        
        if not self.config.TRAILING_STOP:
            return None
        
        position = self.open_positions[symbol]
        trailing_distance = self.config.TRAILING_STOP_DISTANCE
        
        if position['side'].lower() == 'buy':
            # For long positions, move stop up
            new_stop = current_price * (1 - trailing_distance)
            if new_stop > position['stop_loss']:
                position['stop_loss'] = new_stop
                logger.info(f"Trailing stop updated for {symbol}: {new_stop:.4f}")
                return new_stop
        else:
            # For short positions, move stop down
            new_stop = current_price * (1 + trailing_distance)
            if new_stop < position['stop_loss']:
                position['stop_loss'] = new_stop
                logger.info(f"Trailing stop updated for {symbol}: {new_stop:.4f}")
                return new_stop
        
        return None
    
    def get_risk_summary(self) -> Dict:
        """Get risk management summary"""
        return {
            'daily_pnl': self.daily_pnl,
            'daily_trades': self.daily_trades,
            'open_positions': len(self.open_positions),
            'max_positions': self.config.MAX_OPEN_POSITIONS,
            'daily_loss_limit': self.config.MAX_DAILY_LOSS,
            'positions': self.open_positions
        }
