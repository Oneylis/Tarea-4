from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pytest import mark


@mark.parametrize("user,password", [("admin", "admin123"), ("fallo", "admin123")])
def test_login(user, password):
    driver = webdriver.Chrome()
    driver.get("https://as-php.com/login.php")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//div[@class="form-group"]/input[1]').send_keys(user)
    driver.find_element(By.XPATH, '//div[@class="form-group"][2]/input').send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    horadiferente = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('img/iniciosesion/' + horadiferente + '.png')
    assert driver.current_url != 'https://as-php.com/login.php'

def test_logeout():
    driver = webdriver.Chrome()
    driver.get("https://as-php.com/login.php")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//div[@class="form-group"]/input[1]').send_keys('admin')
    driver.find_element(By.XPATH, '//div[@class="form-group"][2]/input').send_keys('admin123')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="navbarDropdown"]').click()
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/div/a[2]').click()
    time.sleep(5)
    horadiferente = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('img/cierresecion/'+horadiferente+'.png')
    assert driver.current_url == 'https://as-php.com/login.php'

def test_myprofile():
    driver = webdriver.Chrome()
    driver.get("https://as-php.com/login.php")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//div[@class="form-group"]/input[1]').send_keys('admin')
    driver.find_element(By.XPATH, '//div[@class="form-group"][2]/input').send_keys('admin123')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="navbarDropdown"]').click()
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/div/a[1]').click()
    time.sleep(5)
    usuario = driver.find_element(By.XPATH, '//*[@id="form-details"]/div[1]/input')
    usuario.send_keys(Keys.CONTROL + "a")
    usuario.send_keys(Keys.DELETE)
    usuario.send_keys("Oneyli")
    driver.find_element(By.XPATH, '//*[@id="update_details"]').click()
    time.sleep(2)
    text = driver.find_element(By.XPATH, '//*[@id="form-details"]/div[1]').text
    horadiferente = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('img/miperfil/' + horadiferente + '.png')
    assert text == 'Details updated successfully.'

def test_userRoles():
    driver = webdriver.Chrome()
    driver.get("https://as-php.com/login.php")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//div[@class="form-group"]/input[1]').send_keys('admin')
    driver.find_element(By.XPATH, '//div[@class="form-group"][2]/input').send_keys('admin123')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/a[4]').click()
    horadiferente = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('img/roles/' + horadiferente + '.png')
    assert driver.current_url == 'https://as-php.com/user_roles.php'

def test_users():
    driver = webdriver.Chrome()
    driver.get("https://as-php.com/login.php")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//div[@class="form-group"]/input[1]').send_keys('admin')
    driver.find_element(By.XPATH, '//div[@class="form-group"][2]/input').send_keys('admin123')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/a[3]').click()
    horadiferente = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('img/usuario/' + horadiferente + '.png')
    assert driver.current_url == 'https://as-php.com/users.php'