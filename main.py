import allure
import pytest

@pytest.fixture()
def setup():
    # Предварительные настройки для теста (если необходимо)
    yield
    # Завершающие действия после теста (если необходимо)

@allure.feature("Моя функциональность")
@allure.story("Мой сценарий")
@allure.title("Проверка функции сложения")
def test_addition(setup):
    num1 = 2
    num2 = 3
    expected_result = 5
    actual_result = num1 + num2
    assert actual_result == expected_result, f"Ожидаемый результат: {expected_result}, Фактический результат: {actual_result}"

# @allure.feature("Моя фича")
# @allure.story("Мой сценарий")
# @allure.title("Мой тест")
# def test_example():
#     # Шаги теста с декораторами allure
#     with allure.step("Шаг 1: Подготовка данных"):
#         # Подготовка данных для теста
#         data = 'test'

#     with allure.step("Шаг 2: Выполнение действия"):
#         # Выполнение действия
#         result = 'test'

#     with allure.step("Шаг 3: Проверка результата"):
#         # Проверка результата
#         assert result == data
        
# @allure.feature("Моя фича")
# @allure.story("Мой сценарий негативный")
# @allure.title("Мой тест")
# def test_example():
#     # Шаги теста с декораторами allure
#     with allure.step("Шаг 1: Подготовка данных"):
#         # Подготовка данных для теста
#         data = 'test'

#     with allure.step("Шаг 2: Выполнение действия"):
#         # Выполнение действия
#         result = 'test'

#     with allure.step("Шаг 3: Проверка результата"):
#         # Проверка результата
#         assert result == data

# Запуск тестов с использованием Allure и сохранением отчета

# import allure
# import pytest


# @allure.story('Тестирование метода сравнения чисел')
# @pytest.mark.parametrize('comment', [('1')])
# def test_number(comment):
#     item = comment
#     with allure.step(f'Вводные данные: {comment}'):
#         pass
#     assert comment == '1'
#     print(comment)
