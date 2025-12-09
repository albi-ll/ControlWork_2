class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce (self, introduce):
        print(f'Меня зовуд {self.name}. Я родился {self.birth_date}. По профессии {self.occupation}. Образования {self.higher_education}  ')

frieren = Person('Frieren', '1999.09.01', 'fullsart', 'KNY')
meg = Person('Meg', '2002.12.10', 'backend', 'BGY')
bet = Person('Bet', '2005.12.10', 'frontend ', 'BGY')
frieren.introduce(meg)
bet.introduce(frieren)
meg.introduce(bet)