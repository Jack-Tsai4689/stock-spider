import requests
import pandas as pd
import time
from fake_useragent import UserAgent
ua = UserAgent()
# pip install pandas
dates = [20210712, 20210713, 20210714]
stockNo = 2330
url_template = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}"

for date in dates:
	url = url_template.format(date, stockNo)
	file_name = "{}_{}.csv".format(stockNo, date)

	user_agent = ua.random
	headers = {'user-agent': user_agent}
	data = pd.read_html(requests.get(url, headers=headers).text)[0]
	data.columns = data.columns.droplevel(0)
	data.to_csv(file_name, index=False)
	time.sleep(5)