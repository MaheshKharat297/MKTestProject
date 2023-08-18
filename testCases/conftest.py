from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "IE":
        driver = webdriver.Ie()
        print("\nLaunching IE browser**************************")
    elif browser == "Firefox":
        driver = webdriver.Firefox()
        print("\nLaunching Firefox browser**************************")
    else:
        driver = webdriver.Chrome()
        print("\nLaunching Chrome browser**************************")
    return driver


def pytest_addoption(parser):  # this will get inputs from CLI command
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this will return browser value to set up method
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata = {"Project Name": "MKTestProject", "Module Name": "MKTestProject", "Tested by": "Mahesh",
                        "Browser": setup}


############### HTML report integration #################

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'MKTestProject'
#     config._metadata['Module Name'] = 'MKTestProject'
#     config._metadata['Tested by'] = 'Mahesh Kharat'
#
#
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)