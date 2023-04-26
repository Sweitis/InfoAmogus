primes = [2, 4, 7, 9]
numbers = primes
primes.extend([12, 17])
print(primes,numbers,id(primes),'\n')
 


gradient = [ ["Russia","Moscow"] , ["USA","NYC"] ]
print(gradient[0][0])



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
elif x_num == o_num or:
    print('True')
 