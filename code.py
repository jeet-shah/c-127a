
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd 
import requests

starturl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(starturl)
def scrape():
    headers = ["Proper name","Distance","Mass","Radius"]
    soup = bs(page.text,'html.parser')
    startable = soup.find('table')
    temp_list = []
    tablerows = startable.find_all("tr")
    for tr in tablerows:
        td = tr.find_all("td")
        row = [i.text.rstrip()for i in td]
        temp_list.append(row)
    star_name,star_distance,star_mass,star_radius = [],[],[],[]
    for i in range(1,len(temp_list)):
        star_name.append(temp_list[i][1])
        star_distance.append(temp_list[i][3])
        star_mass.append(temp_list[i][5])
        star_radius.append(temp_list[i][6])
    df = pd.DataFrame(list(zip(star_name,star_distance,star_mass,star_radius)),columns = [
        "Star name",
        "Star distance",
        "Star mass",
        "Star radius"
    ])
    df.to_csv("star.csv")
scrape()
