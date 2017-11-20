from termcolor import colored

#Examples

#Fucntions 
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

print('A0 ', A0) ##A0  {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print('A1 ', A1) ##A1  range(0, 10)
print('A2 ', A2) ##A2  []
print('A3 ', A3) ##A3  [1, 2, 3, 4, 5]
print('A4 ', A4) ##A4  [1, 2, 3, 4, 5]
print('A5 ', A5) ##A5  {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print('A6',  A6) ##A6 [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]


################################CLASSES###########################
class Patient():
    def __init__(self, name='John Doe', age = 0, sickness = "none"):
        self.name = name
        self.age = age
        self.sickness = sickness

    def display(self):
        print('Name', self.name)
        print("Age", self.age)
        print("Sickness", self.sickness)

    def set_sickness(self, sickness = 'none'):
        self.sickness = sickness
    
joe = Patient('Joe Williams', 31, 'broken arm')

joe.display()
              


class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

Jason = Enemy(5)
Joe = Enemy(19)

Jason.get_energy()
        
        
class calculator:
    
    def addition(x,y):
        added = x + y
        print(added)
        
    def subtraction(x,y):
        sub = x - y
        print(sub)

    def multiplication(x,y):
        mult = x * y
        print(mult)

    def division(x,y):
        div = x / y
        print(div)


calculator.addition(345,1)


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

print('THIS' + str(names[0:3:2])) #prints out Jeff and Diamond

print("THIIIIIIIS" + str(names[1:2])) #only prints out Gary


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

sup = 'hey there guy I wonder what this interview is going to consist of.'


if 'asdf' in sup:
    print('in stringg')
else:
    print('not in string')



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



