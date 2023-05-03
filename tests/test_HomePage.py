import pytest

from pageObject.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

  def test_formSubmission(self, getData):
    homepage = HomePage(self.driver)
    log = self.getLogger()
    log.info("Input First Name is : "+getData["first_name"])
    homepage.getName().send_keys(getData["first_name"])
    log.info("Input Email is : "+getData["email"])
    homepage.getEmail().send_keys(getData["email"])
    log.info("Input Password")
    homepage.getPassword().send_keys("123455")
    homepage.getCheckbox().click()
    log.info("Input Gender is : "+getData["gender"])
    self.selectOptionByText(homepage.getGender(), getData["gender"])
    homepage.submitForm().click()
    alert = homepage.getSuccessMessage().text

    assert "Success" in alert

    self.waitTime(3)

    # self.driver.refresh()

  # @pytest.fixture(params=HomePageData.test_HomePage_data)
  # def getData(self, request):
  #   return request.param
  @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
  def getData(self, request):
    return request.param