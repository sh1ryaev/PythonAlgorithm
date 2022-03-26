import math
import numpy

def MinCountFloor():
    print('Введите количество этажей:')
    n = int(input())
    print('Введите количество шаров:')
    k = int(input())
    br = 0
    if k == 1:
        print('Количество бросков в худшем случае = ' + str(n - 1))
        i = 1
        while i<n:
            print('Количество попыток = ' + str(i))
            print('Бросьте шар с ' + str(i) + ' этажа')
            print('Шар разбился?(y/n)')
            ans = input()
            if ans == 'y':
                print('Нужный этаж '+str(i))
                return
            i+=1
    elif k >= math.log(n, 2):
        print('Колличество бросков в худшем случае = ' + str(round(math.log(n, 2))))
        i = int(n / 2)
        u = n
        d = 1
        count = round(math.log(n,2))
        while True:
            print('Количество попыток = ' + str(count))
            print('Бросьте шар с ' + str(i) + ' этажа')
            print('Шар разбился?(y/n)')
            ans = input()
            if ans == 'y':
                k-=1
                count-=1
                u = i
            else:
                count-=1
                d = i
            diff = u - d
            if diff == 1:
                print('Нужный этаж: ' + str(u))
                return
            if k == 1:
                temp = d + 1
            else:
                i = d+round(diff/2)
    else:
        f = [[0] * k]
        f[0][0] = 1
        j = 0
        i = 0
        c = 1
        while numpy.amax(f)<=n:
            if i == 0:
                f[i][j] = 1
            elif j == 0:
                f[i][j] = i+1
            else:
                f[i][j] = f[i-1][j-1]+f[i-1][j]+1
            if c == k:
                i+=1
                j=0
                c=0
                f = numpy.vstack([f,[0]*k])
            else:
                j+=1
            c += 1
        f.tolist()
        temp = f[i-2][j-2]+1
        u = n
        d = 0
        diff = n-1
        while i>0:
            print('------------------------------')
            print('Количество попыток = ' + str(i))
            print('------------------------------')
            print('Количество шаров = ' + str(k))
            print('------------------------------')
            print('Бросьте шар с ' + str(temp) + ' этажа')
            print('Шар разбился?(y/n)')
            ans = input()
            if ans == 'y':
                k-=1
                i-=1
                u = temp
            else:
                i-=1
                d = temp
            diff = u - d
            if diff == 1:
                print('Нужный этаж: ' + str(u))
                return
            if k == 1:
                temp = d + 1
            else:
                for x in range(i):
                    for z in range(k):
                        if f[x][z] + 1 >= diff:
                            temp = d + f[x - 1][z - 1] + 1


