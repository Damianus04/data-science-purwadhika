# Soal 1
print("soal 1")
x = 0

while x < 5:
    x += 1
    x_string = str(x) + " "
    print(x_string * x)
print("-"*50)

# Soal 2
print("soal 2")
x = 0
output = ""

while x < 5:
    x += 1
    x_string = str(x) + " "
    output += x_string

    print(output)
print("-"*50)

# Soal 3
print("soal 3")
x = 6
output = ""

while x > 1:
    x -= 1
    x_string = str(x) + " "
    output += x_string

    print(output)
print("-"*50)

# Soal 4
print("soal 4")
x = 6
y = 0

while x > 0:
    x -= 1
    y += 1
    y_string = str(y) + " "
    print(y_string * x)
print("-"*50)

# Soal 5
print("soal 5")
x = 0
output = ""

while x < 6:
    x += 1
    x_string = str(x) + " "
    output += x_string

z = 0
for i in range(len(output)):
    z += 1
    if output[i] == " ":
        continue
    else:
        print(output[:-z])

    i += 1
print("-"*50)

# Soal 6
print("soal 6")
x = 6
output = ""

while x > 1:
    x -= 1
    x_string = str(x) + " "
    output += x_string

z = 0
for i in range(len(output)):
    z += 1
    if output[i] == " ":
        continue
    else:
        print(output[:-z])
print("-"*50)

# Soal 7
print("soal 7")
x = 0
y = 5
for i in range(5):
    x += 1
    print(" * " * x)

for i in range(5):
    print(" * " * y)
    y -= 1
