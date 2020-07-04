#Insertion of Node at beginning of the linked list

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


        def insertAtbegin(self,new):
                NewNode=Node(new)
                NewNode.nextval=self.headval
                self.headval=NewNode
                        


S=LinkedList()
S.headval=Node(1)
q=Node(2)
r=Node(3)
S.headval.nextval=q
q.nextval=r
t=Node(4)
r.nextval=t
print("before insertion")
S.traverse()
S.insertAtbegin(0)
print("After insertion at begin")
S.traverse()
