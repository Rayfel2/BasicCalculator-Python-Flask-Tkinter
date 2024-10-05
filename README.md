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

# BasicTkinterCalculator - CI QA Workflow
Este repositorio implementa un flujo de trabajo de integración continua (CI) para verificar la calidad del código mediante la ejecución de pruebas unitarias en cada pull request hacia la rama qa. El objetivo es asegurar que el código funciona correctamente antes de ser integrado en el entorno de calidad (QA).

# CI QA Workflow
## Descripción
El flujo de trabajo se ejecuta automáticamente cada vez que se crea o actualiza un pull request hacia la rama qa. Durante la ejecución, el sistema realiza las siguientes tareas:

Descarga el código del repositorio.
Configura el entorno de Python con la versión 3.8.
Instala y actualiza las dependencias necesarias.
Ejecuta las pruebas unitarias para verificar la funcionalidad del código.
Si las pruebas fallan, sube los resultados de las fallas.

## Configuración del Flujo de Trabajo
name: CI QA Workflow (BasicTkinterCalculator)

on:
  pull_request:
    branches:
      - qa

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip

      - name: Run unit tests
        run: |
          python -m unittest test_calculator.py
        continue-on-error: false

      - name: Upload test results on failure
        if: failure()
        run: |
          echo "Las pruebas fallaron. Subiendo los resultados..."
          
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
