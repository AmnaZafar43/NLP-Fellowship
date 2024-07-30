from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

from clean_text import clean_transcript
from save_to_file import save_to_txt


def get_youtube_transcript(video_url):
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()
    driver.get(video_url)

    # Wait for the transcript button to be clickable and click it
    transcript_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="expand"]'))
    )

    transcript_button.click()

    transcript_option = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="primary-button"]/ytd-button-renderer/yt-button-shape/button')
        )
    )

    transcript_option.click()

    sleep(5)
    # Extract the transcript text
    transcript_elements = WebDriverWait(driver, 100).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "ytd-transcript-segment-list-renderer")
        )
    )

    transcript = [element.text for element in transcript_elements]

    # Close the driver
    driver.quit()

    return transcript

def main():
    video_url = "https://youtu.be/9syvZr-9xwk?si=tTdoLhzlLj01lwAW"
    transcript = get_youtube_transcript(video_url)
    # print(transcript)
    text=clean_transcript(transcript)
    save_to_txt(text,file_name=f'video_output_{str(datetime.now().ctime()).replace(' ','').replace(':','')}')
    print("Transcript Generated Successfully....")


if __name__=="__main__":
    main()
