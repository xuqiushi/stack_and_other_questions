import pandas as pd
from bs4 import BeautifulSoup
from requests_html import HTMLSession


if __name__ == "__main__":
    # Begin requests session
    s = HTMLSession()
    # Get page
    r = s.get("https://www.spotrac.com/nfl/rankings/2019/base/running-back/")
    r.html.render()
    # Get page content, find first table, and save to df
    soup = BeautifulSoup(r.html.html, "lxml")
    table = soup.find_all("table")[0]
    df_list = pd.read_html(str(table))
    df = df_list[0]
    print("x")
