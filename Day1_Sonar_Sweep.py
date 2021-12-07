#create an array called depths. use the data provided
depths = [199, 200, 208, 210, 200, 207, 240, 269, 260,263]
#create a var called increases to track the number of increases. set it at zero
increases = 0
#iterate through each element in the array
for n in range(len(depths) -1):
    #if the next element is greater, add 1 to the number of increases
    if int(depths[n]) < int(depths[n+1]):
        increases += 1
#print the number of increases
print(f"There were {increases} increases in depth.")

