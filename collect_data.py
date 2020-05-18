from selenium.webdriver.common.keys import Keys
from typing import Dict, Any

from scrape.chrome_handler import ChromeHandler
from scrape.settings import XPATHS, BASE_URL


class Main:
    def __init__(self, browser: bool = False, init_id: int = 0) -> None:
        self.handler = ChromeHandler(browser=browser)

        self.id = init_id
        self.results: Dict[str, Any] = {}
        """
        {
            "age_id": {
                "age": 28,
                "image_path": "/path/to/hoge/age_id.png",
            }
        }
        """

        # 1. 初期ページへアクセス
        self.handler.access(BASE_URL, cl='firstChild')

        # 2. 検索ボタンを押す
        self.handler.driver.find_element_by_xpath(
            XPATHS['search_button']
        ).send_keys(Keys.ENTER)
        self.handler.wait(_id="search-results")

    def read_table(self) -> None:
        table_lines = self.handler.driver.find_element_by_id("search-results") \
            .find_element_by_tag_name('tbody') \
            .find_elements_by_tag_name('tr')

        for line in table_lines:
            # tbodyにヘッダもなぜか含まれてるので, スキップする
            if line.get_attribute('class') != 'firstChild':
                # メインロジック
                link = line.find_element_by_class_name('firstChild') \
                    .find_element_by_tag_name('a') \
                    .get_attribute('href')
                age = line.find_element_by_class_name('lastChild')
                # .get_attribute("textContent")

                # print(link, ' => ', age, '...')
                print('age', age)
                print('age.text', age.text)
                print('age.get_attrivute', age.get_attribute('textContent'))
                print('attrs', age.__dict__)

    def run(self) -> None:
        self.read_table()


if __name__ == '__main__':
    Main(browser=True).run()
