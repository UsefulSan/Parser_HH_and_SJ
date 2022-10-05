import json
from classes import HH, Superjob, Vacancy
from bs4 import BeautifulSoup


def save_vacs(data: list) -> None:
    with open('vacancies.txt', 'a', encoding='utf-8') as file:
        for d in data:
            file.write(d.__repr__() + '\n')


def get_hh_vac(req_text, how_many):
    hh = HH(req_text, how_many)
    vacancies = []
    for page in range(hh.iter):
        data = hh.get_request(page)
        json_res = json.loads(data.text)
        for vac in json_res['items']:
            vacancies.append(Vacancy(vac, hh=True))
    save_vacs(vacancies)


def get_sj_vac(name_job):
    sj = Superjob(name_job)
    sj.get_request(50)


print(get_sj_vac('python'))


def load_vacancy(data: list):
    with open('vacancy.txt', 'a', encoding='utf-8') as file:
        for d in data:
            file.write(d.__repr__() + '\n')
