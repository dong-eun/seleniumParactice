from selenium.webdriver.common.by import By


class ConfirmPage:
  inputCountry = (By.ID, "country")
  checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

  def __init__(self, driver):
    self.driver = driver

  def getCountry(self):
    return self.driver.find_element(*ConfirmPage.inputCountry)

  def getCheckBox(self):
    return self.driver.find_element(*ConfirmPage.checkbox)

    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    # self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    # successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
    # assert "Success! Thank you!" in successText
    # self.driver.get_screenshot_as_file('./sample.png')