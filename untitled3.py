# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fjU5DubgFbndWhGlVd2PpzewEzVZ0-pw
"""

word1 = "word1"
word2 = "word2"

if abs(len(word1) - len(word2)) > 1:
    print(False)
    # если длина слов отличается более чем на один, выводим False

if len(word1) == len(word2):
    difference = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            difference += 1
    if difference > 1:
        print(False)
    else:
        print(True)
    # в случае, если слова одинаковой длины, сравниваем их по символам

if len(word1) != len(word2):
    if len(word1) > len(word2):
        word1, word2 = word2, word1
    index = 0
    while index < len(word1) and word1[index] == word2[index]:
        index += 1
    if index == len(word1):
        print(True)
    else:
        print(word1[index:] == word2[index + 1:])
    # если длина слов отличается на 1, и сравниваем символы, если символ добавлен в начало нового слова, сравниваем со следующим за ним символом, прибавляем к индексу следующих букв 1

print(False)