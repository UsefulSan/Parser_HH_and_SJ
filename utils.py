import json
from classes import HH, Superjob, Vacancy
from bs4 import BeautifulSoup


def save_vacs(data: list) -> None:
    with open('vacancies.txt', 'a', encoding='utf-8') as file:
        for d in data:
            file.write(d.__repr__() + '\n')


def get_hh_vac(req_text, how_many):
    hh = HH(req_text, how_many)
    vac = []
    # for page in range(hh.iter):
    #     data = hh.get_request(page)
    #     json_res = json.loads(data.text)
    #     for vac in json_res['items']:
    #         vacancies.append(Vacancy(vac, hh=True))
    # save_vacs(vacancies)
    for i in range(0, how_many):

        name = self.data['name']
        reference = self.data['alternate_url']
        if self.data['snippet']['requirement'] + self.data['snippet']['responsibility']:
            description = self.data['snippet']['requirement'] + self.data['snippet']['responsibility']
        else:
            try:
                description = self.data['snippen']['requirement']
            except:
                description = self.data['snippet']['responsibility']
        try:
            salary = self.data['salary']['from']
        except:
            salary = 0
        vac.append(Vacancy(name, reference, description, salary))
    save_vacs(vac)


def get_sj_vac(name_job):
    vac = []
    sj = Superjob('python')
    response = sj.get_request()
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_="_9fIP1 _249GZ _1jb_5 QLdOc")
    title = soup.find_all('span', class_="_9fIP1 _249GZ _1jb_5 QLdOc")
    description = soup.find_all('span', class_="_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky")
    salary = soup.find_all('span', class_="_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi")
    for i in range(0, len(quotes)):
        name = title[i].find('a', href=True)
        vac.append(Vacancy(quotes[i].text, name['href'], description[i].text, salary[i].text))
    save_vacs(vac)


print(get_sj_vac('python'))
# print(get_hh_vac('python', 50))

def load_vacancy(data: list):
    with open('vacancy.txt', 'a', encoding='utf-8') as file:
        for d in data:
            file.write(d.__repr__() + '\n')
