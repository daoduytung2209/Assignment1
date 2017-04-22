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
            print(menu)

        elif user_input == "C":
            if len(list_completed_items) == 0:
                print("No completed items")
            else:
                print("Completed items:")
            print(menu)
