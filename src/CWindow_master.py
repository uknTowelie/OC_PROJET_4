from tkinter import *
from src.CTournament import Tournament
from src.CPlayer import Player
from src.CWindow_AddPlayer import AddPlayerPage

class MasterPage():
    WINDOW_WIDTH = "1080"
    WINDOW_HEIGHT = "760"
    
    WINDOW_MIN_WIDTH = 480
    WINDOW_MIN_HEIGHT = 360

    WINDOW_BACKGROUND_COLOR = "#669999"
    
    def setPlayerList(self):
        index = 0
        
        self.listbox_player = Listbox(self.frame_playerList,width=30,height = 20)

        if self.tournament == None:
            self.listbox_player.insert(1,"Tournament isnt started")
        elif len(self.tournament.playerTab) == 0:
            self.listbox_player.insert(1,"No player registered")
        else:
            for player in self.tournament.playerTab:
                self.listbox_player.insert(index,player.name + "/" + str(player.elo) + "/" + player.nationality)
                index += 1
        self.listbox_player.pack(padx=(10,0))
    
    def updateScoreBoard(self):
        self.listbox_scoreboard.delete(0,'end')
        self.tournament.scoreboard = []
        for player in self.tournament.playerTab:
            index = 0
            l = len(self.tournament.scoreboard)
            if l == 0:
                self.tournament.scoreboard.append(player)
            while index<l:
                if self.tournament.playerTab[index].point>self.tournament.scoreboard[index].point:
                    self.tournament.scoreboard.insert(index,player)
                    index = 100
                index+=1
        index = 0
        for player in self.tournament.scoreboard:
            self.listbox_scoreboard.insert(index,player.name + " " + str(player.point))
            index+=1
    
    def subNewPlayer(self,popup,i_name,i_elo,i_nationality):
        p = Player(i_name.get(),i_elo.get(),i_nationality.get())
        if len(self.tournament.playerTab) == 0:
            self.listbox_player.delete(0,1)
        self.tournament.addPlayerToTab(p)
        self.listbox_player.insert(len(self.tournament.playerTab),p.name + "/" + str(p.elo) + "/" + p.nationality)
        i_name.delete(0,'end')
        i_elo.delete(0,'end')
        i_nationality.delete(0,'end')
        self.listbox_scoreboard.insert(len(self.tournament.playerTab),p.name + "/" + str(p.point))
        
    def openAddPlayerPopup(self):
        popUpAddPlayer = Toplevel()
        popUpAddPlayer.title("Add a new player")

        addplayer_frame_input = Frame(popUpAddPlayer)

        addplayer_label_name = Label(addplayer_frame_input,text="Type name")
        addplayer_label_name.grid(row=0,column=0)

        addplayer_entry_name = Entry(addplayer_frame_input)
        addplayer_entry_name.grid(row=1,column=0)

        addplayer_label_elo = Label(addplayer_frame_input,text="Type elo")
        addplayer_label_elo.grid(row=0,column=1)

        addplayer_entry_elo = Entry(addplayer_frame_input)
        addplayer_entry_elo.grid(row=1,column=1)

        addplayer_label_nationality = Label(addplayer_frame_input,text="Type nationality")
        addplayer_label_nationality.grid(row=0,column=2)

        addplayer_entry_nationality = Entry(addplayer_frame_input)
        addplayer_entry_nationality.grid(row=1,column=2)

        addplayer_frame_input.pack()

        addplayer_button_submit = Button(popUpAddPlayer,text="Submit",command=lambda : self.subNewPlayer(popUpAddPlayer,addplayer_entry_name,addplayer_entry_elo,addplayer_entry_nationality))
        addplayer_button_submit.pack()

        addplayer_button_exit = Button(popUpAddPlayer,text="Close",command=popUpAddPlayer.destroy)
        addplayer_button_exit.pack()

        popUpAddPlayer.transient(self.window)
        popUpAddPlayer.grab_set()
        self.window.wait_window(popUpAddPlayer)
    
    
            
    def initTournament(self,frame,name,date):
        self.tournament = Tournament(name,date)
        self.label_tournamentInfo['text'] = name + "\n" + date
        self.setPlayerList()
        frame.pack_forget()
        self.frame_section.pack()
        self.frame_startTournament.pack()
        

    def createTournament(self):
        self.button_createTournament.pack_forget()
        
        cTournament_frame_createTournament = Frame(self.window)

        cTournament_frame_inputContainer = Frame(cTournament_frame_createTournament)

        cTournament_label_name = Label(cTournament_frame_inputContainer,text="Type name")
        cTournament_label_name.grid(row=0,column=0)

        cTournament_entry_name = Entry(cTournament_frame_inputContainer)
        cTournament_entry_name.grid(row=1,column=0)

        cTournament_label_date = Label(cTournament_frame_inputContainer,text="Type date")
        cTournament_label_date.grid(row=0,column=1)

        cTournament_entry_date = Entry(cTournament_frame_inputContainer)
        cTournament_entry_date.grid(row=1,column=1)

        cTournament_frame_inputContainer.pack()

        cTournament_button_submit = Button(cTournament_frame_createTournament,text="Create Tournament",command=lambda : self.initTournament(cTournament_frame_createTournament,cTournament_entry_name.get(),cTournament_entry_date.get()))
        cTournament_button_submit.pack()

        cTournament_frame_createTournament.pack()
    
    def startTournament(self):
        print("Ca start tavu")

    def __init__(self):
        self.tournament = None


            # Initialisatio nde la fenetre
        self.window = Tk()
        self.window.geometry(self.WINDOW_WIDTH + "x" + self.WINDOW_HEIGHT)
        self.window.minsize(self.WINDOW_MIN_WIDTH,self.WINDOW_MIN_HEIGHT)
        self.window.title("TournamentSup")
        self.window.config(background=self.WINDOW_BACKGROUND_COLOR)

        self.frame_head = Frame(self.window)

        self.label_tournamentInfo = Label(self.frame_head,text="no Tournament yet")
        self.label_tournamentInfo.grid(row=0,column=0,sticky=W)
        self.label_title = Label(self.frame_head, text="TournamentSup",font=("Arial",40),foreground="#ffffff",background=self.WINDOW_BACKGROUND_COLOR)
        self.label_title.grid(row=0,column=1,sticky=W)

        self.frame_head.columnconfigure(0,weight=4)
        self.frame_head.columnconfigure(1,weight=5)
        self.frame_head.pack(fill=X)

        self.button_createTournament = Button(self.window,text="Create Tournament",command=self.createTournament)
        self.button_createTournament.pack()

        self.frame_section = Frame(self.window,bg=self.WINDOW_BACKGROUND_COLOR,relief=SUNKEN)
        
        self.frame_playerList = Frame(self.frame_section,bg=self.WINDOW_BACKGROUND_COLOR)
        self.frame_playerList_title = Frame(self.frame_playerList,bg=self.WINDOW_BACKGROUND_COLOR)
        self.label_playerList_title = Label(self.frame_playerList_title,text="List of player",font=("Arial",22),bg=self.WINDOW_BACKGROUND_COLOR)
        self.label_playerList_title.grid(row=0,column=0,sticky=W,padx=(10,0))
        self.button_addPlayer = Button(self.frame_playerList_title,text="+",command=self.openAddPlayerPopup)
        self.button_addPlayer.grid(row=0,column=1)
        self.button_deletePlayer = Button(self.frame_playerList_title,text="-")
        self.button_deletePlayer.grid(row=0,column=2)
        self.frame_playerList_title.pack()
        self.listbox_player = None
        self.frame_playerList.grid(row=0,column=0)

        self.frame_rounds = Frame(self.frame_section)
        
        self.label_rounds_title = Label(self.frame_rounds,text="List of rounds")
        self.label_rounds_title.grid(row=0,column=0)

        self.listbox_rounds = Listbox(self.frame_rounds,width=25)
        self.listbox_rounds.insert(0,"Tournament hasnt strated yet")
        self.listbox_rounds.grid(row=1,column=0)

        self.frame_rounds.grid(row=0,column=1)

        self.frame_scoreboard = Frame(self.frame_section)

        self.label_scoreboard_title = Label(self.frame_scoreboard,text="Scoreboard")
        self.label_scoreboard_title.grid(row=0)
        self.listbox_scoreboard = Listbox(self.frame_scoreboard)
        self.listbox_scoreboard.grid(row=1)

        self.frame_scoreboard.grid(row=0,column=2)

        self.frame_startTournament = Frame(self.window)
        
        self.label_roundsEntry = Label(self.frame_startTournament,text="Type number od rounds")
        self.label_roundsEntry.pack()

        self.entry_rounds = Entry(self.frame_startTournament)
        self.entry_rounds.pack()

        self.button_startTournament = Button(self.frame_startTournament,text="Start tournament",command=lambda : self.startTournament)
        self.button_startTournament.pack()

        self.window.mainloop()

    
