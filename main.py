import pytest
import allure

@allure.feature("Моя фича")
@allure.story("Мой сценарий")
@allure.title("Мой тест")
def test_example():
    # Шаги теста с декораторами allure
    with allure.step("Шаг 1: Подготовка данных"):
        # Подготовка данных для теста
        data = 'test'

    with allure.step("Шаг 2: Выполнение действия"):
        # Выполнение действия
        result = 'test'

    with allure.step("Шаг 3: Проверка результата"):
        # Проверка результата
        assert result == data
    with allure.step("Шаг 3: Проверка результата"):
        # Проверка результата
        assert 'text' == data

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
