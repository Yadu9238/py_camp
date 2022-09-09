km = int(input("Enter distance travelled"))
amt = 1
while km > 0:
    amt = amt * (km%10)
    print(amt)
    km = km // 10
print(amt)