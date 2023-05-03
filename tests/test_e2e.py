import pytest
from selenium.webdriver.common.by import By

from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
  def test_e2e(self):

    # options = Options()
    # options.add_experimental_option("detach", True)
    # service = Service(executable_path=ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=options)
    # driver.implicitly_wait(5)
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    log = self.getLogger()
    homePage = HomePage(self.driver)
    log.info("Select Shop menu")
    checkOutPage = homePage.shopItems()
    # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    log.info("Getting all cards title")
    cards = checkOutPage.getCards()
    # cards = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    i = 0
    for card in cards:
      log.info(card.text)
      if card.text == "Blackberry":
        checkOutPage.getCardFooter()[i].click()
      i = i + 1
        # card.find_element(By.XPATH, "div/button").click()

    # for card in cards:
    #   cardTitle = card.find_element(By.XPATH, "div/h4/a").text
    #   if cardTitle == "Blackberry":
    #     card.find_element(By.XPATH, "div/button").click()

    checkOutPage.checkOutItems().click()
    # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    confirmPage = checkOutPage.totalCheckOutItems()
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    log.info("Entering country name as ind")
    confirmPage.getCountry().send_keys("ind")
    self.verifyLinkPresence("India")
    self.driver.find_element(By.LINK_TEXT, "India").click()

    confirmPage.getCheckBox().click()
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

    self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
    log.info("Test received form application is "+successText)
    assert "Sucdfsdfgcess! Thank you!" in successText
    self.driver.get_screenshot_as_file('./sample.png')
    self.waitTime(5)