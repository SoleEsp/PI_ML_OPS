import pandas as pd

#************************************ QUERYS**************************************************

df_amazon_prime_ETL = pd.read_csv('./dataset_ETL/amazon_prime_ETL.csv')
df_disney_plus_ETL = pd.read_csv('./dataset_ETL/disney_plus_ETL.csv')
df_hulu_ETL = pd.read_csv('./dataset_ETL/hulu_ETL.csv')
df_netflix_ETL = pd.read_csv('./dataset_ETL/netflix_ETL.csv')

def get_max_duration(year, platform, duration_type):
    # diccionario de nombres de archivo CSV para cada plataforma
    dataframe = {
        'netflix': df_netflix_ETL,
        'amazon': df_amazon_prime_ETL,
        'disney': df_disney_plus_ETL,
        'hulu': df_hulu_ETL
    }

    selected_df = dataframe[platform]
    
    selected_movies = selected_df.loc[(selected_df["release_year"] == year) & (selected_df["duration_type"] == duration_type)]
        
    max_duration_movie = selected_movies.loc[selected_movies["duration_int"].idxmax()]['title']

    return max_duration_movie

def get_count_platform(platform):
    
    dataframe = {
        'netflix': df_netflix_ETL,
        'amazon': df_amazon_prime_ETL,
        'disney': df_disney_plus_ETL,
        'hulu': df_hulu_ETL
    }
    
    selected_df = dataframe[platform]
    movie = selected_df[selected_df['type'] == 'movie']
    
    return movie.shape[0]

def get_actor(platform,year):
    dataframe = {
        'netflix': df_netflix_ETL,
        'amazon': df_amazon_prime_ETL,
        'disney': df_disney_plus_ETL,
        'hulu': df_hulu_ETL
    }
    
    selected_df = dataframe[platform]
    
    df_year = selected_df[selected_df['release_year'] == year]
    
    actor_counts = df_year['cast'].str.split(',').explode().str.strip().value_counts()
    
    most_frequent_actor = actor_counts.index[0]
    
    return most_frequent_actor

get_actor('amazon',2020)
# get_count_platform('amazon')

#get_max_duration(2020,'disney','min')