from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')      ### optional

driver = webdriver.Chrome(options=options)
res = driver.get("https://www.youtube.com/@MLB/videos")

# Wait up to 10 seconds, to let youtube load the latest videos.
# We use ID video-title-link as it contains exactly the 
# information we want: The title and the link to video.
try:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "video-title-link"))
    )
except TimeoutException:
    print("Could not load Youtube page on time.")

values = [(x.text, x.get_attribute("href")) for x in elements]

for val in values:
    print (val)