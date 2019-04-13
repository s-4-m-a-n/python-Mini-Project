

class Marks():
	def get_marks(self):
		self.Maths=int(input("enter the marks of math :"))
		self.Science=int(input("enter the marks of science :"))
		self.English=int(input("enter the marks of english :"))
		self.Nepali=int(input("enter the marks of Nepali:"))
		self.Computer=int(input("enter the marks of Computer :"))



class student():
	def __init__(self):
		self.name="unknown"
		self.marks=Marks()

	def read_info(self):
		self.name=input("enter the name")
		self.rollno=int(input("enter the roll no "))
		self.clas=int(input("enter the class"))
		self.get()
	def get(self):
		self.marks.get_marks()
		self.get_result()
	def get_result(self):
		self.result=Result()
		self.result.show(self,self.marks)
	 

class Result():
	def show(self,obj,marks):
		self.total=marks.Maths+marks.Science+marks.English+marks.Nepali+marks.Computer
		self.percentage=(self.total/50)*100


def Marksheet(obj):
	print("_______________________________________________________________________________________________________________")
	print("|       Name       | roll no | class | Nepali | English| Science    | Maths | Computer| Total     | percentage |")
	print("|------------------|---------|-------|--------|--------|------------|-------|---------|-----------|------------|")
	for i in obj:
		print(f"|%13.10s     | %7.7d |%5.5d  | %6.6d | %6.6d | %8.8d   | %5.5d | %7.7d| %6.6f   | %6.6f | "%(i.name,i.rollno,i.clas,i.marks.Nepali,i.marks.English,i.marks.Science,i.marks.Maths,i.marks.Computer,i.result.total,i.result.percentage))



def main():
	no_of_std=int(input("enter the no of students"))
	std=[]
	for i in range(0,no_of_std):
		s1=student()
		std.append(s1)
		s1.read_info()

	Marksheet(std)													

							  


if __name__=="__main__":
	main()
	





