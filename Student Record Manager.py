
   
#Student Record Manager / Student Information Handler 
class student:    
    def __init__(self,name,num,marks):
        self.std_name = name
        self.std_rollnumber =int(num)
        self.std_marks =list(marks)

    def av_1(self):
        avg=sum(self.std_marks) /len(self.std_marks)
        return avg

    
std_1=student('venkat',1234,[20,30,40,50])
print(std_1.std_name)
print(std_1.std_rollnumber)
print(std_1.std_marks)
print(std_1.av_1())
