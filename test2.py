from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def scrape(league,league_division,rank_page):
    
    url = f'https://www.streetfighter.com/6/buckler/ranking/league?character_filter=1&character_id=luke&platform=1&user_status=1&home_filter=2&home_category_id=5&home_id=1&league_rank={rank_page}&page=1' 
    
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'

    options = Options()
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--allow-running-insecure-content')

    driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install()),options=options) 

    driver.get(url) 



    driver.add_cookie({
        "name":"buckler_praise_date","value":"1695945638704"
    })
    driver.add_cookie({
        "name":"buckler_r_id","value":"ffacf239-a620-4795-aa40-944eb2c851ab"
    })
    driver.add_cookie({
        "name":"pll_language","value":"en"
    })
    driver.add_cookie({
        "name":"buckler_id","value":"33RUGpVfr3B_1pmws3z4dtJ0TQ--UK8GWj-E5EtcFl2SL0TAqhLvdvxczzKxUaoS"
    })

    # Reload the page to apply the cookies
    driver.get(url)

    # # Wait for a specific condition (e.g., an element to be present or visible) before proceeding
    # wait = WebDriverWait(driver, 3)  # Adjust the timeout as needed
    # ranking_info = wait.until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "ranking_ranking_now__last__TghLM"))
    # )


    # Wait for the page to load completely (you can customize the timeout)
    

  
    # printing the content of entire page 

    

    driver.quit()
  
scrape('Rookie',1,rank_page=1)