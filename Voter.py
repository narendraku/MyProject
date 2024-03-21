age =int(input('enter your age'))
nationality =int (input('if yes then type 1 else 0'))
if age >= 18 and nationality == 1:
 print("you can vote")
elif age >= 18 and nationality == 0:
  print("You are not Indian")
elif age <= 18 and nationality == 1:
  print("your age is below 18, so you are not eligible")
else:
  print("you are not Indian and 18 years old")