class Node:

    def __init__(self,data):

        self.data=data
        self.left=None
        self.right=None

#Inserting into tree
    def Insert_data(self,data):

        if(self.data!=None):
            if(data<self.data):
                if(self.left==None):
                    self.left=Node(data)
                else:
                    self.left.Insert_data(data)

            elif(data>self.data):
                if(self.right==None):
                    self.right=Node(data)
                else:
                    self.right.Insert_data(data)


        else:
            self.data=data
#Inorder Traversal 
    def Inorder(self,ele):

        inorder=[]

        if(ele!=None):
            
            inorder=inorder+self.Inorder(ele.left)
            inorder.append(ele.data)
            inorder=inorder+self.Inorder(ele.right)
        return inorder

            
            

#Print the tree        
    def Print(self):
        if self.left:
            self.left.Print()
        print(self.data)
        if self.right:
            self.right.Print()


p=Node(5)
p.Insert_data(6)
p.Insert_data(1)
p.Insert_data(10)
p.Print()
print("Inorder Traversal")
res=p.Inorder(p)
for i in res:
    print(i,end=" ")
