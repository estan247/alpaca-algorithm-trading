import json
import requests
import time
from bs4 import BeautifulSoup
import alpaca_trade_api as tradeapi

STOCK = '%5EGSPC'.upper()
# SPX

APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'
APCA_API_KEY_ID = ''  # Enter your Alpaca Keys here
APCA_API_SECRET_KEY = ''

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL, api_version='v2') # or use ENV Vars shown below
account = api.get_account()

stock1 = requests.get('https://finance.yahoo.com/quote/' + STOCK + '/history?p=' + STOCK).text
current = requests.get('https://finance.yahoo.com/quote/' + STOCK + '?p=' + STOCK).text

# Average of the past 30 Day Lows

soup1 = BeautifulSoup(stock1, 'html.parser')
soup2 = BeautifulSoup(current, 'html.parser')

current_price = float(soup2.find_all("span", ['Trsdu(0.3s)'])[0].text.replace(",", ""))

day_1 = float(soup1.find_all("span")[25 + 6].text.replace(",", ""))
day_2 = float(soup1.find_all("span")[25 + 13].text.replace(",", ""))
day_3 = float(soup1.find_all("span")[25 + 20].text.replace(",", ""))
day_4 = float(soup1.find_all("span")[25 + 27].text.replace(",", ""))
day_5 = float(soup1.find_all("span")[25 + 34].text.replace(",", ""))
day_6 = float(soup1.find_all("span")[25 + 41].text.replace(",", ""))
day_7 = float(soup1.find_all("span")[25 + 48].text.replace(",", ""))
day_8 = float(soup1.find_all("span")[25 + 55].text.replace(",", ""))
day_9 = float(soup1.find_all("span")[25 + 62].text.replace(",", ""))
day_10 = float(soup1.find_all("span")[25 + 69].text.replace(",", ""))
day_11 = float(soup1.find_all("span")[25 + 76].text.replace(",", ""))
day_12 = float(soup1.find_all("span")[25 + 83].text.replace(",", ""))
day_13 = float(soup1.find_all("span")[25 + 90].text.replace(",", ""))
day_14 = float(soup1.find_all("span")[25 + 97].text.replace(",", ""))
day_15 = float(soup1.find_all("span")[25 + 104].text.replace(",", ""))
day_16 = float(soup1.find_all("span")[25 + 111].text.replace(",", ""))
day_17 = float(soup1.find_all("span")[25 + 118].text.replace(",", ""))
day_18 = float(soup1.find_all("span")[25 + 125].text.replace(",", ""))
day_19 = float(soup1.find_all("span")[25 + 132].text.replace(",", ""))
day_20 = float(soup1.find_all("span")[25 + 139].text.replace(",", ""))
day_21 = float(soup1.find_all("span")[25 + 146].text.replace(",", ""))
day_22 = float(soup1.find_all("span")[25 + 153].text.replace(",", ""))
day_23 = float(soup1.find_all("span")[25 + 160].text.replace(",", ""))
day_24 = float(soup1.find_all("span")[25 + 167].text.replace(",", ""))
day_25 = float(soup1.find_all("span")[25 + 174].text.replace(",", ""))
day_26 = float(soup1.find_all("span")[25 + 181].text.replace(",", ""))
day_27 = float(soup1.find_all("span")[25 + 188].text.replace(",", ""))
day_28 = float(soup1.find_all("span")[25 + 195].text.replace(",", ""))
day_29 = float(soup1.find_all("span")[25 + 202].text.replace(",", ""))
day_30 = float(soup1.find_all("span")[25 + 209].text.replace(",", ""))
day_31 = float(soup1.find_all("span")[25 + 216].text.replace(",", ""))

# Average of the past 30 Day Highs

