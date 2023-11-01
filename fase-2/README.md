# Instrucciones de la Fase-2

Para ejecutar correctamente la aplicación es necesario que tengas instalado Docker y que construyas una imagen de docker a partir del archivo Dockerfile y las dependencias indicadas en requirements.txt

Una vez construida la imagen, sólo es necesario ejecutarla

## Dockerfile

Puedes construir el docker file tal como está en el repositorio, y tendrás acceso a la consola, donde podrás ejecutar train.py y predict.py

![run scripts manually](https://github.com/Jhonier-Jimenez/kidney-stone-prediction/assets/32853930/f52c9d00-36ec-4a3c-9779-64be1540753a)


O puedes descomentar la sección CMD del docker file para que train.py y predict.py se ejecuten automaticamente al ejecutar el docker file

![image](https://github.com/Jhonier-Jimenez/kidney-stone-prediction/assets/32853930/3bfb3586-24d4-4b67-98c6-921dbb39ed6d)

![run scripts automatically](https://github.com/Jhonier-Jimenez/kidney-stone-prediction/assets/32853930/a48870b2-80eb-4196-8c36-c3248ac3fc7a)

## Descripción de los archivos.ipynb

- ### **01_generate_data_and_model**
En este fichero se puede observar cómo se simplifica el proceso que se entregó en la fase-1, y cómo usamos los datos para entrenar un modelo utilizando XGBClassifier.
Esta lógica es la que se lleva posteriormente para crear train.py

- ### 02_run_scripts
En este fichero podemos ver cómo se hace uso de train.py y predict.py desde una consola.

## Descripción de los contenidos de las carpetas

### Datasets

Ficheros train.csv y test.csv para entrenar y posteriormente predecir con el modelo, respectivamente

### Predictions

Fichero predictions.csv donde se guarda y se sobreescribe cada predicción hecha con el modelo

### Scripts

1. ##### train.py
   Con este script se puede entrenar el modelo
   Se puede indicar los siguientes parametros:

- --data_file: Conjunto de datos con los que será entrenado el modelo
- --model_file: Archivo donde será guardado el modelo
- --overwrite_model: En caso de que el modelo ya exista en la raíz del proyecto, deberá especificarse este parámetro para poder sobreescribirlo.

2. ##### predict.py

Con este script se pueden hacer predicciones usando un .pkl ya existente
Se puede indicar los siguientes parametros:

- --input_file: Conjunto de datos con los que será probado el modelo
- --model_file: Modelo con el que se hará la predicción
- --predictions_file: fichero donde se guardan las predicciones hechas con el modelo

### Nota

Cualquier parámetro que sea omitido, tomará los valores entregados por defecto
Ej: Si no especificas el predictions_file donde quieras guardar el resultado de las predicciones, al usar predict.py ; por defecto el resultado de las predicciones será sobre escrito en predictions.csv

