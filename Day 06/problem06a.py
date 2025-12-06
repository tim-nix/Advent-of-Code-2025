# The program input consist in a matrix of
# integers in which each problem's numbers are
# arranged vertically; the last row of the input
# contain the symbols for the operation that needs
# to be performed. Problems are separated by a
# full column of only spaces.
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


# The input consists of a list of strings in which
# each of the strings are integers separated by
# white space.  The last line of the input
# consists of a string of operators (+ and *)
# separated by whitespace.  This function converts
# each line containing numbers into a list of
# integers (stored within the list 'numbers' and
# the last line is converted into a list of
# characters; that is, the operations to be
# performed on each column of numbers. 
def parseInput(values):
   # Construct the matrix of integers
   numbers = list()
   for v in values[:-1]:
      numbers.append([ int(x) for x in v.split() ])

   # Construct the list of operations
   operators = values[-1].split()

   return(numbers, operators)


if __name__ == '__main__':
   values = readFile("input6b.txt")
   numbers, operators = parseInput(values)

   # Iterate through each operation (also the same
   # length as the number of columns.
   result_sum = 0
   for o in range(len(operators)):
      # Initialize result based on the operation
      # to be performed for the column
      if operators[o] == '+':
         result = 0
      else:
         result = 1

      # Iterate through the column and either add
      # or multiply based on the specified operator
      for n in range(len(numbers)):
         if operators[o] == '+':
            result += numbers[n][o]
         elif operators[o] == '*':
            result *= numbers[n][o]
         else:
            print('unknown operator: ' + operators[o])

      # Add the result to the sum
      result_sum += result

   # Display the results
   print('resulting sum = ' + str(result_sum))

