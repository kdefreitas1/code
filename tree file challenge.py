alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# asks user for file name and puts in data and formatas
def read_file():
    which_file = input("What file would you like to use: ")# asks for file
    data = [] #empty list to store file data
    file = open(which_file)
    
    # for loop goes through each line and formats it and adds to data list
    for line in file:
        line = line.split("-")
        for i in range(len(line)):
            line[i] = line[i].strip()
        data.append(line)
        
    return data

# assigns read_file function to tree data var
tree_data = read_file()
"""
this finds the super tall trees returns names seperated and uppercase
it also returns the height of each tree
and returns the names of each tree not seperated
"""
def find_super_tall():
    tree_list = [] # empty list to store tree names
    tree_list_nums = []# empty list to store tree height
    
    """
    for loop goes through each tree to check if height requirements work
    it also checks if the name of the tree works
    """
    for tree in tree_data:
        # checks if > 30 and < 80
        if float(tree[1]) > 30 and float(tree[1]) < 80:
            # check to make sure name doesnt exceed one word
            if len(tree[0].split()) > 1:
                continue
            # adds tree name uppercased to list
            tree_list.append(tree[0].upper())
            # adds the height of tree to list
            tree_list_nums.append(float(tree[1]))
    #puts the list into a string and then into a list seperating each letter with space between words
    tree_string = list((" ").join(tree_list))
    
    return tree_string, tree_list_nums, tree_list
"""
this turns the alphabet into a dictionary and assigns all letters a num
then goes through super tall function and gives all the letters values and each words is in seperate lists
then goes through the list of num of the words in each lists and find the highest num and assigns var the name of that tree
returns name of the best tree
""" 
def tree_name_sum():
    alphabet_list = list(alphabet)# turns alphabet into a list with each letter split apart
    letter_value = {} # empty dict so it can be added to later
    tree_letter_value = [[]]# list of lists so each tree value can be seperated
    counter = 0 #counter for changing which list its the 2nd for loop
                # and is a counter for the last for loop to find the best sum
    best_tree_name = ""#empty string to be cahnged later for best tree name
    
    # goes through letter in the alphabet list and assigns it a number
    for letter in alphabet_list:
        letter_value[letter] = alphabet_list.index(letter) + 1
    
    # goes through the find super tall function and adds the letters value to a list of lists
    for item in find_super_tall()[0]:
        # if the letter is a space it adds new list in list and changes the counter
        if item == " ":
            tree_letter_value.append([])# adds another list to tree value list of lists
            counter += 1 # adds 1 to counter so when adding it adds to new list in list
            continue
        #goes through each letter add the value from the dict to the list
        tree_letter_value[counter].append(letter_value[item])
        
    counter = 0 # resets counter to be used in for loop
    
    """
    for loop goes through each of the lists and its values add the sum and height together
    stores the tree with the highest num in counter
    best tree name stores the name of the best tree
    """
    for i in range(len(tree_letter_value)):
        #replaces the list of lists with sum of num and height of tree
        tree_letter_value[i] = sum(tree_letter_value[i]) + find_super_tall()[1][i]
        # this checks if the best tree num is less than current tree num ignores if it is
        if counter < tree_letter_value[i]:
            #if it is higher changes counter to be that value and adds the name to the best tree var
            counter, best_tree_name = tree_letter_value[i], find_super_tall()[2][i]
        else: 
            pass
        
    return best_tree_name.capitalize()

# prints out best tree from given file from user
print(tree_name_sum())