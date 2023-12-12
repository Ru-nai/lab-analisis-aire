SELECT Edited_US_Cities_Demographics.City, Edited_US_Cities_Demographics.State, Edited_US_Cities_Demographics."Total Population", ciudades_calidad_aire.overall_aqi
FROM Edited_US_Cities_Demographics
INNER JOIN (
    SELECT city, overall_aqi
    FROM ciudades_calidad_aire
    LIMIT 10
) ciudades_calidad_aire
ON LOWER(Edited_US_Cities_Demographics.City) = LOWER(ciudades_calidad_aire.city);



-///-///-///-///-///-///-///-

La consulta está seleccionando los datos tanto de la tabla 'Edited_US_Cites_Demographics' 
como del archivo .csv 'ciudades_calidad_aire.csv'.
Selecciona las columnas involucradas y relevantes para la consulta, siendo la tabla principial de la que 
se seleccionarán los datos: 'Edited_US_Cities_Demographics'. Toma la ciudad, el estado y la población total
(City, State, Total Population) de la tabla 'Edited_US_Cities_Demographics'; y como subconsulta toma y une
la columna 'city' y 'overall_aqi' del archivo 'ciudades_calidad_aire.csv', y limita el resultado de la consulta a las primeras 10 ciudades del archivo .csv 
Con 'ON' se especifica que las ciudades de la tabla 'Edited_US_Cities_Demographics' y las ciudades del archivo
'ciudades_calidad_aire.csv' tienen que coincidir e ignorar las diferencias de mayúsculas / minúsculas, convirtiendo todo a minúscula

-///-///-///-///-///-///-///-

Estos fueron los resultados de la función 'ej_5_analizar_calidad_aire_vs_poblacion':

                City       State  Total Population  overall_aqi
0          melbourne     Florida             80136          139
1          rochester   Minnesota            112216           53
2          rochester    New York            209808           53
3              flint    Michigan             98297           44
4              eagan   Minnesota             66288           32
5          daly city  California            106574           93
6   town 'n' country     Florida             78996           53
7          san ramon  California             76132           27
8          fairfield  California            112972           35
9      santa clarita  California            182367           73
10     silver spring    Maryland             82463           34


Al revisar estos resultados, se puede concluir que no hay una correlación totalmente clara entre la densidad poblacional y la calidad del aire.  
Si bien algunas ciudades con mayor población demuestran una calidad de aire mala  o moderadamente mala, hay otras ciudades en esta misma representación que, teniendo índices poblacionales similares, presentan una calidad de aire moderada o relativamente buena:

- Melbourne, Florida: Con una población de 80,136, su índice de 139  indica una calidad de aire moderamente mala. 

- Rochester, Minnesota: Población de 112,216, índice de calidad de aire de 53, indica calidad de aire  moderada. Es 28.59% mayor en población a Melbourne, FL, sin embargo, su índice de calidad de aire está por debajo en un 61.67%

- Rochester, Nueva York: Esta ciudad de Nueva York casi duplica a Rochester en Minnesota (209,808), sin embargo, su índice de calidad del aire es similar a Rochester, Minnesota, con un valor de 53. Rochester, NY, tiene una población 60.81% mayor a Melbourne, FL, pero su índice de calidad de aire también está por debajo del de Melbourne por 61.67%

- Flint, Michigan: Población de 98,297, calidad de aire de 44, representa una una calidad del aire relativamente buena. Siendo su población 18.48% mayor a la de Melbourne, FL, su AQI es 68.35% menor a la de Melbourne.

- Eagan, Minnesota: Con una población de 66,288, su calidad de aire tiene un índice de 32, lo cual indica una buena calidad de aire. Su población está un 17.28% por debajo que la de Melbourne, FL, y su AQI es 76.98% menor

- Daly City, California: Población de 106,574, AQI de 93, calidad de aire moderamente mala. Teniendo una población de 7.77% mayor a Flint, Michigan, y 5.03% menor a Rochester, Minnesota, Daly City tiene un AQI entre 43.01% y 52.69% mayor a estas ciudades.

- Town 'n' Country, Florida: Población de 78,996, AQI de 53, está en un lugar similar a Rochester, Minnesota

- San Ramon, California (overall_aqi: 27): Cuenta con una buena calidad de aire, un AQI de 27 con una población de 76,132 (ligeramente por debajo de Town 'n' Country, pero superando en un 49.06% su calidad de aire según su AQI)

- Fairfield, California: A pesar de tener una población de 112,972 (similar a Rochester, Minnesota), Fairfield muestra un índice de calidad del aire de 35, siendo este índice 33.96% menor al de Rochester, Minnesota, sugiriendo una calidad del aire relativamente buena.

- Santa Clarita, California: Tiene una población de 182,367 y un índice de calidad del aire de 73, indicando una calidad del aire moderadamente mala. Su población es menor a la de Rochester, Nueva York, pero su AQI es 27.40% mayor al de esta ciudad.

En este caso, puede ser que esta conclusión sea precipitada teniendo en cuenta que se está sacando en base a solo 10 resultados, y habría que hacer un análisis más detallado, considerando distintos factores que puedan afectar la calidad de aire para determinar el motivo por el cuál hay ciudades en  las que el AQI es 'peor' que en otras ciudades si es que la cantidad de la población no influye directamente o significativamente a estos índices.



