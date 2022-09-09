class MyCar:
	def __init__(self,Company,Color,Max_speed):
		query = 1
		while query == 1:
			self.name = str(input("Enter Car company/brand"))
			self.color = str(input("Enter Car color"))
			self.ms = int(input("Enter Max speed of car"))
			print("Add another query? \n 1.Add another\n2.Exit")
			query = int(input())
	def disp(self):
		print(self.name,self.color,self.ms)

c1 = MyCar()
c1.disp()