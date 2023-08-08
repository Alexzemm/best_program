import subprocess

file = open("haha.txt", mode="r")

Call_URL = file.readline()
mycmd = r'start chrome /new-tab {}'.format(Call_URL)
subprocess.Popen(mycmd,shell = True) 
