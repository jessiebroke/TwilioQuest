import sys

inputs = sys.argv
inputs.pop(0)

# for i in range(len(sys.argv)-1):
#     if int(sys.argv[i+1]) % 15 == 0:
#         print("fizzbuzz")
#     elif int(sys.argv[i+1]) % 3 == 0:
#         print("fizz")
#     elif int(sys.argv[i+1]) % 5 == 0:
#         print("buzz")
#     else:
#         print(int(sys.argv[i+1]))

for i in range(len(sys.argv)):
    if int(sys.argv[i]) % 15 == 0:
        print("fizzbuzz")
    elif int(sys.argv[i]) % 3 == 0:
        print("fizz")
    elif int(sys.argv[i]) % 5 == 0:
        print("buzz")
    else:
        print(int(sys.argv[i]))