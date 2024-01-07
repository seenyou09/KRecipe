#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:40:33 2023

@author: seanyoo
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
source = requests.get("https://www.maangchi.com/recipes").text
soup = BeautifulSoup(source, 'html.parser')
articles = soup.find_all("div", class_="module recipes-by-taxomony")

#find indiviudal category 
def getCategory(articles):

    category_link = []
    for article in articles:
        items = article.find_all("li")  # Find all the <li> tags within the <ul> tag
        for category in items:
            link = "https://www.maangchi.com" +category.find("a")["href"]
            category_link.append(link)
            
    return category_link



def getlink(category):
    link_list_2 = []
    source2 = requests.get(category).text
    soup2 = BeautifulSoup(source2, "html.parser")
    articles2 = soup2.find_all("div", class_="taxonomy-card")
    for i in articles2:
        link2 = i.find("a")["href"]
        link_list_2.append(link2)
    return link_list_2


def get_info(link):
    link = str(link)
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'html.parser')

    article3 = soup.find("div", class_="columntwo")
    etitle = article3.find("span", class_="english-name").text
    
    try:
        korean_name = article3.find("strong", string="Korean name:").next_sibling.strip()
    except:
        korean_name = ""
    
    list_ingredient = []  
    list_type = []
    try:
        article4 = soup.find("div", class_="columnthree")
        ingredient = article4.find("strong", string="Made with:").next_sibling.strip()
        list_ingredient = ingredient.split(",")
        r_type = article4.find("span").text
        list_type = r_type.split(",")
    except:
        pass
    try:
        article5 = soup.find("div", class_="hero-video-container video-embed-container")
        video = article5.find("button", title="Play Video")["href"]
    except:
        video = ""
    return etitle, korean_name, list_ingredient, list_type, video
    

if __name__ == "__main__":
    # category_link = getCategory(articles)
    # for item in category_link: #get indivdual category
    #     link_list = getlink(item) 
    #     for i in link_list:
    #         f = get_info(i)
    #         print(f)
    category_link = getCategory(articles)
    data = []  # List to store recipe information

    for item in category_link:  # get individual category
        link_list = getlink(item)
        for i in link_list:
            recipe_info = get_info(i)
            data.append(recipe_info)  # Append recipe information to the list
    df = pd.DataFrame(data, columns=["English Name", "Korean Name", "Ingredients", "Type", "Video"])
    df.to_excel("kreciepe.xlsx")
    print("finish")
    
    
    
    