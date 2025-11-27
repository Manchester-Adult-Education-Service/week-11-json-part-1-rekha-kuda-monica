# -------------------------------------------
# Exercise 1: Book Inventory System (JSON Edition)
# -------------------------------------------
# In this exercise, we are going to build a "Book Inventory System".
# Previously, we typed our data manually into lists inside the code.
# Real-world programmes usually read data from external files.
#
# We will use a JSON file ('books.json') which acts like a database.
#
# Key Concepts to practise:
# - Importing Libraries (json)
# - File Handling (open, load)
# - Lists of Dictionaries
# - Loops (for, while)
# - Conditionals (if, elif, else)
# - Arithmetic & Comparison Operators
#
# IMPORTANT:
# Ensure you have the 'books.json' file in the SAME folder as this exercise
# before you start!
# -------------------------------------------
# GROUP INSTRUCTIONS
# -------------------------------------------
# Work in groups of 2–3. Share the same GitHub repository.
# Roles:
# - One learner acts as the DRIVER (types the code and runs commands).
# - The other learners are NAVIGATORS (observe, guide, and provide suggestions).
#
# After each task:
# - Current learner: git add, commit, and push
# - Next learner: git pull origin main
# -------------------------------------------


import json  # We need this tool to read the external file

# -------------------------------------------
# Task 1: Loading the Data
# -------------------------------------------
# We need to read the 'books.json' file and store the data
# into a variable so we can use it in our programme.
#
# TODO:
# 1. Use the 'with open...' statement to open 'books.json' in 'r' (read) mode.
# 2. Inside the with block, use json.load() to read the file into a variable called 'library'.
# 3. Print the 'library' variable to check that the data loaded correctly.
#
# HINT:
# with open('filename.json', 'r') as file:
#     variable_name = json.load(file)
#
# Write your code below:
with open('books.json', 'r') as file:
    libray_name = json.load(file)
    print(libray_name)



# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your code. You should see a list of book dictionaries print to the console.
# If you get a "FileNotFoundError", check that books.json is in the correct folder.
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with an appropriate message.
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# -------------------------------------------
# Task 2: Building the Main Menu Loop
# -------------------------------------------
# We want the user to be able to choose different actions.
# We need a menu that keeps showing up until the user wants to leave.
#
# TODO:
# 1. Initialise (create) a variable 'choice' to an empty string or "0".
# 2. Create a WHILE loop that runs as long as 'choice' is NOT equal to "3".
# 3. Inside the loop:
#    a. Print the title "--- BOOK INVENTORY ---"
#    b. Print options: "1. View All Books", "2. Search for Book", "3. Exit"
#    c. Ask the user for input and save it to 'choice'.
#    d. Add an IF statement checking if choice is "3". If so, print "Goodbye!".
#    e. Add an ELSE clause to print "Invalid choice" (we will add real features later).
#
# Write your code below:
# NOTE: This loop will become the "home" for all your future code!




# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your code.
# - Can you see the menu?
# - Does it repeat if you type "1" or "2"?
# - Does it stop when you type "3"?
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit.
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# -------------------------------------------
# Task 3: Viewing All Books
# -------------------------------------------
# Now let's make Option 1 work.
#
# ACTION REQUIRED:
# Do NOT create a new loop below.
# Go back UP to your code in Task 2. You will edit the loop you already made.
#
# TODO:
# 1. Inside your Task 2 loop, find where you check 'choice'.
# 2. Add a new condition: if choice == "1":
# 3. Inside this block, create a FOR loop to go through each 'book' in the 'library' list.
# 4. For each book, print the details in a nice format using f-strings.
#    e.g. "Title: [title] | Author: [author] | Stock: [stock]"
# 5. Ensure your "Invalid choice" logic is now an 'else' at the very end.
#
# (Modify the code in Task 2 - Do not write new code here)
# -------------------------------------------


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your code. Select option 1.
# Do you see all 5 books from the JSON file listed neatly?
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage.
# 2. Commit.
# 3. Push.
# The next learner must pull before continuing.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# If you have completed the tasks above, try these extensions to
# really test your skills!
# -------------------------------------------

# Extension 1: Search Functionality
# -------------------------------------------
# Make Option 2 work.
#
# ACTION REQUIRED:
# Scroll back UP to your main loop in Task 2.
#
# TODO:
# 1. Add to your if/else chain: elif choice == "2":
# 2. Ask the user for a search term (e.g. "Enter book title to find: ").
# 3. Create a boolean variable 'found' and set it to False.
# 4. Loop through the 'library' list.
# 5. Check IF the search term is in the book's title.
#    (Tip: Use .lower() on both the input and the title to make it not case-sensitive).
# 6. If found, print the book details and set 'found' to True.
# 7. After the loop, check IF 'found' is still False. If so, print "Book not found."
#
# (Modify the code in Task 2 - Do not write new code here)
# -------------------------------------------


# Extension 2: Inventory Value Calculation
# -------------------------------------------
# Let's practise arithmetic. We want to know the total value of all books in stock.
# Formula: (Price * Stock) for each book, added together.
#
# ACTION REQUIRED:
# Scroll back UP to your main loop in Task 2.
#
# TODO:
# 1. Add a new menu option in your print statements: "4. Calculate Total Inventory Value".
# 2. Update the exit choice to be "5" (Remember to update the while condition too!).
# 3. Add: elif choice == "4":
#    a. Create a variable 'total_value' = 0.
#    b. Loop through the library.
#    c. Multiply price * stock for that book, and add it to 'total_value'.
#    d. Print the final result formatted as currency (e.g. £1234.50).
#
# (Modify the code in Task 2 - Do not write new code here)
# -------------------------------------------


# Extension 3: Saving Data (Writing JSON)
# -------------------------------------------
# This is advanced! Let's allow users to Add a new book and SAVE it to the file.
#
# ACTION REQUIRED:
# Scroll back UP to your main loop in Task 2.
#
# TODO:
# 1. Add a new menu option "5. Add New Book" (Exit is now 6).
# 2. Get inputs for Title, Author, Genre, Price (float), and Stock (int).
# 3. Create a new dictionary with these values.
# 4. Append this dictionary to your 'library' list.
# 5. KEY STEP: Write the updated list back to the file.
#    with open('books.json', 'w') as file:
#        json.dump(library, file, indent=4)
#
# (Modify the code in Task 2 - Do not write new code here)
# -------------------------------------------


# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Use Git to:
# 1. Stage your final changes.
# 2. Commit with an appropriate message (e.g. "Completed extension activity").
# 3. Push your final version to the repository.
# -------------------------------------------