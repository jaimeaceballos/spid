Sistema Policial de Incidencia Delictual de la policia del chubut.

El sistema prentende ser una herramienta de gestion de las causas judiciales generadas en Comisarias, 
estas causas son iniciadas a partir de una denuncia en sede policial. El sistema registra la informacion
que debe ser enviada al MPF (Ministerio Publico Fiscal), autoridades policiales y demas autoridades 
competentes. Tambien provee una importante herramienta de analisis delictual, al ser un repositorio de
toda la informacion generada de causas judiciales, permite la extraccion de la informacion a medida de
la necesidad del analista, y provee una visualizacion espacial de la situacion delictiva de cada 
localidad donde se realiza carga de causas preventivas (Mapa del delito - mapa de puntos).
Tambien se implemeto un servicio de vinculacion con el sistema Coiron, con el fin de alimentar esa base
de datos directamente desde el sistema Policial, cada registro preventivo cargado en el sistema SPID, se
transfiere automaticamente via web service a un mensajero desarrollado por el MPF con el fin de recibir
esta informacion.

Actualmente el sistema SPID, se encuentra siendo migrado desde Django 1.5.1 a la version 1.8.4 del
mismo framework. Para tal tarea fue necesario la instalacion de la herramienta Django-formtools, que dejo
de ser un paquete incluido en la distribucion de django para alivianar el peso del core de django. Para 
tal tarea fue necesario correr el siguiente comando:

$ sudo pip install django-formtools

luego de la instalacion del paquete fue necesario cambiar en el archivo settings, dentro de INSTALLED_APPS
la siguiente linea:

'django.contrib.formtools'

por la siguiente linea:

'formtools'

Otras instalaciones necesarias son:

* wkwtmltopdf
