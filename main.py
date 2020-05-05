from tkinter import *
import random
class node():
   def __init__(self, x, y,letter):
       self.x=x
       self.y=y
       self.letter=letter
   def oncanvas(self):
       the_canvas.create_oval(self.x,self.y,self.x+10,self.y+10,fill="green")
   def draw_name(self):
       the_canvas.create_text(self.x+5,self.y-10,text=self.letter,fill="black")

def drawnodes(Node_list):
    for i in Node_list:
        i.oncanvas()
def create_graph():
    the_canvas.delete("all")
    Node1=node(200,30,"A")
    Node2=node(300,80,"B")
    Node3=node(250,180,"C")
    Node4=node(150,180,"D")
    Node5=node(100,80,"E")
    Nodes=[Node1,Node2,Node3,Node4,Node5]
    Node_Connections=dict()
    for i in Nodes:
        Node_Connections[i]=[]
    for key in Node_Connections:
        for i in Nodes:
            chance=random.randint(1,3)
            if(chance==2 and i.letter!=key.letter):
                Node_Connections[key].append(i)
    for key in Node_Connections:
        the_array=Node_Connections[key]
        for i in the_array:
            the_canvas.create_line(key.x+5,key.y+5,i.x+5,i.y+5,fill="red",width=2)
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
            the_canvas.create_line(key.x+5,key.y+5,(key.x+5)+(xsign*distx),(key.y+5)+(ysign*disty),fill="blue",width=2)
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
    drawnodes(Nodes)
    for key in Nodes:
        key.draw_name()
    LabelA.configure(text=adjacency_matrix[Nodes[0]])
    LabelB.configure(text=adjacency_matrix[Nodes[1]])
    LabelC.configure(text=adjacency_matrix[Nodes[2]])
    LabelD.configure(text=adjacency_matrix[Nodes[3]])
    LabelE.configure(text=adjacency_matrix[Nodes[4]])
window=Tk()
randButton=Button(window,text="New Graph",pady=7,bg="grey",font=("fixedsys",3),command=create_graph)
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
create_graph()
window.mainloop()
