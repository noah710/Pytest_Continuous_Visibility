# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAsdasdsd():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_asdasdsd(self):
    self.driver.get("https://provider.vetnow.com/login")
    self.driver.set_window_size(1920, 1052)
    self.driver.find_element(By.NAME, "_username").click()
    self.driver.find_element(By.NAME, "_username").send_keys("qa_provider_persistent@vetnow.com")
    self.driver.find_element(By.NAME, "_password").click()
    self.driver.find_element(By.NAME, "_password").send_keys("P@ssword1")
    self.driver.find_element(By.CSS_SELECTOR, ".col-6 > .btn").click()
    WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#myClinentMenu .nav-link-text"))) # yes, its clinent
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, "#myClinentMenu .nav-link-text").click() 
