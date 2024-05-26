import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_financials(stock_symbol: str) -> pd.DataFrame:
    URL = "https://www.tickertape.in/stocks/tata-power-company-TTPW#financials"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.prettify())

    financials_div = "financials-table-root"
    table_head = "jsx-227443019"

    mydivs = soup.find("table", class_="jsx-227443019")

    for item in mydivs:
        print(item)

    data = []
    for row in mydivs.find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text)
        data.append(row_data)

    df = pd.DataFrame(data)
    print(df)
    return df


URL = "https://www.screener.in/company/GAIL/consolidated/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())


mydivs = soup.find("table")
i=0

for item in mydivs:
    print(item)


data = []
for row in mydivs.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text.strip())
    data.append(row_data)

df = pd.DataFrame(data)
df.to_csv(f"iter{i}.csv")
i+=1
#print(df)

dfs = pd.read_html("https://www.screener.in/company/GAIL/consolidated/")

for i in range(len(dfs)):
    print(i+1,dfs[i])
    dfs[i].to_csv(f"iter{i}.csv")