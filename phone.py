import time
import datetime


class Phone:
    def __init__(self, status="Closed", app_list=["Settings", "Store", "Notes", "Calculator"], volume=0, brightness=0,
                 battery=100):

        time.sleep(3)
        self.status = status
        self.app_list = app_list
        self.volume = volume
        self.brightness = brightness
        self.battery = battery

    def open(self):
        print("Opening")
        time.sleep(2)
        print("Phone Opened")
        self.status = "Opened"

    def close(self):
        print("Closing 3")
        time.sleep(1)
        print("Closing 2")
        time.sleep(1)
        print("Closing 1")
        time.sleep(1)
        print("Closed")
        self.status = "Closed"

    def app(self, new_app):
        self.app_list.append(new_app)

    def show_app(self):
        for app in range(0, len(self.app_list)):
            print("Apps : " + self.app_list[app])

    def show_battery(self):
        status = self.battery
        print(status)

    def take_note(self, note):
        time_note = datetime.datetime.now().strftime("%d-%m-%Y")
        file = open(time_note + ".txt", "a")
        file.write(note + "\n")
        file.close()

    def read_note(self):
        note = input("Date : ")
        try:
            file = open(note + ".txt", "r")
            for nt in file:
                print(nt, end="")
        except Exception as e:
            print("Oops! ", e.__class__)
            print("You do not have note")

    def settings(self):
        ch = input("Voice : 1, brightness : 2, System Info : 3 --> : ")
        if ch == "3":
            print("""
                              Brand = SAMSUNG XX
                              Year : 2020
                              Android : 9.0
                              Camera : 32/5.1    
                              Battery : 4500    
                              Storage : 16 GB     
                              RAM : 5""")
        elif ch == "2":
            while 1:
                ch_two = input("Brightness Press + to increase + - to decrease brightness, q to exit : ")
                if ch_two == "+":
                    if self.brightness != 50:
                        self.brightness += 2
                        print(f" Level {self.brightness}")
                elif ch_two == "-":
                    if self.brightness != 0:
                        self.brightness -= 2
                        print(f" Level {self.brightness}")
                elif ch_two == "q":
                    print(f" Level {self.brightness}")
                    break
        elif ch == "1":
            while True:
                ch_three = input("Volume Press  to up + ,- to decrease volume, q to exit : ")
                if ch_three == "+":
                    if self.volume != 32:
                        self.volume += 2
                        print(f" Level {self.volume}")
                elif ch_three == "-":
                    if self.volume != 0:
                        self.volume -= 2
                        print(f" Level {self.volume}")
                elif ch_three == "q":
                    print(f" Level {self.volume}")
                    break


phone = Phone()
print("""
             ****************
             Your Choice :
            [1]-Open The Phone :
            [2]-Close The Phone:
            [3]-App List:
            [4]-Take Note:
            [5]-Get Notes:
            [6]-Settings;
            [7]-Add App :
            [8]-Battery Status :
            [q]-Exit:
            ******************""")

while 1:

    choice = input("Your Choice : ")
    if choice == "q":
        print("Working...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        break
    elif choice == "1":
        phone.open()
    elif choice == "2":
        phone.close()
    elif choice == "3":
        phone.show_app()
    elif choice == "4":
        notes = input("Start Write : ")
        phone.take_note(notes)
    elif choice == "5":
        phone.read_note()
    elif choice == "6":
        phone.settings()
    elif choice == "7":
        add = input("Add Apps : ")
        new = add.split(",")
        for i in new:
            phone.app(i)
        time.sleep(2)
        print("Done !")
    elif choice == "8":
        phone.show_battery()
