from fastapi import FastAPI
import pandas as pd
#from surprise import Dataset, Reader, SVD
#from surprise.model_selection import cross_validate
from query import *

app = FastAPI()

@app.on_event('startup')
def startup():
    global df_netflix_ETL, df_amazon_prime_ETL, df_hulu_ETL, df_netflix_ETL, df_disney_plus_ETL, df_platforms_ETL
    df_amazon_prime_ETL = pd.read_csv('./dataset_ETL/amazon_prime_ETL.csv')
    df_disney_plus_ETL = pd.read_csv('./dataset_ETL/disney_plus_ETL.csv')
    df_hulu_ETL = pd.read_csv('./dataset_ETL/hulu_ETL.csv')
    df_netflix_ETL = pd.read_csv('./dataset_ETL/netflix_ETL.csv')
    df_platforms_ETL =  pd.read_csv('./dataset_ETL/df_platforms_ETL.csv')
    

@app.get("/get_max_duration/({anio},{plataforma},{min_o_season})")
async def get_max_duration_1(year: int, platform: str, duration_type: str):
    max_duration_movie = get_max_duration(year, platform, duration_type)
    return {"Titulo": max_duration_movie}

@app.get("/get_scored_count/({plataforma},{puntaje},{anio})")
async def get_scored_count_2(platform: str, scored: float, year: int):
    count = get_score_count(platform, scored, year)
    return {count}

@app.get('/get_count_platform/({plataforma})')
async def get_count_platform_3(platform: str):
    movie = get_count_platform(platform)
    return {'Cantidad de peliculas por plataforma':movie}

@app.get('/get_actor/({plataforma},{anio})')
async def get_actor_4(platform: str, year: int):
    most_frequent_actor = get_actor(platform, year)
    return { most_frequent_actor}


#@app.get('/recommend_movie/({idusuario},{idpelicula}')
#async def recommend_movie_5(user_id: int, movie_id: str):
#    recommend = recommend_movie(user_id, movie_id)
#    return {recommend}