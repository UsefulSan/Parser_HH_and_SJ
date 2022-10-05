from abc import abstractmethod, ABC
import json
import requests
from bs4 import BeautifulSoup


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, name):
        self.text = name
        self.url = 'https://api.hh.ru/vacancies'

    def get_request(self, page):
        param = {'text': self.text, 'page': page, 'pre_page': 100, 'area': 113}
        res = requests.get(self.url, params= param).json()
        return res



class Superjob(Engine):

    @property
    def get_request(self, name_job='python'):
        data = []
        # for p in range(1):

        url = f'https://russia.superjob.ru/vacancy/search/?keywords={name_job}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('span', class_="_9fIP1 _249GZ _1jb_5 QLdOc")
        title = soup.find_all('span', class_="_9fIP1 _249GZ _1jb_5 QLdOc")
        description = soup.find_all('span', class_="_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky")
        salary = soup.find_all('span', class_="_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi")
        for i in range(0, len(quotes)):
            name = title[i].find('a', href=True)
            print(quotes[i].text, name['href'], description[i].text, salary[i].text)

# class Vacancy():
#     def __init__(self, title, reference, description, salary):
#         self.title = title
#         self.reference = reference
#         self.description = description
#         self.salary = salary
#
#     def __repr__(self):
#         return repr(f'{self.title} {self.reference} из {self.description} в {self.salary}')

# sj = Superjob()
# a = sj.get_request("java")

hh = HH('java')
for page in range(5):
    data = hh.get_request(page)
