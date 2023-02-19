import pandas as pd

#************************************ QUERYS**************************************************

df_amazon_prime_ETL = pd.read_csv('./dataset_ETL/amazon_prime_ETL.csv')
df_disney_plus_ETL = pd.read_csv('./dataset_ETL/disney_plus_ETL.csv')
df_hulu_ETL = pd.read_csv('./dataset_ETL/hulu_ETL.csv')
df_netflix_ETL = pd.read_csv('./dataset_ETL/netflix_ETL.csv')


# diccionario de nombres de archivo CSV para cada plataforma
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