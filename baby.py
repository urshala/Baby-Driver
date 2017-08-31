import requests
import bs4
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
import urllib.request as ur
import time

base_url = 'http://www.babydriver-movie.com/'
wd = webdriver.Chrome(r'C:\Users\Deepak\Downloads\Application\chromedriver.exe')
wd.get(base_url)

close = wait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="fancybox-item fancybox-close"]')))
close.click()


soup = bs4.BeautifulSoup(wd.page_source, 'html.parser')

images = soup.find_all('img')
list_of_links = [each.get('src') for each in images]

for each_link in list_of_links:
	full_link = base_url + each_link
	try:
		ur.urlretrieve(full_link, './Images/'+ each_link.split('/')[-1])
	except Exception as e:
		raise e
#ur.urlretrieve(base_url +list_of_links[2], './Images/'+list_of_links[2].split('/')[-1])