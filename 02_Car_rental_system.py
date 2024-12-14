import math

class Car:
    def __init__(self, kind, speed):
        self.kind = kind
        self.speed = speed



class  SUV(Car):
    total = 10
    own_dict = {}
    
    def __init__(self, avail):
        super().__init__("SUV", "190kmph")
        self.avail = avail
    
    def setName(self, name, custId):
        self.own_dict[custId] = {"name": name}
        
    def setTranid(self, tid, custId):
        self.own_dict[custId].update({"Transaction ID": tid})
        
    def setCarid(self, cid, custId):
        self.own_dict[custId].update({"Car ID": cid})

    def updateAvail(self, num):
        self.avail = num


class Sedan(Car):
    total = 10
    own_dict = {}
    
    def __init__(self, avail):
        super().__init__("SUV", "190kmph")
        self.avail = avail

    def setName(self, name, custId):
        self.own_dict[custId] = {"name": name}
        
    def setTranid(self, tid, custId):
        self.own_dict[custId].update({"Transaction ID": tid})
        
    def setCarid(self, cid, custId):
        self.own_dict[custId].update({"Car ID": cid})

    def updateAvail(self,num):
        self.avail = num


class HatchBack(Car):
    total = 10
    own_dict = {}
    
    def __init__(self, avail):
        super().__init__("SUV", "190kmph")
        self.avail = avail
       
    def setName(self, name, custId):
        self.own_dict[custId] = {"name": name}
        
    def setTranid(self, tid, custId):
        self.own_dict[custId].update({"Transaction ID": tid})
        
    def setCarid(self, cid, custId):
        self.own_dict[custId].update({"Car ID": cid})

    def updateAvail(self, num):
        self.avail = num

nums = 10
suv = SUV(nums)
sedan = Sedan(nums)
hatchback = HatchBack(nums)
ch = 'y'

while True:

    print(
        '''Available Car Model: /n
            1. SUV
            2. Sedan
            3. Hatchback
        '''
        )

    if ch == 'y' or ch == "yes":

        sel = input("Select the model : ")
        cname = input("enter customer name : ")
        ccid = input("enter car id : ")
        ctid = input("enter Transaction id : ")
        ccustid = input("enter customer id : ")

        if sel == "suv":
            suv.setName(cname, ccustid)
            suv.setCarid(ccid, ccustid)
            suv.setTranid(ctid, ccustid)
            nums-=1
            suv.updateAvail(nums)

        elif sel == "sedan":
            sedan.setName(cname, ccustid)
            sedan.setCarid(ccid, ccustid)
            sedan.setTranid(ctid, ccustid)
            nums-=1
            sedan.updateAvail(nums)

        else:
            hatchback.setName(cname, ccustid)
            hatchback.setCarid(ccid, ccustid)
            hatchback.setTranid(ctid, ccustid)
            nums-=1
            hatchback.updateAvail(nums)


    print("Do you exit the system?")
    ch = input("Assign to new customer: ")
    print()
    print("***************************************************")
    print()
    if ch == 'q' or ch == 'n':
        break

print()
print("***************************************************")
print()
print("SUV information: ")
for i in suv.own_dict:
    print(i, ":",suv.own_dict[i])
print()
print("***************************************************")
print()
print("Sedan information: ")
for i in suv.own_dict:
    print(i, ":",sedan.own_dict[i])
print()
print("***************************************************")
print()
print("HatchBack information: ")
for i in suv.own_dict:
    print(i, ":",hatchback.own_dict[i])
print()
print("***************************************************")
print()