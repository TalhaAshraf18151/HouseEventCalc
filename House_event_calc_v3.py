import tkinter
from tkinter import *
from tkinter import messagebox 
from tkinter import font

tk = tkinter
main = Tk()  # Name of main window
main.title("House event calculator")  # Title
main.geometry("450x270")  # Size of the window in pixels
main.configure(bg="#D2D4DA")  # Background colour
main.resizable(False, False) #Makes window unable to resize in x and y direction just to keep the user from interfering with the structure in the window


All_events = [] #list in which I will hold my HouseEvent object
names_list = ["Lampada Games", "House Trivia"] #list for holding Event names to be used in drop down   
ph_list = [75, 66] #List for holding points of teams for use in Leader board
ku_list = [60, 68] #                   ''
kw_list = [72, 74] #                   ''
ru_list = [68, 73] #                   ''

#----------------------Frames----------------------#
#Frames are like containers from html they help keep things organized
entry_frame = LabelFrame(main, background="#D2D4DA")
entry_frame.grid(row=0, column=0, padx=10, pady=10, sticky=W)

det_frame = LabelFrame(main, background="#D2D4DA")
det_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=N)

lead_frame = LabelFrame(main, background="#D2D4DA")
lead_frame.grid(row=0, column=1, padx=10, pady=10, sticky=E)

#----------------------Widgets----------------------#
    #-entry_frame labels-#
tk.Label(entry_frame, text="Name of Event", font=("Fixedsys", 12), background="#D2D4DA").grid(column=0, row=0, sticky=W)
tk.Label(entry_frame, text="Is it a sport", font=("Fixedsys", 10), background="#D2D4DA").grid(column=0, row=1, sticky=W)
tk.Label(entry_frame, text="Pohutukawa", font=("Fixedsys", 12), background="#FA6C38").grid(column=0, row=2, sticky=W)
tk.Label(entry_frame, text="Kauri", font=("Fixedsys", 12), background="#62A8F9").grid(column=0, row=3, sticky=W)
tk.Label(entry_frame, text="Kowhai", font=("Fixedsys", 12), background="#FFBC1F").grid(column=0, row=4, sticky=W)
tk.Label(entry_frame, text="Rimu", font=("Fixedsys", 12), background="#01F472").grid(column=0, row=5, sticky=W)
    #-det_frame lables-#
tk.Label(det_frame, text="Event Name", font=("Fixedsys", 12), background="#D2D4DA").grid(column=0, row=0, sticky=W)

entry_1 = tk.Entry(entry_frame, font="Fixedsys", background="#E9E9ED")

is_sport = tk.StringVar()
is_sport.set("Yes")
Radiobutton(entry_frame, text="Yes", variable=is_sport, value="Yes", font=("Fixedsys", 12), background="#D2D4DA").grid(column=1, row=1,)
Radiobutton(entry_frame, text="No", variable=is_sport, value="No", font=("Fixedsys", 12), background="#D2D4DA").grid(column=2, row=1,)

spin_1 = Spinbox(entry_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), width=15, readonlybackground="#E9E9ED", foreground="#FA6C38")
spin_2 = Spinbox(entry_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), width=15, readonlybackground="#E9E9ED", foreground="#0656B1")
spin_3 = Spinbox(entry_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), width=15, readonlybackground="#E9E9ED", foreground="#E09D00")
spin_4 = Spinbox(entry_frame , from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), width=15, readonlybackground="#E9E9ED", foreground="#1C9C76")


# using geometry manager to arange input widgets because we cant use .grid() on them directly because they are needed as variables
entry_1.grid(column=1, row=0, columnspan=2, padx=2)
spin_1.grid(column=1, row=2,columnspan=2)
spin_2.grid(column=1, row=3,columnspan=2)
spin_3.grid(column=1, row=4,columnspan=2)
spin_4.grid(column=1, row=5,columnspan=2)

