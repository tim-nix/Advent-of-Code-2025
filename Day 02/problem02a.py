# Given a collection of ranges for IDs, find (and
# sum) the invalid IDs identified because they are
# made up of some sequence of digits that repeat
# twice.

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

# The input is a single string of ranges.  Each
# separate range is comma delimited.  A single
# range consists of two integer values separated
# by a dash '-'.  Convert the input into a list
# of tuples in which each tuple denotes the
# lower and upper bound of a given range.
def parseInput(value):
   idents1 = value.split(",")
   idents2 = list()
   for i in idents1:
      first, second = i.split("-")
      idents2.append((int(first), int(second)))
      
   return idents2

# Look looking for any string which is made only
# of some sequence of digits repeated twice. So, 
# 55 (5 twice), 6464 (64 twice), and 123123 (123
# twice) would all be invalid strings (returning
# True).
def isRepeat(string):
   # If the string is of odd length, then it
   # can't repeat
   if len(string) % 2 != 0:
      return False

   # Find the mid-point and compare successive
   # characters.  If they don't match, return
   # False
   mid_length = len(string) // 2
   for i in range(mid_length):
      if string[i] != string[mid_length + i]:
         return False

   # Repetitive string is found.
   return True
   
if __name__ == '__main__':
   values = readFile("input2b.txt")
   idents = parseInput(values[0])

   # Iterate through the list of ranges
   sum_invalids = 0
   for low, high in idents:
      # Iterate from low value through high value
      # and add to sum if invalid
      for check in range(low, high + 1):
         if isRepeat(str(check)):
            sum_invalids += check

   # Display the results
   print('sum of invalid IDs = ' + str(sum_invalids))
   
   
