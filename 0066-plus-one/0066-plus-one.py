class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=""
        for i in digits:
            res+=str(i)
        x=int(res)+1
        y=str(x)
        arr=[]
        for i in y:
            arr+=[int(i)]
        return arr