import json

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

print(len(A_level_user))
print('\n')
print(len(B_level_user))
print('\n')
print(len(C_level_user))
print('\n')
print(len(D_level_user))
print('\n')
print(len(E_level_user))



#A级用户为微博数大于1000的人，为他们每人分配A_level5-10,B_level10-20,C_level 20-30,D_level 30-40,E_level 50-60个用户 总115-160
#B级用户为微博数在700-1000的人，为他们每人分配A_level 1-5 B_level 5-10,C_level 10-20,D_level 20-30,E_level 30-40个用户 总65-105
#C级用户为微博数在300-700的人，为他们每人分配A_level 1,B_level 1-5,C_level 15-25,D_level 20-30,E_level 25-35个用户 总60-95
#D级用户为微博数在50-300的人，为他们每人分配A_level 1,B_level 1-5,C_level 15-25,D_level 20-30,E_level 25-35个用户, 总60-95
#E级用户，不考虑分级，每人分配50个用户，其中包括一个A_level
#微博数量小于50的人会被过滤掉


