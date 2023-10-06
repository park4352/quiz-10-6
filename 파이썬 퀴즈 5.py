

def gugudan_number(n):

    print('구구단을 출력합니다.\n')
    for x in range(1, n+1):
        print("------[" +str(x) + "단 ] ----------")
        for y in range(1, n+1):
            print(x,"X",y, "=", x*y)


print("-----------------")
n = int(input("몇 단까지 출력할까요"))

gugudan_number(n)


