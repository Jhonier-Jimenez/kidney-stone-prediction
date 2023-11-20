# Instrucciones para ejecutar Fase-3

**1**. Primero que todo debemos tener instalado Docker y Docker Compose  y asegurase de que este corriendo o ejecutandose en nuestro ordenador.

![run scripts manually](https://user-images.githubusercontent.com/15114373/284045822-655ccc94-f2af-43f6-ab4a-0e8e614862d8.png)

**2**. Clonamos la carpeta Fase-3 en nuestro IDE.

![run scripts manually](https://user-images.githubusercontent.com/15114373/284045818-135ef85a-0732-4b2e-a034-ecd158d03376.png)

**3**. Una ves estando en el proyecto abrimos una terminal y ejecutamos el siguiente comando: **docker-compose up --build** ,este comando se utiliza para construir y levantar los servicios definidos en el archivo **docker-compose.yml** que se encuentra en el proyecto,este comando es útil cuando queremos realizar cambios en el código fuente o en la configuración del contenedor sin tener que volver a crear la imagen,en caso de realizar un cambio simplemete ejecutamos **docker-compose up** para levantar el servicio de nuevo, ya que asegura que las imágenes se reconstruyan antes de iniciar los servicios.

![run scripts manually](https://user-images.githubusercontent.com/15114373/284045820-8350ee61-0b9c-4639-b7aa-16e16aa5aa3b.png)

**4**. Cuando se construye la imagen y se sube el servicio, nos mostrara el puerto y la ruta donde se esta ejecutando.

![run scripts manually](https://user-images.githubusercontent.com/15114373/284045823-fbbe42b3-eb7d-44f3-9c6a-4619a024e305.png)

y verificamos que en el el Docker Desktop  el contenedor fase_3 se encuentre corriendo. 

![run scripts manually](https://user-images.githubusercontent.com/15114373/284045827-8869ac6a-b92f-4379-a77a-032ed0207b50.png)

**5**. Una ves todo este funcionando correctamente, pasamos hacer las pruebas de los servicios de nuestra API.
En este caso usaremos la herraminta PostMan para consumir nuestra API.
Empezaremos con la prueba de prediccion; Para esto utilizaremos la ruta **http://localhost:8000/predict/** , que pondremos en en el postman usando el metodo **POST**,y luego nos vamos a la pestaña que dice **Body** y luego en **raw** y seleccionamos la opcion de **JSON** y ponemos los datos para hacer la predicion:

**{**

 **"id":691,  
  "gravity":1.021,  
  "ph":5.53,  
  "osmo":874,  
  "cond":17.8,  
  "urea":385,  
  "calc":2.21  
}**

![run scripts manually](https://user-images.githubusercontent.com/15114373/284045828-470b8444-1950-4eef-bc26-8abd1d092cfd.png)

Luego le damos al boton **Send**.
Y nos mostrara el resultado en de la prediccion, en este caso nos muestra un **1** indicandonos que con esos datos la persona posee calculo renal.

![run scripts manually](https://user-images.githubusercontent.com/15114373/284045829-75585881-0adc-4ffa-9c6a-b53fc5980c80.png)

En el caso de que no posea calculo renal saldra como resultado un **0**.

**{**

  **"id":692,  
  "gravity":1.013,  
  "ph":6.19,  
  "osmo":443,  
  "cond":14.8,  
  "urea":124,  
  "calc":1.45  
}**

![run scripts manually](https://user-images.githubusercontent.com/15114373/284045830-a1c11ec6-6582-4542-9ee2-7ebcdbe5a186.png)

Ahora probaremos el servicio de Train con el metodo **POST** con la siguiente ruta: **http://localhost:8000/train/**

Luego le damos al boton **Send**.

![run scripts manually](https://user-images.githubusercontent.com/15114373/284045832-8692481f-5176-4eb1-ad63-43dfcb8e1ba7.png)

En la respuesta nos mostrara un mensaje diciendo que **el modelo fue entrenado y guardado correctamente**.


Este modelo se guardara en nuestro proyecto con el nombre de **modelNew.pkl**.

![run scripts manually](https://user-images.githubusercontent.com/15114373/284045833-73492e81-ccac-4524-9f4b-8612daec7692.png)

