count = 0
no = 500
while True:
  count += 1
  print(f"Your {count} attempt")
  guess = int(input(f"Guess my number\n"))
  if guess == no:
    break
  elif guess >= no:
    print("You are too high")
    continue
  elif guess <= no:
    print("You are too low")
    continue
  else:
    print("Please try again")
    exit()
print("Congratulations, you got it right in ", count, "attempt(s)")