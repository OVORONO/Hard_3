from functools import reduce

def reduce_fun(prev, tec):
    if tec[0] > prev[0]:
        print(tec[0], ' '.join(tec[1]))
        return tec
    else:
        return prev

f = open('news.txt', 'r', encoding="utf8")
array = []
for line in f.readlines():
    count, *post = line.split()
    array.append([int(count), post])

print(array[0][0], ' '.join(array[0][1]))
reduce(reduce_fun, array)


'''

newspaper = News('news(к 3 доп задаче).txt').readNews().postNews()
'''
#g = input()
#a = 0
#while a < 100:
#    sps = input()
#    sps = int(sps)
#    if a < sps:
#        a = sps
#        print(a)
#    else:
#        print('иди нахуй')

#mass = [1, 13, 91, 11, 82, 12]
#maxim = mass[0:1:1]
#oleg = mass[1:2:1]
#igor = mass[2:3:1]
#gena = mass[3:4:1]
#lexa = mass[4:5:1]
#ara = mass[5:6:1]

#while maxim < oleg and igor and gena and lexa:

#    if maxim < ara:
#        maxim = ara
#    elif maxim < lexa:
#        maxim = lexa
#    elif maxim < gena:
#        maxim = gena
#    elif maxim < igor:
#        maxim = igor
#    elif maxim < oleg:
#        maxim = oleg


#print(maxim)
#def large(arr):
#    max_ = arr[0]
#    for ele in arr:
#        if ele > max_:
#           max_ = ele
#    return max_


#result = large(mass)
#print(result)
#print(mass)


#with open('news(к 3 доп задаче).txt','r+') as f:
#    for i in iter(f):

#        Headline = i
#        sps.append(Headline)

#print(sps)
#       print(re.search(r'\d+', Headline).group())






        #num = [int(x) for x in i.split() if x.isdigit()]






#print("введите слово")
#a = input()

#with open('news(к 3 доп задаче).txt','r+') as f:

#    for i in iter(f):
#        if a in i:
#            print(i)

#f = open('news(к 3 доп задаче).txt','r+')
#if a in f.read():
#    print(f.readline())
#else:
#    print ("Данного числа в тексте нету")
#    exit()

#def check_ones_only(lst):
#    for s in lst:
#       if not s.isdigit() or s.count('1') != len(s):
#            return False
#    return True

#print(s)

#a1="1"
#b1 = int(a1)
#a2="2"
#b2 = int(a2)
#a3="3"
#b3 = int(a3)
#a4="4"
#b4 = int(a4)
#a5="5"
#b5 = int(a5)
#a6="6"
#b6 = int(a6)
#a7="7 "
#b7 = int(a7)
#a8="8 "
#b8 = int(a8)
#a9="9 "
#b9 = int(a9)
#a10="10 "
#b10 = int(a10)
#a11="11 "
#b11 = int(a11)
#a12="12 "
#b12 = int(a12)
#a13="13 "
#b13 = int(a13)
#a14="14 "
#b14 = int(a14)
#a15="15 "
#b15 = int(a15)
#a16="16 "
#b16 = int(a16)
#a17="17 "
#b17 = int(a17)
#a18="18 "
#b18 = int(a18)
#a19="19 "
#b19 = int(a19)
#a20="20 "
#b20 = int(a20)
#a999="999"
#b999 = int(a999)

#data = []
#with open("news(к 3 доп задаче).txt") as file:
#    for line in file:
#        data.append([str(x) for x in line.split()])

#file = open("news(к 3 доп задаче).txt", "r+")
#chisla = []
#print(data)
#for chisla in data:
#    if 5 in data:
#        chisla.append(b5)
#for chisla in data:
#    if '6' in file:
#        chisla.append(b6)
#print(chisla)


#    for i in iter(file):
#        if chisla in i:
#            print(i)

#    chisla = [int(chisla)]
#max = reduce(lambda a, b: a if (a > b) else b, chisla)
#print(max)
#print(chisla)


#for i in iter(file):
#    if a in i:
#        print(i)
