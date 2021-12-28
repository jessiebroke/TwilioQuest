import sys

order_of_succession = sys.argv
order_of_succession.pop(0)
# print(order_of_succession)

# for (i = 0; i < len(sys.argv); i++)
for i in range(len(sys.argv)):
    print(i+1, str(order_of_succession[i]))

# for (i = 0; i < sys.getsizeof(order_of_succession); i++ )
