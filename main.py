from tkinter import *
import sys
import webbrowser

class App:        
    def get_name_pass_label(self):
        usernameLabel = Label(self.root, text="Username").grid(row=0, column=0)
        self.username = StringVar()
        usernameEntry = Entry(self.root, textvariable=self.username).grid(row=0, column=1)  

        #password label and password entry box
        passwordLabel = Label(self.root,text="Password").grid(row=1, column=0)  
        self.password = StringVar()
        passwordEntry = Entry(self.root, textvariable=self.password, show='*').grid(row=1, column=1)
        auth = {
        "login": self.username,
        "password": self.password
        }
        return auth

    def download_git(self):
        pass
    def __init__(self):
        self.root = Tk()
        self.root.title("Source Control")
        self.root.geometry("600x600")
        auth_data = self.get_name_pass_label()
        self.root.mainloop()

    
class git(App):
    def __init__(self, params=None):
        pass
    def clone(self, params=None):
        pass
    def add(self, params=None):
        pass
    def commit(self, params=None):
        pass
    def push(self, params=None):
        pass
    def pull(self, params=None):
        pass
    def checkout(self, params=None):
        pass
    def branch(self, params=None):
        pass
    def merge(self, params=None):
        pass




def main():
    app = App()

main()
