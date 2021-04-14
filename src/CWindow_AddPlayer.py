from tkinter import *
from src.CPlayer import Player


class AddPlayerPage:

    def registerPlayer(self):
        name = self.entry_name.get()
        elo = int(self.entry_elo.get())
        nationality = self.entry_nationality.get()

        self.parent.tournament.playerTab.append(Player(name,elo,nationality))
        self.parent.setPlayerList()
        

    def __init__(self,i_parent):
        self.parent = i_parent
        self.window = Tk()
        self.window.title("Add a new player")
        

        self.frame_inputContainer = Frame(self.window,pady=5)

        self.label_nameTitle = Label(self.frame_inputContainer,text="Type Name :",padx=10)
        self.label_nameTitle.grid(row=0,column=0,sticky=W)

        self.entry_name = Entry(self.frame_inputContainer)
        self.entry_name.grid(row=1,column=0,padx=5)

        self.label_eloTitle = Label(self.frame_inputContainer,text="Type elo :",padx=10)
        self.label_eloTitle.grid(row=0,column=1,sticky=W)

        self.entry_elo = Entry(self.frame_inputContainer)
        self.entry_elo.grid(row=1,column=1,padx=5)

        self.label_nationalityTitle = Label(self.frame_inputContainer,text="Type nationality :",padx=10)
        self.label_nationalityTitle.grid(row=0,column=2,sticky=W)

        self.entry_nationality = Entry(self.frame_inputContainer)
        self.entry_nationality.grid(row=1,column=2,padx=5)

        self.frame_inputContainer.pack()
        self.button_submit = Button(self.window,text="Register player",command=self.registerPlayer)
        self.button_submit.pack(pady=20)

        self.window.mainloop()