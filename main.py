from fastapi import FastAPI
import pandas as pd

#cargar archivos 
df_amazon_prime = pd.read_csv('./dataset/amazon_prime_titles.csv',delimiter = ',',encoding = "utf-8")
df_disney_plus = pd.read_csv('./dataset/disney_plus_titles.csv',delimiter= ',', encoding = "utf-8" )
df_hulu = pd.read_csv('./dataset/hulu_titles.csv',delimiter= ',', encoding = "utf-8" )
df_netflix = pd.read_csv('./dataset/netflix_titles.csv',delimiter= ',', encoding = "utf-8" )

df_rating1 = pd.read_csv('./dataset/rating/1.csv',delimiter = ',',encoding = "utf-8")
df_rating2 = pd.read_csv('./dataset/rating/2.csv',delimiter = ',',encoding = "utf-8")
df_rating3 = pd.read_csv('./dataset/rating/3.csv',delimiter = ',',encoding = "utf-8")
df_rating4 = pd.read_csv('./dataset/rating/4.csv',delimiter = ',',encoding = "utf-8")
df_rating5 = pd.read_csv('./dataset/rating/5.csv',delimiter = ',',encoding = "utf-8")
df_rating6 = pd.read_csv('./dataset/rating/6.csv',delimiter = ',',encoding = "utf-8")
df_rating7 = pd.read_csv('./dataset/rating/7.csv',delimiter = ',',encoding = "utf-8")
df_rating8 = pd.read_csv('./dataset/rating/8.csv',delimiter = ',',encoding = "utf-8")

#generamos la columna id
df_amazon_prime = df_amazon_prime.assign(id='a' + df_amazon_prime['show_id'].astype(str))
df_disney_plus = df_disney_plus.assign(id='d' + df_disney_plus['show_id'].astype(str))
df_hulu = df_hulu.assign(id='h' + df_hulu['show_id'].astype(str))
df_netflix = df_netflix.assign(id='n' + df_netflix['show_id'].astype(str))

#rellenamos los espacios nulos con la letra G de la columna rating
df_amazon_prime.fillna(value={'rating': 'G'}, inplace=True)
df_disney_plus.fillna(value={'rating': 'G'}, inplace=True)
df_hulu.fillna(value={'rating': 'G'}, inplace=True)
df_netflix.fillna(value={'rating': 'G'}, inplace=True)

#modificamos el formao para qu todos queden igual AAAA-mm-dd
df_amazon_prime['date_added'] = pd.to_datetime(df_amazon_prime['date_added'].astype(str), format='%B %d, %Y')
df_disney_plus['date_added'] = pd.to_datetime(df_disney_plus['date_added'].astype(str), format='%B %d, %Y')
df_hulu['date_added'] = pd.to_datetime(df_hulu['date_added'].astype(str), format='%B %d, %Y')
# antes de convertir al formato pedido se elimino el espacio en blanco de cada texto de la columna 'date_added'
df_netflix['date_added'] = df_netflix['date_added'].str.lstrip() 
df_netflix['date_added'] = pd.to_datetime(df_netflix['date_added'].astype(str), format='%B %d, %Y')



app = FastAPI()

@app.get("/saludar")
def saludar():
    return {"mensaje": "Hola mundo"}