#Deletion of node of the linked list

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


        def deleteNode(self,data):
                currentnode=self.headval
                while(currentnode.dataval!=data):
                        #print(currentnode.dataval)
                        p=currentnode
                        currentnode=currentnode.nextval
                #print(currentnode.dataval)
                #print(p.dataval)
                p.nextval=currentnode.nextval
                
                        


S=LinkedList()
S.headval=Node(1)
q=Node(2)
r=Node(3)
S.headval.nextval=q
q.nextval=r
t=Node(4)
r.nextval=t
print("before Deletion")
S.traverse()
S.deleteNode(2)
print("After deletion ")
S.traverse()
