score = input("Enter Score: ")
s = float(score)
if s > 1.0 or s < 0.0:
    print("Error. Value is outside range 0.0 - 1.0")
elif s >= 0.9:
    print('A')
elif s >= 0.8:
    print('B')
elif s >= 0.7:
    print('C')
elif s >= 0.6:
    print('D')
else:
    print('F')





