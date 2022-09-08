class student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def calcAvg(self):
        avg=(self.mark1+self.mark2+self.mark3)/3
        return avg
    def introduce(self):
        print("Average marks of {} is {}".format(self.name,self.calcAvg()))


x=0
while x == 0:
    y=input("Type exit to exit or press any key to continue")
    if y.lower()=="exit":
        print("You have successfully exited")
        break
    else:
        name=input("Enter name")
        mark1=int(input("Enter mark 1"))
        mark2=int(input("Enter mark 2"))
        mark3=int(input("Enter mark 3"))
        obj=student(name,mark1,mark2,mark3)
        obj.introduce()
        
    

        
