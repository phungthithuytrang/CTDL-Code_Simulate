import matplotlib.pyplot as plt
 

def Data():
    data=[[]]
    temp=[]
    name=[]
    i=0
    for line in open('sample.txt', 'r'):
        lines = [i for i in line.split()]
        if i==0:
            for j in lines:
                name.append(j)
                temp=[]
                data.append(temp)
        else:
            for j in lines:
                num=lines.index(j)
                data[num].append(float(j))
        i=i+1
 
    for dl in data:
       print("@")
       for i in dl:
           print(i)
    for z in data[1:-1]:
        plt.plot(data[0], z , label=name[data.index(z)], marker = 'o')
        plt.yticks(z)

    plt.title("Simulate")
    plt.xlabel('File size (kb)')
    plt.ylabel('Time')

    plt.legend()
    plt.show()

def finddetail(str,title):
    data=[[]]
    x=[]
    for line in open(str, 'r'):
        lines = [i for i in line.split()]
        x.append(lines[0])
        temp=[]
        for j in lines[1:]:
            temp.append((float)(j))
        data.append(temp)
    minL=[]
    meanL=[]
    maxL=[]
    for dl in data[1:]:
        minL.append(min(dl))
        maxL.append(max(dl))
        meanL.append(sum(dl)/len(dl))

    #plt.plot(x, minL , label="min", marker = 'o')
    #plt.plot(x, maxL , label="max", marker = 'o')
    plt.plot(x, meanL , label="mean", marker = 'o')

    #plt.yticks(minL)
    #plt.yticks(maxL)
    plt.yticks(meanL)

    plt.title(title)
    plt.xlabel('File size (kb)')
    plt.ylabel('Time (s)')

    plt.legend()
    #plt.show()
    print(title,"\n")
    for z in x:
        print(z,"\t",minL[x.index(z)],"\t",meanL[x.index(z)],"\t",maxL[x.index(z)],"\n")


def CTDL():
    read=['docBTree1.txt','docAVL1.txt','docBST1.txt','docTrie1.txt']
    compare=['sosanhBTree1.txt','sosanhAVL1.txt','sosanhBST1.txt','sosanhTrie1.txt']
    name=['BTree','AVL','BST','Trie']
    title=['Mean Readfile Time','Mean Compare Time']
    Process(read,name,title[0])
    Process(compare,name,title[1])

def BlockandSen():
    file=['timecompareBlock.txt','timecompareSen.txt']
    name=['Block','Sentence']
    Process(file,name,'Efficient')


def CTDLDetail():
    read=['docBTree1.txt','docAVL1.txt','docBST1.txt','docTrie1.txt']
    compare=['sosanhBTree1.txt','sosanhAVL1.txt','sosanhBST1.txt','sosanhTrie1.txt']
    name=['BTree','AVL','BST','Trie']
    for x in read:
        t=[x]
        Process(t,name,read[read.index(x)])
    print("\n\n")
    for x in compare:
        t=[x]
        Process(t,name,compare[compare.index(x)])

def Process(list,name,title):
    first=[]
    second=[]
    chart=[]
    data=[]
    for line in open(list[0], 'r'):
        lines = [i for i in line.split()]
        first.append(lines[0])
        second.append(lines[1])
        temp=[]
        for j in lines[2:]:
            temp.append((float)(j))
        data.append(temp)
    chart.append(data)

    if(len(list)==1):
        meanL=[]
        maxL=[]
        minL=[]
        for dl in data:
            minL.append(min(dl))
            maxL.append(max(dl))
            meanL.append(sum(dl)/len(dl))
        x=[]
        for i in first:
            x.append('P'+str(first.index(i)+1))
        plt.plot(x, meanL)
        plt.title(title)
        plt.xlabel('File pair')
        plt.ylabel('Time(s)')
        print(title,'\n')
        for z in x:
            print(z,"\t",first[x.index(z)],"\t",second[x.index(z)],"\t",minL[x.index(z)],"\t",meanL[x.index(z)],"\t",maxL[x.index(z)],"\n")
        #plt.show()
  
    if(len(list)>1):
        for item in list[1:]:
            data=[]
            for line in open(item, 'r'):
                lines = [i for i in line.split()]
                temp=[]
                for j in lines[2:]:
                    temp.append((float)(j))
                data.append(temp)
            chart.append(data)
        meanL=[]
        for ch in chart:
            meanN=[]
            for dl in ch:
                meanN.append(sum(dl)/len(dl))
            meanL.append(meanN)
        x=[]
        for i in first:
            x.append('P'+str(first.index(i)+1))
        index=0;
        print(len(x))
        print(len(meanL))
        for line in meanL:
            plt.plot(x, line , label=name[index])
            index=index+1
            plt.yticks(line)

        plt.title(title)
        plt.xlabel('File pair')
        plt.ylabel('Time(s)')
        plt.legend()

        plt.show()

def Resultcompare1(file1,file2):
    first=[]
    second=[]
    data1=[]
    data2=[]
    y=[]
    x=[]
    for line in open(file1, 'r'):
        lines = [i for i in line.split()]
        first.append(lines[0])
        second.append(lines[1])
        data1.append(float(lines[2]))

    for line in open(file2, 'r'):
        lines = [i for i in line.split()]
        data2.append(float(lines[2]))

    for i in range(len(first)):
        y.append(abs(data1[i]-data2[i]))

    for i in first:
        x.append('P'+str(first.index(i)+1))
    
    plt.plot(x, y)
    plt.show()
def Resultcompare2(file):
    first=[]
    second=[]
    data=[]

    for line in open(file, 'r'):
        lines = [i for i in line.split()]
        data
        first.append(lines[0])
        second.append(lines[1])
        temp=[]
        for j in lines[2:]:
            temp.append(float(j))

    for i in first:
        x.append('P'+str(first.index(i)+1))
    plt.plot(x, data)

#CTDL()

#finddetail('desdata.txt','Des file Readtime')
#finddetail('sourdata.txt','Sour file Readtime')
#finddetail('sosanhBTree1.txt','Compare Time')
#list=['sosanhBTree1.txt']
#name=['abc']
#Process(list,name,"Compare Time")
#CTDLDetail()
#Resultcompare1('kqSen.txt','kqBlock.txt')
BlockandSen()






