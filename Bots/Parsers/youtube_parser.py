from bs4 import BeautifulSoup as BS
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class ParserYoutube:
    """
    Парсер страницы Youtube

    Methods:
        one_request создает объект, который будет искать видео по определенному запросу
        parse Парсит сайт и возвращает список ссылок на найденные видео

    Returns:
        Объект, который парсит и возвращает ссылки со страницы
        Количество ссылок определяется пользователем
    """
    def __init__(self) -> None:
        self._link = "https://www.youtube.com/"

    @classmethod
    def one_request(cls, request: str):
        """
        Парсер страницы Youtube с определенным запросом

        :param request запрос в Youtube

        :return объект класса, который парсит страницу с запросом
        """
        self = cls.__new__(cls)
        self._link = "https://www.youtube.com/results?" + urlencode({"search_query": request})
        return self

    def parse(self, n: int) -> list[str]:
        """
        Поиск и вывод ссылок на первые ролики

        :param n количество ссылок, которые нужно вывести со страницы

        :return список ссылок на видео по ссылке
        """
        match self._link:
            case "https://www.youtube.com/": return self._parse_main(n)
            case _: return self._parse_by_link(n)

    def _parse_main(self, n: int) -> list[str]:
        """
        Парсинг главной страницы сайта

        :param n количество ссылок, которые нужно вывести со страницы

        :return список ссылок на видео по ссылке
        """
        links: list[str] = []  # Ссылки на видео

        # Используя Chrome браузер, открываем страницу Youtube
        browser = webdriver.Chrome()
        browser.get(self._link)
        html = browser.page_source
        browser.quit()

        # Парсинг html кода
        soup = BS(html, "html.parser")
        contents = soup.find_all("div", {"class": "style-scope ytd-rich-item-renderer", "id": "content"})

        # Находим видео и сохраняем их в список
        for video in contents:
            video = video.find_next('a', {"id": "thumbnail"})
            links.append(f"https://www.youtube.com{video.attrs['href']}")
            if len(links) == n:
                break

        return links

    def _parse_by_link(self, n: int) -> list[str]:
        """
        Парсинг страницы с определенным запросом

        :param n количество ссылок, которые нужно вывести со страницы

        :return список ссылок на видео по ссылке
        """
        links: list[str] = []  # список видео

        # Используя Chrome браузер, открываем страницу Youtube
        browser = webdriver.Chrome()
        browser.get(self._link)
        html = browser.page_source
        sleep(3)
        browser.quit()

        # Парсинг html кода
        soup = BS(html, "html.parser")
        contents = soup.find_all("ytd-thumbnail", {"class": "style-scope ytd-video-renderer"})

        # Находим видео и сохраняем их в список
        for video in contents:
            video = video.find_next('a', {"id": "thumbnail"})
            links.append(f"https://www.youtube.com{video.attrs['href']}")
            if len(links) == n:
                break

        return links


# Пример работы - вывод 5 ссылок с главной страницы и 5 ссылок по запросу "Майнкрафт"
if __name__ == "__main__":
    parserYt = ParserYoutube()
    print(*parserYt.parse(5), sep='\n')  # 5 случайных популярных видео с главной страницы Youtube

    parserLinkYt = ParserYoutube().one_request("Майнкрафт")
    print(*parserLinkYt.parse(5), sep='\n')  # 5 видео с Youtube по запросу
