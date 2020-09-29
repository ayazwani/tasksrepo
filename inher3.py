class parent1():
	"""docstring for parent1
example of hiearchal inheritance

	"""
	def view(self):
		print("this is parent 1")

class parent2(parent1):
	def view2(self):
		print("this is parent 2")

class child(parent1):
	def view3(self): 
		print("this is child")

ob = child()
ob2 = parent2() 
ob.view()
ob2.view()