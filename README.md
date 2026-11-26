# Examen Final - Programación Web

Este proyecto fue realizado para el examen final de Programación Web, utilizando Python, Flask, HTML y CSS.

La idea es crear una página principal desde la cual se pueda ingresar a dos ejercicios.

## Ejercicio 1: Compra de pinturas

En este ejercicio se creó un formulario donde se ingresa el nombre, la edad y la cantidad de tarros de pintura que se quieren comprar.

Cada tarro cuesta $9.000 y el descuento depende de la edad:

- Menores de 18 años: sin descuento.
- Entre 18 y 30 años: 15% de descuento.
- Mayores de 30 años: 25% de descuento.

Al presionar el botón de calcular, se muestra el precio original, el descuento y el total que se debe pagar.

## Ejercicio 2: Inicio de sesión

En este ejercicio se creó un formulario para ingresar un usuario y contraseña.

Se utilizan dos usuarios de prueba:

- **juan** / **admin**
- **pepe** / **user**

Si los datos son correctos, aparece un mensaje de bienvenida. Si no coinciden, se muestra un mensaje de error.

## Herramientas utilizadas

- Python
- Flask
- HTML
- CSS
- PyCharm

## Cómo ejecutar el proyecto

1. Abrir el proyecto en PyCharm.
2. Instalar las dependencias con `pip install -r requirements.txt`.
3. Ejecutar el archivo `main.py`.
4. Abrir `http://127.0.0.1:5000/` en el navegador.

## Comentario final

Con este trabajo pude practicar la creación de páginas HTML, el uso de formularios, los estilos CSS y la conexión de estos elementos con Python mediante Flask.