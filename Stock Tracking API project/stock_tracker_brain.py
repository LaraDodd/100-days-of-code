"""this module contains all the complex calculation classes and methods"""
from data import Data
from datetime import datetime, timedelta
from twilio.rest import Client


def significant_percentage_change(percentage_change: float) -> bool:
    """checks if percentage change is above or below 10%

    Returns:
    Boolean indicating whether the change is significant (above or below 10%)"""

    if abs(percentage_change) <= 3:
        return False
    else:
        return True


class StockTrackerBrain(Data):

    def __init__(self, stock_name, stock_symbol):
        self.stock_symbol = stock_symbol
        self.stock_name = stock_name
        self.percentage_change = round(self.get_open_percentage_difference(), 2)
        super().__init__(stock_symbol=self.stock_symbol, stock_name=self.stock_name)


    def get_open_percentage_difference(self) -> float:
        """calls get_stock_data function to get stock data, using datetime to find the current date, it tries to
        find yesterday and the day before yesterday's close values from the data. If it has been a weekend, it pulls
        the most recent last 2 close values. Finds the close difference and calculates the close percentage difference

        Returns:
        percentage_difference - float indicating the percentage difference between the 2 most recent close values"""

        # pull stock data as a json
        stock_data = self.get_stock_data()
        stock_data = self.get_stock_data()

        # use datetime to pull dates
        today_date = datetime.date(datetime.today())
        yesterday = today_date - timedelta(days=1)
        day_before_yesterday = today_date - timedelta(days=2)

        # get yesterday close
        try:
            last_recorded_day_close = stock_data["Time Series (Daily)"][str(yesterday)]["4. close"]
        except KeyError:
            last_recorded_day = today_date - timedelta(days=3)
            last_recorded_day_close = stock_data["Time Series (Daily)"][str(last_recorded_day)]["4. close"]

        print(f"last recorded day close: {last_recorded_day_close}")

        # get day before yesterday close
        try:
            second_to_last_recorded_day_close = stock_data["Time Series (Daily)"][str(day_before_yesterday)][
                "4. close"]
        except KeyError:
            second_to_last_recorded_day = today_date - timedelta(days=4)
            second_to_last_recorded_day_close = \
                stock_data["Time Series (Daily)"][str(second_to_last_recorded_day)]["4. close"]

        print(f"second to last recorder day: {second_to_last_recorded_day_close}")

        # find difference and percentage difference
        difference = float(last_recorded_day_close) - float(second_to_last_recorded_day_close)
        print(f"difference in closes: {round(difference)}")
        percentage_change = 100 * difference / float(second_to_last_recorded_day_close)

        return percentage_change

    def get_top_3_articles_in_string(self) -> str:
        """calls get_news function which gets all article based in passed in stock name. Manipulates resulting dict
        to get top 3 article titles and their URL's.

        Returns:
        text_message = string containing formatted article titles and URLS"""

        news_data = self.get_news()

        top_3_articles = [news_data["articles"][i] for i in range(0, 3)]

        text_message = ""
        for article in top_3_articles:
            text_message += article["title"]
            text_message += f" {article['url']}\n"
            text_message += "\n"

        return text_message

    def write_text(self) -> str:
        """Writes formatted text by pulling in text message from text_message.txt and replacing the placeholders:
        [STOCK], [PERCENTAGE DIFF] and [ARTICLES]

        Args:
        percentage_difference - Value of the percentage difference for the last 2 recorded close values
        stock_name - Name of the stock

        Returns:
        message_contents - string containing formatted text message to send"""

        if self.percentage_change > 0:
            symbol = "🔺"
        else:
            symbol = "🔻"
        # Replace the [percentage difference] [articles] [stock] placeholders with the actual name.
        with open("text_message.txt") as message:
            message_contents = message.read()

        # use replace function to replace name section of string with actual name
        message_contents = message_contents.replace("[STOCK]", f"{self.stock_name}")
        message_contents = message_contents.replace("[PERCENTAGE DIFF]", f"{symbol}{self.percentage_change}%")
        message_contents = message_contents.replace("[ARTICLES]", f"{self.get_top_3_articles_in_string()}")

        return message_contents

    def send_text(self) -> None:
        """creates client object using the API twillo.rest class. Creates a message using this class and sends it
        to my phone number"""
        account_sid = "AC1528a805a7d8cd40e96df09d118bafad"
        auth_token = "f1c976d15dd55641ef772c62cd01837e"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=self.write_text(),
            from_="+14706467644",
            to="+447518361866"
        )

        print(message.status)
