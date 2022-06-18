import os
from tkinter import *
from tkinter import ttk

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
act_month = 0
days_nb = [31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
act_day = 1
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
wich_day = 0
year = 1212
day_list = []
margin = wich_day % 7

root = Tk()
frm = ttk.Frame(root, padding=5, borderwidth=2)
frm.grid()

entry_save = ttk.Entry(frm)
entry_load = ttk.Entry(frm)

for i in range(0, 35):
    day_list.append(ttk.Button(frm))

monday = ttk.Label(frm, text="Monday", width=20)
tuesday = ttk.Label(frm, text="Tuesday", width=20)
wednesday = ttk.Label(frm, text="Wednesday", width=20)
thursday = ttk.Label(frm, text="Thursday", width=20)
friday = ttk.Label(frm, text="Friday", width=20)
saturday = ttk.Label(frm, text="Saturday", width=20)
sunday = ttk.Label(frm, text="Sunday", width=20)

year_lb = ttk.Label(frm, text=year)
month_lb = ttk.Label(frm, text=month[act_month])
day_lb = ttk.Label(frm, text=act_day)
wich_day_lb = ttk.Label(frm, text=days[wich_day])

def skip_day():
    global month, act_month, days_nb, act_day, days, year, year_lb, month_lb, day_lb, wich_day, wich_day_lb, margin
    act_day += 1
    if (act_day > days_nb[act_month]):
        act_day = 1
        act_month += 1
        if (act_month >= 12):
            act_month = 0
            year += 1
    wich_day += 1
    if (wich_day >= 7):
        wich_day = 0

    day_lb['text'] = act_day
    month_lb['text'] = month[act_month]
    year_lb['text'] = year
    wich_day_lb['text'] = days[wich_day]
    if act_day == 1:
        margin = wich_day
    i = 0
    for _ in range(len(day_list)):
        if i == act_day:
            day_list[i - 1 + margin]["text"] += "\nAJD"
            break
        i +=1

    if act_day == 1:
        if act_month == 0:
            day_list[days_nb[11] + margin]["text"] = ""
        else:
            print(days_nb[act_month - 1] - 1 + margin)
            day_list[days_nb[act_month - 1] - 1 + margin]["text"] = ""
    else:
        day_list[i-2 + margin]["text"] = ""

def rewind_day():
    global month, act_month, days_nb, act_day, days, year, year_lb, month_lb, day_lb, wich_day, wich_day_lb
    act_day -= 1
    if (act_day <= 0):
        act_month -= 1
        if (act_month < 0):
            act_month = 11
            year -= 1
        act_day = days_nb[act_month]
    wich_day -= 1
    if (wich_day < 0):
        wich_day = 6

    day_lb['text'] = act_day
    month_lb['text'] = month[act_month]
    year_lb['text'] = year
    wich_day_lb['text'] = days[wich_day]

def save():
    global month, act_month, days_nb, act_day, days, year, year_lb, month_lb, day_lb, wich_day, wich_day_lb, entry_save
    content = entry_save.get()
    if (not content):
        return
    else:
        try:
            for saves in os.scandir("./saves"):
                if (saves.is_file() == True and saves.name == content + ".save"):
                    os.remove(f"./saves/{content}.save")
        except:
            os.mkdir("./saves")
        with open(f"./saves/{content}.save", "w") as tf:
            tf.write(f"{year}\n{act_month}\n{act_day}\n{wich_day}")

def load():
    global month, act_month, days_nb, act_day, days, year, year_lb, month_lb, day_lb, wich_day, wich_day_lb, entry_load
    content = entry_load.get()
    if (not content):
        return
    else:
        try:
            for saves in os.scandir("./saves"):
                if (saves.is_file() == True and saves.name == content + ".save"):
                    with open(f"./saves/{content}.save", "r") as tf:
                        load = tf.readlines()
                        try:
                            tmp_year = int(load[0])
                            tmp_month = int(load[1])
                            tmp_day = int(load[2])
                            tmp_wich = int(load[3])

                            year = tmp_year
                            act_month = tmp_month
                            act_day = tmp_day
                            wich_day = tmp_wich

                            day_lb['text'] = act_day
                            month_lb['text'] = month[act_month]
                            year_lb['text'] = year
                            wich_day_lb['text'] = days[wich_day]
                        except:
                            print("error")
                            return
        except:
            os.mkdir("./saves")

def main():
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    ttk.Button(frm, text="Next", command=skip_day).grid(column=2, row=2)
    ttk.Button(frm, text="prev", command=rewind_day).grid(column=1, row=2)

    entry_save.grid(column=1, row=1)
    ttk.Button(frm, text="save", command=save).grid(column=2, row=1)
    entry_load.grid(column=3, row=1)
    ttk.Button(frm, text="load", command=load).grid(column=4, row=1)

    year_lb.grid(column=0, row=0)
    month_lb.grid(column=0, row=1)
    day_lb.grid(column=0, row=2)
    wich_day_lb.grid(column=0, row=3)

    ttk.Separator(frm, orient="horizontal").grid(column=0, row=4, sticky="ew", columnspan=50)

    monday.grid(column=1, row=5)
    tuesday.grid(column=2, row=5)
    wednesday.grid(column=3, row=5)
    thursday.grid(column=4, row=5)
    friday.grid(column=5, row=5)
    saturday.grid(column=6, row=5)
    sunday.grid(column=7, row=5)

    ttk.Separator(frm, orient="horizontal").grid(column=1, row=6, sticky="ew", columnspan=7)
    ttk.Separator(frm, orient="horizontal").grid(column=1, row=8, sticky="ew", columnspan=7)
    ttk.Separator(frm, orient="horizontal").grid(column=1, row=10, sticky="ew", columnspan=7)
    ttk.Separator(frm, orient="horizontal").grid(column=1, row=12, sticky="ew", columnspan=7)
    ttk.Separator(frm, orient="horizontal").grid(column=1, row=14, sticky="ew", columnspan=7)
    ttk.Separator(frm, orient="vertical").grid(column=1, row=6, sticky="ens", rowspan=10)
    ttk.Separator(frm, orient="vertical").grid(column=2, row=6, sticky="ens", rowspan=10)
    ttk.Separator(frm, orient="vertical").grid(column=3, row=6, sticky="ens", rowspan=10)
    ttk.Separator(frm, orient="vertical").grid(column=4, row=6, sticky="ens", rowspan=10)
    ttk.Separator(frm, orient="vertical").grid(column=5, row=6, sticky="ens", rowspan=10)
    ttk.Separator(frm, orient="vertical").grid(column=6, row=6, sticky="ens", rowspan=10)

    for i in range(len(day_list)):
        if i == act_day:
            day_list[i - 1 + margin]["text"] += "\nAJD"
        day_list[i].grid(column=i%7 + 1, row=int(i/7) * 2 + 7)

    root.mainloop()

main()