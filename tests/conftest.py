import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.safari.options import Options as SafariOptions

driver = None

def pytest_addoption(parser):
  parser.addoption(
    '--browser_name', action='store', default='chrome'
  )


@pytest.fixture(scope="class")
def setup(request):
  global driver
  browser_name = request.config.getoption("browser_name")
  #Chrome 브라우저 선택
  if browser_name == "chrome":
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("detach", True) # Chrome 종료 시 WebDriver 세션 유지
    chrome_options.add_experimental_option("useAutomationExtension", False) # Chrome 자동화 확장 미 사용
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']) # Chrome 자동화 기능 비활성화
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") # 자동화 감지 Blink 기능 비활성
    chrome_options.add_argument("--disable-extensions") # 확장프로그램 미사용
    chrome_options.add_argument("--disable-infobars") # 정보 표시줄 비활성화
    chrome_options.add_argument("--disable-notifications") # 알림 비활성화
    chrome_options.add_argument("--disable-popup-blocking") # 팝업 차단 비활성화
    chrom_service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrom_service, options=chrome_options)
  #Firefox 브라우저 선택
  elif browser_name == "firefox":
    firefox_options = FirefoxOptions()
    firefox_options.set_preference("dom.webdriver.enabled", False) # WebDriver 속성 감지 비활성화
    firefox_options.set_preference("dom.webnotifications.enabled", False) # 웹 알림을 표시 비활성화
    firefox_options.set_preference("dom.push.enabled", False) # 푸시 알림 비활성화
    firefox_options.set_preference("useAutomationExtension", False) # 자동확장 기능 비활성화
    firefox_service = FirefoxService(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
  # Safari 브라우저 선택
  elif browser_name == "safari":
    safari_options = SafariOptions()
    safari_options.automatic_inspection = True # 자동화 감지 비활성화
    safari_options.preferences = {
      "security.enable_java": False, # java 미 실행
      "security.enable_java_script": True, # java script 실행
      "browser.popups.showPopupBlocker": False # 팝업 차단 비활성화
    }
    driver = webdriver.Safari(options=safari_options)

  driver.get("https://rahulshettyacademy.com/angularpractice/")
  driver.implicitly_wait(5)
  driver.maximize_window()
  request.cls.driver = driver
  yield
  driver.close()

  # @pytest.fixture(params=HomePageData.getTestData)
  # def getData(request):
  #   return request.param

  # @pytest.fixture(params=HomePageData.getTestData)
  # def getData(request):
  #   return request.param# @pytest.fixture(params=HomePageData.getTestData)
  # # def getData(request):
  # #   return request.param

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
      xfail = hasattr(report, 'wasxfail')
      if (report.skipped and xfail) or (report.failed and not xfail):
        file_name = report.nodeid.replace("::", "_") + ".png"
        _capture_screenshot(file_name)
        if file_name:
          html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                 'onclick="window.open(this.src)" align="right"/></div>' % file_name
          extra.append(pytest_html.extras.html(html))
      report.extra = extra


def _capture_screenshot(name):
  driver.get_screenshot_as_file(name)
