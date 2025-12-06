# The program input consist in columns of integers
# and the last row of the input contain the
# symbols for the operation that needs to be
# performed. Problems are separated by a full
# column of only spaces. In this case, the numbers
# are written right-to-left in columns. Each
# number is given in its own column, with the most
# significant digit at the top and the least
# significant digit at the bottom.
#
# Add or multiply, as appropriate, each column of
# numbers and calculate the grand total found by
# adding together all of the answers to the
# individual problems.

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


# Split the input into two lists: a list of
# strings containing the numbers and a list of
# operators stored as characters.
def parseInput(values):
   # Store the list of numbers (still stored as
   # strings)
   numbers = values[:-1]

   # Store the list of operations as characters
   operators = values[-1].split()

   return(numbers, operators)


if __name__ == '__main__':
   values = readFile("input6b.txt")
   numbers, operators = parseInput(values)

   # Parse through the array of numbers column by
   # column extracting each digit within the
   # column and convert to a corrected integer.
   corrected_nums = list()
   corrected_column = list()
   for x in range(len(numbers[0])):
      num = ''
      for y in range(len(numbers)):
         if numbers[y][x] != ' ':
            num = num + numbers[y][x]

      # If digits were found, then add the
      # converted number to the list.
      if num != '':
         corrected_column.append(int(num))
      else:
         # Otherwise, the end of the column of
         # numbers has been found so add the list
         # of corrected column numbers to the main
         # list of corrected numbers.
         corrected_nums.append(corrected_column)
         corrected_column = list()

   # There is no final column of whitespace so add
   # the last list of column numbers
   corrected_nums.append(corrected_column)
   
   # Iterate through each operation
   result_sum = 0
   for o in range(len(operators)):
      # Initialize result based on the operation
      # to be performed
      if operators[o] == '+':
         result = 0
      else:
         result = 1

      # Iterate through the row and either add
      # or multiply based on the specified operator
      for n in corrected_nums[o]:
         if operators[o] == '+':
            result += n
         elif operators[o] == '*':
            result *= n
         else:
            print('unknown operator: ' + operators[o])

      # Add the result to the sum
      result_sum += result

   # Display the results
   print('resulting sum = ' + str(result_sum))
