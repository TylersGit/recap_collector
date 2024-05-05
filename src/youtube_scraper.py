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


def get_video_urls():
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

    # for val in values:
    #     print (val)

    return values

def process_urls(url_list, game_list):
    """Returns the list of relevant URLs according to the playing teams. 

    Args:
        url_list: A list of all recent videos from the MLB youtube channel.
        game_list: A list of relevant games according to the set roster. 
    """
    relevant_urls = []
    for url in url_list:
        # url[0] is the video name. 
        video = url[0]
        if "vs." in video:
            for game in game_list:  
                teams = game.split(",")[0:2]
                for team in teams:
                    print(video, team)
                    if team in video:
                        relevant_urls.append(url)

    for url in relevant_urls:
        print(url)

if __name__ == "__main__":
    url_list = get_video_urls()
    