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
#client.order(instrument_name="BTC-PERPETUAL", side="long", amount=50000, order_type="market")
#client.close_position(instrument="BTC-PERPETUAL", order_type = "limit")


res = client.get_open_orders()
print(res)


