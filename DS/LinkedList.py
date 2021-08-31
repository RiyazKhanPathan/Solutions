class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

 

class Sll:
    def __init__(self):
        self.nodeObject = None
        self.length = 0

    def insertAt(self,index,data):
        temp = self.nodeObject
        if temp is None:
            print("Empty List")
            return
        count=0
        while temp:
            if index==count:
                NewNode = Node(data)
                temp.data, NewNode.next = NewNode.data, temp.next
                break
            count+=1
            temp = temp.next
        else:
            print("list out of index");
            return 
    def append(self,data):
        temp = self.nodeObject
        self.length +=1
        if temp is None:
            NewNode = Node(data)
            self.nodeObject = NewNode
            return
        while temp.next:
            temp = temp.next
        NewNode = Node(data)
        temp.next = NewNode
        
    def delete(self,data):
        temp = self.nodeObject
        while temp.data is not data:
            temp = temp.next
        temp.data = temp.next.data
        temp.next = temp.next.next
        self.length-=1
        
    def __iter__(self):
        curNode = self.nodeObject
        while curNode:
            yield curNode.data
            curNode = curNode.next
    def display(self):
        for i in self:
            print(i)
        # temp = self.nodeObject
        # if temp is None:
        #     print("Empty")
        # else:
        #     while temp:
        #         print(temp.data)
        #         temp = temp.next
    
l = Sll()   
l.append(0)
l.append(1)
l.append(2)
l.append(3)
l.insertAt(1,4)
l.delete(4)

print("Length:",l.length)

 

l.display()
