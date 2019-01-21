def read(data, filename):
    f=open(filename, 'r', encoding='utf-8')
    for line in f:
        line=line.strip()
        a=line.split(' || ')
        data.append(a)

def show(data):
    for i in range(len(data)):
        i = data[i]
        print(*i)

def find(data, fam):
    for line in data:
        if fam==line[0]:
            print(*line)

def dop(data, r):
    str = []
    str.append(r)
    data.append(str)
    for i in range(len(data)):
        i = data[i]
        print(*i)



data=[]
read(data,'input.txt')
show(data)
find(data,'')