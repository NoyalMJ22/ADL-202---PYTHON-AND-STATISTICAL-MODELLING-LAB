
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

with open("untitled.txt", "r") as file:
    text = file.read()
    print("Components of the file:\n",text,"\nPrime Numbers:")
    for number in text.split():
        if is_prime(int(number)):
            print(number)
