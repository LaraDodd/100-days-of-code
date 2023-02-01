import requests
from twilio.rest import Client
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


# this should be in a module called data, with get stock data and get news data
# and we should pass in Stock Symbol to the class when we make it
def get_stock_data(stock_symbol: str) -> dict:
    """Calls Alphavantage API, pulls in stock data about specific stock symbol passed in

    Args:
    stock_symbol - a string passed in denoting the stock symbol to request data about

    Returns:
    data - daily stock data about the stock"""

    api_key = "8B27V9R1FGX0GHZ1"
    endpoint = "https://www.alphavantage.co/query?"

    param_dict = {"function": "TIME_SERIES_DAILY_ADJUSTED",
                  "symbol": stock_symbol,
                  "apikey": api_key,
                  }
    # import weather data
    response = requests.get(url=endpoint, params=param_dict)
    response.raise_for_status()

    # change data to json
    data = response.json()
    return data


def significant_percentage_change(percentage_change: float) -> bool:  # turn into brain class method
    """checks if perecentage change is above or below 10%

    Returns:
    Boolean indicating whether the change is significant (above or below 10%)"""

    if abs(percentage_change) <= 3:
        return False
    else:
        return True


def get_open_percentage_difference(stock_symbol: str) -> float:  # turn into brain class
    """calls get_stock_data function to get stock data, using datetime to find the current date, it tries to
    find yesterday and the day before yesterday's close values from the data. If it has been a weekend, it pulls
    the most recent last 2 close values. Finds the close difference and calculates the close percentage difference

    Returns:
    percentage_difference - float indicating the percentage difference between the 2 most recent close values"""

    # pull stock data as a json
    stock_data = get_stock_data(stock_symbol)

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
        second_to_last_recorded_day_close = stock_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]
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


def get_news(stock_name: str) -> dict:  # this should be part of the data class
    """Takes in stock name and pulls article data about this name from the news api. It filters articles by
    english language, todays date only. Sorts articles by popularity first.

     Returns:
     data - article data in form of dictionary with nested dictionaries and lists"""

    api_key = "737f56d3a261423c979fbd9548e0cfd8"
    endpoint = "https://newsapi.org/v2/everything?"

    param_dict = {"q": stock_name,  # change to name of the stock
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


def get_top_3_articles_in_string() -> str:
    """calls get_news function which gets all article based in passed in stock name. Manipulates resulting dict
    to get top 3 article titles and their URL's.

    Returns:
    text_message = string containing formatted article titles and URLS"""

    news_data = get_news("TESLA or Elon")

    top_3_articles = [news_data["articles"][i] for i in range(0, 3)]

    text_message = ""
    for article in top_3_articles:
        text_message += article["title"]
        text_message += f" {article['url']}\n"
        text_message += "\n"

    return text_message


def write_text(percentage_difference: float, stock_name: str) -> str:
    """Writes formatted text by pulling in text message from text_message.txt and replacing the placeholders:
    [STOCK], [PERCENTAGE DIFF] and [ARTICLES]

    Args:
    percentage_difference - Value of the percentage difference for the last 2 recorded close values
    stock_name - Name of the stock

    Returns:
    message_contents - string containing formatted text message to send"""

    if percentage_difference > 0:
        symbol = "🔺"
    else:
        symbol = "🔻"
    # Replace the [percentage difference] [articles] [stock] placeholders with the actual name.
    with open("text_message.txt") as message:
        message_contents = message.read()

    # use replace function to replace name section of string with actual name
    message_contents = message_contents.replace("[STOCK]", f"{stock_name}")
    message_contents = message_contents.replace("[PERCENTAGE DIFF]", f"{symbol}{percentage_difference}%")
    message_contents = message_contents.replace("[ARTICLES]", f"{get_top_3_articles_in_string()}")

    return message_contents


def send_text():
    """creates client object using the API twillo.rest class. Creates a message using this class and sends it
    to my phone number"""
    account_sid = "AC1528a805a7d8cd40e96df09d118bafad"
    auth_token = "f1c976d15dd55641ef772c62cd01837e"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=write_text(percentage_difference=today_percentage_difference, stock_name="TESLA"),
        from_="+14706467644",
        to="+447518361866"
    )

    print(message.status)


# ========= MAIN CODE ==========
# call function to find percentage difference
today_percentage_difference = round(get_open_percentage_difference("TSLA"), 2)

# if the percentage difference is significant call get news function
if significant_percentage_change(today_percentage_difference):
    print(f"percentage difference: {today_percentage_difference}%")
    print(write_text(percentage_difference=today_percentage_difference, stock_name="TESLA"))
    send_text()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
