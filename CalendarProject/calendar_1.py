import datetime


class Event:
    list_of_events = []

    def __init__(self, name, date, time):
        self.nam = name
        self.dat = date
        self.tim = time

    def add(self):
        self.nam = input("Title?: ")
        for _ in range(len(self.name)):
            if ord(self.name[_]) in range(48, 58) or ord(self.name[_]) in range(97, 123) or \
                ord(self.name[_]) in range(65,
                                                                                                                    91) \
                    or ord(self.name[_]) in range(44, 47) or ord(self.name[_]) == 32:
                continue
            else:
                print("Invalid input!")

        self.date = input("Date?(DD.MM.YYYY): ")

        dy, mt, yr = self.date.strip().split(".")
        if len(dy) < 2 or len(mt) < 2 or len(yr) < 4:
            print("Invalid input")
            return
        try:
            datetime.datetime(int(yr), int(mt), int(dy))
        except ValueError:
            print("Invalid input!")
            return
        self.time = input("Time?(HH:MM): ")
        hh, mm = self.tim.strip().split(":")
        if int(hh) < 0 or int(hh) > 24 or len(hh) < 2:
            print("Invalid input!")
            return
        if int(mm) < 0 or int(mm) >= 60 or len(mm) < 2:
            print("Invalid input!")
            return

        ev =  self.name + " " + self.date + " " + self.time
        Event.list_of_events.append(ev)

    def __str__(self):
        return "\nTytuł: " + self.name + "\n" + "Data: " + self.date + " " + self.time + "\n"


class ListingStrategy():
    def list_calendar(self):
        pass


class ListEventsStrategy(ListingStrategy):
    def list_calendar(self):
        for i in range(len(Event.list_of_events)):
            spl = Event.list_of_events[i].split(" ")
            print("\nTitle: " + spl[0] + "\nDate: " + spl[1] + "\nTime: " + spl[2])


class IcalendarStrategy(ListingStrategy):

    def list_calendar(self):
        head = "\nBEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VTIMEZONE\nTZID:Europe/Warsaw\nX-LIC-LOCATION:Europe\
            /Warsaw\nEND:VTIMEZONE\n"
        tail = "\nEND:VCALENDAR"

        for i in range(len(Event.list_of_events)):
            spl = Event.list_of_events[i].split(" ")
            d, m, y = spl[1].split(".")
            hh,mm = spl[2].split(":")
            print(head + "BEGIN:VEVENT\nDTSTART:"+y+m+d+"T"+hh+mm+"00\nDTEND:"+y+m+d+"T"+hh+mm+"00\nSUMMARY:"\
                + spl[0]+"\nEND:VEVENT" + tail)
