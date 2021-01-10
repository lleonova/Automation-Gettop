from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import AbstractEventListener
from app.logger import MyListener, logger

from app.application import Application

def browser_init(context):

    context.driver = webdriver.Chrome(executable_path='./chromedriver')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox(executable_path='./geckodriver')

    #context.driver = EventFiringWebDriver(webdriver.Chrome(executable_path='./chromedriver'), MyListener())

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)
    context.driver.wait = WebDriverWait(context.driver, 10)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

