import pytest
from selenium.webdriver.common.by import By

from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
  def test_e2e(self):
    log = self.getLogger()
    homePage = HomePage(self.driver)
    log.info("Move to Shop Menu")
    checkOutPage = homePage.shopItems()
    log.info("Get all cards title")
    cards = checkOutPage.getCards()
    log.info("Select Blackberry Phone and add to cart")
    i = 0
    for card in cards:
      if card.text == "Blackberry":
        checkOutPage.getCardFooter()[i].click()
      i = i + 1
    log.info("Move to Checkout page")
    checkOutPage.checkOutItems().click()
    confirmPage = checkOutPage.totalCheckOutItems()
    log.info("Entering country name as ind")
    confirmPage.getCountry().send_keys("ind")
    self.verifyLinkPresence("India")
    self.driver.find_element(By.LINK_TEXT, "India").click()
    confirmPage.getCheckBox().click()
    self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
    log.info("Test received form application is "+successText)
    assert "Sucdfsdfgcess! Thank you!" in successText
    self.driver.get_screenshot_as_file('./sample.png')
    self.waitTime(5)