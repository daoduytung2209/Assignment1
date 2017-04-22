# Name: Dao Duy Tung
# Date: 21/4/2017
# Brief program details: This program is a simple shopping list that could
# also be used for TODO lists or similar purposes.
# The program maintains a list of items in a file, and each item has:
# •	name, price, priority (1, 2 or 3), whether it is required or completed
# Users can choose to see the list of required items or completed items, including a total of the (estimated) price of
# all of those items. The lists will be sorted by priority.
# Users can add new items and mark items as completed.
# They cannot change items from completed to required.
# Github project link: https://github.com/daoduytung2209/A1


from operator import itemgetter


# Pseudocode for load_items function:
# Open items.csv and read the content
# Initialize for loop that accesses each line in the file
# Replace "\n" by "" in each line
# Split each line in the file by the comma and add to list_data
# Close the file
# Return list_data

def load_items(filename):
    list_data = []
    input_file = open(filename, "r")
    for each in input_file:
        if "\n" in each:
            each = each.replace("\n", "")
        split_data = each.split(",")
        list_data.append(split_data)
    input_file.close()
    return list_data


def print_items(list_items):
    list_items.sort(key=itemgetter(2))
    item_names = []
    item_prices = []
    item_priorities = []

    for each in list_items:
        item_names.append(each[0])
        item_prices.append(float(each[1]))
        item_priorities.append(each[2])

    for i in range(0, len(list_items)):
        print("{}. {:<25}${:.2f} ({})".format(i, item_names[i], item_prices[i], item_priorities[i]))
    print("Total expected price for {} items: ${:.2f}".format(len(list_items), sum(item_prices)))


# Pseudocode for complete_an_item function:
# Display the list of required items
# Prompt user to enter the number of a required item to mark as completed
# Error-check whether the input entered is out of the item's range or not
# Display the name of the item which is marked as completed
# Initialize the for loop to change the status of the item from required "r" to completed "c" if the number user entered
# is the index of a required item
# Display Menu

def complete_an_item(final_list_items, list_completed_items, list_required_items):
    print_items(list_required_items)
    print("Enter the number of an item to mark as completed")

    valid_number = False
    while not valid_number:
        try:
            item_number = int(input())
            while item_number not in range(0, len(list_required_items)):
                print("Invalid item number")
                item_number = int(input())
            valid_number = True
        except ValueError:
            print("Invalid input; enter a number")

    print("{} marked as completed".format(list_required_items[item_number][0]))

    for i in range(len(final_list_items)):
        list_required_items[item_number][3] = 'c'
        if list_required_items[item_number][1] in final_list_items[i]:
            final_list_items[i] = list_required_items[item_number]

    list_completed_items.append(list_required_items[item_number])
    list_required_items.remove(list_required_items[item_number])
    print("""Menu:
R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit
""")


def main():
    list_required_items = load_items("items.csv")
    list_required_items.sort(key=itemgetter(2))
    list_completed_items = []
    final_list_items = load_items("items.csv")
    print("""Shopping list 1.0 - by Dao Duy Tung
{} items loaded from items.csv""".format(len(list_required_items)))
    menu = """Menu:
R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit
"""
    print(menu)
    user_input = input().upper()
    while user_input != "Q":

        if user_input == "R":
            if len(list_required_items) == 0:
                print("No required items")
            else:
                print("Required items:")
                print_items(list_required_items)
            print(menu)

        elif user_input == "C":
            if len(list_completed_items) == 0:
                print("No completed items")
            else:
                print("Completed items:")
                print_items(list_completed_items)
            print(menu)

        elif user_input == "A":
            new_items = []
            input_name = input("Item name: ")
            while input_name == "":
                print("Input can not be blank")
                input_name = input("Item name: ")

            valid_price = False
            while not valid_price:
                try:
                    input_price = float(input("Price: $"))
                    while input_price < 0:
                        print("Price must be >= $0")
                        input_price = float(input("Price: $"))
                    valid_price = True
                except ValueError:
                    print("Invalid input; enter a valid number")

            valid_priority = False
            while not valid_priority:
                try:
                    input_priority = int(input("Priority: "))
                    while input_priority not in range(1, 4):
                        print("Priority must be 1, 2 or 3")
                        input_priority = int(input("Priority: "))
                    valid_priority = True
                except ValueError:
                    print("Invalid input; enter a valid number")

            print("{}, ${:.2f} (priority {}) added to shopping list".format(input_name, input_price, input_priority))

            new_items.append(input_name)
            new_items.append(str(input_price))
            new_items.append(str(input_priority))
            new_items.append('r')
            list_required_items.append(new_items)
            final_list_items.append(new_items)
            print(menu)

        elif user_input == "M":
            if len(list_required_items) == 0:
                print("No required items")
                print(menu)
            else:
                complete_an_item(final_list_items, list_completed_items, list_required_items)
        else:
            print("Invalid menu choice")
            print(menu)
        user_input = input().upper()