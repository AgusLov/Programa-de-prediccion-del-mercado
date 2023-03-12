# Programa de prediccion del mercado

Este es mi primer programa escrito en Python que utiliza Facebook Prophet para predecir el precio de apertura de una acción en un período futuro. El programa permite al usuario ingresar el ticker de la acción a analizar y descarga los datos históricos de Yahoo Finance. Luego, ajusta un modelo Prophet y realiza una predicción para el período especificado.

# Créditos
Este programa está basado en el tutorial "Predicción de precios de Ethereum con Python" de Benedict Neo, publicado en Medium (https://medium.com/bitgrit-data-science-publication/ethereum-price-prediction-with-python-3b3805e6e512).

Se ha utilizado su trabajo como base para el análisis de datos, la visualización de gráficos y la implementación del modelo de Prophet para la predicción de precios. También se han realizado algunas modificaciones y se han añadido nuevas funcionalidades.

# Requerimientos
El programa requiere las siguientes librerías de Python:

* pandas
* yfinance
* datetime
* dateutil
* plotly
* fbprophet

Estas librerías se pueden instalar a través del gestor de paquetes pip ejecutando el siguiente comando:
> pip install pandas yfinance datetime dateutil plotly fbprophet

# Cómo utilizar
1. Ejecutá el archivo predict.py en la consola de comandos.

2. Ingresá el ticker de la acción que deseás analizar cuando se te solicite.

3. El programa descargará los datos históricos de la acción y generará un gráfico de la serie de precios de apertura.

4. Si los datos se han descargado correctamente, el programa intentará generar una predicción de precios utilizando el modelo Prophet.

5. El programa generará dos archivos HTML: uno con el gráfico de la predicción y otro con los componentes de la predicción.

Tené en cuenta que si se introduce un ticker inválido o si hay problemas de conexión al descargar los datos, el programa mostrará un mensaje de error y se detendrá. En este caso, deberás reiniciar el programa.

# Limitaciones
El programa tiene las siguientes limitaciones:

* Solo funciona con acciones que se pueden descargar de Yahoo Finance.
* El modelo Prophet asume que los datos son estacionarios y que no hay cambios estructurales en los datos históricos.
* La predicción del modelo Prophet no debe interpretarse como una garantía del precio futuro de la acción.

# Contribuir
Si encontrás algún error o problema en el código, o si deseás contribuir con una nueva funcionalidad, no dudes en abrir un issue o enviar una pull request.
