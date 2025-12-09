class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education


    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education


    @occupation.setter
    def occupation(self, new_job):
        self.__occupation = new_job

    @higher_education.setter
    def higher_education(self, value):
        self.__higher_education = value


    def introduce(self):
        edu = "есть высшее образование" if self.__higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. "
              f"У меня {edu}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        edu = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился в группе {self.group_name}. У меня {edu}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Моё хобби {self.hobby}. У меня {edu}.")




cl1 = Classmate("Кристина", "20.02.2004", "студент", True, "IN-2-24")
cl1.introduce()

fr1 = Friend("Ирина", "14.02.2005", "студент", True, "шыть")
fr1.introduce()
