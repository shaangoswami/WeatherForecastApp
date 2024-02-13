from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    # go to https://openweathermap.org/ >> api >> select data collection according to need >> 
    # Copy APIcall from APIdoc >> get api key
    data = requests.get("follow above"+city+"appid={API key} ").json()
    w_label1.config(text=data['weather'][0]['main'])           
    wb_label2.config(text=data['weather'][0]['description'])
    temp_label1.config(text=str(int(data['main']['temp']-273.15)))
    pre_label1.config(text=data['main']['pressure'])
win = Tk()
win.title("Blizzard Cloud")
win.config(bg= "light blue")
win.geometry("500x570")

name_label= Label(win,text="Blizzard cloud",
                  font=("Times New Roman",40,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

list_name =("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")

city_name= StringVar()
com = ttk.Combobox(win,text="Blizzard cloud",values = list_name,
                  font=("Times New Roman",20,"bold"),textvariable=city_name)              
com.place(x=25,y=120,height=50,width=450)


w_label= Label(win,text="Weather Climate",
                  font=("Times New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)
w_label1= Label(win,text="",
                  font=("Times New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)



wb_label= Label(win,text="Weather Description",
                  font=("Times New Roman",17))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label2= Label(win,text="",
                  font=("Times New Roman",17))
wb_label2.place(x=250,y=330,height=50,width=210)



temp_label= Label(win,text="Temperature",
                  font=("Times New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1= Label(win,text="",
                  font=("Times New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)


pre_label= Label(win,text="Pressure",
                  font=("Times New Roman",20))
pre_label.place(x=25,y=470,height=50,width=210)
pre_label1= Label(win,text="",
                  font=("Times New Roman",20))
pre_label1.place(x=250,y=470,height=50,width=210)

done_button= Button(win,text="Done",
                  font=("Times New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()