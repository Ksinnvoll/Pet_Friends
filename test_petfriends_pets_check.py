from conftest import driver, web_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password

base_url = "https://petfriends.skillfactory.ru/login"

def test_show_all_pets(driver):
    driver.get(base_url)
    driver.find_element(By.ID, 'email').send_keys(valid_email)
    driver.find_element(By.ID, 'pass').send_keys(valid_password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

   # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.LINK_TEXT, "PetFriends")))

    # Переходим в Мои питомцы
    driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    # Проверяем количество своих питомцев
    statistic = driver.find_element(By.CSS_SELECTOR, 'html > body > div > div > div')
    statistic.text
    print('Статистика пользователя:', statistic.text)

    # Получаем имена, фото, возраст, породы питомцев
    name_list = []
    pets_with_photo = []
    names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr/td[1]')
    images = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr/th[1]')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        if names[i].text != '':
            name_list.append(i)
    print('Количество питомцев пользователя:', len(name_list))

    for i in range(len(names)):
        if images[i].get_attribute('src') != '':
            pets_with_photo.append(i)
    print('Питомцев с фото:', len(pets_with_photo))     # почему-то показывает, что у всех питомцев есть фото

    # Проверяем, что у питомцев есть имя, фото, возраст, порода
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0









