from bs4 import BeautifulSoup as bs
import requests
from tkinter import *

response = requests.get("https://www.trthaber.com/haber/spor/").text
html_content = bs(response, "html.parser")

titles = [i.find("a").text.strip() for i in html_content.find_all("div", {"class":"title"})]
contents = [i.find("a").text.strip() for i in html_content.find_all("div", {"class":"description"})]

window = Tk()
window.geometry("800x650")

for i in range(len(titles)):
    Label(text=titles[i], fg="#f00").pack()
    Label(text=contents[i]).pack()
    Label(text="").pack()

window.mainloop()