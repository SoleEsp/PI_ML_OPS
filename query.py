import pandas as pd
#from surprise import Dataset, Reader, SVD
#from surprise.model_selection import cross_validate


#************************************ QUERYS**************************************************

df_amazon_prime_ETL = pd.read_csv('./dataset_ETL/amazon_prime_ETL.csv')
df_disney_plus_ETL = pd.read_csv('./dataset_ETL/disney_plus_ETL.csv')
df_hulu_ETL = pd.read_csv('./dataset_ETL/hulu_ETL.csv')
df_netflix_ETL = pd.read_csv('./dataset_ETL/netflix_ETL.csv')

df_platforms_ETL = pd.read_csv('./dataset_ETL/df_platforms_ETL.csv')

# diccionario de nombres de archivo CSV para cada plataforma
# se sigue manteniendo de esta forma para que la ejecucion de los query sea mas rapida
# solo se utlizara el df_platforms cuando sea necesario, ya que la ejecucion demora en dar un resultado

dataframe = {
        'Netflix': df_netflix_ETL,
        'Amazon': df_amazon_prime_ETL,
        'Disney': df_disney_plus_ETL,
        'Hulu': df_hulu_ETL
    }

def get_max_duration(year, platform, duration_type):
    
    if platform not in dataframe:
        return f'La plataforma "{platform}" no es válida. Las plataformas válidas son: Netflix, Disney, Amazon, Hulu.'
    
    selected_df = dataframe[platform]
    
    if duration_type not in ['min', 'season']:
        return f'Por favor ingrese alguno de los siguientes valores correctos\n duration_type: min o season'
    
    selected_movies = selected_df.loc[(selected_df["release_year"] == year) & (selected_df["duration_type"] == duration_type)]
    
    if selected_movies.empty:
        return f"No hay resultados para el año {year}. Intente con otro año."
        
    max_duration_movie = selected_movies.loc[selected_movies["duration_int"].idxmax()]['title']

    return max_duration_movie

def get_score_count(platform, scored, year):
    
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
    
    return f'Cantidad de peliculas : {count}'


def get_count_platform(platform):
    
    if platform not in dataframe:
        return f'La plataforma "{platform}" no es válida. Las plataformas válidas son: Netflix, Disney, Amazon, Hulu.'
    
    selected_df = dataframe[platform]
    movie = selected_df[selected_df['type'] == 'movie']
    
    return movie.shape[0]

def get_actor(platform,year):
    
    if platform not in dataframe:
        return f'La plataforma "{platform}" no es válida. Las plataformas válidas son: Netflix, Disney, Amazon, Hulu.'
    
    selected_df = dataframe[platform]
    
    df_year = selected_df[selected_df['release_year'] == year]
    
    if df_year.empty:
        return f"No se encontraron resultados para el año {year}. Intente con otro año."
    
    actor_counts = df_year['cast'].str.split(',').explode().str.strip().value_counts()
    
    most_frequent_actor = actor_counts.index[0]
    
    return f"Actor: {most_frequent_actor}, Cantidad de veces repetida: {actor_counts[most_frequent_actor]}"

''''
def recommend_movie(user_id, movie_id):
    # Seleccionar solo las columnas necesarias
    ratings = df_platforms_ETL[['userId', 'title', 'scored']]

    # Definir el rango de calificaciones
    reader = Reader(rating_scale=(1, 5))

    # Cargar los datos
    data = Dataset.load_from_df(ratings, reader)

    # Entrenar el modelo
    algo = SVD()
    trainset = data.build_full_trainset()
    algo.fit(trainset)

    # Predecir la calificación del usuario para la película
    prediction = algo.predict(user_id, movie_id, verbose=False)

    # Obtener la predicción y devolver si la película es recomendada o no
    if prediction.est >= 3.5:
        return f"La película es recomendada."
    else:
        return f"La película no es recomendada."
'''