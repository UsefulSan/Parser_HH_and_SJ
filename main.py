from utils import get_hh_vac, get_sj_vac, read_all, top_10


def main():
    while True:
        user_input = input('Выберите действие:\n'
                           '1. Загрузить список вакансий с HH\n'
                           '2. Загрузить список вакансий с SJ\n'
                           '3. Вывести все загруженные вакансии\n'
                           '4. Вывести топ 10 вакансий по заработной плате\n'
                           '>>> ')
        match user_input:
            case '1':
                text_input = input('Введите название должности\n' '>>> ')
                numb_input = input('Введите количество искомых вакансий\n' '>>> ')
                get_hh_vac(text_input, numb_input)
            case '2':
                text_input = input('Введите название должности\n' '>>> ')
                get_sj_vac(text_input)
            case '3':
                read_all()
            case '4':
                top_10()


if __name__ == "__main__":
    main()
