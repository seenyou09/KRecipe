# KRecipe
### Created and deployed a streamlit app to try: 


<img src="image/app.jpeg" alt="Your Image" width="250"/>

## **Summary:**
----

####    I created an app designed to recommend a list of recipes based on the ingredients you input. Recognizing the common challenge faced by college students who often have limited ingredients due to their perishable nature and solo living lifestyle, my app is geared towards optimizing the culinary experience even with limited resources. The app's functionality is powered by Python's Beautiful Soup, which is employed for web scraping of Maangchi's collection of online recipes. Leveraging Natural Language Processing (NLP) tools such as TF-IDF and cosine similarity, the app calculates the similarity between the ingredients. The app empowers users to create wholesome and delicious meals, fostering a love for cooking and a connection to the rich world of Korean cuisine.


### **Data Scraping and Cleaning:**
----

####     Built a web scraper that extracts Korean recipe information from the website "maangchi.com" and saves the data into an Excel file. The Excel file contained English Name, Korean Name, list of ingredients, category of food, and YouTube URL link. In addition, I created a data preprocessing pipeline for a Korean recipe dataset, focusing on cleaning and preparing the data for further analysis or application in a machine-learning model. The cleaning steps involve handling text data, removing duplicates, and creating new columns with parsed and cleaned information.


### **Building Model for Recipe Recommendation:**

----

####     Constructing an effective recommendation model involved utilizing TF-IDF (Term Frequency-Inverse Document Frequency) to evaluate the significance of each ingredient. TF-IDF works by assigning weights to words based on their frequency in a specific document relative to their frequency across all documents. In the context of our app, each recipe is treated as a document, and the ingredients as the words.

####     To optimize the model, I eliminated common ingredients such as salt, pepper, water, etc. Though essential in cooking, could potentially skew the recommendation results. The step was measuring the similarity between the user-provided ingredients and the database of ingredients using cosine similarity. It refines the recommendations by filtering out the top similar recipes, ensuring that users receive the most similar recipes. For example, let's consider a scenario where a user inputs "kimchi" and "tofu" as ingredients. The recommendation model, after TF-IDF processing and cosine similarity calculation, filters through the database to present recipes prioritizing recipes that have kimchi as this is a more significant ingreident.

####     While attempting to enhance the recommendation model, I attempted to use Word2Vec, a powerful word embedding technique, However, through experiment, it became evident that the performance of the model did not improve; in fact, it appeared to worsen. This observed decline is due to inherent challenges posed by certain Korean ingredients, whose meanings may not be effectively captured by the Word2Vec embedding. 

