import requests
import pandas as pd
from bs4 import BeautifulSoup

#-----Variables-----

#Source Page
page = requests.get("https://www.ufc.com/rankings")
soup = BeautifulSoup(page.content, "html.parser")

#Source area (Rankings Box)
rankings = soup.find(class_ = "view-grouping-content")

#Names and Numbers of rank
ranking_name_rows = rankings.find_all(class_ = "views-row")
ranking_num_rows = rankings.find_all(class_ = "views-field views-field-weight-class-rank")

#Lists of names and numbers
ranking_names = [item.get_text().strip() for item in ranking_name_rows]
ranking_nums = [item.get_text().strip() for item in ranking_num_rows]

#Insertation of the rank number 1 into ranking_nums
var = "1"
ranking_nums.insert(0, var)


#Creation of table
p4p_ranking = pd.DataFrame(
    {
        "Name": ranking_names,
        "Rank": ranking_nums,
    })


def display_rankings():
    return p4p_ranking
