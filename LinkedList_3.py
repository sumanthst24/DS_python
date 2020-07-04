#Insertion of Node at end of the linked list

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


        def insertAtEnd(self,new):
                NewNode=Node(new)
                currentnode=S.headval
                while(currentnode.nextval!=None):
                        currentnode=currentnode.nextval
                currentnode.nextval=NewNode
                        


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
S.insertAtEnd(5)
print("After insertion at end")
S.traverse()
