from ctypes import alignment
from tkinter import *
from tkinter import ttk

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
act_month = 0
days_nb = [31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
act_day = 1
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
wich_day = 0
year = 1212

root = Tk()
frm = ttk.Frame(root, padding=5, borderwidth=2)
frm.grid()

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
    global month, act_month, days_nb, act_day, days, year, year_lb, month_lb, day_lb, wich_day, wich_day_lb
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

def main():
    year_lb.grid(column=0, row=0)
    month_lb.grid(column=0, row=1)
    day_lb.grid(column=0, row=2)
    wich_day_lb.grid(column=0, row=3)

    ttk.Separator(frm, orient="horizontal").grid(column=0, row=4, sticky="ew", columnspan=50)

    ttk.Separator(frm, orient="horizontal").grid(column=1, row=6, sticky="ew", columnspan=7)
    ttk.Separator(frm, orient="horizontal").grid(column=1, row=7, sticky="ew", columnspan=7)
    ttk.Separator(frm, orient="horizontal").grid(column=1, row=8, sticky="ew", columnspan=7)
    ttk.Separator(frm, orient="horizontal").grid(column=1, row=9, sticky="ew", columnspan=7)
    ttk.Separator(frm, orient="horizontal").grid(column=1, row=10, sticky="ew", columnspan=7)
    ttk.Separator(frm, orient="vertical").grid(column=1, row=6, sticky="ens", rowspan=5)
    ttk.Separator(frm, orient="vertical").grid(column=2, row=6, sticky="ens", rowspan=5)
    ttk.Separator(frm, orient="vertical").grid(column=3, row=6, sticky="ens", rowspan=5)
    ttk.Separator(frm, orient="vertical").grid(column=4, row=6, sticky="ens", rowspan=5)
    ttk.Separator(frm, orient="vertical").grid(column=5, row=6, sticky="ens", rowspan=5)
    ttk.Separator(frm, orient="vertical").grid(column=6, row=6, sticky="ens", rowspan=5)

    monday.grid(column=1, row=5)
    tuesday.grid(column=2, row=5)
    wednesday.grid(column=3, row=5)
    thursday.grid(column=4, row=5)
    friday.grid(column=5, row=5)
    saturday.grid(column=6, row=5)
    sunday.grid(column=7, row=5)

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
    ttk.Button(frm, text="Next", command=skip_day).grid(column=2, row=1)
    ttk.Button(frm, text="prev", command=rewind_day).grid(column=3, row=1)
    root.mainloop()

main()