from abc import ABC, abstractmethod


class JobSiteAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_text):
        """
        Абстрактный метод для получения списка вакансий с сайта по заданному тексту поиска.
        :param search_text: Текст поиска
        :return: список вакансий
        """
        pass


class JobFile(ABC):
    @abstractmethod
    def add_jobs(self, job):
        """
        Абстрактный метод для добавления вакансии в файл.
        :param job: Вакансия
        """
        pass

    @abstractmethod
    def get_top_n_jobs(self, **kwargs):
        """
        Абстрактный метод для получения топ N вакансий из файла.
        :param kwargs: Дополнительные параметры
        :return: топ N вакансий
        """
        pass

    @abstractmethod
    def clear(self, job):
        """
        Абстрактный метод для очистки файла от вакансий.
        :param job: Вакансия
        """
        pass
