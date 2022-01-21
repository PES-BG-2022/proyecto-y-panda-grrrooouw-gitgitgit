En este documento dejaremos los pasos necesarios para poder utilizar el ambiente creado para el scrap de datos:

Paso #0: VITAL
clonar repositorio a tu directorio de trabajo


Paso #1:

Es necesario crear un ambiente virtual (como diría Don Omar: "una diva virtual") nuevo.
Eso implica que se debe ingresar a anaconda prompt, se desactiva el ambiente base y se utiliza el comando siguiente:

conda create -n "nombre del ambiente que quieren sin comillas" python=3.7

Paso #2:

se deben instalar las librerias ubicadas en enviroment_final.yml 

realizar el siguiente comando:

conda env update --name "nombre del ambiente donde se copiaran las librerias/paquetes"--file "dirección donde se encuentra el archivo enviroment_final.yml incluyéndolo"  


Paso #3:
dentro de la terminal, con el ambiente actualizado con las librerias necesarias ingresar el siguiente comando:

cd "el directorio de trabajo donde clonaron el repositorio"


Paso #4:

correr el programa con el siguiente comando:

streamlit run main.py 

GRACIAS por descargar nuestro programa, son $100

   