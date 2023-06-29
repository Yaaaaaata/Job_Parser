class Job:
    def __init__(self, title, link, salary, description):
        """
        Конструктор класса Job.

        :param title: Название вакансии.
        :param link: Ссылка на вакансию.
        :param salary: Зарплата.
        :param description: Описание вакансии.
        """
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def to_dict(self):
        """
        Возвращает словарь с атрибутами объекта.

        :return: Словарь с атрибутами объекта.
        """
        return {'title': self.title, 'salary': self.salary, 'description': self.description}

    def __eq__(self, other):
        """
        Проверяет равенство объектов по зарплате.

        :param other: Другой объект класса Job.
        :return: True, если зарплаты равны, иначе False.
        """
        try:
            if isinstance(other, Job):
                return self.validate_salary(self.salary) == self.validate_salary(other.salary)
            return NotImplemented
        except TypeError:
            pass

    def __lt__(self, other):
        """
        Проверяет, что зарплата текущего объекта меньше зарплаты другого объекта.

        :param other: Другой объект класса Job.
        :return: True, если зарплата текущего объекта меньше зарплаты другого объекта, иначе False.
        """
        try:
            if isinstance(other, Job):
                if self.salary is None or other.salary is None:
                    return False
                return self.validate_salary(self.salary) < self.validate_salary(other.salary)
            return NotImplemented
        except TypeError:
            pass

    def __gt__(self, other):
        """
        Проверяет, что зарплата текущего объекта больше зарплаты другого объекта.

        :param other: Другой объект класса Job.
        :return: True, если зарплата текущего объекта больше зарплаты другого объекта, иначе False.
        """
        try:
            if isinstance(other, Job):
                if self.salary is None or other.salary is None:
                    return False
                return self.validate_salary(self.salary) > self.validate_salary(other.salary)
            return NotImplemented
        except TypeError:
            pass

    @staticmethod
    def validate_salary(salary):
        """
        Проверяет корректность значения зарплаты.

        :param salary:
        """
        if salary is None or salary == 0:
            return float('-inf')
        return salary

    @classmethod
    def from_dict(cls, data):
        """
        Создает объект класса Job из словаря.

        :param cls: Класс Job.
        :param data: Словарь с атрибутами объекта.
        :return: Объект класса Job.
        """
        return cls(data['title'], data['company'], data['salary'], data['description'])
