file = open("my_text", 'w')
file.write("\nHello")
file.write("\n1")
file.write("\nworld")
file.close()

try:
  with open("my_text", 'r') as file:
    contents = file.read()
    print(contents)

  with open("my_text", 'a') as file:
    file.write("\nread")
    file.write("\nThis")
    file.write("\nTime")
except err:
  print(err)
finally:
  print("Done reading!")

