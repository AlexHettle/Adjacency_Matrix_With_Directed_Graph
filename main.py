from tkinter import *
import random

#Toggle used by the program to tell if the user wants random node locations or not
location_toggle = False


#the node class used to make it easy to access the coordinates and letter
#of each node. Also has methods that place the node on canvas and draw the name
#inside the node.

class node():
   def __init__(self, x, y,letter):
       self.x=x
       self.y=y
       self.letter=letter
   def oncanvas(self):
       the_canvas.create_oval(self.x-10,self.y-10,self.x+20,self.y+20,fill="green")
   def draw_name(self):
       the_canvas.create_text(self.x+5,self.y+5,text=self.letter,fill="black", font = "bold")



#Used to change label about node location
def node_toggle():
    global location_toggle
    if (location_toggle):
        location_toggle=False
        Toggle_Label.configure(text="Random Location: OFF")
    else:        
        location_toggle=True
        Toggle_Label.configure(text="Random Location: ON")
        
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
    #If and else used depending on if user wants a random node location
    if(location_toggle):
        Node1=node(random.randint(15, 320),random.randint(15, 165),"A")#creating all 5 nodes in graph
        Node2=node(random.randint(15, 320),random.randint(15, 165),"B")
        Node3=node(random.randint(15, 320),random.randint(15, 165),"C")
        Node4=node(random.randint(15, 320),random.randint(15, 165),"D")
        Node5=node(random.randint(15, 320),random.randint(15, 165),"E")
    else:
        Node1=node(170,15,"A")#creating all 5 nodes in graph
        Node2=node(270,75,"B")
        Node3=node(220,165,"C")
        Node4=node(120,165,"D")
        Node5=node(70,75,"E")
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
                                   i.y+5,fill="red",width=1)
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
                                   (key.y+5)+(ysign*disty),fill="blue",width=3)
            
            
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
    
    
    
    
#This final chunk of code formats the text, window, and GUI.
window=Tk()
Backround_Canvas = Canvas(window,width=601,height=401, highlightthickness=0)
Backround_Canvas.configure(bg="#c0cff3")
Backround_Canvas.place(x=0,y=0)
line1 = Backround_Canvas.create_line(0, 48,600, 48,fill="#C0E8F3",width=10)
oval = Backround_Canvas.create_oval(408, 29.5, 438, 65, fill="#CBC0F3",width=0)
rec1 = Backround_Canvas.create_rectangle(0, 0, 600, 30, fill='#CBC0F3',width=0)
rec2 = Backround_Canvas.create_rectangle(0, 66, 600, 96, fill='#CBC0F3',width=0)
Backofgraph = Backround_Canvas.create_rectangle(0, 91, 360, 410, fill='#C0E8F3',width=0)
randButton=Button(window,text="New Graph",padx = 18, pady=9,bg="#CBC0F3", fg = "white", font=("fixedsys",3), command=create_graph)
randButton.place(x=49,y=355)
window.title("Graph with adjacency matrix")
window.resizable(False,False)
TitleLabel = Label(text="Adjacency Matrix Generator",font=("fixedsys",20),bg="#CBC0F3", fg = "white")
TitleLabel.place(x=0,y=30)
window.geometry("600x400")
window.configure(bg="#c0cff3")
the_canvas = Canvas(window,width=348,height=191, highlightthickness=0)
the_canvas.configure(bg="white")
the_canvas.place(x=0,y=100)
rec6 = Backround_Canvas.create_rectangle(0, 300, 600, 400, fill='#CBC0F3',width=0)
rec7 = Backround_Canvas.create_rectangle(348, 300, 600, 400, fill='#C0E8F3',width=0)
Toggle_Button=Button(window,text="TOGGLE",padx = 30, pady=9,bg="#CBC0F3", fg = "white", font=("fixedsys",3),command=node_toggle)
Toggle_Button.place(x=180,y=355)
Toggle_Label=Label(text="Random Location: OFF",font=("fixedsys",20),bg="#CBC0F3", fg = "white")
Toggle_Label.place(x=15,y=310)
Backofgraph2 = Backround_Canvas.create_rectangle(0, 91, 600, 101, fill='#C0E8F3',width=0)
Backofgraph3 = Backround_Canvas.create_rectangle(0, 291, 600, 301, fill='#C0E8F3',width=0)
line2 = Backround_Canvas.create_line(0, 78,600, 78,fill="white",width=10)
line3 = Backround_Canvas.create_line(0, 18,600, 18,fill="white",width=10)
rec8 = Backround_Canvas.create_rectangle(360, 291, 600, 400, fill='#c0cff3',width=0)
rec4 = Backround_Canvas.create_rectangle(375, 129, 585, 370, fill='#C0E8F3',width=0)
Letters=Label(text="A B C D E",font=("fixedsys",20),bg="#C0E8F3", fg = "white")
Letters.place(x=405,y=130)
LabelA=Label(text="",font=("fixedsys",20),bg="#CBC0F3", fg = "white")
LabelA.place(x=405,y=165)
A=Label(text="A",font=("fixedsys",20),bg="#C0E8F3", fg = "white")
A.place(x=380,y=165)
LabelB=Label(text="",font=("fixedsys",20),bg="#CBC0F3", fg = "white")
LabelB.place(x=405,y=200)
B=Label(text="B",font=("fixedsys",20),bg="#C0E8F3", fg = "white")
B.place(x=380,y=200)
LabelC=Label(text="",font=("fixedsys",20),bg="#CBC0F3", fg = "white")
LabelC.place(x=405,y=235)
C=Label(text="C",font=("fixedsys",20),bg="#C0E8F3", fg = "white")
C.place(x=380,y=235)
LabelD=Label(text="",font=("fixedsys",20),bg="#CBC0F3", fg = "white")
LabelD.place(x=405,y=270)
D=Label(text="D",font=("fixedsys",20),bg="#C0E8F3", fg = "white")
D.place(x=380,y=270)
LabelE=Label(text="",font=("fixedsys",20),bg="#CBC0F3", fg = "white")
LabelE.place(x=405,y=305)
E=Label(text="E",font=("fixedsys",20),bg="#C0E8F3", fg = "white")
E.place(x=380,y=305)

#runs program
create_graph()
window.mainloop()
