from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import excel_exporter

def scrap(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    all_reviews_button = driver.find_element_by_xpath('//a[@data-sort="reviews-dd"]')
    all_reviews_button.click()
    time.sleep(5)
    load_more_button = driver.find_element_by_xpath('//div[@data-profile_action="reviews-dd"]')
    try:
        while load_more_button.is_displayed():
            load_more_button.click()
            time.sleep(5)
    except:
        pass

    review_list = []
    reviews = driver.find_elements_by_css_selector('div.rev-text.mbot0')
    for review in reviews:
        review_dict = {}
        rate = review.find_element_by_css_selector('div.ttupper')
        rate_level = rate.get_attribute('aria-label')
        rate_level = rate_level.replace('Ternilai ', '')
        # r_text = review.text.replace('TERNILAI', '').replace('\n', ' ').strip().rstrip()
        r_text = review.get_attribute('textContent').replace('Ternilai', '').replace('\n', ' ').strip().rstrip()
        review_dict['rate'] = rate_level
        review_dict['review'] = r_text
        review_list.append(review_dict)
    excel_exporter.export(review_list)
    driver.quit()