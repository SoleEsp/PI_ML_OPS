
# <h1 align=center> **PI_01_Data_Engineer-EDA-ETL-FastAPI-DetaSpace** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>
<hr>  

## **PROYECTO INDIVIDUAL Nº1 para Henry_ Febrero 2023 _ Data Engineering**

## Contexto

Este es un proyecto el cual se trabaja sobre archivos en csv y json, luego se hace un EDA y ETL (solo a los fines de este proyecto), para luego levantarlo en una API hecha por fastAPI

## Introducción

Soy Soledad Espiritu, en esta oportunidad estoy realizando este proyecto, como parte de los laboratorios de Henry donde he realizado un Bootcamp de 6 módulos, intensivos.

<p


## **Propuesta de trabajo**

Este proyecto tiene como objetivo realizar una ingestión de datos desde diversas fuentes, aplicar transformaciones pertinentes y hacer los datos limpios disponibles para su consulta a través de una API construida en un entorno virtual dockerizado.

Los datos serán proporcionados en diferentes formatos, como archivos CSV, JSON y PARQUET. Para asegurar que los datos sean precisos y útiles, se realizará un análisis exploratorio de datos (EDA) para cada conjunto de datos. Luego, los conjuntos de datos se relacionarán entre sí para permitir el acceso a la información a través de consultas a la API.

 La API permitirá a los usuarios realizar consultas y acceder a los datos limpios que se han procesado y almacenado en el sistema.
<br/>

Las consultas que se realizan son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:

    El función debe ser: get_max_duration(year, platform, duration_type)

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año:

    la función debe ser: get_score_count(platform, scored, year))

+ Cantidad de películas por plataforma con filtro de PLATAFORMA. 

    La función debe ser: get_count_platform(platform)

+ Actor que más se repite según plataforma y año:

    La función debe ser: get_actor(platform, year)

+ Sistema de recomendacion:

    La funcion debe ser: recommender_movie(id_user, movie_id)


<br/>


**`Trabajo Realizado`**:

+ El análisis exploratorio de datos (EDA) se llevó a cabo con el objetivo de cumplir con los objetivos establecidos. Durante el EDA, se analizaron los valores faltantes y los errores en la estructura de los conjuntos de datos proporcionados. Se enfocó en los datos que serían utilizados para realizar las consultas finales, con el fin de garantizar que los datos estén limpios y listos para ser utilizados en la API.

+ Durante el proceso de ETL (extracción, transformación y carga) de datos, se realizó una limpieza exhaustiva de los datos, enfocándonos en el objetivo propuesto.

Para mejorar el rendimiento y evitar problemas de tiempo de respuesta en la ejecución de consultas, se trabajó con cada archivo .csv por separado durante el proceso de ETL. De esta manera, se evitó que el procesamiento de grandes volúmenes de datos en un solo archivo afecte el rendimiento de la API.

Además, es importante destacar que, en aquellos casos en que era necesario trabajar con un archivo grande, se tomaron medidas para minimizar su impacto en el rendimiento de la API. Para ello, se seleccionaron únicamente las columnas necesarias para las consultas y se eliminaron aquellas que no eran relevantes.
<br/>

**`Estructura de carpetas`**:

+ EDA

    - archivo jupiter Notebook (con anotaciones en markdown de los pasos realizados)

+ ETL

    - archivo jupiter Notebook con las consignas resueltas (contiene anotaciones en markdown de los pasos realizados)

+ dataset: contiene los archivos .csv para trabajarlos

+ dataset_ETL: contiene los archivos que se crearon luego de aplicar las consignas propuestas



Archivos globales:

    + main.py (Estructura de API)


<br/>

<br/>

## **Material consultado**

+ https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

+ https://fastapi.tiangolo.com/tutorial/
  
+ https://github.com/juliom86/awesome-RecSys

+ https://pandas.pydata.org/docs/development/contributing_docstring.html


