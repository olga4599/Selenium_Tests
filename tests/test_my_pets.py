import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import email, password
from config_my_pets import testing
from config_my_pets import show_my_pets
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_show_my_pets(show_my_pets):

    #Проверка, что открылась страница Мои питомцы
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "Olga111111111"

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    #Получаем число питомцев из статистики
    user_table = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    pets_num = user_table[0].text.split('\n')
    pets_num = pets_num[1].split(':')
    pets_num = int(pets_num[1])

    #Получаем число питомцев из таблицы
    pet_table = pytest.driver.find_elements(By.XPATH, '//tbody/tr')
    row_num = list(pet_table)
    row_num = len(row_num)

    #Проверка что число пистомцев из статистики равно числу из таблицы
    assert pets_num == row_num
    print(f'Pets number: {pets_num}')
    print(f'Number of pets in the table: {row_num}')

def test_photo(show_my_pets):

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))

    # Сохранение элементов статистики в переменную "statistic"
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    # Сохранение элементов с атрибутом "img" в переменную "images"
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Получение количества питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Нахождение половины от количества питомцев
    half = number // 2

    # Нахождение количества питомцев с фотографией
    number_of_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_of_photos += 1

    # Проверка того, что количество питомцев с фотографией больше или равно половине количества питомцев
    assert number_of_photos >= half
    print(f'Количество фото: {number_of_photos}')
    print(f'Половина от числа питомцев: {half}')

def test_pet_data(show_my_pets):

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//tbody/tr/td')))
    pet_table = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td')

    for i in range(len(pet_table)):
        pet_info = pet_table[i].text.replace('\n', '')
        pet_data = pet_info.split(" ")
        result = len(pet_data)
        assert result != ""

def test_pets_have_different_names(show_my_pets):

    #Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//tbody/tr/td')))

    pet_table = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td')
    #Создаем лист с именами питомцев
    pet_list = []
    for i in range(len(pet_table)):
        pet_info = pet_table[i].text.replace('\n', '')
        pet_data = pet_info.split(" ")
        pet_list.append(pet_data[0])
    pet_list = pet_list[::4]
    #Проверяем имена с списке
    pet_names = []
    count = 0
    for i in pet_list:
        if i not in pet_names:
            pet_names.append(i)
    assert pet_list == pet_names
    print(pet_names)




