from xsql import Database
"""
Handy Suite Console Scripts to interact with the database
"""
def menu():
    menu = [[1, 'Display an item in more readable formats'],
    [2, 'Enable / Disable an item'],
    [3, 'Change category of item']]
    print("User Menu:")
    for _ in menu:
        print(" {:2} :: {}".format(_[0], _[1]))

def displayTable(query):
    print 'Database output begins...'
    print("{:4} || {:3} || {:16} || {}".format('ID', 'Off', 'Category', 'Content'))
    for element in Database.queryTableAll(query):
        print("{:4} || {:3} || {:16} || {}".format(element[0], element[3], element[2], element[1]))
    print 'Database output complete...'
    # paused = raw_input('Press Enter to continue...')

def inspectTable(table):
    displayTable(table)

    repeat = True
    while (repeat):
        menu()
        choice = raw_input('Choose an option: (q to quit): ')
        user_input = choice.strip()
        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        else:
            repeat = False

def main():
    repeat = True
    while (repeat):
        table = None
        user_input = raw_input("{}\nWhich table would you like to inspect? (q to quit): ".format(Database._tables))
        choice = user_input[0].lower()
        if choice == 'f':
            inspectTable('facts')
        elif choice == 'j':
            inspectTable('jokes')
        elif choice == 'p':
            inspectTable('phrases')
        elif choice == 'r':
            inspectTable('rather')
        else:
            repeat = False

if __name__ == '__main__':
    main()
