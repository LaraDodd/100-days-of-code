import requests
from twilio.rest import Client
from datetime import datetime, timedelta



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stock_data(): # this should be in a module called data, with get stock data and get news data
                      # and we should pass in Stock Symbol to the class when we make it

    api_key = "8B27V9R1FGX0GHZ1"
    endpoint = "https://www.alphavantage.co/query?"

    param_dict = {"function": "TIME_SERIES_DAILY_ADJUSTED",
                  "symbol": "TSLA",
                  "apikey": api_key,
                  }
    # import weather data
    response = requests.get(url=endpoint, params=param_dict)
    response.raise_for_status()

    # change data to json
    data = response.json()
    return data


def significant_percentage_change(percentage_change) -> bool: # turn into brain class method
    if abs(percentage_change) <= 3:
        return False
    else:
        return True




def get_open_percentage_difference(): # turn into brain class

    #pull stock data as a json
    stock_data = get_stock_data()

    #use datetime to pull dates
    today_date = datetime.date(datetime.today())
    yesterday = today_date - timedelta(days=1)
    day_before_yesterday = today_date - timedelta(days=2)

    #get yesterday close
    try:
        last_recorded_day_close = stock_data["Time Series (Daily)"][str(yesterday)]["4. close"]
    except KeyError:
        last_recorded_day = today_date - timedelta(days=3)
        last_recorded_day_close = stock_data["Time Series (Daily)"][str(last_recorded_day)]["4. close"]

    print(f"last recorded day close: {last_recorded_day_close}")

    #get day before yesterday close
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
    percentage_change = 100 * difference/float(second_to_last_recorded_day_close)

    return percentage_change


def get_news(stock_name): # this should be part of the data class
    api_key = "737f56d3a261423c979fbd9548e0cfd8"
    endpoint = "https://newsapi.org/v2/everything?"

    param_dict = {"q": stock_name, # change to name of the stock
                  "from": str(datetime.date(datetime.today())),
                  "language": "en",
                  "sortBy": "popularity",
                  "apiKey": "737f56d3a261423c979fbd9548e0cfd8",
                  }
    # import weather data
    response = requests.get(url=endpoint, params=param_dict)
    response.raise_for_status()

    # change data to json
    data = response.json()
    return data

def get_top_3_articles_in_string():

    news_data = get_news("TESLA or Elon")

    top_3_articles = [news_data["articles"][i] for i in range(0, 3)]

    text_message = ""
    for article in top_3_articles:
        text_message += article["title"]
        text_message += f" {article['url']}\n"

    return text_message

def write_text(percentage_difference, stock_name):
    # Replace the [percentage difference] [articles] [stock] placeholders with the actual name.
    with open("text_message.txt") as message:
        message_contents = message.read()

    # use replace function to replace name section of string with actual name
    message_contents = message_contents.replace("[STOCK]", f"{stock_name}")
    message_contents = message_contents.replace("[PERCENTAGE DIFF]", f"{percentage_difference}%")
    message_contents = message_contents.replace("[ARTICLES]", f"{get_top_3_articles_in_string()}")

    return message_contents


def send_text():
    account_sid = "AC1528a805a7d8cd40e96df09d118bafad"
    auth_token = "f1c976d15dd55641ef772c62cd01837e"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body= write_text(percentage_difference=today_percentage_difference, stock_name="TESLA"),
        from_="+14706467644",
        to="+447518361866"
    )

    print(message.status)

# ========= MAIN CODE ==========
# call function to find percentage difference
today_percentage_difference = round(get_open_percentage_difference(), 2)

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
