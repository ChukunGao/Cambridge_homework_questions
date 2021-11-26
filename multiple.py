def gcd(a, b):
        while b:
                a, b = b, a%b
        return a

for i in range(2, 20):
    for j in range(i+1, 20):
        if gcd(j, i) > 1:
                break
        tempi = i
        tempj = j
        continuelist = 0
        testnum = 1
        flag = 0
        flag2 = 0
        lastzero = 0
        while continuelist < tempi*tempj:
                while testnum > 0:
                        if flag2 == 0:
                                temptestnum = testnum
                        if testnum % tempi == 0 or testnum % tempj == 0:
                                flag = 1
                        testnum -= tempj
                        flag2 = 1
                if flag == 1:
                        continuelist += 1
                else:
                        continuelist = 0
                        lastzero = temptestnum
                testnum = temptestnum + 1
                flag2 = 0
                flag = 0
        lastzero += 1
        print(i, j, lastzero)