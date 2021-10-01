from api_client import Client
import asyncio
import websockets
import json
from call_api import call_api
from call_api import call_api_private
from historical_data import *
import time
import datetime as dt
import pandas as pd


client = Client()
result = client.get_order_book(instrument='BTC-PERPETUAL', depth=1000)
bid = result['bids']
ask = result['asks']
print("bid, length {}:\n{}".format(len(bid),bid))
print("ask, length {}:\n{}".format(len(ask),ask))


