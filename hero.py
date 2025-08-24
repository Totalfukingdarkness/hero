from faker import Faker
import file_operations
from random import *
import os

SKILLS = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд']

ALPHABET = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}

def runic_skill(skill: str, alphabet: dict) -> str:
    modified_skill: str = ''
    for letter in skill:
        modified_letter = letter.replace(letter, alphabet[letter])
        modified_skill = modified_skill + modified_letter
    return modified_skill

def main():
    os.makedirs('output/svg/', mode=0o777, exist_ok=True)

    for i in range(1, 11):
        fake = Faker('ru_RU')
        first_name = fake.first_name()
        last_name = fake.last_name()
        job = fake.job()
        city = fake.city()

        random_strength = randint(3, 18)
        random_agility = randint(3, 18)
        random_endurance = randint(3, 18)
        random_intelligence = randint(3, 18)
        random_luck = randint(3, 18)

        select_skill = sample(SKILLS, 3)
        skill_1 = runic_skill(select_skill[0], ALPHABET)
        skill_2 = runic_skill(select_skill[1], ALPHABET)
        skill_3 = runic_skill(select_skill[2], ALPHABET)

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'job': job,
            'town': city,
            'strength': random_strength,
            'agility': random_agility,
            'endurance': random_endurance,
            'intelligence': random_intelligence,
            'luck': random_luck,
            'skill_1': skill_1,
            'skill_2': skill_2,
            'skill_3': skill_3,
        }

        file_operations.render_template('hero/charsheet.svg', f'output/svg/result{i}.svg', context)


if __name__ == '__main__':

    main()
