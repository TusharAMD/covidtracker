from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
import time
def getLocation():
    options = Options()
    options.add_argument("--use--fake-ui-for-media-stream")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.Chrome(executable_path = './chromedriver.exe',options=options) #Edit path of chromedriver accordingly
    timeout = 20
    driver.get("https://tusharamd.github.io/simpleLocationUtility/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(20)
    #longitude = driver.find_elements_by_xpath('//*[@id="longitude"]') #Replace with any XPath    
	
    longitude = driver.find_elements_by_xpath('//*[@id="lat"]') #Replace with any XPath
    #print(longitude)
    for x in longitude:
	    print(x)
	
    longitude = [x.text for x in longitude] 
    
    longitude = str(longitude[0])    
    latitude = driver.find_elements_by_xpath('//*[@id="lon"]')    
    latitude = [x.text for x in latitude]    
    latitude = str(latitude[0])    
    driver.quit()    
    return (latitude,longitude)
