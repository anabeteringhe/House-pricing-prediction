import requests # type: ignore
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv("CSVs\Links.csv")
linkList = df.values.tolist()
HouseDataList = []
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'}

def scrapeData(url):
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.content.decode(), "html.parser")

    tableValue = []
    tableKeys = []

    Keys = soup.find_all("div", {"data-cy": "table-label-content"})
    tableKeys = [div.text for div in Keys]

    # print(len(tableKeys))
    # print(tableKeys)

    for key in tableKeys:
        tableValue.append(soup.find("div", {"aria-label":key}).text)

    for key in tableKeys:
        tableValue = [value.replace(key, '') for value in tableValue]

    # print(len(tableValue))
    # print(tableValue)

    houseDetails = {}

    # num_attributes_keys = len(tableKeys)
    # num_attributes_values = len(tableValue)

    # print("Number of attributes in keys:", num_attributes_keys)
    # print("Number of attributes in values:", num_attributes_values)


    for key in tableKeys:
        for value in tableValue:
            houseDetails[key] = value
            tableValue.remove(value)
            break

    # print(houseDetails)
    if(soup.find("strong", {"aria-label":"Preț"}) == None):
        price = "N/A"
    else:
        price=soup.find("strong", {"aria-label":"Preț"}).text
        
    houseDetails["Preț"] = price

    HouseDataList.append(houseDetails)

    # print(HouseDataList)

for i in range(len(linkList)):
    scrapeData(linkList[i][1])

DataSet = pd.DataFrame(HouseDataList)
DataSet.to_csv(r"C:\Users\Ana\Desktop\House-pricing-prediction-master\CSVs\UneditedDataSetSoup--tab-separated.csv", encoding="utf-16", sep='\t')
DataSet.to_csv(r"C:\Users\Ana\Desktop\House-pricing-prediction-master\CSVs\UneditedDataSetSoup.csv", encoding="utf-16")