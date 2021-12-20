"""написать функцию num_translate(), переводящую числительные от 0 до 10 с английского на русский язык.
num_translate("one") - один
num_translate("eight") - восемь"""
import random

table_num = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(table):
    return table_num.get(table)


print(num_translate(''))

"""Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
в котором ключи - первые буквы имен, а значения - списки, содержащие имена, начинающиеся с соотвествующей буквы """

co_worker = {
    'И': ['Иван','Илья'],
    'М': 'Мария',
    'П': 'Петр'
}


def thesaurus(*co_workers):
    co_dict = dict()
    for co_worker in co_workers:
        co_dict.setdefault(co_worker[0], [])
        co_dict[co_worker[0]].append(co_worker)
    return co_dict


print(thesaurus("Петр", "Мария", "Илья", "Иван"))

"""Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трех списков
(по одному из каждого):"""

game_nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
game_adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
game_adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# for nouns, adverbs, adjectives in zip (game_nouns, game_adverbs, game_adjectives):
#     print(f'{nouns}, {adverbs}, {adjectives}')

def get_jokes(num):
    joke_list = []
    for i in range(num):
        nouns = random.choice(game_nouns)
        adverbs = random.choice(game_adverbs)
        adjectives = random.choice(game_adjectives)
        joke_list.append(f'{nouns} {adverbs} {adjectives}')
    return joke_list

print(get_jokes(5))
print(get_jokes(6) == True)
