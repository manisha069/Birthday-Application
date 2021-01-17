import datetime
import win10toast

def toast(message):
	toaster=win10toast.ToastNotifier()
	toaster.show_toast('Python', message)

data={"193":"Shelly's birthday", 
"1611": "Manisha's Birthday",
"1701":"MLH day 7"}
curr= datetime.datetime.now()
today=str(curr.day)+str(curr.month)
while True:
    if today in data.keys():
        toast(data[today])

