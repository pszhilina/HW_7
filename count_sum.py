num = int(input('Число: '))
sum2 = 0
while num > 0:
    d = num % 10
    num = num // 10
    if d % 2 != 0:
        sum2 += pow(d,2)
print(sum2)



