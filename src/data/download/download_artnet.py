import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep


def get_details_urls(driver):
    driver.get(url)

    while True:
        try:
            driver.find_element(By.CLASS_NAME, 'search.header-ac')
            break
        except:
            sleep(5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    btn_load_next = driver.find_element(By.CLASS_NAME, 'btn.btn-link.load-more.next')
    for i in range(2):
        btn_load_next.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
    
    all_details = driver.find_elements(By.CLASS_NAME, 'details-link')

    urls = []
    for detail in all_details:
        urls.append(detail.get_attribute('href'))
    del urls[::2]

    return urls


def get_img_url(driver, url):
    driver.get(url)

    while True:
        try:
            driver.find_element(By.CLASS_NAME, 'search.header-ac')
            break
        except:
            sleep(5)

    try:
        btn_view = driver.find_element(By.CLASS_NAME, 'zoom-cursor')
    except:
        return None

    btn_view.click()

    while True:
        try:
            img_container = driver.find_element(By.CLASS_NAME, 'iviewer_cursor')
            img = img_container.find_elements(By.XPATH, ".//*")
            break
        except:
            sleep(2)

    return img[0].get_attribute('src')

def download_img(driver, url, name):
    driver.get(url)

    '''saveas = ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys('S') \
        .key_up(Keys.CONTROL) \
        .send_keys(name) \
        .key_down(Keys.ALT) \
        .send_keys('S') \
        .key_up(Keys.ALT) \
        .perform()'''
    
    pyautogui.hotkey('ctrl','s')
    sleep(2)
    pyautogui.typewrite(name)
    pyautogui.press('enter')


def download_imgs(path):
    htmls = []

    driver = webdriver.Chrome()

    try:
        urls = []
        with open(os.path.join(path, 'url_details.txt'), 'r') as f:
            lines = f.readlines()
        for line in lines:
            urls.append(line.rstrip())
    except:
        urls = get_details_urls(driver)
        with open(os.path.join(path, 'url_details.txt'), 'w') as f:
            for url in urls:
                f.write(url + '\n')

    for i in range(34, len(urls)):
        img_url = get_img_url(driver, urls[i])

        if img_url:
            download_img(driver, img_url, 'lynch_{:03d}'.format(i))

    driver.quit()

    return htmls


url = 'http://artnet.com/artists/david-lynch/'

download_imgs('C:/Users/mrshu/lynch-room/data/lynch/')