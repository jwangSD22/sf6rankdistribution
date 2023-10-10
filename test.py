from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


 
url = "https://scrapeme.live/shop/" 
options = Options()
options.add_argument("--headless")
 
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options) as driver: 
	driver.get(url)
	
	test=driver.find_element(By.CLASS_NAME,'woocommerce-loop-product__title')

	print(test.text)