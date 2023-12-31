from vacancies import HhRuAPI, SuperJobAPI
from jsonjob import JsonJobFile


def menu():
    """
    Функция для вывода меню и обработки выбора пользователя.
    """
    job_file = JsonJobFile("jobs.json")
    while True:
        print("1. Получить вакансии с SuperJob")
        print("2. Получить вакансии с HeadHunter")
        print("3. Вывести топ N вакансий по зарплате")
        print("4. Очистить файл jobs.json")
        print("5. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            keyword = input("Введите ключевое слово: ")
            sj_api = SuperJobAPI()
            jobs = sj_api.get_vacancies(keyword)
            job_file.add_jobs(jobs)
            print(f"Найдено {len(jobs)} вакансий на SuperJob")
        elif choice == "2":
            keyword = input("Введите ключевое слово: ")
            hh_api = HhRuAPI()
            jobs = hh_api.get_vacancies(keyword)
            job_file.add_jobs(jobs)
            print(f"Найдено {len(jobs)} вакансий на HeadHunter")
        elif choice == "3":
            n = int(input("Введите количество вакансий для вывода: "))
            top_jobs = job_file.get_top_n_jobs(n)
            for i, job in enumerate(top_jobs):
                profession = job.get('profession') or job.get('name')
                payment_from = job.get('payment_from') or job.get('salary', {}).get('from')
                payment_to = job.get('payment_to') or job.get('salary', {}).get('to')
                currency = job.get('currency') or job.get('salary', {}).get('currency')
                print(f"{profession} Заработная плата: {payment_from} до {payment_to} {currency}")
        elif choice == "4":
            job_file.clear(None)
            print("Файл jobs.json очищен")
        elif choice == "5":
            exit()
        else:
            print("Неправильный выбор")


if __name__ == "__main__":
    menu()
