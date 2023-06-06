def sorter():
    text = input("Type a message:")
    text = text.lower()

    x_num = text.count('x')
    o_num = text.count('o')
    if x_num == o_num or (x_num == 0 and o_num == 0) or (x_num == 0 or o_num == 0):
         print('True')
    else:
         print('False')
sorter()
