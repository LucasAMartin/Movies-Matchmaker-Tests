from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class MoviesMatchmakerTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_login(self):
        driver = self.driver
        driver.get("https://moviesmatchmaker.com/")
        driver.find_element(By.ID, "rightButton").click()
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.NAME, "password")
        username_field.send_keys("lucas")
        password_field.send_keys("LUCAS")
        submit_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/form/div/button')
        submit_button.click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rightListButton")))
        except:
            self.fail("Login Failed")

    def test_trending(self):
        driver = self.driver
        driver.get("https://moviesmatchmaker.com/")
        driver.find_element(By.XPATH, '//*[@id="headerButtons"]/button[1]').click()
        assert '<link rel="stylesheet" href="/static/styles/display_movies.css">' in driver.page_source


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
