from  behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@given(u'I launch the app')
def launchBrowser(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)



@when(u'I open the Orange HRM')
def openApp(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com')


@then(u'Verify that the logo present on page')
def verifyLogo(context):
    try:
        wait = WebDriverWait(context.driver, 10)
        logo = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "orangehrm-login-branding"))
        )
        assert logo.is_displayed(), "Logo is not displayed after 10 seconds"
    except TimeoutException:
        raise AssertionError("Logo not found or not visible within timeout.")



@then(u'Close the browser')
def closeBrowser(context):
    context.driver.quit()
    print("✅ Browser closed.")
