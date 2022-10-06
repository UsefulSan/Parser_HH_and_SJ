from classes import Superjob

def main():
    name_job = input('Введите название вакансии')
    sj = Superjob()
    sj.get_request(name_job)


if __name__ == "__main__":
    main()

from utils import *


def main():
    while True:
        user_input = input('Выберите действие:\n1. Сформировать файл с вакансиями с HH и Superjob\n2. Вывести список '
                           'из вакансий c HH\n3. Вывести список вакансии с SJ\nВвод: ')
        if int(user_input) == 1:
            vacancy_1 = hh_data()
            load_vacancy(vacancy_1)
            vacancy_2 = sj_data()
            load_vacancy(vacancy_2)
            print('Файл загружен!')
        if int(user_input) == 2:
            vacancy_1 = hh_data()
            for i in range(5):
                print(i+1, vacancy_1[i])
        if int(user_input) == 3:
            vacancy_2 = sj_data()
            for i in range(5):
                print(i + 1, vacancy_2[i])


if __name__ == '__main__':
    main()





