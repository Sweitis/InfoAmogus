text = input('Type a message:')
text = text.lower
x_num = 0
o_num = 0
for i in text:
    if i == 'x':
        x_num += 1
    elif i == 'o':
        o_num += 1
if x_num == o_num:
    print("True")
else:
    print("False")