import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

##bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
##
##
##df = pd.DataFrame(bridge_height)
##df['STD'] = pd.rolling_std(df['meters'], 2)
##
##df_std = df.describe()['meters']['std']
##print(df_std)
##
##df = df[ (df['STD']  < df_std)]
##
##
##df['meters'].plot()
##
##plt.show()


def mod(num1,num2):
    yes = []
    for i in range(num1, num2):
        if i % 5 == 0:
            #print(str(i) + ' yes 5')
            yes.append(i)
        elif i % 3 == 0:
            #print(str(i) +  ' yes 3')
            yes.append(i)
        else:
            pass
    print(yes)
        
mod(360, 500)



A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

print('A0 ', A0)
print('A1 ', A1)
print('A2 ', A2)
print('A3 ', A3)
print('A4 ', A4)
print('A5 ', A5)
print('A6',  A6)




##input_list = [5,3,5,6,7,20,30,35,37,45,100,45,50]

##def div_by_five(num):
##    if num % 5 == 0:
##        return True
##    else:
##        return False

##************generator (doesn't load into memory)***************8
##xyz = (i for i in input_list if div_by_five(i))

##for i in xyz:
##    print(i)

##[print(i) for i in xyz]
##
##************list-loads into memory**********
#xyz = [i for i in input_list if div_by_five(i)]

#print(xyz)



##[[print(i,ii) for ii in range(5) for i in range(5)]]



#************Enumerate example***********************

example = ['left', 'right', 'up', 'down']

#gives index
for i,j in enumerate(example):
    print(i, j)


#make dictionary
new_dict = dict(enumerate(example))

print(new_dict)



#**********     LISTS   **********************

names= ['Jeff', 'Gary', 'Diamond', 'Sam']
#names.reverse()

#print(names)

#reverse list
print(names[::-1])

rev_names = list(reversed(names))
print(rev_names)

print('THIS' + str(names[0:3:2]))


##for i in names:
##    print('Hello, ' + i)
##    print(' '.join(['Hello there, ' + i]))
##
##
##[print('Hello there, ' + i) for i in names]
##

#who = 'Dre'
#howMany = 12
#print('{} bought {} apples today!'.format(who, howMany))


###**************     ZIP     ***************************
x = [1,3,5,7]
y = [2,6,3,7]
z = ['a','d','z','f']

for a,b in zip(x,z):
    print(a,b)

############ dictionary zip #################
test = dict(zip(('Paul', 'Anne', 'Joe'),('A','G','F')))

print(test)


##    
##[print((x, y)) for x in [1,2,3] for y in [3,1,4] if x != y]
##
##
##
##questions = ['name', 'quest', 'favorite color']
##answers = ['lancelot', 'the holy grail', 'blue']
##for q, a in zip(questions, answers):
##    print('What is your {}?  It is {}.'.format(q, a))
##
##
##
##
##
##
##
##
sup = 'hey there guy I wonder what this interview is going to consist of.'


if 'asdf' in sup:
    print('in stringg')
else:
    print('not in string')




