class base:
	def fun1(self):
		print("this is base class")

class child(base):
	def fun2(self):
		print("hello from child")

obj = child()
obj.fun1()
obj.fun2()

class parent:
	def __init__(self,fname,age):
		self.fname=fname
		self.age=age

	def view(self):
		print(self.fname,self.age)

class child(parent):
	"""docstring for child
"""
	def __init__(self,fname,age):
		parent.__init__(self,fname,age)
		self.lname = 'wani'

	def view(self):
		print(self.fname,self.age,self.lname)


ob1 = child('Ayaz',23)
ob1.view()		
		
