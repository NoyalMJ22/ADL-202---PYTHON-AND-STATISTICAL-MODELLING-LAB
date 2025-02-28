s=input("Enter a string")
print("# Using for loop")

for char in s:
    print(char,end=" ")
print("\n# Using range")
for i in  range(len(s)):
    print(s[i])
print("\n# Using enumerate")

for index,char in enumerate(s):
    print(index,char)
