class Person:
    def __init__(self,name,age):
        self.name=name
        self.age =age
    def Print_Student(student):
        print("Name Is",student.name,student.age,"age")
    

class Family(Person):
    def __init__(self,fatherName,name,age):
        self.fatherName=fatherName
        Person.__init__(self,name, age)
        print("Name:{} ,Age={} , Father Name:{} ".format(self.name,self.age,self.fatherName))

f=Family("a","b",10)


class base(object): 
   def base_func2(self): 
      print('Method of base class')
class child(base): 
   def base_func1(self): 
      print('Method of child class')
      super(child, self).base_func2() 

class next_child(child): 
   def base_func(self): 
      print('Method of next_child class')
      super(next_child, self).base_func1() 
obj2 = child()
obj2.base_func1()
obj = next_child() 
obj.base_func()

class Team:
   def show_Team(self):
      print("This is our Team:")

# Testing class inherited from Team
class Testing(Team):
   TestingName = ""

   
 
# Dev class inherited from Team
class Dev(Team):
   DevName = ""

   
 
# Sprint class inherited from Testing and Dev classes
class Sprint(Testing, Dev):
   def show_parent(self):
      print("Testing :", self.TestingName)
      print("Dev :", self.DevName)

s1 = Sprint()  # Object of Sprint class
s1.TestingName = "James"
s1.DevName = "Barter"
s1.show_Team()
s1.show_parent()

try:
  print(5/0)
except:
  print("An exception occurred")


class PostDetail:
   title=None
   body =None
   def get(self):
      
      print(self.title)
   
   
   
   
   
class Post(PostDetail):
   title="khue post"
   body="khue"


   

post = Post()
post.get()

