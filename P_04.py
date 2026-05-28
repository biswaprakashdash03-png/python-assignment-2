side = float(input("Enter side of cube: "))

volume = side ** 3

print("Volume of cube is:", volume)

if volume > 1000:
    print("Volume is greater then 1000")
else:
    print("Volume is below 1000")