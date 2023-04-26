text = list(input('Type a message:'))
x_num = 0
o_num = 0
for i in text:
    if x_num == 'X' or x_num == 'x':
        x_num += 1
    elif o_num == 'O' or  o_num == 'o':
        o_num += 1
        if x_num == 0 and o_num == 0:
            print('True')
        elif x_num == o_num:
            print('True')

 