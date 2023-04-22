from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Driver Variables
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)

# Start and Finish Variables
driver.get("https://en.wikipedia.org/wiki/Special:Random")
start = driver.current_url
finish = "https://en.wikipedia.org/wiki/Adolf_Hitler"

# Goto Start
driver.get(start)
print("Started at " + driver.current_url)
current = driver.current_url

while driver.current_url != finish:
    if driver.current_url != current:
        current = driver.current_url
        print("Changed page to " + driver.current_url)

print("Finished!")
