#How to use this script:
# 1. Copy the code below.
# 2. Open ThinkOrSwim platform.
# 3. Go to Charts tab.
# 4. Click on Studies > Edit Studies.
# 5. Click on Strategies tab.
# 6. Click on Create.
# 7. Paste the code into the editor.
# 8. Name the strategy (e.g., Daily Levels).
# 9. Click on OK.
# 10. Click on Apply.
# 11. Click on OK again.


declare upper;
declare once_per_bar;

input startTime = 820; #hint startTime: start time in EST 24-hour time
input endTime = 1600; #hint endTime: end time in EST 24-hour time

def adjStartTime = startTime;
def adjEndTime = endTime;

# we use a 1 bar offset to get orders to line up, so adjust for that here
def marketOpen = if SecondsTillTime(adjEndTime) >= 60 and SecondsFromTime(adjStartTime) >= -60 then 1 else 0;

AddOrder(OrderType.BUY_TO_OPEN, marketOpen, low, 1, Color.White, Color.White, name="OHLC|"+open[-1]+"|"+high[-1]+"|"+low[-1]+"|"+close[-1]);
AddOrder(OrderType.SELL_TO_CLOSE, marketOpen, high, 1, Color.White, Color.White, name="SellClose");