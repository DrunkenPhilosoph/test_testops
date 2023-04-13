import allure
import pytest


@allure.story('Тестирование метода добавления отпуска с позитивными данными')
@pytest.mark.parametrize('comment', [(1)])
def test_number(comment):
    item = comment
    with allure.step(f'Вводные данные: {comment}'):
        pass
    assert comment == 1