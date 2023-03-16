def poem(str):
    list_1=[]
    for word in str:
        sum=0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum+=1
            list_1.append(sum)
        return len(list_1) == list_1.count(list_1[0])


str_1=[x for x in input().split()]
if poem(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')
print(str_1)