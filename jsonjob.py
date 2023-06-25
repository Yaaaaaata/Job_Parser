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
            for job in jobs:
                json.dump(job, f, ensure_ascii=False)
                f.write("\n")

    def get_top_n_jobs(self, n):
        """
        Возвращает топ N вакансий с самой высокой зарплатой.

        :param n: Количество вакансий в топе.
        :return: Список объектов класса Job.
        """
        with open(self.file_name, "r", encoding="utf-8") as f:
            #jobs = [Job(**json.loads(line)) for line in f]
            jobs = [Job.from_dict(json.loads(line)) for line in f if line.strip()]
        sorted_jobs = sorted(jobs, key=lambda x: x.salary or 0, reverse=True)
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

