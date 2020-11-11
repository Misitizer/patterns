import re
from abc import ABC, abstractmethod


class AbstractClient(ABC):

    @abstractmethod
    def __init__(self, api_key: str) -> None:
        pass

    @abstractmethod
    def shorten_link(self, link: str) -> str:
        pass


class ShortenerClient(AbstractClient):

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def shorten_link(self, link: str) -> str:
        return 'xxx'


class TextProcessor:

    def __init__(self, text, shortener_client: AbstractClient) -> None:
        self.text = text
        self.shortener_client = shortener_client

    def process(self) -> str:
        changed_text = self.text

        links = re.findall(
            r'https?://[^\r\n\t") ]*',
            self.text,
            flags=re.MULTILINE
        )

        for link in links:
            shortened = self.shortener_client.shorten_link(link)
            changed_text = changed_text.replace(link, shortened)

        return changed_text


processor = TextProcessor(
    text='Ссылка 1: https://yandex.ru  Ссылка 2: https://google.com',
    shortener_client=ShortenerClient(api_key='123')
)

print(processor.process())