
# this program does .. runs loop.. if n is in the list..it continues or skips , then goes to next statement and prints
#doesnt stop entire loop like BREAK

numbersTaken = [2,5,12,13,17]

print('here a numbers still available ')

for n in range (1,20):
    if n in numbersTaken:
        continue
    print(n)