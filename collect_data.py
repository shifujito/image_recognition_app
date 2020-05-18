from selenium.webdriver.common.keys import Keys
import requests
import time
import os
from typing import List, Optional

from scrape.chrome_handler import ChromeHandler
from scrape.settings import XPATHS, BASE_URL, BASE_DIR, TIME_SPAN


class Result:
    def __init__(self, age: int, _id: int, link: str) -> None:
        self.age = age
        self._id = _id
        self.link = link
        self.path: Optional[str] = None

    def __str__(self) -> str:
        return "{}. {} => {}".format(self._id, self.age, self.link)

    __repr__ = __str__

    def save(self) -> None:
        res = requests.get(BASE_URL + self.link)
        extension = None

        if res.headers['content-type'] == 'image/jpeg':
            extension = 'jpg'
        elif res.headers['content-type'] == 'image/png':
            extension = 'png'
        else:
            # 未対応形式
            return None

        filename = f"{self.age}_{self._id:0=4}.{extension}"
        self.path = os.path.join(BASE_DIR, 'data', filename)

        with open(self.path, "wb") as f:
            f.write(res.content)


class Main:
    def __init__(self, browser: bool = False, init_id: int = 0) -> None:
        """
        Args:
            browser(bool):  Seleniumでブラウザを開くかどうか
            init_id(int): 初期画像ID(既存のMAX IDより大きい値を渡す)
        """
        self.handler = ChromeHandler(browser=browser)

        self._id = init_id
        self.results: List[Result] = []

        # 1. 初期ページへアクセス
        self.handler.access(BASE_URL, cl='firstChild')

        # 2. 検索ボタンを押す
        self.handler.driver.find_element_by_xpath(
            XPATHS['search_button']
        ).send_keys(Keys.ENTER)
        self.handler.wait(_id="search-results")
        self.wait()

    @staticmethod
    def wait() -> None:
        time.sleep(TIME_SPAN)

    def move_to_next(self):
        self.handler.driver.find_element_by_xpath(
            XPATHS['next_button']
        ).send_keys(Keys.ENTER)
        self.handler.wait(_id="search-results")
        self.wait()

    def read_table(self, recursive=False) -> None:
        self.handler.set_soup()

        for line in self.handler.soup.find("table", {"id": "search-results"}).findAll("tr"):
            image_td = line.find("td", {"class": "firstChild"})
            if image_td is None:
                # 最初の一行は th なので, みつからない => continue
                continue

            link = image_td.find("a").find('img').get('src')
            age = line.find("td", {"class": "lastChild"}).get_text()

            if age.isdigit():
                result = Result(age=int(age), _id=self._id, link=link)
                result.save()
                self.results.append(result)
                self._id = self._id + 1
                self.wait()

                print(result)  # Log

        if recursive:
            self.wait()

            # 次のページへ行き, 再び同様の処理
            self.move_to_next()
            self.read_table(recursive=True)

    def run(self) -> None:
        self.read_table(recursive=True)
        self.handler.fin()


if __name__ == '__main__':
    Main(browser=False, init_id=105).run()
