import allure
import pytest

@allure.feature("Login")
@allure.story("Valid Login")
@pytest.mark.parametrize("username, password", [("user1", "pass1"), ("user2", "pass2")])
def test_valid_login(username, password):
    with allure.step("Open login pag"):
        # Открываем страницу входа
        pass
    
    with allure.step("Enter username and password"):
        # Вводим имя пользователя и пароль
        pass
    
    with allure.step("Click on login button"):
        # Нажимаем на кнопку входа
        pass
    
    with allure.step("Verify login successful"):
        # Проверяем, что вход успешен
        pass

@allure.feature("Login")
@allure.story("Invalid Login")
@pytest.mark.parametrize("username, password", [("user1", "wrongpass"), ("invaliduser", "pass2")])
def test_invalid_login(username, password):
    with allure.step("Open login page"):
        # Открываем страницу входа
        pass
    
    with allure.step("Enter username and password"):
        # Вводим имя пользователя и пароль
        pass
    
    with allure.step("Click on login button"):
        # Нажимаем на кнопку входа
        pass
    
    with allure.step("Verify login failed"):
        # Проверяем, что вход не удался
        pass

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
        
@allure.feature("Моя фича")
@allure.story("Мой сценарий негативный")
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

@allure.story('Тестирование метода сравнения чисел')
@pytest.mark.parametrize('comment', [('2')])
def test_number(comment):
    item = comment
    with allure.step(f'Вводные данные: {comment}'):
        pass
    assert comment == '1'
    print(comment)
