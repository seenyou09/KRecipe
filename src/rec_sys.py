
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import unidecode, ast

class rec_sys:
    def __init__(self, N, n_ingred, category, df):
        self.numberOfRec = N
        self.n_ingred = n_ingred
        self.df_recipes = df
        self.category = category
        self.tfidf = TfidfVectorizer()
        self.df_recipes['IngredientsType_Parsed'] = self.df_recipes.IngredientsType_Parsed.astype('U')
        self.kreciepe_matrix = self.tfidf.fit_transform(self.df_recipes['IngredientsType_Parsed'])
        self.scores = self.new_ingred_tftIdf()
    
    def new_ingred_tftIdf(self):
        ingredients_tfidf = self.tfidf.transform([self.n_ingred])
        cos_sim = map(lambda x: cosine_similarity(ingredients_tfidf, x), self.kreciepe_matrix)
        self.scores = list(cos_sim)
        return self.scores
    
    def get_recommendations(self):

        top = sorted(range(len(self.scores)), key=lambda i: self.scores[i], reverse=True)[:self.numberOfRec]


        recommendation = pd.DataFrame(columns = ['recipe', 'ingredients', 'score', 'url','category'])
        count = 0
        for i in top:
            for category_item in self.category:
                if category_item in self.df_recipes["Category"][i]:
                    recommendation.at[count, 'recipe'] = self.df_recipes['English Name'][i]
                    recommendation.at[count, 'ingredients'] = self.df_recipes['IngredientsType_Parsed'][i]
                    recommendation.at[count, 'url'] = self.df_recipes['Video'][i]
                    score_value = float(self.scores[i])  
                    recommendation.at[count, 'score'] = "{:.3f}".format(score_value)  
                    recommendation.at[count, 'category'] =self.df_recipes['Category'][i]
                    count += 1
                else:
                    pass
        return recommendation

if __name__ == "__main__":
    df_recipes = pd.read_excel('/Users/seanyoo/Desktop/KRecipe/xlsx/kreciepe.xlsx')
    category ="side dish"
    trial = rec_sys(10, "beef, rice, soup",category, df_recipes)
    yes = trial.get_recommendations()
    yes
