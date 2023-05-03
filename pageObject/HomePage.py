from selenium.webdriver.common.by import By

from pageObject.CheckOutPage import CheckOutPage


class HomePage:

  shop = (By.CSS_SELECTOR, "a[href*='shop']")
  name = (By.CSS_SELECTOR, "input[name='name']")
  email = (By.NAME, "email")
  password = (By.ID, "exampleInputPassword1")
  checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
  gender = (By.ID, "exampleFormControlSelect1")
  submit = (By.XPATH, "//input[@type='submit']")
  message = (By.CLASS_NAME, "alert-success")

  def __init__(self, driver):
    self.driver = driver

  def shopItems(self):
    self.driver.find_element(*HomePage.shop).click()
    checkOutPage = CheckOutPage(self.driver)
    return checkOutPage

  def getName(self):
    return self.driver.find_element(*HomePage.name)

  def getEmail(self):
    return self.driver.find_element(*HomePage.email)

  def getPassword(self):
    return self.driver.find_element(*HomePage.password)
  def getCheckbox(self):
    return self.driver.find_element(*HomePage.checkbox)

  def getGender(self):
    return self.driver.find_element(*HomePage.gender)

  def submitForm(self):
    return self.driver.find_element(*HomePage.submit)

  def getSuccessMessage(self):
    return self.driver.find_element(*HomePage.message)