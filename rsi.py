from os import utime
import telegram

bot = telegram.Bot(token='1811677602:AAFGUEGeoZb4SyzNDS_e9CtvHf3QnZlWrxA')  ####자기 TELEGRAM API와 ID를 입력해준다
chat_id = 1781176234  ## 숫자만 입력

import requests
import pandas as pd
import time
import webbrowser
import numpy as np

a = 1

while True:

    def rsiindex(symbol):
        url = "https://api.upbit.com/v1/candles/minutes/1"  #### minutes 뒤에 원하는 분 설정을 넣으면 된다 기본적으로 3분으로 설정

        querystring = {"market": symbol, "count": "500"}

        response = requests.request("GET", url, params=querystring)

        data = response.json()

        df = pd.DataFrame(data)

        df = df.reindex(index=df.index[::-1]).reset_index()

        df['close'] = df["trade_price"]

        global a

        if a == 1:
            a = 2

        def rsi(ohlc: pd.DataFrame, period: int = 14):
            ohlc["close"] = ohlc["close"]
            delta = ohlc["close"].diff()

            up, down = delta.copy(), delta.copy()
            up[up < 0] = 0
            down[down > 0] = 0

            _gain = up.ewm(com=(period - 1), min_periods=period).mean()
            _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()

            RS = _gain / _loss
            return pd.Series(100 - (100 / (1 + RS)), name="RSI")

        rsi = rsi(df, 14).iloc[-1]
        print(symbol)
        print('upbit 1 minute RSI:', rsi)
        print('')
        if rsi < 28:  ######## rsi 지수가 30미만이면 텔레그램봇을통해 메시지 전송 ,원하는 숫자로 수정가능
            bot.sendMessage(chat_id=chat_id, text=f"{symbol}:rsi:{round(rsi, 3)}")
        time.sleep(0.1)


    def stockrsi(symbol):
        url = "https://api.upbit.com/v1/candles/minutes/3"

        querystring = {"market": symbol, "count": "500"}

        response = requests.request("GET", url, params=querystring)

        data = response.json()

        df = pd.DataFrame(data)

        series = df['trade_price'].iloc[::-1]

        df = pd.Series(df['trade_price'].values)

        period = 14
        smoothK = 3
        smoothD = 3

        delta = series.diff().dropna()
        ups = delta * 0
        downs = ups.copy()
        ups[delta > 0] = delta[delta > 0]
        downs[delta < 0] = -delta[delta < 0]
        ups[ups.index[period - 1]] = np.mean(ups[:period])
        ups = ups.drop(ups.index[:(period - 1)])
        downs[downs.index[period - 1]] = np.mean(downs[:period])
        downs = downs.drop(downs.index[:(period - 1)])
        rs = ups.ewm(com=period - 1, min_periods=0, adjust=False, ignore_na=False).mean() / \
             downs.ewm(com=period - 1, min_periods=0, adjust=False, ignore_na=False).mean()
        rsi = 100 - 100 / (1 + rs)

        stochrsi = (rsi - rsi.rolling(period).min()) / (rsi.rolling(period).max() - rsi.rolling(period).min())
        stochrsi_K = stochrsi.rolling(smoothK).mean()
        stochrsi_D = stochrsi_K.rolling(smoothD).mean()

        print(symbol)

        print('')
        time.sleep(1)


    rsiindex("KRW-BTC")  ###원하는 코인종목을 밑에 추가해주면 추가가된다 #기본적으로 비트,도지,이클,이더,리플
    # stockrsi("KRW-BTC")
    rsiindex("KRW-DOGE")
    rsiindex("KRW-ETC")
    rsiindex("KRW-ETH")
    rsiindex("KRW-XRP")
    rsiindex("KRW-EOS")
    rsiindex("KRW-UPP")
    rsiindex("KRW-SOLVE")
    rsiindex("KRW-TON")
    rsiindex("KRW-LBC")
    rsiindex("KRW-EMC2")
    rsiindex("KRW-HUNT")
    rsiindex("KRW-ONG")
    rsiindex("KRW-DAWN")
    rsiindex("KRW-BTT")
    rsiindex("KRW-ELF")
    rsiindex("KRW-MED")
    rsiindex("KRW-PLA")
    rsiindex("KRW-CRE")
    rsiindex("KRW-BCH")
    rsiindex("KRW-VET")
    rsiindex("KRW-EDR")
    rsiindex("KRW-HUM")
    rsiindex("KRW-AQT")
    rsiindex("KRW-SAND")
    rsiindex("KRW-IGNIS")
    rsiindex("KRW-MVL")
    rsiindex("KRW-AHT")
    rsiindex("KRW-SSX")
    rsiindex("KRW-TSHP")
    rsiindex("KRW-HBAR")
    rsiindex("KRW-DMT")
    rsiindex("KRW-RFR")
    rsiindex("KRW-LOOM")
    rsiindex("KRW-IQ")


