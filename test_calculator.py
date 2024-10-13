import unittest
from TkinterCalculadora import (
    Calculator as DesktopCalculator,
)  # para calculadora de escritorio
from app import app, Calculator as WebCalculator  # para calculadora web
import tkinter as tk


class TestDesktopCalculator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.calc = DesktopCalculator(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_append_value(self):
        # Prueba la función de añadir valores
        self.calc.append_value("5")
        self.assertEqual(self.calc.result_var.get(), "5")
        self.calc.append_value("3")
        self.assertEqual(self.calc.result_var.get(), "53")

    def test_clear_result(self):
        # Prueba la función de limpiar el resultado
        self.calc.result_var.set("12345")
        self.calc.clear_result()
        self.assertEqual(self.calc.result_var.get(), "")

    def test_calculate_result(self):
        # Prueba la función de calcular resultados
        self.calc.result_var.set("5+3")
        self.calc.calculate_result()
        self.assertEqual(self.calc.result_var.get(), "8")

        self.calc.result_var.set("10/2")
        self.calc.calculate_result()
        self.assertEqual(self.calc.result_var.get(), "5.0")

        # Prueba de manejo de errores
        self.calc.result_var.set("5/0")
        self.calc.calculate_result()
        self.assertEqual(self.calc.result_var.get(), "Error")


class TestWebCalculator(unittest.TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        self.app = app.test_client()
        self.app.testing = True

    def test_calculator_append_value(self):
        calculator = WebCalculator()
        calculator.append_value(5)
        self.assertEqual(calculator.result, "5")
        calculator.append_value("+")
        calculator.append_value(3)
        self.assertEqual(calculator.result, "5+3")

    def test_calculator_clear_result(self):
        calculator = WebCalculator()
        calculator.append_value(10)
        calculator.clear_result()
        self.assertEqual(calculator.result, "")

    def test_calculator_calculate_result_valid_expression(self):
        calculator = WebCalculator()
        calculator.append_value(10)
        calculator.append_value("+")
        calculator.append_value(5)
        calculator.calculate_result()
        self.assertEqual(calculator.result, "15")

    def test_calculator_calculate_result_invalid_expression(self):
        calculator = WebCalculator()
        calculator.append_value(10)
        calculator.append_value("/")
        calculator.append_value(0)
        calculator.calculate_result()
        self.assertEqual(calculator.result, "Error")

    def test_calculator_calculate_result_syntax_error(self):
        calculator = WebCalculator()
        calculator.append_value("10 +")
        calculator.calculate_result()
        self.assertEqual(calculator.result, "Error")

    def test_index_get(self):
        # Prueba la respuesta GET en la ruta principal
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"current_input", response.data
        )  # Verifica que la plantilla se esté renderizando

    def test_index_post_append(self):
        # Prueba la acción de agregar un valor
        response = self.app.post(
            "/", data={"action": "append", "value": "5", "current_input": ""}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"5", response.data)

    def test_index_post_clear(self):
        # Prueba la acción de limpiar el resultado
        response = self.app.post(
            "/", data={"action": "clear", "value": "", "current_input": "10"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"", response.data)

    def test_index_post_calculate(self):
        # Prueba la acción de calcular
        response = self.app.post(
            "/", data={"action": "calculate", "value": "", "current_input": "10+5"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"15", response.data)


if __name__ == "__main__":
    unittest.main()
