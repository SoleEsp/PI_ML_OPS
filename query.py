import pandas as pd

#************************************ QUERYS**************************************************

def get_max_duration(year, platform, duration_type):
    # diccionario de nombres de archivo CSV para cada plataforma
    dataframe = {
        'Netflix': df_netflix,
        'Amazon': df_amazon_prime,
        'Disney': df_disney_plus,
        'Hulu': df_hulu
    }

    if platform not in dataframe:
        return print(f'La plataforma "{platform}" no es válida. Las plataformas válidas son: Netflix, Disney, Amazon, Hulu.')
    
    selected_df = dataframe[platform]
    
    if duration_type not in ['min', 'season']:
        return print(f'Por favor ingrese alguno de los siguientes valores correctos\n duration_type: min o season')
    
    selected_movies = selected_df.loc[(selected_df["release_year"] == year) & (selected_df["duration_type"] == duration_type)]

    if selected_movies.empty:
        return print(f"No hay resultados para el año {year}. Intente con otro año.")
            
    max_duration_movie = selected_movies.loc[selected_movies["duration_int"].idxmax()]['title']

    return print('Titulo: ',max_duration_movie)