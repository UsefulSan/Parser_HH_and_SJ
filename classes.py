from abc import abstractmethod, ABC

import requests


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, name_job, quantity):
        self.text = name_job
        self.iter = int(quantity / 100)
        self.url = 'https://api.hh.ru/vacancies'

    def get_request(self, page):
        url = self.url + self.text
        param = {'text': self.text, 'page': page, 'pre_page': 100, 'area': 113}
        response = requests.get(self.url, params=param)
        return response


class Superjob(Engine):

    def __init__(self, name_job):
        self.text = name_job
        self.url = 'https://russia.superjob.ru/vacancy/search/?keywords='

    def get_request(self):
        url = self.url + self.text
        response = requests.get(url)
        return response


class Vacancy():
    def __init__(self, title, reference, description, salary, hh=False):
        # self.data = data
        self.hh = hh
        self.title = title
        self.reference = reference
        self.description = description
        self.salary = salary

    def __repr__(self):
        return repr(f'{self.title}|{self.reference}|{self.description}|{self.salary}')
