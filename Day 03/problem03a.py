# The input consists of multiple arrays of batteries;
# that is, a line of digits with each digit (1 to 9)
# corresponding to a joltage rating.  Within each
# bank, you need to turn on exactly two batteries;
# the joltage that the bank produces is equal to the
# number formed by the digits on the batteries you've
# turned on. For example, if you have a bank like
# 12345 and you turn on batteries 2 and 4, the bank
# would produce 24 jolts. (You cannot rearrange
# batteries.)
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

   # Iterate through the battery arrays
   sum_jolts = 0
   for array in battery_arrays:
      # Find the index of the largest digit within
      # the array (excluding the last digit)
      m_i = array.index(max(array[:-1]))

      # Find the largest digit within the array
      # slice of digits to the right of the largest
      # digit
      next_digit = max(array[m_i + 1:])

      # Convert into a two-digit number and add to sum
      max_value = (array[m_i] * 10) + next_digit
      sum_jolts += max_value

   # Print out the sum of the maximum joltage
   print('sum of maximum joltage = ' + str(sum_jolts))
   
