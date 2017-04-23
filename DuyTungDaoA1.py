"""
Name: Dao Duy Tung
Date: 21/4/2017
Brief program details: This program is a simple shopping list that could
also be used for TODO lists or similar purposes.
The program maintains a list of items in a file, and each item has:
•	name, price, priority (1, 2 or 3), whether it is required or completed
Users can choose to see the list of required items or completed items, including a total of the (estimated) price of
all of those items. The lists will be sorted by priority.
Users can add new items and mark items as completed.
They cannot change items from completed to required.
Github project link: https://github.com/daoduytung2209/A1
"""


from operator import itemgetter


"""
Pseudocode for load_items function:
- Open items.csv and read the content
- Initialize for loop that accesses each line in the file
- Replace "\n" by "" in each line
- Split each line in the file by the comma and add to list_data
- Close the file
- Return list_data
"""


def load_items(filename):  # Load the items.csv file and store the result in list_data to pass to any functions that
    # need access to it
    list_data = []  # List of spilt data from the file
    input_file = open(filename, "r")  # Open the file to read the content inside
    for each in input_file:
        if "\n" in each:
            each = each.replace("\n", "")  # Replace "\n" by "" in each line
        split_data = each.split(",")  # Split each line in the file by the comma
        list_data.append(split_data)
    input_file.close()  # Close the file
    return list_data


def print_items(list_items):  # Print the list of items as the sample output with name, price and priority
    list_items.sort(key=itemgetter(2))  # Sort the list by priority
    item_names = []  # List of item's names
    item_prices = []  # List of item's prices
    item_priorities = []  # List of item's priorities

    for each in list_items:
        item_names.append(each[0])  # Add item names to item_names list
        item_prices.append(float(each[1]))  # Add item prices to item_prices list
        item_priorities.append(each[2])  # Add item priorities to item_priorities list

    for i in range(0, len(list_items)):
        print("{}. {:<25}${:.2f} ({})".format(i, item_names[i], item_prices[i], item_priorities[i]))  # Print the list
        # of items by access each element in item_names, item_prices, item_priorities list with the string format
    print("Total expected price for {} items: ${:.2f}".format(len(list_items), sum(item_prices)))  # Print the total
    # price for the total amount of items


"""
Pseudocode for complete_an_item function:
- Display the list of required items
- Prompt user to enter the number of a required item to mark as completed
- Error-check whether the input entered is out of the item's range or not
- Display the name of the item which is marked as completed
- Initialize the for loop to change the status of the item from required "r" to completed "c" if the number user entered
- is the index of a required item
- Display Menu
"""


def complete_an_item(final_list_items, list_completed_items, list_required_items):  # Do the mark an item as completed
    # feature that allow the user to choose one item, and change that item from required to completed
    print_items(list_required_items)  # Call print_items function with list_required_items as parameter
    print("Enter the number of an item to mark as completed")

    valid_number = False
    while not valid_number:  # Error-check user inputs for the value error of input number
        try:
            item_number = int(input())
            while item_number not in range(0, len(list_required_items)):  # Error-check user inputs if the input is out
                # of item's range
                print("Invalid item number")
                item_number = int(input())
            valid_number = True
        except ValueError:
            print("Invalid input; enter a number")

    print("{} marked as completed".format(list_required_items[item_number][0]))  # Print the name of an item
    # corresponding to the index of an item

    for i in range(len(final_list_items)):
        list_required_items[item_number][3] = 'c'  # Replace "r" with "c" as from required item to completed item
        if list_required_items[item_number][1] in final_list_items[i]:
            final_list_items[i] = list_required_items[item_number]  # Replace the item in final list items by the item
            # which is chosen by user with 'c' in the end

    list_completed_items.append(list_required_items[item_number])  # Add the item which is marked as completed to the
    # completed list items
    list_required_items.remove(list_required_items[item_number])  # Remove the item which is marked as completed from
    # the required list items
    print("""Menu:
R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit""")


