class C2dVec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
a = C2dVec(1,3)
b = C3dVec(1,5,7)
print(a)
print(b)