class test:
	def __init__(self):
       		self.Testname = ""
       		self.Released = False
	
	def create(self):
		pass
	def save(self):
		pass
	def release(self):
		pass
	def delete(self):
		pass
	def attempt(self):
		pass
	def submit(self):
		pass


class summativeTest(test):
	def __init__(self):
		self.testDeadline = 0 #not sure on data type

	def setTestDeadline(self, deadline):
		pass


class formativeTest(test):
	def __init__(self):
		self.maxAttempt = 0

	def setMaxAttempts(self, maxAttempts):
		pass


