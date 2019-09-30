# Website_Blocker

Python Script To Block List Of Website For Particular Amount Of Time
Change The Path Form Hosts To Path Of Your Hosts File.

# Scheduling a Python program on a Windows Computer

Chnage File Extension To pyw (blocker.py to blocker.pyw)

Open the Control Panel and then click on the Administrative Tools

Double-click on the Task Scheduler, and then choose the option ‘Create Basic Task…'

Type a name for your task and then press Next

Choose to start the task ‘Daily’ since we wish to run the Python script daily

Browse to find the pyw.

Done..



# Scheduling a Python program on a 24/7 server

We Can't Keep our computer for 24/7,and it is not practical, so if you want to execute a Python script at a particular time every day, you probably need a computer that is on all the time.

PythonAnywhere gives you access to such a computer and you can upload a Python script there and schedule it to run at a certain time every day. This can be useful when you want for example to extract some values (e.g. weather data)Â from a website and generate a text file with the value or other reports every day.

To schedule Python script for execution on PythonAnywhere please follow the simple steps below:

Sign up for a free account at https://www.pythonanywhere.com and then login.

Go to your Dashboard and then to Files and then to the Upload a File button and upload the Python file you want to schedule for execution.

Go to Tasks and set the time (UTC) of the day that you want your script to be executed and type in the name of the Python file you uploaded (e.g. myscript.py).

Click the Create button and you're done.

Now Your Python file will execute every day at the time given by you.
