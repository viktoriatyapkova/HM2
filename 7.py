x = int(input())
s = 2 # начальное кол-во делителей
if x**0.5 % 1 == 0: # для четного числа
    s += 1
    q = int(x**0.5) - 1 #значение i в последнем цикле
else:
    q = int(x**0.5) #для нечетного числа
for i in range (1, q + 1):
    if x % i == 0:
        s += 2
print (s) 