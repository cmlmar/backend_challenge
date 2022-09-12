import asyncio

from decouple import config
from binance import AsyncClient, BinanceSocketManager

api_key = config("api_key")
api_secret = config("secret_key")


async def get_price(symbol, price):
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client, user_timeout=2)

    ts = bm.trade_socket(symbol)


    async with ts as tscm:
        while True:
            res = await tscm.recv()
            if res["p"] > price:
                print(res["p"])

    await client.close_connection()


if __name__ == "__main__":
    symbol = input("insert symbol:  ")
    price = input("insert price:  ")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_price(symbol, price))
