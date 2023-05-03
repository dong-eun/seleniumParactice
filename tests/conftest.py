import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

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
    print("Chrome Driver")
    options = Options()
    options.add_experimental_option("detach", True)
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
  #Firefox 브라우저 선택
  elif browser_name == "firefox":
    print("Firefox Driver")
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

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
