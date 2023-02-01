import requests
from datetime import datetime, timedelta

"""this module contains class which pulls all data information from various APIs"""


class Data:
    def __init__(self, stock_symbol: str, stock_name: str):
        self.stock_symbol = stock_symbol
        self.stock_name = stock_name

    def get_stock_data(self):
        """Calls Alphavantage API, pulls in stock data about specific stock symbol passed in

        Args:
        stock_symbol - a string passed in denoting the stock symbol to request data about

        Returns:
        data - daily stock data about the stock"""

        api_key = "8B27V9R1FGX0GHZ1"
        endpoint = "https://www.alphavantage.co/query?"

        param_dict = {"function": "TIME_SERIES_DAILY_ADJUSTED",
                      "symbol": self.stock_symbol,
                      "apikey": api_key,
                      }
        # import weather data
        response = requests.get(url=endpoint, params=param_dict)
        response.raise_for_status()

        # change data to json
        data = response.json()
        return data

    def get_news(self) -> dict:
        """Takes in stock name and pulls article data about this name from the news api. It filters articles by
        english language, todays date only. Sorts articles by popularity first.

         Returns:
         data - article data in form of dictionary with nested dictionaries and lists"""

        api_key = "737f56d3a261423c979fbd9548e0cfd8"
        endpoint = "https://newsapi.org/v2/everything?"

        param_dict = {"q": self.stock_name,  # change to name of the stock
                      "from": str(datetime.date(datetime.today())),
                      "language": "en",
                      "sortBy": "popularity",
                      "apiKey": api_key,
                      }
        # import weather data
        response = requests.get(url=endpoint, params=param_dict)
        response.raise_for_status()

        # change data to json
        data = response.json()
        return data
