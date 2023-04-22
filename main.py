import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Driver Variables
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)

# Start & Finish Variables
driver.get("https://en.wikipedia.org/wiki/Special:Random")
start = driver.current_url
with open("FinishPages.txt", "r", encoding='utf-8') as f:
    finish = f.read().splitlines()
    finish = finish[random.randint(0, len(finish) - 1)]
    finish = "https://en.wikipedia.org/wiki/" + finish

# Goto Start
driver.get(start)
print("Started at " + driver.current_url + ". Get to " + finish)
current = driver.current_url

# Loop
while driver.current_url != finish:
    if driver.current_url != current:
        current = driver.current_url
        print("Changed page to " + driver.current_url)

# Finish
print("Finished!")
