# class car:
#     def __init__(self,model,color,year):
#         self.model=model
#         self.color=color
#         self.year=year
#     def display_info(self):
#         print(f" model: {self.model}, color: {self.color}, year: {self.year}")
# car1=car("BMW","BLACK",2020)
# car2=car("GTR","BLUE",2020)

# car1.display_info()




# class car:
#     def abc(self,model,color,year):
#         self.model=model
#         self.color=color
#         self.year=year
#     def display_info(self):
#         print(f" model: {self.model}, color: {self.color}, year: {self.year}")

# car1=car()
# car1.abc("BMW","BLACK","2020")
# # car1=car("BMW","BLACK",2020)
# # car2=car("GTR","BLUE",2020)

# car1.display_info()


# class employee:
#     def __init__(self,salary,job,age):
#         self.salary=salary
#         self.job=job
#         self.age=age
#     def display_info(self):
#         print(f"salary: {self.salary} job: {self.job} age: {self.age}")
# nijas=employee("100000","engineer","23")
# rinz=employee("1000000","engineer","24")

# rinz.display_info()    # print attributes
# print(rinz.age)


# rinz.job="IPS"            #change attribute
# rinz.display_info()

# print(rinz.job)


# comparisson method

# lously coupled

# class company:
#     def __init__(self,cname,location):
#         self.cname=cname
#         self.location=location

# class employee:
#         def __init__(self,name,age,comp:company):
#              self.name=name
#              self.age=age
#              self.comp=comp

#         def employee_info(self):
#              print(f"name: {self.name}")
#              print(f"age: {self.age}")
#              print(f"company name: {self.comp.cname}")
#              print(f"company location: {self.comp.location}")

# employee1=employee("rinz","30",company("vipro","london"))
# employee1.employee_info()


#tightly coupled

# class company:
#     def __init__(self,cname,location):
#         self.cname=cname
#         self.location=location

# class employee:
#         def __init__(self,name,age,cname,location):
#              self.name=name
#              self.age=age
#              self.comp=company(cname,location)

#         def employee_info(self):
#              print(f"name: {self.name}")
#              print(f"age: {self.age}")
#              print(f"company name: {self.comp.cname}")
#              print(f"company location: {self.comp.location}")

# employee1=employee("rinz","24","vipro","london")
# employee1.employee_info()

#INNER CLASS

# class company:
#     class employee:
#         def __init__(self,cname,location):
#             self.cname=cname
#             self.location=location

# class employee:
#         def __init__(self,name,age,cname,location):
#              self.name=name
#              self.age=age
#              self.comp=company.employee(cname,location)

#         def employee_info(self):
#              print(f"name: {self.name}")
#              print(f"age: {self.age}")
#              print(f"company name: {self.comp.cname}")
#              print(f"company location: {self.comp.location}")

# employee1=employee("rinz","24","vipro","london")
# employee1.employee_info()


#CLASS VARIABLE

# class employee:
#     company="ABC"   #class variable
#     @classmethod
#     def change_company_name(cls,new_name):
#          cls.company=new_name
#     def __init__(self,name,position):
#          self.name=name   #instance variable
#          self.position=position
# emp1=employee("nijas","developer")
# emp2=employee("rinz","developer")

# print(emp1.company)
# print(emp2.company)

# print(emp2.name)

# employee.change_company_name="xyz"
# print(employee.company)
        



#STATIC METHOD

# class mathoperation:
     
#     @staticmethod    #decorators

#     def add(a,b):
#          return a+b
# print(mathoperation.add(2,5))



#PRIVATE ATTRIBUTES

# class employee:
#     def __init__(self,name,salary):
#             self.name=name              #public attribute
#             self.__salary=salary        #private attribute
#     def display_employee(self):
#           print(f"name: {self.name} , salary:{self.__salary}")
#     def update_salary(self,new_salary):
#         self.__salary=new_salary
# emp=employee("nijas",100000)
# emp.display_employee()


# emp.update_salary(5000000000)
# emp.display_employee()

# emp.name="nisar"
# emp.display_employee()

# emp.salary=100000



#INHERITENCE

# 1.Single inheritence

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print(f"{self.name} is making noise")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} is barking")

# Dog1=Dog("anu")
# Dog1.speak()

#2.Multiple inheritence

# class engine:
#     def start_engine(self):
#         print("engine started")
# class wheel:
#     def rotate(self):
#         print("wheel is moving")
# class car(engine,wheel):
#     def name(self):
#         print("car name ")

# car=car()
# car.start_engine()
# car.rotate()
# car.name()

# 3.Heirarchial inheritence

# class Animal:
#     def speak(self):
#         print("animal speak")

# class Dog(Animal):
#     def speak(self):
#         print("dog barks")
# class cat(Animal):
#     def speak(self):
#         print("meoww")
# dog=Dog()
# Cat=cat()
# dog.speak()
# Cat.speak()


#Duck typing



# class Dog:
#     def speak(self):
#         print("dog barks")
# class Cat:
#     def speak(self):
#         print("meoww")

# def make_noise(animal):
#     try:
#         animal.speak()
#     except:
#         print("animal does not speak")

# dog=Dog()
# cat=Cat()
# make_noise(dog)
# make_noise(cat)


# class Animal:
#     def speak(self):
#         print("animal speak")

# class Dog(Animal):
#     def speak(self):
#         print("dog barks")
# class Cat(Animal):
#     def speak(self):
#         print("meoww")

# animals = [ Dog(), Cat()]
# for animal in animals:
#     animal.speak()



#ABSTRACTION

# from abc import ABC ,abstractmethod

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class rectangle(shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width*self.height
    
# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14 * self.radius**2
    
# ret=rectangle(10,20)
# print(ret.area())

# cir=circle(5)
# print(cir.area())
        



    



