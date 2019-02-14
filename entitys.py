class student:
	def __init__(self):
		self.studentID = 0
		self.name = ""
		self.dateOfBirth = 0
		self.testScore = 0 
		self.attemptRemaining = 0

	def getTestFeedback(self):
		pass
	def getTestScore(self):
		pass
	def setMaxAttempt(self):
		pass
	def attemptRemainingCounter(self):
		pass

class lecturer:
	def __init__(self):
		self.lecturerID = 0
		self.name = ""
		self.studentList = []

	def getStudentResults(self):
		pass
