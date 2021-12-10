from tkinter import * 
from tkinter.ttk import *
import tkinter.scrolledtext as st
import tkinter as tk
import http.client
import urllib.parse
import urllib
import json

top = Tk()   
top.geometry("700x500")  
top.title("LiGoogle")
def submit():
    root = Tk()   
    root.geometry("700x500") 
    root.title("LiGoogle") 
    conn = http.client.HTTPSConnection("google-search3.p.rapidapi.com")
    headers = {
        'x-user-agent': "desktop",
        'x-proxy-location': "US",
        'x-rapidapi-host': "google-search3.p.rapidapi.com",
        'x-rapidapi-key': key.get()
    }
    conn.request("GET", "/api/v1/search/q="+ urllib.parse.quote(str(term.get())) +"&num=5", headers=headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    your_json = result
    parsed = json.loads(your_json)
    google = json.dumps(parsed, indent=4, sort_keys=True)
    top.destroy()
    text_area = st.ScrolledText(root,
                            width = 67, 
                            height = 20, 
                            )
    text_area.grid(column = 0, pady = 10, padx = 10)
    text_area.insert(tk.INSERT, google)
    root.mainloop()

# the label for user_name 
term_text = Label(top, 
                  text = "Search term")
key_text = Label(top, 
                      text = "Key")

    
submit_button = Button(top, 
                       text = "Submit",
                            command = submit
                            )
term_text.grid()
key_text.grid()

term = Entry(top,
                             width = 30)
term.grid(column = 2, row = 0)

key = Entry(top,
                                 width = 30)
key.grid(row = 1, column = 2) 
submit_button.grid()


top.mainloop() 