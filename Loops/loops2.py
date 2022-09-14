def Biggie_Size(list):
    for x in range (len(list)):
        if list[x]>0:
            list[x]="big"    #task 1
    return list
z=[-1,-5,5,-3,6,1,5]
# print(Biggie_Size(z))

def Count_Positives (list):
    count=0
    for x in range (len(list)):
        if list[x]>0:
            count+=1
    list[len(list)-1]=count   #task 2
    return list
x=[1,6,-4,-2,-7,-2]
# print(Count_Positives (x))

def Sum_Total(list):
    total=0
    for x in range (len(list)):  #task 3
        total+=list[x]
    return total
x=[1,2,3,4]
# print(Sum_Total(x))

def Average(list):
    total=0
    for x in range (len(list)):
        total+=list[x]
    return (total/(len(list)))  #task 4
x=[1,2,3,4]
# print(Average(x))

def Length(list):
    return(len(list))   #task 5
x=[37,2,1,-9]
# print(Length(x))


def Minimum(list):
    min=list[0]
    for x in range(len(list)):    #task 6
        if list[x]<min:
            min=list[x]
    return min
# print(Minimum([37,-20,1,-9]))

def Maximum(list):
    max=list[0]
    for x in range(len(list)):  #task 7
        if list[x]>max:
            max=list[x]
    return max
# print(Maximum([37,-20,1,-9]))

def ultimate_analysis(list):
    mydec = {
        'sum_total':Sum_Total(list),
        'average':Average(list),
        'minimum':Minimum(list),
        'maximum':Maximum(list),        #task 8
        'length':Length(list)
    }
    return mydec

# print(ultimate_analysis([37,2,1,-9]))

def Reverse_List(list):
    j=int(len(list))-1
    temp=0
    for x in range(int(len(list)/2)):       #task9
        temp=list[x]
        list[x]=list[j]
        list[j]=temp
        j-=1
    return list

# print(Reverse_List([37,2,1,-9]))

