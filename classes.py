from abc import abstractmethod, ABC
import json
import requests
from bs4 import BeautifulSoup


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, request_name, quantity):
        self.name = request_name
        self.iter = int(quantity / 100)
        self.url = 'https://api.hh.ru/vacancies'

    def get_request(self, page):
        param = {'text': self.name, 'page': page, 'pre_page': 100, 'area': 113}
        res = requests.get(self.url, params=param)
        return res


class Superjob(Engine):

    def __init__(self, name_job):
        self.text = name_job
        self.url = 'https://russia.superjob.ru/vacancy/search/?keywords='

    # @property
    def get_request(self, page):
        url = self.url + self.text
        response = requests.get(url)
        return response


class Vacancy():
    def __init__(self, data, hh=False):
        self.data = data
        self.hh = hh
        self.title = self.get_title()
        self.reference = self.get_reference()
        self.description = self.get_description()
        self.salary = self.get_salary()

    def __repr__(self):
        return repr(f'{self.title}|{self.reference}|{self.description}|{self.salary}')

    def get_title(self):
        if self.hh:
            return self.data['name']

    def get_reference(self):
        if self.hh:
            return self.data['alternate_url']


    def get_description(self):
        if self.hh:
            if self.data['snippet']['requirement'] and self.data['snippet']['responsibility']:
                return self.data['snippet']['requirement'] + self.data['snippet']['responsibility']
            else:
                try:
                    return self.data['snippet']['requirement']
                except:
                    return self.data['snippet']['responsibility']

    def get_salary(self):
        if self.hh:
            try:
                return self.data['salary']['from']
            except:
                return 0

    def get_sj(self):
        if self.hh:
            pass
        else:
        #     name = self.data['name']
        #     reference = self.data['alternate_url']
        #     if self.data['snippet']['requirement'] + self.data['snippet']['responsibility']:
        #         description = self.data['snippet']['requirement'] + self.data['snippet']['responsibility']
        #     else:
        #         try:
        #             description = self.data['snippen']['requirement']
        #         except:
        #             description = self.data['snippet']['responsibility']
        #     try:
        #         salary = self.data['salary']['from']
        #     except:
        #         salary = 0
        #     return name, reference, description, salary
        # else:
            sj = Superjob('python')
            response = sj.get_request()
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('span', class_="_9fIP1 _249GZ _1jb_5 QLdOc")
            title = soup.find_all('span', class_="_9fIP1 _249GZ _1jb_5 QLdOc")
            description = soup.find_all('span', class_="_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky")
            salary = soup.find_all('span', class_="_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi")
            for i in range(0, len(quotes)):
                name = title[i].find('a', href=True)
                print(quotes[i].text, name['href'], description[i].text, salary[i].text)

    def output_all(self):
        vacancies_list = []
        with open('vacancies.txt', 'r', encoding='utf-8') as file:
            for line in file.readline():
                vacancies_list.append(line)
            return vacancies_list


# sj = Superjob('java')
# sj.get_request()



v = Vacancy('python')
v.get_title()
