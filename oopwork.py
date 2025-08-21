# class student:     # (16/08/25)
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display_grade(self):
#         if self.marks >=90 :
#             print(f"{self.name} :Grade A")
#         elif self.marks >=75 and self.marks <90 :
#             print(f"{self.name} :Grade B")
#         elif self.marks >=50 and self.marks <75 :
#             print(f"{self.name} :Grade C")
#         else :
#             print("Fail")
# s1=student("rinz",49)
# s2=student("nijas",99)
# s1.display_grade()
# s2.display_grade()        



#2
# class Bankaccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance
#     def deposite(self,amount):
#         self.amount=amount
#         print(f"Deposited :{self.amount}")
#         if self.amount >0:
#             self.__balance +=self.amount
#     def withdraw(self,money):
#         self.money=money
#         print(f"Withdraw : {self.money}")
#         if self.__balance>0 and self.money < self.__balance:
#             self.__balance -=self.money
#         else:
#             print(f"Insufficient balance")
#     def get_balance(self):
#         print(f"Final balance:{self.__balance}")
# B1=Bankaccount("Alice",1000)
# B1.deposite(500)
# B1.withdraw(1700)
# B1.get_balance()




#3 
# class bird:
#     def sound(self):
#         print("Birds makes sound ")
# class parrot(bird):
#     def sound(self):
#         print("parrot says Heloo")
# class sparrow(bird):
#     def sound(self):
#         print("sparrow chirps")
# def make_sound(bird):
#     try:
#         bird.sound()
#     except AttributeError:
#         print("not make sound")
# parrot=parrot()
# sparrow=sparrow()
# make_sound(parrot)
# make_sound(sparrow)



#4
# class Book:
#     def __init__(self,title,author,copies):
#         self.title=title
#         self.author=author
#         self.copies=copies
#     def display_info(self)
#         print(f"{self.title},{self.author},{self.copies}")

# Books=[]

# for book in Book
#     Title=input("Enter book title: ")
#     Author=input("Enter author: ")
#     Copies=input("Enter copies: ")
#     print("...more books")
#     book.append(Title)
#     book.append(Author)
#     book.append(Copies)

# lst=[]


# rinzna
        
