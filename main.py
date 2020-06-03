from tkinter import *
import random
#the node class used to make it easy to access the coordinates and letter
#of each node. Also has methods that place the node on canvas and draw the name
#above the node.
class node():
   def __init__(self, x, y,letter):
       self.x=x
       self.y=y
       self.letter=letter
   def oncanvas(self):
       the_canvas.create_oval(self.x,self.y,self.x+10,self.y+10,fill="green")
   def draw_name(self):
       the_canvas.create_text(self.x+5,self.y-10,text=self.letter,fill="black")
#Goes through all nodes in a list and uses their oncanvas method to draw them
#on canvas. Also draws the name of each node.
def drawnodes(Node_list):
    for i in Node_list:
        i.oncanvas()
        i.draw_name()
#goes through the process of creating the randomly generated directed graph
#and matching adjacendy matrix.
def create_graph():
    the_canvas.delete("all")#clears canvas 
    Node1=node(200,30,"A")#creating all 5 nodes in graph
    Node2=node(300,80,"B")
    Node3=node(250,180,"C")
    Node4=node(150,180,"D")
    Node5=node(100,80,"E")
    Nodes=[Node1,Node2,Node3,Node4,Node5]
    Node_Connections=dict()
    #creates a dictionary where each key is a node and each value is a node
    #the key is directed to.
    #Example: Node_connections[A]=[B,C] means A->-B and A->-C
    for i in Nodes:
        Node_Connections[i]=[]
    #Will go through every key and every node in a previously created node list
    #and randomly determine what connections each node will have.
    for key in Node_Connections:
        for i in Nodes:
            chance=random.randint(1,3)
            #determines if i should be a connection (Node_Connections[key]=[i])
            #also makes sure a node doesnt connect to itself
            if(chance==2 and i.letter!=key.letter):
                Node_Connections[key].append(i)
    #goes through all nodes that have a connection and connects them with a red
    #line. A blue line will be added later to show the direction of connection.
    for key in Node_Connections:
        the_array=Node_Connections[key]
        for i in the_array:
            the_canvas.create_line(key.x+5,key.y+5,i.x+5,
                                   i.y+5,fill="red",width=2)
    #Finds the midpoint between connected nodes and draws a blue line to show
    #direction.
    for key in Node_Connections:
        the_array=Node_Connections[key]
        for i in the_array:
            distx=abs((key.x+5)-(i.x+5))*.5
            disty=abs((key.y+5)-(i.y+5))*.5
            xsign,ysign=1,1
            if(key.x+5>i.x+5):
                xsign=-1
            if(key.y+5>i.y+5):
                ysign=-1
            the_canvas.create_line(key.x+5,key.y+5,(key.x+5)+(xsign*distx),
                                   (key.y+5)+(ysign*disty),fill="blue",width=2)
    #This chunk of code goes through taking the graph and making an adjacency
    #matrix out of it.
    adjacency_matrix=dict()
    for i in Nodes:
        adjacency_matrix[i]=[0,0,0,0,0]
    for key in Node_Connections:
        for i in Node_Connections[key]:
            if(i.letter=="A"):
                adjacency_matrix[key][0]=1
            if(i.letter=="B"):
                adjacency_matrix[key][1]=1
            if(i.letter=="C"):
                adjacency_matrix[key][2]=1
            if(i.letter=="D"):
                adjacency_matrix[key][3]=1
            if(i.letter=="E"):
                adjacency_matrix[key][4]=1
    #draws nodes on canvas.
    drawnodes(Nodes)
    #Puts adjacency matrix on canvas
    LabelA.configure(text=adjacency_matrix[Nodes[0]])
    LabelB.configure(text=adjacency_matrix[Nodes[1]])
    LabelC.configure(text=adjacency_matrix[Nodes[2]])
    LabelD.configure(text=adjacency_matrix[Nodes[3]])
    LabelE.configure(text=adjacency_matrix[Nodes[4]])
#This final chunk of code formats the text and window.
window=Tk()
randButton=Button(window,text="New Graph",pady=7,bg="grey",font=("fixedsys",3),
                  command=create_graph)
randButton.place(x=400,y=130)
window.title("Graph with adjacency matrix")
window.geometry("500x200")
window.configure(bg="white")
LabelA=Label(text="",font=("fixedsys",5),bg="white")
LabelA.place(x=400,y=20)
LabelB=Label(text="",font=("fixedsys",5),bg="white")
LabelB.place(x=400,y=40)
LabelC=Label(text="",font=("fixedsys",5),bg="white")
LabelC.place(x=400,y=60)
LabelD=Label(text="",font=("fixedsys",5),bg="white")
LabelD.place(x=400,y=80)
LabelE=Label(text="",font=("fixedsys",5),bg="white")
LabelE.place(x=400,y=100)
the_canvas = Canvas(window,width=350,height=200, highlightthickness=0)
the_canvas.configure(bg="white")
the_canvas.pack(side=LEFT)
#runs program
create_graph()
window.mainloop()
