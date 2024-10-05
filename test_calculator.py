import unittest
from TkinterCalculadora import Calculator  # Cambia esto por la ruta correcta de tu archivo de calculadora
import tkinter as tk

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.calc = Calculator(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_append_value(self):
        # Prueba la función de añadir valores
        self.calc.append_value('5')
        self.assertEqual(self.calc.result_var.get(), '5')
        self.calc.append_value('3')
        self.assertEqual(self.calc.result_var.get(), '53')

    def test_clear_result(self):
        # Prueba la función de limpiar el resultado
        self.calc.result_var.set("12345")
        self.calc.clear_result()
        self.assertEqual(self.calc.result_var.get(), "")

    def test_calculate_result(self):
        # Prueba la función de calcular resultados
        self.calc.result_var.set("5+3")
        self.calc.calculate_result()
        self.assertEqual(self.calc.result_var.get(), '8')

        self.calc.result_var.set("10/2")
        self.calc.calculate_result()
        self.assertEqual(self.calc.result_var.get(), '5.2')

        # Prueba de manejo de errores
        self.calc.result_var.set("5/0")
        self.calc.calculate_result()
        self.assertEqual(self.calc.result_var.get(), "Error")

if __name__ == "__main__":
    unittest.main()
