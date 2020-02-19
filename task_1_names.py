# -*- coding: utf-8 -*-

# Задача с именами
# Есть файл с именами. Нужно выполнить следующие действия и посчитать результат:
#
# 1) Отсортировать все имена в лексикографическом порядке
# 2) Посчитать для каждого имени алфавитную сумму – сумму порядковых номеров букв (MAY: 13 + 1 + 25 = 39)
# 3) Умножить алфавитную сумму каждого имени на порядковый номер имени в отсортированном списке (индексация
# начинается с 1). Например, если MAY находится на 63 месте в списке, то результат для него будет 63 * 39 = 2457.
# 4) Просуммировать произведения из п. 3 для всех имен из файла и получить число. Это число и будет ответом.

SOURCE_FILE = 'путь до файла'


class NameOperations:

    def __init__(self, file):
        self.file = file
        self.sorted_list = None
        self.alpha_sum_list = []
        self.multiplication_list = []
        self.the_answer = 0

    def run(self):
        self._get_sorted_list()
        self._alpha_sum()
        self._multiplication()
        self._final_sum()

    def _get_sorted_list(self):
        '''Отсортировать все имена в лексикографическом порядке'''
        with open(self.file, 'r', encoding='utf-8') as file:
            for line in file:
                words_list = line.split(sep=',')
                clean_word_list = []
                for word in words_list:
                    clean_word_list.append(word.strip('"'))
            self.sorted_list = sorted(clean_word_list)
            print(self.sorted_list)
            return self.sorted_list

    def _alpha_sum(self):
        '''Посчитать для каждого имени алфавитную сумму – сумму
        порядковых номеров букв (MAY: 13 + 1 + 25 = 39)'''
        for word in self.sorted_list:
            one_word_sum = 0
            for letter in word:
               one_word_sum += ord(letter) - 64
            self.alpha_sum_list.append(one_word_sum)
        print(self.alpha_sum_list)
        return self.alpha_sum_list

    def _multiplication(self):
        '''Умножить алфавитную сумму каждого имени на порядковый номер
         имени в отсортированном списке (индексация начинается с 1).
         Например, если MAY находится на 63 месте в списке,
         то результат для него будет 63 * 39 = 2457'''

        for i in range(len(self.alpha_sum_list)):
            self.multiplication_list.append((i + 1) * self.alpha_sum_list[i])
        print(self.multiplication_list)
        return self.multiplication_list

    def _final_sum(self):
        '''Просуммировать произведения из п. 3 для всех имен
        из файла и получить число. Это число и будет ответом.'''
        self.the_answer = sum(self.multiplication_list)
        print(self.the_answer)
        return self.the_answer


operations = NameOperations(file=SOURCE_FILE)
operations.run()
assert len(operations.multiplication_list) == len(operations.alpha_sum_list)
assert ord('A') - 64 == 1
