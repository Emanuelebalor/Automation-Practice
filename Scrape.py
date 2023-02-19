from Setup import Login
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time


class ScrapeTables(Login):
    url = "https://qa-practice.netlify.app/web-table.html"

    def __init__(self):
        super(ScrapeTables, self).__init__()

    # takes the entire web element bit Beautifull soup and reads it with pandas
    # will print the table on the page
    def table_static(self):
        self.get(self.url)
        time.sleep(2)
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'lxml')
        tables = soup.find_all('table')
        dataframes = pd.read_html(str(tables))
        print(dataframes[0])




