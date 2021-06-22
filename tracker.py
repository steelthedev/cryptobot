import requests

def get_prices():
    coins = ["BTC", "ETH", "XRP", "LTC", "BCH", "ADA", "DOT", "LINK", "BNB", "XLM"]

    crypto_source = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = []

    for i in crypto_source:
        data.append({
            "coin": i,
            "price": crypto_source[i]["USD"]["PRICE"],
            "change_day": crypto_source[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_source[i]["USD"]["CHANGEPCTHOUR"]
        })


    return data

    


if __name__ == "__main__":
    print(get_prices())