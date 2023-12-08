width = int(input("Give Dimension of your Diamond: "))

# Upper half
for i in range (width):
    print(" " * (width-i) + " *" * (i+1))
 
# Lower Half
for j in range (width-1):
    print(" " * (j+2) + " *" * (width-1-j))