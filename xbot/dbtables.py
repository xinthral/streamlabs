from xsql import Database
"""
Handy Suite Console Scripts to interact with the database
"""
def displayMenu():
    menu = [[1, 'Display an item in more readable formats'],
    [2, 'Enable / Disable an item'],
    [3, 'Change category of item']]
    print("User Menu:\n")
    for _ in menu:
        print("\t{:2} :: {}".format(_[0], _[1]))

def displayTable(query):
    print 'Database output begins...'
    print("{:4} || {:3} || {:16} || {}".format('ID', 'Off', 'Category', 'Content'))
    for element in Database.queryTableAll(query):
        print("{:4} || {:3} || {:16} || {}".format(element[0], 1 if element[3] == 0 else 0, element[2], element[1]))
    print 'Database output complete...'

def inspectTable(user_input):
        user_input = raw_input("{}\nWhich table would you like to inspect?:".format(Database._tables))
        if user_input == 'f':
            displayTable('facts')
        elif user_input == 'j':
            displayTable('jokes')
        elif user_input == 'p':
            displayTable('phrases')
        elif user_input == 'r':
            displayTable('rather')
        else:
            pass

def main():
    repeat = True
    while (repeat):
        displayMenu()
        choice = raw_input('Choose an option: (q to quit): ')
        user_input = choice[0].lower()
        if user_input == '1':
            inpsectTable()
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        else:
            repeat = False

if __name__ == '__main__':
    main()