#--Leader board--##
Label(lead_frame, text="Leaderboard", font=("Fixedsys", 15), background="#D2D4DA").grid(column=0, row=0, columnspan=2, pady=10)
Label(lead_frame, text="Pohutukawa", font=("Fixedsys", 11), background="#FA6C38").grid(column=0, row=1, sticky=W, pady=5)
Label(lead_frame, text="Kauri", font=("Fixedsys", 11), background="#62A8F9").grid(column=0, row=2, sticky=W, pady=5)
Label(lead_frame, text="Kowhai", font=("Fixedsys", 11), background="#FFBC1F").grid(column=0, row=3, sticky=W, pady=5)
Label(lead_frame, text="Rimu", font=("Fixedsys", 11), background="#01F472").grid(column=0, row=4, sticky=W, pady=5)
Label(lead_frame, text= sum(ph_list), font=("Fixedsys", 12), background="#FA6C38").grid(column=1, row=1, sticky=W, pady=5, padx= 3)
Label(lead_frame, text= sum(ku_list), font=("Fixedsys", 12), background="#62A8F9").grid(column=1, row=2, sticky=W, pady=5, padx= 3)
Label(lead_frame, text= sum(kw_list), font=("Fixedsys", 12), background="#FFBC1F").grid(column=1, row=3, sticky=W, pady=5, padx= 3)
Label(lead_frame, text= sum(ru_list), font=("Fixedsys", 12), background="#01F472").grid(column=1, row=4, sticky=W, pady=5, padx= 3)


#-----------defining the class using which I will create my house event objects-----------#
class HouseEvent:
    def __init__(self, name, eventtype, ph_points, ku_points, kw_points, ru_points, who_won):
        self.name = name
        self.eventtype = eventtype
        self.ph_points = ph_points
        self.ku_points = ku_points
        self.kw_points = kw_points
        self.ru_points = ru_points
        self.who_won = who_won
        
    def get_name(self):
        # the_thing = "Name : " + self.name + "/nIs it a sport : " + self.eventtype
        return(["Name : " + self.name, "Is a sport : " + self.eventtype, "Pohutukawa Points : " + str(self.ph_points), "Kauri Points : " + str(self.ku_points), "Kowhai Points : " + str(self.kw_points), "Rimu Points : " + str(self.ru_points), "Winner : " + self.who_won])

    def get_event_type(self):
        return(self.eventtype)

    def get_ph_pt(self):
        return(self.ph_points)

    def get_ku_pt(self):
        return(self.ku_points)

    def get_kw_pt(self):
        return(self.kw_points)

    def get_ru_pt(self):
        return(self.ru_points)

    def get_who_won(self):
        return(self.who_won)

#--Pre made house events--#
All_events.append(HouseEvent("Lampada Games", "Yes", 75, 60, 72, 68, "Pohutukawa"))
All_events.append(HouseEvent("House Trivia", "No", 66, 68, 74, 73, "Kowhai"))
#----------------Drop down to select which events details need to be accessed----------------#
value_inside = tkinter.StringVar()
# Set the default value of the variable
value_inside.set("Select an event")
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
question_menu_1 = tkinter.OptionMenu(det_frame, value_inside, *names_list)
question_menu_1.config(font="Fixedsys", background="#D2D2DA", activebackground="#E9E9ED")
question_menu_1.grid(row=0, column=1)

