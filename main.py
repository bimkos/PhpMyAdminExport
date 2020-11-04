from selenium import webdriver  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url", help="http://example.com/pma", type=str)
    parser.add_argument("-user","--username", help="admin", type=str)
    parser.add_argument("-pass","--password", help="admin_password", type=str)
    parser.add_argument("-db","--database", help="database name for export", type=str)
    parser.add_argument("-o","--output", help="output dir", type=str)
    args = parser.parse_args()

    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : args.output}
    options.add_experimental_option("prefs",prefs)
    options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(args.url)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "pma_username")))
    driver.find_element_by_name("pma_username").send_keys(args.username)
    driver.find_element_by_name("pma_password").send_keys(args.password)
    driver.find_element_by_xpath("/html/body/div/div/form/fieldset[2]/input[1]").click()
    driver.get(args.url + "/db_export.php?db=" + args.database)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "buttonGo")))
    driver.find_element_by_id("buttonGo").click()