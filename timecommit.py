import time
import os
from datetime import datetime
from datetime import date as dt

name = raw_input("Enter your name")
today = dt.today()
d2 = today.strftime("%B %d, %Y")

now = datetime.now()
time_string = now.strftime("%H:%M:%S")

os.system("git add .")
os.system("git commit -m " + "'Commit by " + name + " on " + d2 + " " + time_string +  "'")
os.system("git push origin master")
