nums = tuple(map(int,input("Enter Numbers:").split()))

even = tuple(n for n in nums if n%2==0)
odd = tuple(n for n in nums if n%2!=0)

print("Even:",even)
print("Odd:",odd)
