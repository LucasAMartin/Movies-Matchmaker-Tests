from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


def login(driver):
    driver.get("https://moviesmatchmaker.com/")
    driver.find_element(By.ID, "rightButton").click()
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys("lucas")
    password_field.send_keys("LUCAS")
    submit_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/form/div/button')
    submit_button.click()


class MoviesMatchmakerTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_main_search(self):
        driver = self.driver
        driver.get("https://moviesmatchmaker.com/")
        driver.find_element(By.XPATH, '/html/body/section/form/input').send_keys("The Dark Knight")
        driver.find_element(By.ID, "searchButton").click()
        assert '<link rel="stylesheet" href="/static/styles/display_movies.css">' in driver.page_source

    def test_main_search_autofill(self):
        driver = self.driver
        driver.get("https://moviesmatchmaker.com/")
        driver.find_element(By.XPATH, '/html/body/section/form/input').send_keys("The Dark Knight")
        driver.find_element(By.XPATH, '//*[@id="ul"]/li[1]').click()
        assert '<link rel="stylesheet" href="/static/styles/display_movies.css">' in driver.page_source

    def test_main_search_tab_enter(self):
        driver = self.driver
        driver.get("https://moviesmatchmaker.com/")
        search_box = driver.find_element(By.XPATH, '/html/body/section/form/input')
        search_box.send_keys("The Dark Knight")
        search_box.send_keys(Keys.TAB)
        search_box.send_keys(Keys.ENTER)
        assert '<link rel="stylesheet" href="/static/styles/display_movies.css">' in driver.page_source

    def test_login(self):
        driver = self.driver
        login(driver)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rightListButton")))
        except:
            self.fail("Login Failed")

    def test_list(self):
        driver = self.driver
        login(driver)
        driver.find_element(By.XPATH, '//*[@id="headerButtons"]/button[1]').click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "navMyList")))
        except:
            self.fail("My List Failed")

    def test_trending(self):
        driver = self.driver
        driver.get("https://moviesmatchmaker.com/")
        driver.find_element(By.XPATH, '//*[@id="headerButtons"]/button[1]').click()
        assert '<link rel="stylesheet" href="/static/styles/display_movies.css">' in driver.page_source


if __name__ == '__main__':
    unittest.main()

