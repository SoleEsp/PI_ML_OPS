from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Mi aplicación personalizada")

df_amazon_prime_ETL = pd.read_csv('./dataset_ETL/amazon_prime_ETL.csv')
df_disney_plus_ETL = pd.read_csv('./dataset_ETL/disney_plus_ETL.csv')
df_hulu_ETL = pd.read_csv('./dataset_ETL/hulu_ETL.csv')
df_netflix_ETL = pd.read_csv('./dataset_ETL/netflix_ETL.csv')
df_platforms_ETL =  pd.read_parquet('./dataset_ETL/df_platforms_ETL.parquet')

dataframe = {
        'Netflix': df_netflix_ETL,
        'Amazon': df_amazon_prime_ETL,
        'Disney': df_disney_plus_ETL,
        'Hulu': df_hulu_ETL
    }    

@app.get("/")
async def root():
    return {"message": "Proyecto Individual 01 - Espiritu, Soledad. Gracias por testear mi api!"}

@app.get("/get_max_duration/({anio},{plataforma},{min_o_season})")
async def get_max_duration_1(year: int, platform: str, duration_type: str):
    
    if platform not in dataframe:
        return f'La plataforma "{platform}" no es válida. Las plataformas válidas son: Netflix, Disney, Amazon, Hulu.'
    
    #seleccionamos el dataframe segun lo ingresado
    selected_df = dataframe[platform]
    
    if duration_type not in ['min', 'season']:
        return f'Por favor ingrese alguno de los siguientes valores correctos\n duration_type: min o season'
    
    #se filtra el df segun el año y tipo de duracion
    selected_movies = selected_df.loc[(selected_df["release_year"] == year) & (selected_df["duration_type"] == duration_type)]
    
    if selected_movies.empty:
        return f"No hay resultados para el año {year}. Intente con otro año."
    
    # se obtiene el de mas duracion    
    max_duration_movie = selected_movies.loc[selected_movies["duration_int"].idxmax()]['title']

    return {"Titulo": max_duration_movie}

@app.get("/get_scored_count/({plataforma},{puntaje},{anio})")
async def get_scored_count_2(platform: str, scored: float, year: int):
    
    #validacion de palabras correctas
    if platform not in dataframe.keys():
        return f'La plataforma "{platform}" no es válida. Las plataformas válidas son: Netflix, Disney, Amazon, Hulu.'
    
    # Obtener la inicial de la plataforma
    platform_id = platform.lower()[0]
    
    df_filtered = df_platforms_ETL[df_platforms_ETL['type'] == 'movie']
    
    # Filtrar el DataFrame por plataforma y año
    df_filtered = df_platforms_ETL[(df_platforms_ETL['id'].str.startswith(platform_id)) & (df_platforms_ETL['release_year'] == year)]
    
    if df_filtered.empty:
        return f"No se encontraron resultados para el año {year}. Intente con otro año."
    
    #value_counts = df_filtered['scored'].value_counts()
    
    # Contar la cantidad de películas que tienen un puntaje mayor a scored
    count = len(df_filtered[df_filtered['scored'] > scored])
    
    return {'Cantidad de peliculas ': count}

@app.get('/get_count_platform/({plataforma})')
async def get_count_platform_3(platform: str):
    
    if platform not in dataframe:
        return f'La plataforma "{platform}" no es válida. Las plataformas válidas son: Netflix, Disney, Amazon, Hulu.'
    
    # se filtra segun la plataforma y solo peliculas
    selected_df = dataframe[platform]
    movie = selected_df[selected_df['type'] == 'movie']
    
    return {'Cantidad de peliculas por plataforma':movie.shape[0]}

@app.get('/get_actor/({plataforma},{anio})')
async def get_actor_4(platform: str, year: int):
    
    if platform not in dataframe:
        return f'La plataforma "{platform}" no es válida. Las plataformas válidas son: Netflix, Disney, Amazon, Hulu.'
    
    selected_df = dataframe[platform]
    
    df_year = selected_df[selected_df['release_year'] == year]
    
    if df_year.empty:
        return f"No se encontraron resultados para el año {year}. Intente con otro año."
    
    actor_counts = df_year['cast'].str.split(',').explode().str.strip().value_counts()
    
    most_frequent_actor = actor_counts.index[0]
    
    return  f"Actor: {most_frequent_actor}. Cantidad de veces repetida: {actor_counts[most_frequent_actor]}"
