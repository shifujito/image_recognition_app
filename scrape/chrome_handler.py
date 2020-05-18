from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from typing import Optional

from .settings import CHROME_DRIVER_PATH


class ChromeHandler:
    def __init__(self, browser: bool = False) -> None:
        op = Options()
        op.add_argument("--disable-gpu")
        op.add_argument("--disable-extensions")
        op.add_argument("--proxy-server='direct://'")
        op.add_argument("--proxy-bypass-list=*")
        op.add_argument("--start-maximized")
        op.add_argument("--headless")

        if browser:
            self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        else:
            self.driver = webdriver.Chrome(
                CHROME_DRIVER_PATH, options=op
            )

        self.soup = None

    def __wait__(self, _time: int, key: str, val: str) -> None:
        print("Search Element: ({}, {})".format(key, val))
        WebDriverWait(self.driver, _time).until(
            EC.presence_of_element_located(
                (key, val)
            )
        )

    def wait(self,
             _id: Optional[str] = None,
             cl: Optional[str] = None,
             selector: Optional[str] = None,
             _time: int = 30) -> None:
        params = [
            (By.ID, _id),
            (By.CLASS_NAME, cl),
            (By.CSS_SELECTOR, selector)
        ]
        for param in params:
            if isinstance(param[1], str):
                self.__wait__(
                    _time, param[0], param[1]
                )

    def access(self,
               url: str,
               _id: Optional[str] = None,
               cl: Optional[str] = None,
               selector: Optional[str] = None) -> None:
        self.driver.get(url)
        self.wait(_id=_id, cl=cl, selector=selector)
        self.set_soup()

    def set_soup(self) -> None:
        self.soup = BeautifulSoup(
            self.driver.page_source,
            features="html.parser"
        )

    def fin(self) -> None:
        self.driver.quit()
