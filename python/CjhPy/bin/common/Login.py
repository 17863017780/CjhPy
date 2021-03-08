
from selenium.webdriver import firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import config

firefox_options = Options()
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
#禁用图片
# firefox_options.add_argument('blink-settings=imagesEnabled=false')
firefox_options.add_argument('--disable-gpu')
#无头浏览
# firefox_options.add_argument('--headless')
# path="/usr/local/bin/geckodriver.exe"
# firefox = webdriver.Firefox(firefox_options=firefox_options,executable_path=path)
# firefox = webdriver.Firefox(options=firefox_options)
firefox = webdriver.Firefox()

login_url = "https://passport.jd.com/new/login.aspx?ReturnUrl=http%3A%2F%2Fhome.jd.com%2F"


# 只是为了获取cookie
def login():
    firefox.get(login_url)
    print("this is running")
    firefox.find_element_by_xpath("//*[@id=\"content\"]/div[2]/div[1]/div/div[3]/a").click()
    firefox.find_element_by_id('loginname').send_keys(config.ACCOUNT[0]['username'])
    # print(config.ACCOUNT[0]['username']+'1324'+config.ACCOUNT[0]['pwd'])
    firefox.find_element_by_id('nloginpwd').send_keys(config.ACCOUNT[0]['pwd'])
    firefox.find_element_by_id('loginsubmit').click()
    time.sleep(1)
    cookie_string = firefox.get_cookies()
    # print("获取的cookie is",cookie_string)
    cookie = [item["name"] + "=" + item["value"] for item in cookie_string]
    cookiestr = '; '.join(item for item in cookie)
    print(" the cookie is :" +cookiestr)
    if( cookiestr.__len__() != 0):
        config.COOKIE =str(cookiestr)
        # print("213")
    firefox.close()

if __name__ == '__main__':
    login()
