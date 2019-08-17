class Person(object):
    def __init__(self,name,age ):
        self._name=name
        self._age=age 
    @property
    def name (self):
        return self._name
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age=age 
    def study(self):
        if(self._age<16):print(self._name+"playing py")
        else: print(self._name+"playing c++")
def main():
    person=Person("Saturn",15)
    person.study()
    person.age=20
    person.study()
    print(person.age)
if __name__ == '__main__':
    main()
    