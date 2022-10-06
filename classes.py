from abc import abstractmethod, ABC
from math import ceil

import requests


class Engine(ABC):
    """
    Абстрактный класс для поисковых систем
    """

    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    """
    Класс Head Hunter
    """

    def __init__(self, name_job: str, quantity):
        self.text = name_job
        self.iter = ceil(float(quantity) / 100)
        self.url = 'https://api.hh.ru/vacancies/'

    def get_request(self, page: int):
        param = {'text': self.text, 'page': page, 'per_page': 100, 'area': 113}
        return requests.get(self.url, params=param)


class Superjob(Engine):
    """
    Класс Superjob
    """

    def __init__(self, name_job: str):
        self.text = name_job
        self.url = 'https://russia.superjob.ru/vacancy/search/?keywords='

    def get_request(self):
        url = self.url + self.text
        response = requests.get(url)
        return response


class Vacancy():
    def __init__(self, title: str, reference: str, description: str, salary: str, hh=False):
        # self.data = data
        self.hh = hh
        self.title = title
        self.reference = reference
        self.description = description
        self.salary = salary

    def __repr__(self):
        return repr(f'{self.title}|{self.reference}|{self.description}|{self.salary}')
