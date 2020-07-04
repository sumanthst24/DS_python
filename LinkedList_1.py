class Node:
        def __init__(self,dataVal=None):
                self.dataval=dataVal
                self.nextval=None

        
class LinkedList:
        def __init__(self):
                self.headval=None

        def traverse(self):
                printval=S.headval
                while(printval!=None):
                        print(printval.dataval)
                        printval=printval.nextval
                        


S=LinkedList()
S.headval=Node(1)
q=Node(2)
r=Node(3)
S.headval.nextval=q
q.nextval=r
S.traverse()