day_1_high = float(soup1.find_all("span")[25 + 5].text.replace(",", ""))
day_2_high = float(soup1.find_all("span")[25 + 12].text.replace(",", ""))
day_3_high = float(soup1.find_all("span")[25 + 19].text.replace(",", ""))
day_4_high = float(soup1.find_all("span")[25 + 26].text.replace(",", ""))
day_5_high = float(soup1.find_all("span")[25 + 33].text.replace(",", ""))
day_6_high = float(soup1.find_all("span")[25 + 40].text.replace(",", ""))
day_7_high = float(soup1.find_all("span")[25 + 47].text.replace(",", ""))
day_8_high = float(soup1.find_all("span")[25 + 54].text.replace(",", ""))
day_9_high = float(soup1.find_all("span")[25 + 61].text.replace(",", ""))
day_10_high = float(soup1.find_all("span")[25 + 68].text.replace(",", ""))
day_11_high = float(soup1.find_all("span")[25 + 75].text.replace(",", ""))
day_12_high = float(soup1.find_all("span")[25 + 82].text.replace(",", ""))
day_13_high = float(soup1.find_all("span")[25 + 89].text.replace(",", ""))
day_14_high = float(soup1.find_all("span")[25 + 96].text.replace(",", ""))
day_15_high = float(soup1.find_all("span")[25 + 103].text.replace(",", ""))
day_16_high = float(soup1.find_all("span")[25 + 110].text.replace(",", ""))
day_17_high = float(soup1.find_all("span")[25 + 117].text.replace(",", ""))
day_18_high = float(soup1.find_all("span")[25 + 124].text.replace(",", ""))
day_19_high = float(soup1.find_all("span")[25 + 131].text.replace(",", ""))
day_20_high = float(soup1.find_all("span")[25 + 138].text.replace(",", ""))
day_21_high = float(soup1.find_all("span")[25 + 145].text.replace(",", ""))
day_22_high = float(soup1.find_all("span")[25 + 152].text.replace(",", ""))
day_23_high = float(soup1.find_all("span")[25 + 159].text.replace(",", ""))
day_24_high = float(soup1.find_all("span")[25 + 166].text.replace(",", ""))
day_25_high = float(soup1.find_all("span")[25 + 173].text.replace(",", ""))
day_26_high = float(soup1.find_all("span")[25 + 180].text.replace(",", ""))
day_27_high = float(soup1.find_all("span")[25 + 187].text.replace(",", ""))
day_28_high = float(soup1.find_all("span")[25 + 194].text.replace(",", ""))
day_29_high = float(soup1.find_all("span")[25 + 201].text.replace(",", ""))
day_30_high = float(soup1.find_all("span")[25 + 208].text.replace(",", ""))

# Average the highs and lows

day_1 = (day_1 + day_1_high) / 2
day_2 = (day_2 + day_2_high) / 2
day_3 = (day_3 + day_3_high) / 2
day_4 = (day_4 + day_4_high) / 2
day_5 = (day_5 + day_5_high) / 2
day_6 = (day_6 + day_6_high) / 2
day_7 = (day_7 + day_7_high) / 2
day_8 = (day_8 + day_8_high) / 2
day_9 = (day_9 + day_9_high) / 2
day_10 = (day_10 + day_10_high) / 2
day_11 = (day_11 + day_11_high) / 2
day_12 = (day_12 + day_12_high) / 2
day_13 = (day_13 + day_13_high) / 2
day_14 = (day_14 + day_14_high) / 2
day_15 = (day_15 + day_15_high) / 2
day_16 = (day_16 + day_16_high) / 2
day_17 = (day_17 + day_17_high) / 2
day_18 = (day_18 + day_18_high) / 2
day_19 = (day_19 + day_19_high) / 2
day_20 = (day_20 + day_20_high) / 2
day_21 = (day_21 + day_21_high) / 2
day_22 = (day_22 + day_22_high) / 2
day_23 = (day_23 + day_23_high) / 2
day_24 = (day_24 + day_24_high) / 2
day_25 = (day_25 + day_25_high) / 2
day_26 = (day_26 + day_26_high) / 2
day_27 = (day_27 + day_27_high) / 2
day_28 = (day_28 + day_28_high) / 2
day_29 = (day_29 + day_29_high) / 2
day_30 = (day_30 + day_30_high) / 2

#Price Arrays 14 Day & 30 Day

arr1 = [day_1, day_2, day_3, day_4, day_5, day_6, day_7]

max = arr1[0]
# Loop through the array
for i in range(0, len(arr1)):
    # Compare elements of array with max
    if (arr1[i] > max):
        max = arr1[i];

min = min(arr1)

higharr1 = max
lowarr1 = min
median = (higharr1 + lowarr1) / 2
lq = (median + lowarr1) / 2
middle_median = (median + lq) / 2
stoploss = lq - (((float(lq)) * 5) / 100)

# Convert Integer to a string

change_percent = ((float(median) - float(lq)) / float(lq)) * 100
#change_percent = str(round(change_percent, 3))

STOCK = 'SPX'

if current_price > median:
    SPX_overbought = True
    SPX_status = ('SPX fails: S&P 500 Index is currently overbought ' +
                   STOCK + ": buy $" + str(round(lq, 4)) + " sell $" + str(round(median, 4)) + ' Current Price: ' + str(round(current_price, 4)))
    print(SPX_status)
    #print('')
    #print('SPX fails: S&P 500 Index is currently overbought')
else:
    SPX_overbought = False
    SPX_status = ('SPX: S&P 500 Index is withing range')
    SPX_status = ('SPX: S&P 500 Index is withing range ' +
                   STOCK + ": buy $" + str(round(lq, 4)) + " sell $" + str(round(median, 4)) + ' Current Price: ' + str(round(current_price, 4)))
    print(SPX_stats)
