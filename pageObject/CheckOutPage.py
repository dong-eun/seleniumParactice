from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckOutPage:

  cardTitle = (By.CSS_SELECTOR, ".card-title a")
  cardFooter = (By.CSS_SELECTOR, ".card-footer button")
  checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
  totalCheckout = (By.XPATH, "//button[@class='btn btn-success']")

  def __init__(self, driver):
    self.driver = driver

  def getCards(self):
    return self.driver.find_elements(*CheckOutPage.cardTitle)

  def getCardFooter(self):
    return self.driver.find_elements(*CheckOutPage.cardFooter)

  def checkOutItems(self):
    return self.driver.find_element(*CheckOutPage.checkOut)

  def totalCheckOutItems(self):
    self.driver.find_element(*CheckOutPage.totalCheckout).click()
    confirmPage = ConfirmPage(self.driver)
    return confirmPage