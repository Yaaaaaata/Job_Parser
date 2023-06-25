import os
import requests
from tools import JobSiteAPI


class HhRuAPI(JobSiteAPI):
    def get_vacancies(self, search_text):
        """
        Получает список вакансий с сайта hh.ru по заданному тексту поиска.
        :param search_text: Текст поиска
        :return: список вакансий
        """
        url = 'https://api.hh.ru/vacancies'
        headers = {'User-Agent': 'api-test-agent'}
        params = {
            'text': search_text,
            'area': 1,
            'per_page': 100,
            'page': 0
        }
        response = requests.get(url, headers=headers, params=params)
        if response.ok:
            data = response.json()
            vacancies = data['items']
            print(f'Найдено вакансий: {data["found"]}')
            for vacancy in vacancies:
                name = vacancy['name']
                employer_name = vacancy['employer']['name']
                salary = vacancy.get('salary')
                description = vacancy.get('snippet', {}).get('requirement')
                if salary:
                    salary_from = salary.get('from')
                    salary_to = salary.get('to')
                    currency = salary.get('currency')
                    if salary_from and salary_to:
                        print(f'{name} - {employer_name}, зарплата от {salary_from} до {salary_to} {currency}')
                    elif salary_from:
                        print(f'{name} - {employer_name}, зарплата от {salary_from} {currency}')
                    elif salary_to:
                        print(f'{name} - {employer_name}, зарплата до {salary_to} {currency}')
                    else:
                        print(f'{name} - {employer_name}, зарплата не указана')
                else:
                    print(f'{name} - {employer_name}, зарплата не указана')
                if description:
                    print(f'Требования к соискателю: {description}')
                else:
                    print('Описание вакансии не найдено')
            return vacancies
        else:
            print('Ошибка при выполнении запроса:', response.status_code)
            return []


class SuperJobAPI(JobSiteAPI):
    def __init__(self):
        self.api_key = os.getenv('SJ_API_KEY')
        self.access_token = os.getenv('SJ_ACCESS_TOKEN')

    def get_vacancies(self, search_text):
        """
        Получает список вакансий с сайта superjob.ru по заданному тексту поиска.
        :param search_text: Текст поиска
        :return: список вакансий
        """
        url = 'https://api.superjob.ru/2.0/vacancies/?t=4&count=100'
        headers = {
            'X-Api-App-Id': self.api_key,
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {'keyword': search_text}
        response = requests.get(url, headers=headers, params=params)
        if response.ok:
            data = response.json()
            vacancies = data['objects']
            print(f'Найдено вакансий: {len(vacancies)}')
            for vacancy in vacancies:
                profession = vacancy['profession']
                payment_from = vacancy.get('payment_from')
                payment_to = vacancy.get('payment_to')
                currency = vacancy.get('currency')
                if payment_from and payment_to:
                    print(f'{profession} - зарплата от {payment_from} до {payment_to} {currency}')
                elif payment_from:
                    print(f'{profession} - зарплата от {payment_from} {currency}')
                elif payment_to:
                    print(f'{profession} - зарплата до {payment_to} {currency}')
                else:
                    print(f'{profession} - зарплата не указана')
            return vacancies
        else:
            print('Ошибка при выполнении запроса:', response.status_code)
            return []
