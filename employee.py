class employee:
	def __init__(self,name,group,title):
		self.name = name
		self.group = group
		self.title = title

	def is_bonus_eligible(self):
		if self.title == "manager":
			return True
		else:
			return False
