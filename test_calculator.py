"""
Модуль с unit-тестами для проверки функций калькулятора.
Использует встроенную библиотеку unittest.
"""
import unittest
from calculatot import add, subtract, multiply, divide



class TestCalculator(unittest.TestCase):
    """
    Набор тестов для проверки арифметических операций.
    Каждый метод тестирует одну функцию.
    """

    def test_add(self):
        """
        ТЕСТ №1. Проверка функции сложения.
        Проверяем:
         - сложение положительных чисел
         - сложение отрицательных чисел
         - сложение с нулём
         - сложение дробных чисел
        """
        print("Тестирование функции add...")

        # Положительные числа
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)

        # Отрицательные числа
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -3), -8)

        # Ноль
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 7), 7)

        # Дробные числа
        self.assertEqual(add(2.5, 3.5), 6.0)
        # допустимое округление при проверке плавающих чисел
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=1)

        print("✅ test_add пройден")

    def test_subtract(self):
        """
        ТЕСТ №2. Проверка функции вычитания.
        Проверяем:
         - вычитание положительных чисел
         - вычитание отрицательных чисел
         - вычитание с нулём
         - получение отрицательного результата
         - дробные числа
        """
        print("Тестирование функции subtract...")

        # Положительные числа
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(100, 50), 50)

        # Равные числа
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(0, 0), 0)

        # Отрицательный результат
        self.assertEqual(subtract(3, 10), -7)
        self.assertEqual(subtract(0, 5), -5)

        # Отрицательные числа
        self.assertEqual(subtract(-2, -2), 0)
        self.assertEqual(subtract(-5, -3), -2)

        # Дробные числа
        self.assertEqual(subtract(2.5, 1.5), 1.0)

        print("✅ test_subtract пройден")

    def test_multiply(self):
        """
        ТЕСТ №3. Проверка функции умножения.
        Проверяем:
         - умножение на ноль
         - умножение положительных чисел
         - умножение отрицательных чисел
         - умножение дробных чисел
         ВНИМАНИЕ: в учебных примерах иногда тесты могут изначально падать намеренно.
                """
        print("Тестирование функции multiply...")

        # Умножение на ноль
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0, 0), 0)

        # Положительные числа
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(7, 8), 56)
        self.assertEqual(multiply(2, 100), 200)

        # Отрицательные числа
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(5, -4), -20)
        self.assertEqual(multiply(-3, -3), 9)

        # Дробные числа
        self.assertEqual(multiply(2.5, 2), 5.0)
        self.assertAlmostEqual(multiply(1.5, 1.5), 2.25, places=2)

        print("✅ test_multiply пройден")

    def test_divide(self):
        """
        ТЕСТ №4. Проверка функции деления (без деления на ноль).
        Проверяем:
         - деление целых чисел
         - деление отрицательных чисел
         - получение дробных результатов
         - деление нуля (0 / x)
        """
        print("Тестирование функции divide...")

        # Целочисленное деление (результат — число с плавающей точкой)
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(100, 4), 25.0)

        # Дробные результаты
        self.assertEqual(divide(5, 2), 2.5)
        self.assertAlmostEqual(divide(7, 2), 3.5, places=1)

        # Деление отрицательных чисел
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)

        # Деление нуля
        self.assertEqual(divide(0, 5), 0.0)

        print("✅ test_divide пройден")

        # Деление с дробным результатом
        self.assertEqual(divide(7, 2), 3.5)
        self.assertAlmostEqual(divide(1, 3), 0.333333, places=5)

        # Деление отрицательных чисел
        self.assertEqual(divide(-6, 2), -3.0)
        self.assertEqual(divide(8, -2), -4.0)
        self.assertEqual(divide(-8, -2), 4.0)

        # Деление нуля
        self.assertEqual(divide(0, 5), 0.0)

        print(" ✅ test_divide пройден")

        def test_divide_by_zero(self):
            """
            ТЕСТ №5. Проверка обработки деления на ноль.
            Ожидается, что функция вызовет исключение ZeroDivisionError.
            """
            print(" Тестирование деления на ноль...")

            # Проверяем, что вызывается исключение
            with self.assertRaises(ZeroDivisionError):
                divide(5, 0)

            with self.assertRaises(ZeroDivisionError):
                divide(-10, 0)

        self.assertEqual(divide(5, -1), -5.0)

        print(" ✅ test_edge_cases пройден")

        def run_all_tests():
            """
            Функция для запуска всех тестов с подробным выводом.
            """
            # Создаём набор тестов
            suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)

            # Запускаем с максимальной детализацией
            runner = unittest.TextTestRunner(verbosity=2)
            result = runner.run(suite)

            # Выводим статистику
            print("\n" + "=" * 50)
            print("СТАТИСТИКА ТЕСТИРОВАНИЯ")
            print("=" * 50)
            print(f"Запущено тестов: {result.testsRun}")
            print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
            print(f"Провалено: {len(result.failures)}")
            print(f"Ошибок: {len(result.errors)}")
            print("=" * 50)
            return result

        if __name__ == '__main__':
            """
            Точка входа при запуске файла напрямую.
            """
            print("\n" + "=" * 60)
            print("🔍 ЗАПУСК UNIT-ТЕСТОВ ДЛЯ КАЛЬКУЛЯТОРА")
            print("=" * 60 + "\n")

            # Запускаем тесты
            unittest.main(verbosity=2)
