"""
External integrations for ClawedBot
"""

from .telegram_notifier import TelegramNotifier
from .tradingview_webhook import WebhookServer

__all__ = ['TelegramNotifier', 'WebhookServer']
