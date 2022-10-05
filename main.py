from classes import Superjob

def main():
    name_job = input('Введите название вакансии')
    sj = Superjob()
    sj.get_request(name_job)


if __name__ == "__main__":
    main()