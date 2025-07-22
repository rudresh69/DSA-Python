CustomerID = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
search = int(input("Enter the CustomerID to search: "))
flag = 0

for i in CustomerID:
    if i == search:
        flag = 1
        break
    else:
        flag = 0

if flag == 1:
    print(f"CustomerID {search} found.")
else:
    print(f"CustomerID {search} not found.")
