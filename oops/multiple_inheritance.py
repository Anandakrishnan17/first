class Calculate1:
    def add(self,a,b):
        return a+b
class Calculate2:
    def sub(self,a,b):
        return a-b
class Calculate3:
    def mul(self,a,b):
        return a*b  
class Calculate4(Calculate1,Calculate2,Calculate3):
    def div(self,a,b):
        return a/b          

obj=Calculate4() 
print(obj.add(4,5)) 
print(obj.sub(10,5)) 
print(obj.mul(4,5)) 
print(obj.div(30,5))   