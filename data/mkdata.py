import json
import random

with open('final.json', 'r') as f:
    result_dict = json.load(f)
#result_dict = dict(result_dict)
#print(result_dict)
print(len(result_dict))
A_level_user = []
B_level_user = []
C_level_user = []
D_level_user = []
E_level_user = []
#过滤掉微博数小于50的人
for i in result_dict:

    if i[1] <= 100:
        E_level_user.append(i)
    elif i[1]>100 and i[1]<=500:
        D_level_user.append(i)
    elif i[1]>500 and i[1]<=1200:
        C_level_user.append(i)
    elif i[1]>1200 and i[1]<=2100:
        B_level_user.append(i)
    elif i[1]>2100:
        A_level_user.append(i)

#A级用户为微博数大于1000的人，为他们每人分配A_level5-10,B_level10-20,C_level 20-30,D_level 30-40,E_level 40-50个用户 总105-150

#微博数量小于50的人会被过滤掉

sum_count = 0
count=0
for i in A_level_user:
    count += 1
    sum_count+=1
    i.append(count)
    i.append(sum_count)
count = 0
for i in B_level_user:
    sum_count+=1
    count+=1
    i.append(count)
    i.append(sum_count)
count = 0
for i in C_level_user:
    count+=1
    sum_count+=1
    i.append(count)
    i.append(sum_count)
count = 0
for i in D_level_user:
    count+=1
    sum_count+=1
    i.append(count)
    i.append(sum_count)
count = 0
for i in E_level_user:
    count+=1
    sum_count+=1
    i.append(count)
    i.append(sum_count)

result = []
temp=[]
#开始造假
for i in A_level_user:
    print(len(A_level_user))
    A__level_user = A_level_user.remove(i)
    print(len(A_level_user))
    no_A = random.randint(5,10)
    temp_A = random.sample(A_level_user,no_A)
    #print(no)
    #print(temp)
    no_B = random.randint(10,20)
    temp_B =random.sample(B_level_user,no_B)
    no_C = random.randint(20,30)
    temp_C = random.sample(C_level_user,no_C)
    no_D = random.randint(30,40)
    temp_D = random.sample(D_level_user,no_D)
    no_E = random.randint(40,50)
    temp_E = random.sample(E_level_user,no_E)
    #print(temp_A)
    for m in temp_A:
        temp.append(i[0][0])
        temp.append(temp_A[0][0][0])
        result.append(temp)
        temp = []
    print(temp_A)
    print(result)
    for m in temp_B:
        temp.append(i[0][0])
        temp.append(temp_B[0][0][0])
        result.append(temp)
        temp = []
    print(result)
    for m in temp_C:
        temp.append(i[0][0])
        temp.append(temp_C[0][0][0])
        result.append(temp)
        temp = []
    print(result)
    for m in temp_D:
        temp.append(i[0][0])
        temp.append(temp_D[0][0][0])
        result.append(temp)
        temp = []
    print(result)
    for m in temp_E:
        temp.append(i[0][0])
        temp.append(temp_E[0][0][0])
        result.append(temp)
        temp = []
    print('A:')
    print(len(result))
    print('\n')

#开始造假

