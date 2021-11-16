from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def join_zoom(link, pas, name, user_name, msg, chromedriver_path = "/usr/local/bin/chromedriver",  dur = 5700):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(chromedriver_path, options=options)
    browser.set_window_size(1800,1800)
    browser.get(link)
    
    time.sleep(3)
    while True:
        try:
            browser.find_element_by_id('inputname').send_keys(user_name)
        except:
            time.sleep(5)
            print('Не удалось вбить имя!')
            continue
        break
    while True:
        try:
            browser.find_element_by_id('joinBtn').click()
        except:
            time.sleep(5)
            print('Не войти!')
            continue
        break

    
    while True:
        try:
            browser.find_element_by_name('inputpasscode').send_keys(pas)
        except:
            time.sleep(5)
            print('Не ввести пароль!')
            continue
        break  
    
    while True:
        try:
            browser.find_element_by_id('joinBtn').click()
        except:
            time.sleep(5)
            print('Не войти после пароля!')
            continue
        break
    while True:
        try:
            browser.find_element_by_class_name('video-avatar__avatar-title').click()
            browser.find_element_by_class_name('video-avatar__avatar-title').click()
            browser.find_element_by_xpath('//*[@id="wc-footer"]/div/div[2]/div[3]/button/div/div').click()
        except:
            time.sleep(5)
            print('Не открыть чат')
            continue
        break

    try:
        browser.find_element_by_xpath('//*[@id="wc-container-right"]/div/div[4]/textarea').click()
    except:
        time.sleep(5)
        print('Не могу выделить чат!')
    while True:
        try:
            browser.find_element_by_class_name('video-avatar__avatar-title').click()
            browser.find_element_by_class_name('video-avatar__avatar-title').click()
            browser.find_element_by_xpath('//*[@id="wc-footer"]/div/div[2]/div[3]/button/div/div').click()
            time.sleep(10)
            browser.find_element_by_xpath('//*[@id="wc-container-right"]/div/div[4]/textarea').click()
        except:
            time.sleep(5)
            print('Не могу выделить чат!')
            continue
        break
    while True:
        try:
            browser.find_element_by_xpath('//*[@id="wc-container-right"]/div/div[4]/textarea').send_keys(msg)
        except:
            time.sleep(5)
            print('Не могу написать в чат!')
            continue
        break
    while True:
        try:
            browser.find_element_by_xpath('//*[@id="wc-container-right"]/div/div[4]/textarea').send_keys(Keys.RETURN)
        except:
            time.sleep(5)
            print('Не могу отправить сообщения в чат!')
            continue
        break
    time.sleep(dur)
    while True:
        try:
            browser.find_element_by_class_name('video-avatar__avatar-title').click()
            browser.find_element_by_class_name('video-avatar__avatar-title').click()
            browser.find_element_by_xpath('//*[@id="wc-footer"]/div/div[3]/div/button').click()
            browser.find_element_by_xpath('//*[@id="wc-footer"]/div[2]/div[2]/div[3]/div/div/button').click()
        except:
            time.sleep(10)
            print('Не выйти')
            continue
        break
    print('Я отсидел конференцию {}'.format(name))
    browser.quit()