from selenium import webdriver
import time

def scrap(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    try:
        reviews_button = driver.find_element_by_xpath('//*[@id="mainframe"]/div[1]/div/div[1]/div[2]/div[1]/div/a[3]')
        reviews_button.click()
        time.sleep(3)
        all_reviews_button = driver.find_element_by_xpath('//a[@data-sort="reviews-dd"]')
        all_reviews_button.click()
        time.sleep(3)
        load_more_button = driver.find_element_by_xpath('//div[@data-profile_action="reviews-dd"]')
        i = 0
        while load_more_button.is_displayed() and i < 20:
            load_more_button.click()
            i += 1
            time.sleep(3)
    except:
        pass

    review_rates, reviews = [], []
    # review_elements = driver.find_elements_by_xpath("//div[@class='rev-text mbot0']")
    review_elements = driver.find_elements_by_xpath("//div[contains(@class, 'rev-text') and contains(@class, 'mbot0')]")
    for review in review_elements:
        try:
            rate = review.find_element_by_xpath(
                '//*[@id="reviews-container"]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[1]/div[3]/div[1]')
            rate_level = rate.get_attribute('aria-label')
            rate_level = rate_level.replace('Ternilai ', '')
            r_text = review.get_attribute('textContent').replace('Ternilai', '').replace('\n', ' ').strip().rstrip()
            review_rates.append(rate_level)
            reviews.append(r_text)
        except:
            pass
    driver.quit()
    return review_rates, reviews