text = input("Type a message:")
text = text.lower()

x_num = text.count('x')
o_num = text.count('o')

if x_num == o_num or (x_num == 0 and o_num == 0):
    print('True')
else:
    print('False')





# Проверьте, содержит ли строка одинаковое количество "x" и "o".

# Верните логическое значение True или False 
# Строка может быть в любом регистре и содержать любые символы!

# Примеры ввода/вывода:
#   строка "ooxx" => true
#   строка "xooxx" => false
#   строка "ooxXm" => true
#   строка "zpzpzpp" => true # когда нет "x" и "o", должно быть возвращено значение true
#   строка "zzoo" => false

#elif (x_num == 0 and o_num == 0) or x_num == o_num:
    #print('True')