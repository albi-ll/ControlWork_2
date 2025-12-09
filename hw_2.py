class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce (self):
        print(f'Меня зовуд {self.name}. Я родился {self.birth_date}.'
              f' По профессии {self.occupation}. Образования {self.higher_education}  ')

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce (self):
        print( f'Меня зовуд {self.name}. Я родился {self.birth_date}.'
              f' По профессии {self.occupation}. Образования {self.higher_education}  '
               f'Мой группа {self.group_name} ')

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education , hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce (self):
        print(f'Меня зовуд {self.name}. Я родился {self.birth_date}.'
              f' По профессии {self.occupation}. Образования {self.higher_education} ,'
              f'Мой хобби  {self.hobby} ')

frieren = Person('Frieren', '1999.09.01', 'fullsart', 'KNY')
class_mate_one = Classmate('Meg', '2002.12.10', 'backend', 'BGY',"group-59")
class_mate_two = Classmate('Bet', '2005.12.10', 'frontend ', 'ASYA','group-61')
class_friend_one = Friend('Jony', '1999.12.10',
                       'backend', 'KRSU', 'читать')
class_friend_two = Friend('Koly', '2002.02.08',
                      'frontend', 'KGMA', 'петь')
frieren.introduce()
class_mate_one.introduce()
class_mate_two.introduce()
class_friend_one.introduce()
class_friend_two.introduce()


