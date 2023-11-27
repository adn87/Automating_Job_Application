from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time

URL = ("https://www.linkedin.com/jobs/search/"
       "?currentJobId=3772064921&f_AL=true&geoId=92000000&keywords=software"
       "%20developer&location=Worldwide&origin=JOB_"
       "SEARCH_PAGE_JOB_FILTER&refresh=true")
USER_NAME = ["PUT YOUR USERNAME"]
PASSWORD = ["PUT YOUR PASSWORD"]


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# Click sing in Button
time.sleep(2)
sign_in = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()

# Sign in
time.sleep(5)
username = driver.find_element(By.ID, value="username")
username.send_keys(USER_NAME)

password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# Get listing
time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Locate the apply button
        easy_apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button--top-card button")
        easy_apply.click()

        submit_button = driver.find_element(By.CSS_SELECTOR, value="footer button")
        submit_button.click()

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped")
        else:
            print("Submitting job application")
            submit_button.click()
    except NoSuchElementException:
        abort_application()
        print("no application button, skipped")
        continue

time.sleep(5)
driver.quit()


