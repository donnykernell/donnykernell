

from calendar_1 import Event, ListEventsStrategy, IcalendarStrategy
from menu import Menu, MenuCommand, ExitCommand


class NewEventCommand(MenuCommand):
    def execute(self):
        Event.add(self)
        print("Current number of events: "+str(len(Event.list_of_events)))
        print("\n")
    def description(self):
        return "New Event"


class ListEvents(MenuCommand):
    def execute(self):
        ListEventsStrategy().list_calendar()

    def description(self):
        return "List Events in Text"


class Icalendar(MenuCommand):
    def execute(self):
        IcalendarStrategy().list_calendar()

    def description(self):
        return "List Events in iCalendar"


def main():
    menu = Menu()
    menu.register(NewEventCommand())
    menu.register(ListEvents())
    menu.register(Icalendar())
    menu.register(ExitCommand(menu))

    menu.run()


if __name__ == "__main__":
    main()