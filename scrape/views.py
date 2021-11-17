from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# Create your views here.
def scrape_view(request):
    PATH = 'chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options,executable_path=PATH)
    driver.get("https://youtube.com")
    print(driver.title)
    element = driver.find_element_by_xpath("//button[@aria-label='Guide']")
    element.click()
    time.sleep(3)
    return render(request,"scrape.html")