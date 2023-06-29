from professions import Job
from tools import JobFile
import json
from vacancies import HhRuAPI, SuperJobAPI


class JsonJobFile(JobFile):
    def __init__(self, file_name):
        """
        Конструктор класса JsonJobFile.

        :param file_name: Имя файла для хранения данных.
        """
        self.file_name = file_name
        self._create_file()

    def _create_file(self):
        """
        Создает файл для хранения данных.
        """
        with open(self.file_name, "a", encoding="utf-8") as f:
            pass

    def add_jobs(self, jobs):
        """
        Добавляет вакансии в файл.

        :param jobs: Список объектов класса Job.
        """
        with open(self.file_name, "a", encoding="utf-8") as f:
            f.write("[")
            for i, job in enumerate(jobs):
                json.dump(job, f, ensure_ascii=False)
                if i != len(jobs) - 1:
                    f.write(", \n")
            f.write("]")

    def get_top_n_jobs(self, n):
        """
        Возвращает топ N вакансий с самой высокой зарплатой.

        :param n: Количество вакансий в топе.
        :return: Список объектов класса Job.
        """
        with open(self.file_name, "r", encoding="utf-8") as f:
            jobs = json.load(f)

        def sort_key(job):
            salary = job.get('salary')
            if salary is not None:
                salary_from = salary.get('from')
                salary_to = salary.get('to')
                if salary_to is None and salary_from is None:
                    return 1, 2
                elif salary_to is None:
                    return salary_from
                elif salary_from is None:
                    return salary_to
                else:
                    return salary_from, salary_to
            else:
                payment_from = job.get('payment_from')
                payment_to = job.get('payment_to')
                if payment_to is None or payment_to == 0:
                    return payment_from
                else:
                    return payment_to

        sorted_jobs = sorted(jobs, key=sort_key, reverse=True)
        top_jobs = sorted_jobs[:n]
        return top_jobs

    def clear(self, job):
        """
        Очищает файл.

        :param job: Объект класса Job.
        """
        with open(self.file_name, 'w', encoding='utf-8') as f:
            pass


def get_jobs_from_hh():
    """
    Получает вакансии с сайта hh.ru.

    :return: Список объектов класса Job.
    """
    hh_parser = HhRuAPI()
    jobs = hh_parser.get_vacancies("Название")
    job_file = JsonJobFile("jobs.json")
    job_file.add_jobs(jobs)
    return jobs


def get_jobs_from_sj():
    """
    Получает вакансии с сайта superjob.ru.

    :return: Список объектов класса Job.
    """
    sj_parser = SuperJobAPI()
    jobs = sj_parser.get_vacancies("Название")
    job_file = JsonJobFile("jobs.json")
    job_file.add_jobs(jobs)
    return jobs


if __name__ == "__main__":
    get_jobs_from_hh()
    get_jobs_from_sj()
