import time

from selenium.webdriver import ActionChains


def test_single_shadow_dom(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(3)
    shadow_element_1 = driver.find_element_by_css_selector("#userName")
    act = ActionChains(driver)
    act.move_to_element(shadow_element_1).perform()
    driver.execute_script("arguments[0].shadowRoot.getElementById('kils').value='ramnath'", shadow_element_1)
    time.sleep(5)
    driver.find_element_by_xpath("//a[.='Training']")


def test_nested_shadow_dom(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(3)
    shadow_element_1 = driver.find_element_by_css_selector("#userName")
    act = ActionChains(driver)
    act.move_to_element(shadow_element_1).perform()
    driver.execute_script("arguments[0].shadowRoot.getElementById('app2').shadowRoot.getElementById('pizza').value='Veggie Paradise'", shadow_element_1)
    time.sleep(5)
    driver.find_element_by_xpath("//a[.='Training']")


def test_shadow_dom_inside_iframe(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(3)
    shadow_element_1 = driver.find_element_by_css_selector("#userName")
    act = ActionChains(driver)
    act.move_to_element(shadow_element_1).perform()
    driver.switch_to.frame("pact")
    shadow_element_1 = driver.find_element_by_css_selector("#snacktime")
    driver.execute_script("arguments[0].shadowRoot.getElementById('tea').value='ofcourse'", shadow_element_1)
    time.sleep(5)
    driver.switch_to.default_content()
    driver.find_element_by_xpath("//a[.='Training']")