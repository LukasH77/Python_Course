# Fun little one liner:
# print("You could name your band " + input("Hello world! This is the Band Name Generator.\nTell me the city you grew up in.\n") + input(" Now, if you have one, the name of your pet. Else some name you deem fitting.\n"))

# Ok, now properly:
print("Hello world! This is the Band Name Generator.")

city = input("Tell me the city you grew up in.\n")
name = input("Now, if you have one, the name of your pet. Else some name you deem fitting.\n")

print("You could name your band " + city + " " + name + ".\nThank you for using our services.")
