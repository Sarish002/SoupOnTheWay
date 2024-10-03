from ttkbootstrap import *
import Web

root = Window(themename = "journal")
root.geometry("800x500")
root.title("Distance calculator")

distance = StringVar(root,
                     "")
mystyle = Style()
mystyle.configure("default.TButton", font = ("Comic Sans MS", 15, "bold"))

L1 = Label(root,
           text = "Take off: ",
           font = ("Comic Sans MS", 15, "bold"))
L1.place(relx = 0.1575,
         rely = 0.2,
         anchor = "center")

L2 = Label(root,
           text = "Landing: ",
           font = ("Comic Sans MS", 15, "bold"))
L2.place(relx = 0.6075,
         rely = 0.2,
         anchor = "center")

L3 = Label(root,
           text = "",
           textvariable = distance,
           font = ("Comic Sans MS", 12, "bold"),
           justify = "center")
L3.place(relx = 0.5,
         rely = 0.7,
         anchor = "center")

E1 = Entry(root,
           font = ("Comic Sans MS", 15, "bold"),
           width = 10)
E1.place(relx = 0.245,
         rely = 0.2,
         anchor = "w")

E2 = Entry(root,
           font = ("Comic Sans MS", 15, "bold"),
           width = 10)
E2.place(relx = 0.69,
         rely = 0.2,
         anchor = "w")

def Get_Distance():
    global E1, E2
    city1 = Web.Distance().City(E1.get())
    city2 = Web.Distance().City(E2.get())

    dist = Web.Distance(city1, city2)
    distance.set(dist.distance)

B1 = Button(root,
            text = "Find the distance",
             style = "default.TButton",
            command = Get_Distance)
B1.place(relx = 0.5,
         rely = 0.4,
         anchor = "center")

root.mainloop()