##class CompanyMember:  
##    '''Represents Company  Member.'''  
##    def __init__(self, name, designation, age):  
##        self.name = name  
##        self.designation = designation  
##        self.age = age  
##    def tell(self):  
##        '''Details of an employee.'''  
##        print('Name: ', self.name,'\nDesignation : ',self.designation, '\nAge : ',self.age)  
##  
##class FactoryStaff(CompanyMember):  
##    '''Represents a Factory Staff.'''  
##    def __init__(self, name, designation, age, overtime_allow):  
##        CompanyMember.__init__(self, name, designation, age)  
##        self.overtime_allow = overtime_allow  
##        CompanyMember.tell(self)  
##        print('Overtime Allowance : ',self.overtime_allow)  
##  
##class OfficeStaff(CompanyMember):  
##    '''Represents a Office Staff.'''  
##    def __init__(self, name, designation, age, travelling_allow):  
##        CompanyMember.__init__(self, name, designation, age)  
##        self.marks = travelling_allow  
##        CompanyMember.tell(self)  
##        print('Traveling Allowance : ',self.travelling_allow)  
##
##mike = OfficeStaff('Mike', 'Texas', '34', '3242')
##
##print(mike)
a = ['a','b','c','d','e','f','a']

for i in range(len(a)):
    if i == 6:
        print(a[i])
