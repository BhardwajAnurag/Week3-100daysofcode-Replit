print("Animal Sounds")
print("-------------")
exit = ""
while exit != "yes":
  animal = input("What animal sound you want?:\n")
  if animal == "cow":
    print("Cow goes moo")
  else:
    print("idk your animal noise")
  exit = input("Do you wish to exit?:\n")

exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")

counter = 0
while counter <= 5:
  print(counter)
  counter +=1