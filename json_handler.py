import pandas as pd
import datetime as dt
import json


def json_to_df(response):
    res = json.loads(response)
    df = pd.DataFrame(res['result'])

    df['ticks'] = df.ticks/1000
    df['timestamp'] = [dt.datetime.utcfromtimestamp(date) for date in df.ticks]

    return df


