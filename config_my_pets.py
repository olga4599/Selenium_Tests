import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import email, password
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/Users/Olga/ChromeDriver/chromedriver.exe')
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()

@pytest.fixture()
def show_my_pets():
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    #Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys(email)

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
    # Вводим парль
    pytest.driver.find_element(By.ID, 'pass').send_keys(password)

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    #Нажимаем кнопку для входа
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Мои питомцы')]")))
    #Нажимаем кнопку для перехода к Моим питомцам
    pytest.driver.find_element(By.XPATH, "//a[contains(text(),'Мои питомцы')]").click()

