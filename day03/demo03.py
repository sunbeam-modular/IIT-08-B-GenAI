# import required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# start the selenium browser session
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
# load desired page in the browser
driver.get("https://nilesh-g.github.io/learn-web/HTML/demo08.html")
print("Page Title:", driver.title)
# define wait strategy
driver.implicitly_wait(5)
# interact with web controls
list_items = driver.find_elements(By.TAG_NAME, "li")
for item in list_items:
    print(item.text)
# stop the session
driver.quit()
