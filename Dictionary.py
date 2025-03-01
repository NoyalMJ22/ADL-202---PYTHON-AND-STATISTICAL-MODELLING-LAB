#Creating a Dictionary
books = {"The Great Gatsby":10,"1984":15,"To Kill a Mockingbird":8}
print("The Dictionary\n",books)

#Accessing the value of 1984
print("\nStock for '1984':", books.get("1984", "Book not found"))

#Updating the Key Value Pair
books.update({"The Catcher in the Rye": 12, "1984": 20})

#Printing the updated file
print("\nUpdated Dictionary:\n",books)

#Deleting a Key Value Pair
books.pop("To Kill a Mockingbird")

#Displaying the Dictionary After Deleting a key value pair
print("\nUpdated Dictionary after poping a Value:", books)

#Checking if the book exists
print("\n'The Great Gatsby' exists:" if "The Great Gatsby" in books else "Does not exist")

#Displaying all the keys
print("\nAll book titles:", list(books.keys()))

#Finding the length of the Dictionary
print("\nNumber of books:", len(books))

#Updating and adding 2 more Key value pairs
books.update({"Pride and Prejudice": 5, "Moby Dick": 7})

#Displaying the final dictionary
print("\nFinal Dictionary:", books)
