
# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
x = 0
timer = None




# ---------------------------- TIMER RESET ------------------------------- # 
def Reset_countdown():
    global rep, x
    rep = 0 
    x = 0
    Timer_text.config(text='Timer', fg=GREEN)
    Check_mark.config(text='')
    canvas.itemconfig(time_counted, text='00:00')
    window.after_cancel(timer) 
    #如果要關掉倒數的function，要用after_cancel()，
    #並且把after放進()裡面，例如after_cancel(after(xxxxms, function object, *arg))


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def Start_countdown():
    global rep
    global x
    rep += 1
    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        Timer_text.config(text='Take a long break~~', fg=RED)

    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        Timer_text.config(text='Short Break!!', fg=PINK)

    else:
        count_down(WORK_MIN*60)
        Timer_text.config(text='Work Time', fg=GREEN)
        num_of_chechmark = rep-x
        Check_mark.config(text='✓'*num_of_chechmark)
        x += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(total_sec):
    global timer
    time = divmod(total_sec,60)
    canvas.itemconfig(time_counted, text='{1:02d}:{0:02d}'.format(time[1],time[0]))

    if total_sec > 0 :
        timer = window.after(1000,count_down,total_sec-1)

    if total_sec == 0 :
        Start_countdown()
    
    

#以下是在測試after()是不是可以在loop裡面，進行有先後順利的顯示功能，因為after會重複進行2nd arg所引入的func object，
#如果放多個count_down在loop裡，會同時出現這些count_down，最後一個出來的會覆蓋在在外層顯現出來，其他會在背景倒數。

# def count_down_test1(total_sec):
#     time = divmod(total_sec,60)
#     Countdown_test1.config(text='{:02d}:{:02d}'.format(time[0],time[1]))

#     if total_sec > 0 :
#         window.after(1000,count_down_test1,total_sec-1)   

# def count_down_test2(total_sec):
#     time = divmod(total_sec,60)
#     Countdown_test2.config(text='{:02d}:{:02d}'.format(time[0],time[1]))

#     if total_sec > 0 :
#         window.after(1000,count_down_test2,total_sec-1)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

#Set up window
window = Tk()
window.title('Pomomdoro')
window.config(padx=100, pady=50, bg=YELLOW)


#Set up Timer label
Timer_text = Label(text='Timer', font=('Arial',40,'bold'), fg=GREEN, bg=YELLOW)
Timer_text.grid(column=1, row=0)

#Set up test label
# Countdown_test1 = Label(text='00:00', font=(FONT_NAME,35,'bold'))
# Countdown_test1.grid(column=2,row=1)

# Countdown_test2 = Label(text='00:00', font=(FONT_NAME,35,'bold'))
# Countdown_test2.grid(column=0,row=1)

#Set up tomato background pic via Canvas()
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='./tomato.png')
canvas.create_image(100,112,image= tomato_img)
time_counted = canvas.create_text(100,150,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1, row= 1)


#Set up check mark
Check_mark = Label(text = '', fg=GREEN, bg=YELLOW)
Check_mark.grid(column=1, row=3)


#Set up Start/Reset buttons and their function
Start_button = Button(text='Start', highlightbackground=YELLOW, command=Start_countdown)
Start_button.grid(column=0, row=2)
Reset_button = Button(text='Reset', highlightbackground=YELLOW, command=Reset_countdown)
Reset_button.grid(column=2, row=2)





window.mainloop()