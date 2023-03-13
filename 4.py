a=int(input())
b=int(input())
max=1 # изначальный максимальный отрезок макс. отрезок 
n=1 # кол-во чисел
while a != 0 or  b != 0:
    while a>b:  # возрастающий отрезок
        n+=1 
        if n>max: # если отрезок больше макс.отрезка, то мы присваиваем  значение этого отрезка
            max=n 
            a=b
            b=int(input()) 
        else:
            a=b
            b=int(input()) # продолжаем послед-ть, не присваивая макс.знач.
    n=1 
    while a<b: # убывающий отрезок
        n+=1 
        if n>max: # аналогично
            max=n
            a=b
            b=int(input())
        else:
            a=b
            b=int(input())
    n=1
    while a==b: # если отрезок - прмая вида х=а или у=а , то отрезок всегда один
        n=1
        a=b
        b=int(input())
print(max)