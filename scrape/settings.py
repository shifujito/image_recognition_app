import os

BASE_DIR = os.getcwd()
BASE_URL: str = "https://www.talent-databank.co.jp"
CHROME_DRIVER_PATH: str = os.path.join(
    os.path.expanduser('~'), 'Selenium', 'chromedriver'
)

XPATHS = {
    "search_button": "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[4]/input",
    "table_path": "/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/table/tbody",
    "next_button": "/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/span/a[5]"
}

TIME_SPAN = 10  # アクセス秒間隔, 対象サイト負荷軽減のため一定より大きくすること
