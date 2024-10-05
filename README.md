# BasicTkinterCalculator

## Descripción
Este es un proyecto de una calculadora básica desarrollada en Python utilizando la biblioteca Tkinter para la interfaz gráfica de usuario. La calculadora permite realizar operaciones matemáticas básicas como suma, resta, multiplicación y división.

## Tecnologías Utilizadas
- **Python**: Lenguaje de programación utilizado para desarrollar la lógica de la calculadora.
- **Tkinter**: Biblioteca estándar de Python para la creación de interfaces gráficas de usuario.

## Esquema de Base de Datos
Este proyecto no utiliza una base de datos, por lo que esta sección no aplica.

## Cómo Correr el Proyecto
1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu_usuario/BasicTkinterCalculator.git
    ```
3. Navega al directorio del proyecto:
    ```bash
    cd BasicTkinterCalculator
    ```
4. Ejecuta el archivo principal de la calculadora:
    ```bash
    python calculadora.py
    ```

## Cómo Correr el Comando de Pruebas
1. Asegúrate de tener Python instalado en tu sistema.
2. Navega al directorio del proyecto:
    ```bash
    cd BasicTkinterCalculator
    ```
3. Ejecuta el archivo de pruebas con el comando:
    ```bash
    python -m unittest test_calculator.py
    ```

# CI QA Workflow - BasicTkinterCalculator
Este repositorio implementa un flujo de trabajo de integración continua (CI) para verificar la calidad del código mediante la ejecución de pruebas unitarias en cada pull request hacia la rama qa. El objetivo es asegurar que el código funciona correctamente antes de ser integrado en el entorno de calidad (QA).

# CI QA Workflow
## Descripción
El flujo de trabajo se ejecuta automáticamente cada vez que se crea o actualiza un pull request hacia la rama qa. Durante la ejecución, el sistema realiza las siguientes tareas:

1. Descarga el código del repositorio.
2. Configura el entorno de Python con la versión 3.8.
3. Instala y actualiza las dependencias necesarias.
4. Ejecuta las pruebas unitarias para verificar que el código es funcional.
5. Si las pruebas son exitosas, despliega la aplicación en el servidor de producción.

## Configuración del Flujo de Trabajo
El flujo de trabajo de integración continua (CI) se activa cuando se crea o actualiza un pull request hacia la rama qa. El proceso se ejecuta en un entorno de Ubuntu y consta de varios pasos: primero, se realiza la verificación del código fuente del repositorio; luego, se configura el entorno de Python con la versión 3.8. A continuación, se instalan las dependencias necesarias, y se ejecutan pruebas unitarias para verificar el correcto funcionamiento de la aplicación. Si alguna de las pruebas falla, se genera un mensaje indicando que las pruebas no pasaron, lo que permite a los desarrolladores identificar y solucionar problemas antes de fusionar los cambios en la rama principal.

## Implementación del CD con Ejecutable
Para la fase de Continuous Deployment (CD) del proyecto, se creo un ejecutable, El ejecutable fue generado utilizando la herramienta PyInstaller, que convierte los archivos .py en un ejecutable independiente que contiene todo lo necesario para ejecutar el programa. Esto elimina la necesidad de un intérprete de Python o dependencias externas en el sistema del usuario final.

Pasos para Generar el Ejecutable
Instalación de PyInstaller: Antes de crear el ejecutable, se debe instalar PyInstaller en el entorno de desarrollo. Para ello, se utiliza el siguiente comando:
pip install pyinstaller
Generación del Ejecutable: Una vez instalado PyInstaller, se procede a crear el ejecutable a partir del archivo principal de la calculadora (calculadora.py). El comando es el siguiente:
pyinstaller --onefile calculadora.py

Este proceso de creación del ejecutable se puede integrar en un pipeline de CD, donde, después de que el código haya pasado las pruebas unitarias y esté listo para su despliegue

## Detalles Técnicos
Plataforma: El flujo de trabajo se ejecuta en la versión más reciente de Ubuntu.
Entorno Python: Se utiliza Python 3.8 para la ejecución del código.
Dependencias: El flujo de trabajo asegura que pip está actualizado antes de ejecutar las pruebas.
Pruebas Unitarias: Se ejecutan utilizando el módulo unittest en Python, evaluando el archivo test_calculator.py.
Manejo de Fallos: Si las pruebas fallan, el proceso de CI se detendrá y subirá los resultados de las fallas.

## Cómo Funciona
Este flujo de trabajo es esencial para mantener la calidad del código en el proyecto. Automatiza el proceso de verificación antes de que cualquier cambio sea integrado en la rama qa, lo que ayuda a reducir el riesgo de introducir errores en el entorno de pruebas.


## Contribuidores
- Rayfel Ogando (#1107535) - [Rayfel2](https://github.com/Rayfel2)
- Eladio Tavarez (#1108874) - [Eventr077](https://github.com/Eventr077)
- Diego Rodriguez (#1105880) - [D1egoSebastian](https://github.com/D1egoSebastian)
- Axel Felix (#1106662) - [Notengonombredisponible](https://github.com/Notengonombredisponible)
- Andres Taveras (#1107975) - [FandresT101](https://github.com/FandresT101)
- Angel Soriano (#1107555) - [LoyaKnight](https://github.com/LoyaKnight)
