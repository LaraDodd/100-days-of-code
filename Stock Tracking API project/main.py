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


def significant_percentage_change() -> bool:
    return False


def get_open_differences():
    pass

#pull stock data as a json
stock_data = get_stock_data()

today_date = datetime.date(datetime.today())
print(today_date)
yesterday = today_date - timedelta(days=1)
day_before_yesterday = today_date - timedelta(days=2)
print(yesterday)


yesterday_close = stock_data["Time Series (Daily)"][str(yesterday)]["4. close"]
print(yesterday_close)
try:
    last_recorded_day_before_yesterday_close = stock_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]
except KeyError:
    last_recorded_day_before_yesterday = today_date - timedelta(days=4)
    last_recorded_day_before_yesterday_close = \
        stock_data["Time Series (Daily)"][str(last_recorded_day_before_yesterday)]["4. close"]


print(last_recorded_day_before_yesterday_close)




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
account_sid = "AC1528a805a7d8cd40e96df09d118bafad"
auth_token = "f1c976d15dd55641ef772c62cd01837e"
if significant_percentage_change():
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="STOCK INFO",
        from_="+14706467644",
        to="+447518361866"
    )

    print(message.status)

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