def main():
    list_required_items = load_items("items.csv")  # List of required items
    list_required_items.sort(key=itemgetter(2))  # Sort the list required items by priority
    list_completed_items = []  # List of completed items
    final_list_items = load_items("items.csv")  # List of total amount of items
    print("""Shopping list 1.0 - by Dao Duy Tung
{} items loaded from items.csv""".format(len(list_required_items)))  # Print total amount of items in items.csv file
    menu = """Menu:
R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit"""
    print(menu)
    user_input = input(">>>").upper().strip()  # Handle uppercase and lowercase letters for user inputs
    while user_input != "Q":
        if user_input == "R":
            if len(list_required_items) == 0:  # Display the prompt if there are no required items left
                print("No required items")
            else:
                print("Required items:")
                print_items(list_required_items)  # Call print_items function with list_required_items as parameter
            print(menu)

        elif user_input == "C":
            if len(list_completed_items) == 0:  # Display the prompt if there are no required items have been marked as
                # completed yet
                print("No completed items")
            else:
                print("Completed items:")
                print_items(list_completed_items)  # Call print_items function with list_completed_items as parameter
            print(menu)

        elif user_input == "A":
            new_items = []  # List of added items
            input_name = input("Item name: ").strip()
            while input_name.strip() == "":  # Error-check user inputs for the name of new item if user entered blank
                # space
                print("Input can not be blank")
                input_name = input("Item name: ").strip()

            valid_price = False
            while not valid_price:  # Error-check user inputs for the value error of the input price
                try:
                    input_price = float(input("Price: $"))
                    while input_price < 0:  # Error-check user inputs if the inputs price are less than 0
                        print("Price must be >= $0")
                        input_price = float(input("Price: $"))
                    valid_price = True
                except ValueError:
                    print("Invalid input; enter a valid number")

            valid_priority = False
            while not valid_priority:  # Error-check user inputs for the value error of the input priority
                try:
                    input_priority = int(input("Priority: "))
                    while input_priority not in range(1, 4):  # Error-check user inputs if the inputs price are not 1
                        # or 2 or 3
                        print("Priority must be 1, 2 or 3")
                        input_priority = int(input("Priority: "))
                    valid_priority = True
                except ValueError:
                    print("Invalid input; enter a valid number")

            print("{}, ${:.2f} (priority {}) added to shopping list".format(input_name, input_price, input_priority))
            # Print the added item with its name, price and priority
            new_items.append(input_name)  # Add the input name to the new items lists
            new_items.append(str(input_price))  # Add the input price to the new items lists
            new_items.append(str(input_priority))  # Add the input priority to the new items lists
            new_items.append('r')  # Add the 'r' to the new items lists as required item
            list_required_items.append(new_items)  # Add the new item to the required list items
            final_list_items.append(new_items)  # Add the new item to the final list items to write in the items.csv
            # file
            print(menu)

        elif user_input == "M":
            if len(list_required_items) == 0:  # Display the prompt if there are no required items left
                print("No required items")
                print(menu)
            else:
                complete_an_item(final_list_items, list_completed_items, list_required_items)  # Call the
                # complete an item fuction

        else:  # Error-check for user input if they enter the value out of the menu's index
            print("Invalid menu choice")
            print(menu)
        user_input = input(">>>").upper().strip()  # Handle uppercase and lowercase letters

    output_file = open("items.csv", "w")  # Open the file to write in additional content
    for each in final_list_items:
        output_file.write(
            "{},{},{},{}\n".format(each[0], each[1], each[2], each[3]))  # Rewrite the items.csv file with
        # 'c' in the end of each item as a completed items
    output_file.close()  # Close the file

    print("{} items saved to items.csv".format(len(final_list_items)))  # Print total amount of items saved to
    # items.csv file
    print("Have a nice day :)")
main()