def add(a, b):
    """
    Возвращает сумму двух чисел.

    Параметры:
    a (int/float) – первое слагаемое
    b (int/float) – второе слагаемое

    Возвращает:
    int/float – результат сложения
    """

    return a + b


def subtract(a, b):
    """
    Возвращает разность двух чисел (a − b).

    Параметры:
    a (int/float) – уменьшаемое
    b (int/float) – вычитаемое

    Возвращает:
    int/float – разность
    """

    return a - b


def multiply(a, b):
    """
    Возвращает произведение двух чисел.

    Параметры:
    a (int/float) – первый множитель
    b (int/float) – второй множитель

    Возвращает:
    int/float – произведение
    """

    return a * b


def divide(a, b):
    """
    Возвращает результат деления а на b.

    Параметры:
    a (int/float) – делимое
    b (int/float) – делитель

    Возвращает:
    float – частное

    Исключения:
    ZeroDivisionError – при попытке деления на ноль
    """

    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


if __name__ == '__main__':
    # Демонстрация работы функций
    print("=" * 40)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КАЛЬКУЛЯТОРА")
    print("=" * 40)
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"divide(15, 3) = {divide(15, 3)}")
    print(f"divide(10, 2) = {divide(10, 2)}")
    print("=" * 40)