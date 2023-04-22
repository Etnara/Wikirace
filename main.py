import random
import time
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
print("Started at " + driver.current_url.split("https://en.wikipedia.org/wiki/")[1].replace("_", " "))
print("Get to " + finish.split("https://en.wikipedia.org/wiki/")[1].replace("_", " "))

# Start Timer
timeStart = time.time()

# Loop
counter = 1
current = driver.current_url
while driver.current_url != finish:
    if driver.current_url != current:
        counter += 1
        current = driver.current_url
        print("Changed page to " + driver.find_element("id", "firstHeading").text)

# Finish
timeEnd = time.time()
timeElapsed = int(timeEnd - timeStart)

mins = timeElapsed // 60
sec = timeElapsed % 60
if timeElapsed > 3600:
    print("Really bruh. Over an hour?!?!")
elif mins != 0:
    print("Finished in " + str(counter) + " moves and " + str(mins) + " minutes and " + str(sec) + " seconds!")
else:
    print("Finished in " + str(counter) + " moves and " + str(sec) + " seconds!")
