# Event Coordinator

You are starting up your own event coordination business and want to create a Python application using generators to help manage your events.

This project will help you practice and further master the use of generators by managing and coordinating customer events for your business.

## Data
A guestlist of names and their ages are provided in the file `guest_list.txt`

## Goals:
- define generator function that will yield each read line so that each guest name is yielded each time for the generator,
- add a guest,
- find out which guests are aged 21 and over, 
- create 3 separate generator functions, one for each table, that will yield tuples of ("Food Name", "Table X", "Seat Y") for each of the 5 seats at each table, 
- assign a table and seat number with meal selection to each guest.