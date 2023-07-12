

"""
Youtube Piano Player by Zoda
"""
_config={
"piano": "https://youtu.be/3gZC5763wYk",
"author":"Zoda",
"version":"0.0.1"
}

#Libs
#from pyautogui import press
import sys
import webbrowser
import os

#Player class
class Player:
	def __init__(self,notes):
		self.notes=notes
		self.play()

	def play(self):
		for i in len(range(len(self.notes.splitlines()))):
			print(self.notes.splitlines()[i])

class Commands:
	def __init__(self,command,*args):
		self.command=command
		self.commands={
"play": self.play
}
		self.args=args
		if self.command in self.commands:
			if self.commands[self.command].__code__.co_argcount != 1:
				self.commands[self.command](*self.args)
			else:
				self.commands[self.command]()
		else:
			print("command not found")
	def play(self,args):
		if args[1] == "file":
			if len(args) != 3:
				print("3 argument required not:"+str(len(args)))
				sys.exit()
			if os.path.isfile(args[2]):
				with open(args[2]) as f:
					content=f.read()
					Player(content)
			else:
				print("its not a file or file not found")

if len(sys.argv)<2:
	print("A argument required")
else:
	Commands(sys.argv[1],sys.argv[1:])
