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
