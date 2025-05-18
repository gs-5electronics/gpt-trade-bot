from pybit.unified_trading import HTTP

api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET_KEY"

session = HTTP(
    testnet=False,
    api_key=api_key,
    api_secret=api_secret
)

balance = session.get_wallet_balance(accountType="UNIFIED")
usdt_balance = balance["result"]["list"][0]["totalEquity"]
print("Ваш баланс USDT:", usdt_balance)