#Function that takes the users input and uses the class constructor the make an object and then append it to the list we created above
def make_obj(): 
    global value_inside
    global question_menu_1
    name = entry_1.get()
    event_type = is_sport.get()
    points_ph = int(spin_1.get())
    points_ku = int(spin_2.get())
    points_kw = int(spin_3.get())
    points_ru = int(spin_4.get())
    #validating name input
    if name.strip() != "" and name not in names_list and len(name) <= 20:
        #Sorting Scores
        points_list = [('Pohutukawa', points_ph), ('Kauri', points_ku),("Kowhai", points_kw), ('Rimu', points_ru)]
        points_list.sort(reverse=YES, key = lambda x: x[1])
        #Validating Points input
        if points_ph == 0 and points_ku == 0 and points_kw == 0 and points_ru == 0:
            messagebox.showerror("Points Error", "Please enter points")
        else:
            names_list.append(str(name))    
            first_check = None
            second_check = None
            third_check = None
            
            if points_list[0][1] == points_list[1][1]:
                first_check = True

                if points_list[1][1] == points_list[2][1]:
                    second_check = True

                    if points_list[2][1] == points_list[3][1]:
                        third_check = True

                    else:
                        third_check = False

                else:
                    second_check = False   

            else:
                first_check = False
                second_check = False
                third_check = False
            #Setting the winner variable by first finding out if there are multiple winners and then setting the winner as the singular or multiple winners found
            if points_list[0][1] != 0:
                    
                if first_check == True:
                    if second_check == True:
                        if third_check == True:
                            winners = "All teams tied"
                        else:
                            winners = points_list[0][0] +", "+ points_list[1][0] + ", " + points_list[2][0]
                    else:
                        winners = points_list[0][0]+", "+ points_list[1][0]
                else:
                    winners = points_list[0][0]
            else:
                winners = 0

            #Creating the House event object and appending it to a list for it to be stored
            All_events.append(HouseEvent(name, event_type, points_ph, points_ku, points_kw, points_ru, winners))
            #Adding scores to house points list for leader board
            ph_list.append(points_ph)
            ku_list.append(points_ku)
            kw_list.append(points_kw)
            ru_list.append(points_ru)
            # Variable to keep track of the option

            # Create the optionmenu widget and passing 
            # the options_list and value_inside to it
            Label(lead_frame, text= sum(ph_list), font=("Fixedsys", 12), background="#FA6C38").grid(column=1, row=1, sticky=W)
            Label(lead_frame, text= sum(ku_list), font=("Fixedsys", 12), background="#62A8F9").grid(column=1, row=2, sticky=W)
            Label(lead_frame, text= sum(kw_list), font=("Fixedsys", 12), background="#FFBC1F").grid(column=1, row=3, sticky=W)
            Label(lead_frame, text= sum(ru_list), font=("Fixedsys", 12), background="#01F472").grid(column=1, row=4, sticky=W)
            #Destroying previous option menu so that when we add a new one with the updated list there is no overlap
            question_menu_1.destroy() 
            value_inside = tkinter.StringVar()
            value_inside.set("Select an event")
            #This option menu has to be put in because the one that is there previously will now be missing an event
            question_menu_1 = tkinter.OptionMenu(det_frame, value_inside, *names_list)
            question_menu_1.config(font="Fixedsys", background="#D2D2DA", activebackground="#E9E9ED")
            question_menu_1.grid(row=0, column=1)
    #Erorr messages if the data is not valid
    elif name in names_list:
        messagebox.showerror("Name Error", "An event with this name already exists please chose another name")
    elif name.strip() == "":    
       messagebox.showerror("Name Error", "You must enter a name for the event")
    elif len(name) > 20:
       messagebox.showerror("Name Error", "Your name is too long it must be 20 characters only")

#Function for showing event details. It takes the string var from the option menu then uses a class function get_info() to pull information from the desired object and show it in an infobox 
def info_func():
    entry = value_inside.get()
    for info in All_events:
        if entry == info.name:
            global question_menu_1
            question_menu_1.destroy()
            question_menu_1 = tkinter.OptionMenu(det_frame, value_inside, *names_list)
            question_menu_1.grid(row=0, column=1)
            question_menu_1.config(font="Fixedsys", background="#D2D2DA", activebackground="#E9E9ED")
            tkinter.messagebox.showinfo("Event Details", "\n".join(info.get_name()))
            
#button for saving event it calls the make_obj function and creates each event as an object
tk.Button(entry_frame, text="Save Event", command=make_obj, font=("Fixedsys"), background="#C7C7D1", activebackground="#E9E9ED").grid(row=7, column=0,columnspan=3, pady=5)
#Button for showing details it calls the info_func which shows a infobox with information. Refer to the comments for the info_func() for more details on how that works
tk.Button(det_frame, text="Show Details", command=info_func, font=("Fixedsys"), background="#C7C7D1", activebackground="#E9E9ED").grid(column=0, row=1, columnspan=2)

main.mainloop()