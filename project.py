from tkinter import*
import random
root = Tk()
root.geometry("500x500")
root.maxsize(500,500)
root.title("Color Randomizer")
label_color = Label(root, font=("Vivaldi", 45, "bold", "italic"))
label_color.place(relx=0.5, rely=0.4, anchor=CENTER)
label_score = Label(root, text="Score: 0", font=("Yu Gothic", 20))
label_score.place(relx=0.2, rely=0.2, anchor=CENTER)
input_name = Entry(root)
input_name.place(relx=0.5, rely=0.55, anchor=CENTER)
class game():
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["black","green","pink","yellow","blue","red","violet","brown","lavender"]
        self.color = ["black","green","pink","yellow","blue","red","brown","lavender"]
        self.bg=["gold","violet","coral","pale violet red"]
        self.bg_random=random.randint(0, 3)
        self.random_no_text=random.randint(0, 7)
        self.random_no_color = random.randint(0, 7)
        label_color["text"] = self.text[self.random_no_text]
        label_color["fg"] = self.color[self.random_no_color]
        label_color["bg"]=self.bg[self.bg_random]
        root.configure(background=self.bg[self.bg_random])
        btn["bg"]=self.bg[self.bg_random]
        btn["fg"]=self.bg[self.bg_random]
        btn["font"]=("Comic Sans MS", 1)
        btn.place(relx=0.0, rely=0.0, anchor=CENTER)
        label_score["bg"]=self.bg[self.bg_random]
        btn["state"]=DISABLED
    def change_score(self):
        if(label_color["fg"]==input_name.get()):
            self.__score+=1
            label_score["text"]="Score: "+str(self.__score)
            self.text = ["black","green","pink","yellow","blue","red","violet","brown","lavender"]
            self.color = ["black","green","pink","yellow","blue","red","brown","lavender"]
            self.bg=["gold","violet","coral","pale violet red"]
            self.bg_random=random.randint(0, 3)
            self.random_no_text=random.randint(0, 7)
            self.random_no_color = random.randint(0, 7)
            label_color["text"] = self.text[self.random_no_text]
            label_color["fg"] = self.color[self.random_no_color]
            label_color["bg"]=self.bg[self.bg_random]
            btn["bg"]=self.bg[self.bg_random]
            btn["fg"]=self.bg[self.bg_random]
            root.configure(background=self.bg[self.bg_random])
            label_score["bg"]=self.bg[self.bg_random]
        else:
            self.__score=self.__score-1
            label_score["text"]="Score: "+str(self.__score)
obj = game()
btn = Button(root, text="START", command=obj.updateGame, relief=FLAT, font=("Comic Sans MS", 20), bg="red", fg="white")
btn.place(relx=0.8, rely=0.9, anchor=CENTER)
btn_check=Button(root,text="Check",command=obj.change_score,relief=FLAT,font=("Comic Sans MS", 20), bg="red", fg="white")
btn_check.place(relx=0.5, rely=0.7, anchor=CENTER)
root.mainloop();
