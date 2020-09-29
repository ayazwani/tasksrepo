class parent1():
	"""docstring for parent1"""
	def fun1(self):
		print("this is parent 1")

class parent2(object):
		"""docstring for parent2"""
		def fun2(self):
			print("this is parent 2")

class child(parent1,parent2):
	def fun3(self):
		print("this is child class")

ob = child()
ob.fun1()
ob.fun2()
ob.fun3()
				