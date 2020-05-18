import os

BASE_DIR = os.getcwd()
BASE_URL: str = "https://www.talent-databank.co.jp/"
CHROME_DRIVER_PATH: str = os.path.join(
    os.path.expanduser('~'), 'Selenium', 'chromedriver'
)
