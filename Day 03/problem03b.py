# The input consists of multiple arrays of batteries;
# that is, a line of digits with each digit (1 to 9)
# corresponding to a joltage rating.  Within each
# bank, you need to turn on exactly twelve batteries;
# the joltage that the bank produces is equal to the
# number formed by the digits on the batteries you've
# turned on. (You still cannot rearrange batteries.)
#
# Find the largest possible joltage each bank can
# produce and the sum of the maximum joltage from
# each bank

# Read in the data file and convert it to a list
# of strings.
def readFile(filename):
   lines = []
   try:
      with open(filename, "r") as file:
         line = file.readline()
         while line:
            lines.append(line.replace('\n', ''))
            line = file.readline()

         file.close()
            
   except FileNotFoundError:
      print("Error: File not found!")
   except:
      print("Error: Can't read from file!")
   
   return lines

# Convert the list of battery arrays (each initally
# stored as a string) into a list containing a lists
# of integer digits.
def parseInput(values):
   digit_list = list()
   for v in values:
      digit_list.append([ int(i) for i in list(v) ])
      
   return digit_list

   
if __name__ == '__main__':
   values = readFile("input3b.txt")
   battery_arrays = parseInput(values)

   # Total batteries to turn on
   total_on = 12
   # Iterate through the battery arrays
   sum_jolts = 0
   for array in battery_arrays:
      # Add each found digit to this list
      digits = []

      # Start at the beginning of the array
      # but exclude the tail according to the
      # number of needed remaining digits
      head = 0
      tail = -(total_on - 1)
      while tail <= 0:
         # Can't slice [head:0] so separate case
         # last digit
         if tail == 0:
            digits.append(max(array[head:]))
         else:
            # Find index of max digit (but leave
            # enough digits at the end for the
            # remainder of needed batteries
            max_i = array[head:tail].index(max(array[head:tail]))
            digits.append(array[head + max_i])

            # Calculate the beginning of the next
            # slice
            head = head + max_i + 1

         # Reduce the end of the slice by one
         tail += 1

      # Convert list of digits into single value
      max_value = int(''.join([ str(i) for i in digits ]))

      # Add to total output joltage
      sum_jolts += max_value

   # Print out the sum of the maximum joltage
   print('sum of maximum joltage = ' + str(sum_jolts))