#B级用户为微博数在700-1000的人，为他们每人分配A_level 1-5 B_level 5-10,C_level 10-20,D_level 20-30,E_level 30-40个用户 总65-105
for i in B_level_user:
    no_A = random.randint(1,5)
    temp_A = random.sample(A_level_user,no_A)
    #print(no)
    #print(temp)
    no_B = random.randint(5,10)
    temp_B =random.sample(B_level_user,no_B)
    no_C = random.randint(10,20)
    temp_C = random.sample(C_level_user,no_C)
    no_D = random.randint(20,30)
    temp_D = random.sample(D_level_user,no_D)
    no_E = random.randint(30,40)
    temp_E = random.sample(E_level_user,no_E)
    print(temp_A)
    for m in temp_A:
        temp.append(i[0][0])
        temp.append(temp_A[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_B:
        temp.append(i[0][0])
        temp.append(temp_B[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_C:
        temp.append(i[0][0])
        temp.append(temp_C[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_D:
        temp.append(i[0][0])
        temp.append(temp_D[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_E:
        temp.append(i[0][0])
        temp.append(temp_E[0][0][0])
        result.append(temp)
        temp = []
    print("B:")
    print(len(result))
    print('\n')

#C级用户为微博数在300-700的人，为他们每人分配A_level 1,B_level 1-5,C_level 15-25,D_level 20-30,E_level 25-35个用户 总60-95

for i in C_level_user:
    #no_A = random.randint(5,10)
    temp_A = random.sample(A_level_user,1)
    #print(no)
    #print(temp)
    no_B = random.randint(1,5)
    temp_B =random.sample(B_level_user,no_B)
    no_C = random.randint(15,25)
    temp_C = random.sample(C_level_user,no_C)
    no_D = random.randint(20,30)
    temp_D = random.sample(D_level_user,no_D)
    no_E = random.randint(25,35)
    temp_E = random.sample(E_level_user,no_E)
    #print(temp_A)
    for m in temp_A:
        temp.append(i[0][0])
        temp.append(temp_A[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_B:
        temp.append(i[0][0])
        temp.append(temp_B[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_C:
        temp.append(i[0][0])
        temp.append(temp_C[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_D:
        temp.append(i[0][0])
        temp.append(temp_D[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_E:
        temp.append(i[0][0])
        temp.append(temp_E[0][0][0])
        result.append(temp)
        temp = []
    print('C:')
    print(len(result))
    print('\n')

#D级用户为微博数在50-300的人，为他们每人分配A_level 1,B_level 1-5,C_level 15-25,D_level 20-30,E_level 25-35个用户, 总60-95

for i in D_level_user:
    #no_A = random.randint(5,10)
    temp_A = random.sample(A_level_user,1)
    #print(no)
    #print(temp)
    no_B = random.randint(1,5)
    temp_B =random.sample(B_level_user,no_B)
    no_C = random.randint(15,25)
    temp_C = random.sample(C_level_user,no_C)
    no_D = random.randint(20,30)
    temp_D = random.sample(D_level_user,no_D)
    no_E = random.randint(25,35)
    temp_E = random.sample(E_level_user,no_E)
    #print(temp_A)
    for m in temp_A:
        temp.append(i[0][0])
        temp.append(temp_A[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_B:
        temp.append(i[0][0])
        temp.append(temp_B[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_C:
        temp.append(i[0][0])
        temp.append(temp_C[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_D:
        temp.append(i[0][0])
        temp.append(temp_D[0][0][0])
        result.append(temp)
        temp = []

    for m in temp_E:
        temp.append(i[0][0])
        temp.append(temp_E[0][0][0])
        result.append(temp)
        temp = []
    print('D:')
    print(len(result))
    print('\n')


#E级用户，不考虑分级，每人分配50-100个用户，其中包括1-5个A_level
for i in E_level_user:
    #no_A = random.randint(1,5)
    #temp_A = random.sample(A_level_user,no_A)
    no = random.randint(50,100)
    temp_E = random.sample(result_dict,no)
    #for m in temp_A:
     #   temp.append(i[0][0])
      #  temp.append(temp_A[0][0][0])
       # result.append(temp)
        #temp = []
    for m in temp_E:
        temp.append(i[0][0])
        temp.append(temp_E[0][0][0])
        result.append(temp)
        temp = []
    print('E:')
    print(len(temp_A))
    print(len(temp_E))
    print(len(result))
    print('\n')
result = set(result)
fileoj = open('fakedata.json','w', encoding='utf8')
for i in result:
    i=json.dumps(i)
    fileoj.write(i)
    fileoj.write('\n')
fileoj.close()


