### Actuall ###
class Student():
    class_ = "student"
    def __init__(self,name,age,test_1,test_2,test_3):
        self.name = name
        self.age = age 
        self.test_1 = test_1
        self.test_2 = test_2
        self.test_3 = test_3

    def calcaverage(self):
        return int((self.test_1 + self.test_2 + self.test_3)/3)

John = Student("John","24", 78, 65, 82)

print(John.calcaverage())





#class Student():
#    def __init__(self,name,age,test_1,test_2,test_3):
#        self.name = name
#        self.age = age 
#        self.test_1 = test_1
#        self.test_2 = test_2
#        self.test_3 = test_3

#class john(Student):
#    def __init__(self,test_1,test_2,test_3):
#        Student.__init__(self)
#        self.test_1 = test_1
#        self.test_2 = test_2
#        self.test_3 = test_3

#john = Student("John", '24', '33', '45', '42')
#jane = Student("jane", '25', '43', '44', '40')
#jack = Student("Jack", "27", '40', '37', '35')

#john_test1 = int(getattr(john, "test_1"))
#john_test2 = int(getattr(john, 'test_2'))
#john_test3 = int(getattr(john, 'test_3'))

#john_total_score = john_test1 + john_test2 + john_test3
#john_avg_total_score = (john_total_score)/3
#print(int(john_avg_total_score))

#test_1 = int(input("Enter test-1 score: " ))
#test_2 = int(input("Enter test-2 score: " ))
#test_3 = int(input("Enter test-3 score: " ))

#print(setattr(john, "age", '35'))
#print(getattr(john, 'age'))
#print(hasattr(john, "address"))














