## Sistema Experto de Evaluación de Créditos Hipotecarios
Este proyecto implementa un sistema experto para evaluar solicitudes de créditos hipotecarios utilizando Streamlit para la interfaz de usuario y Experta para el motor de inferencia basado en reglas.

## Descripción
El sistema permite a los usuarios ingresar sus datos personales y laborales, así como información sobre la propiedad que desean adquirir y el plazo de devolución del préstamo. Basado en un conjunto de reglas predefinidas, el sistema evalúa la elegibilidad del solicitante y, en caso de ser aprobado, calcula una cuota mensual estimada.

## Características
Interfaz de Usuario Intuitiva: Desarrollada con Streamlit para una fácil interacción.

Motor de Reglas: Utiliza la librería Experta para aplicar reglas de negocio en la evaluación de créditos.

Validación de Requisitos: Evalúa la edad, antigüedad laboral, sueldo y tipo de trabajo del solicitante.

Cálculo de Cuota: Si el crédito es aprobado, calcula la cuota mensual estimada basándose en el valor(en pesos) de la propiedad, la cantidad de UVA, la tasa de interés (que varía según el tipo de trabajo) y el plazo de devolución.

## Reglas de Negocio
El motor de reglas (MotorCredito) aplica las siguientes validaciones y cálculos:

Edad: El solicitante debe tener entre 18 y 80 años.

Sueldo Mínimo: El sueldo debe ser igual o superior a $1000.

Tipo de Trabajo: El solicitante debe estar "En relación de dependencia" o ser "Monotributista". No se aprueban créditos para trabajos "Informales".

Antigüedad Laboral: El solicitante debe tener una antigüedad mínima de 3 años en su trabajo actual.

Aprobación de Préstamo:

Se calcula la cuota mensual del préstamo hipotecario.

La tasa de interés es del 6% anual para "En relación de dependencia" y del 8% anual para "Monotributo".

La cuota mensual calculada no debe superar el 25% del sueldo del solicitante.

## Cómo Ejecutar el Sistema
Para ejecutar este sistema experto en tu máquina local, sigue los siguientes pasos:

## Clonar el repositorio (o guardar los archivos):
Asegúrate de tener los archivos main.py, motor.py y utils.py en la misma carpeta. Para este ejemplo, asumiremos que el archivo principal se llama main.py y contiene la clase SistemaExperto, y que motor.py contiene MotorCredito.

## Construir imagen de docker:
Parado sobre el root del proyecto, en la terminal ejecuta el siguiente comando:

docker build -t sistema-experto .

## Ejecutar la aplicación
docker run --name sistema-experto -p 8501:8501 sistema-experto

Esto levantará la aplicación y podrás acceder desde tu navegador en:
http://localhost:8501

## Alternativa Docker Hub
Crearse una cuenta si es que no se tiene
docker login -> para loguearse
docker pull tiagocae32/sistema-experto:firstappdockerse
docker run --name sistema-experto -p 8501:8501 tiagocae32/sistema-experto:firstappdockerse
Une vez que ya esta creado el contenedor -> docker start sistema-experto

## Estructura del Código
main.py: Contiene la clase SistemaExperto que maneja la interfaz de usuario de Streamlit y orquesta la evaluación del crédito.

motor.py: Define la clase MotorCredito, que hereda de KnowledgeEngine de Experta e implementa las reglas de negocio para la evaluación del crédito.

utils.py: Contiene funciones de utilidad, como to_int para convertir cadenas a enteros de forma segura.

## Url Deploy
https://sistema-experto-2uzzennqwtbwpd4vrsmkbu.streamlit.app/
