# Python 3 code to print MAC
# in formatted way.

import uuid

# joins elements of getnode() after each 2 digits.

print("The MAC address in formatted way is : ", end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                for ele in range(0, 8 * 6, 8)][::-1]))
