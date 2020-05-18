from .chrome_handler import ChromeHandler


class Main:
    def __init__(self, browser: bool = False) -> None:
        self.handler = ChromeHandler(browser=browser)

    def run(self):
        pass


if __name__ == '__main__':
    Main(browser=True).run()
