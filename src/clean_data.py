# This script is a data preprocessing pipeline for a Korean recipe dataset, focusing on cleaning and preparing the data for further analysis or application in a machine learning model. The cleaning steps involve handling text data, removing duplicates, and creating new columns with parsed and cleaned information.

import pandas as pd
import nltk
vocabulary = nltk.FreqDist()

df = pd.read_excel('/Users/seanyoo/Desktop/KRecipe/xlsx/koreanFood_data.xlsx')
df = df.drop("Unnamed: 0", axis=1)
df =df.dropna()
df.head(10)

#clean text from str to list 
def clean_text(ingredient_str):
    ingredient_list = [item.strip(" ' ") for item in ingredient_str.strip("[]").split(",")]
    return ingredient_list

#ingredient parser 
def ingredient_parser(ingredients):
    remove_word_list = ["kosher salt", 'toasted seasame oil', "water", "sugar", "soy sauce","vegetable oil","ground black pepper", "hot pepper flakes","flour", "honey","vinegar"]
    ingred_list = []
    for ingred in ingredients:
        #ingred.translate(translator)
        if ingred not in remove_word_list:
            ingred_list.append(ingred)
        else:
            pass
    
    ingred_str = ", ".join(ingred_list)
    
    return ingred_str

def find_remove_words(df):
    #from this list we have a list of common ingredients to get rid of
    for ingredient_list in df['Ingredients']:
        for ingredients in ingredient_list:
            ingredients = ingredients.split(",")
            vocabulary.update(ingredients)
    for word, frequency in vocabulary.most_common(200)[1:]:
        print(f'{word}: {frequency}')


    remove_word_list = ["kosher salt", 'toasted seasame oil', "water", "sugar", "soy sauce","vegetable oil","ground black pepper", "hot pepper flakes","flour", "honey","vinegar"]

def createCategory(category):
    key = ["side dish", "main dish", "snack", "appetizer", "dessert"]
    category_list = []
    for item in category:
        if item in key:
            category_list.append(item)
    return category_list
            
if __name__ == "__main__":
    remove_word_list = ["kosher salt", 'toasted seasame oil', "water", "sugar", "soy sauce","vegetable oil","ground black pepper", "hot pepper flakes","flour", "honey","vinegar",'"']
    df['Ingredients'] = df['Ingredients'].apply(clean_text)
    df['Type'] = df['Type'].apply(clean_text)
    df['Category'] = df['Type'].apply(createCategory)
    
    df['IngredientsType'] = df.apply(lambda row: row['Ingredients'] + row['Type'], axis=1)
    df['IngredientsType_Parsed'] = df['IngredientsType'].apply(ingredient_parser)
    df = df.drop_duplicates(subset=["Korean Name"])
    df.to_excel("kreciepe2.0.xlsx")
    
    

