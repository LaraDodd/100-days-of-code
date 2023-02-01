from data import Data
from stock_tracker_brain import StockTrackerBrain, significant_percentage_change

STOCK = "TSLA"
COMPANY_NAME = "Tesla"


# ========= MAIN CODE ==========
tesla_data = Data(stock_name=COMPANY_NAME, stock_symbol=STOCK)
tesla_tracker_brain = StockTrackerBrain(tesla_data)

# call function to find percentage difference
today_percentage_difference = tesla_tracker_brain.percentage_change

# if the percentage difference is significant call get news function
if significant_percentage_change(today_percentage_difference):
    print(f"percentage difference: {today_percentage_difference}%")
    print(tesla_tracker_brain.write_text())
    tesla_tracker_brain.send_text()

# netflix_data = Data(stock_name="Netflix", stock_symbol="NFLX")
# netflix_tracker_brain = StockTrackerBrain(stock_name="Netflix", stock_symbol="NFLX") #need to figure out a way to pass in
# # data object instead of just attributes again
#
# # call function to find percentage difference
# today_percentage_difference = netflix_tracker_brain.percentage_change
#
# # if the percentage difference is significant call get news function
# if significant_percentage_change(today_percentage_difference):
#     print(f"percentage difference: {today_percentage_difference}%")
#     print(netflix_tracker_brain.write_text())
#     netflix_tracker_brain.send_text()
