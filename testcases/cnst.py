class Human:
    def __init__(self,color,hgt):
        self.color1=color
        self.hgt1=hgt
        print(color,hgt)
    def attend(self,a):
        print(a+" "+"is attended" + self.color1 + str(self.hgt1))
    def pasd(self,p):
        print(p + " " + "passed" + self.color1)
srikanth=Human("red",5.5)
srikanth.attend("srikanth")
rajesh=Human("dsfsdf",12)
rajesh.attend("rj")

