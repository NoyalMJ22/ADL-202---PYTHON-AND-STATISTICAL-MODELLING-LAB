lst=list(map(int,input("Enter the numbers: ").split()))

print("list: ",lst)

lst.append(int(input("Enter a number to append: ")))
print("List after append:", lst)

position = int(input("Enter position to insert: "))
value = int(input("Enter value to insert: "))
lst.insert(position, value)
print("List after insert:", lst)

num = int(input("Enter value to remove: "))
if num in lst:
    lst.remove(num)
    print("List after remove:", lst)
else:
    print(f"{num} not found in the list.")

print("\nSorting the list in descending order:")
lst.sort()
lst.reverse()
print("Sorted list:", lst)
