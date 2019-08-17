class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age 
        
    def study(self,course):
        print(self.name,"study",course)


class StudentPrivate(object):
    #用__表示私有函数和私有属性
    def __init__(self,name):
        self.__name=name
    def __say(self):
        print("hello")


def main():
    stu1=Student("stu1",0)
    stu1.study("python")
    stu2=StudentPrivate("xiaoming")
    # stu2.__say
    # print(stu2.__name)
    
    #_Class可以访问私有成员
    stu2._StudentPrivate__say()


if __name__ == '__main__':
    main()
    
