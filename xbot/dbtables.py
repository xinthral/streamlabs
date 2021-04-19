from xsql import Database
"""
Handy Suite Console Scripts to interact with the database
"""
def menu():
    """ Display Menu Items """
    menu = [[1, 'Display an item in more readable formats'],
    [2, 'Enable / Disable an item'],
    [3, 'Change category of item']]
    print("User Menu:")
    for _ in menu:
        print(" {:2} :: {}".format(_[0], _[1]))

def displayItem(item_id, table):
    """ Given a database tuple response, outputs formatted for readability """
    divider = "\t..::--== ==--::.."
    item = Database.queryTableID(item_id, table)
    print(divider)
    print("{:8}: {}".format("Visible", ('Yes' if str(item[3]) == '0' else 'No')))
    print("{:8}: {}".format("Category", item[2]))
    count = 1
    for line in item[1].split(Database._delim):
        print("Line {} :: {}".format(count, line))
        count += 1
    print(divider)
    pause()

def displayTable(query):
    """ Given a table name, print out formatted contents """
    print 'Database output begins...'
    print("{:4} || {:3} || {:16} || {}".format('ID', 'Off', 'Category', 'Content'))
    for element in Database.queryTableAll(query):
        print("{:4} || {:3} || {:16} || {}".format(element[0], element[3], element[2], element[1]))
    print 'Database output complete...'

def flipVisibility(item_id, table):
    """ Change the visibility boolean in the database """
    current = Database.queryTableID(item_id, table)
    flipped = 1 if str(current[3]) == '0' else 0
    # table, column, value, pid
    Database.updateVisibility((table, 'isBlocked', int(flipped), int(item_id)))
    pause()

def inspectItem(item_id, table):
    """ Given a table name, cycle through item id's """
    repeat = True
    while(repeat):
        menu()
        choice = raw_input('Choose an option: (q to quit): ')
        user_input = choice.strip()
        if user_input == '1':
            displayItem(item_id, table)
        elif user_input == '2':
            flipVisibility(item_id, table)
        elif user_input == '3':
            pass
        else:
            repeat = False

def inspectTable(table):
    """ Given a table name, setup to manipulate table """
    displayTable(table)
    domain = [str(x[0]) for x in Database.queryTableAll(table)]
    repeat = True
    while (repeat):
        item_id = raw_input("What is the item ID you would like to inspect? (q to quit): ")
        if str(item_id) in domain:
            inspectItem(item_id, table)
        else:
            repeat = False

def pause():
    paused = raw_input("Press Enter to continue...")

def main():
    """ Initialize Logic """
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
