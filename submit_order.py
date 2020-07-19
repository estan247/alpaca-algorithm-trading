#Submiting a a bracket order using Alpaca Api
import alpaca_trade_api as tradeapi
import requests
from bs4 import BeautifulSoup


APCA_API_BASE_URL = ''
APCA_API_KEY_ID = ''
APCA_API_SECRET_KEY = ''

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL, api_version='v2')

STOCK = 'AAPL'

api.submit_order(
    symbol=STOCK,
    qty=10,
    side='buy',
    type='market',
    time_in_force='day',
    order_class='bracket',
    take_profit=dict(
        limit_price=400,
    ),
    stop_loss=dict(
        stop_price=300,
        limit_price=300,
    ),
)
