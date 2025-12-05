# The program input consists of a list of fresh
# ingredient ID ranges, a blank line, and a list
# of available ingredient IDs. The fresh ID ranges
# are inclusive: the range 3-5 means that
# ingredient IDs 3, 4, and 5 are all fresh. The
# ranges can also overlap; an ingredient ID is
# fresh if it is in any range.
#
# Count all of the IDs that the fresh ingredient
# ID ranges consider to be fresh. An ingredient ID
# is still considered fresh if it is in any range.
#
# Now, the second section of the database (the
# available ingredient IDs) is irrelevant.


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


# Convert the list of strings into a list that
# contains a tuple for each range; the
# low and high value of the range. The second
# portion of the list of strings (the list of
# ingredients) is ignored.
def parseInput(values):
   cut_point = values.index('')
   ranges_str = values[:cut_point]
   
   ranges = list()
   for r in ranges_str:
      a, b = r.split('-')
      ranges.append((int(a), int(b) + 1))
   
   return ranges


# Determine if one range (low1, high1) is within
# the other range (low2, high2), or vice verse.
# Return 'True' if so, 'False' otherwise. 
def withinRange(low1, high1, low2, high2):
   if low1 in range(low2, high2):
      return True

   if low2 in range(low1, high1):
      return True

   if high1 in range(low2, high2):
      return True

   if high2 in range(low1, high1):
      return True

   return False


if __name__ == '__main__':
   values = readFile("input5b.txt")
   ranges = parseInput(values)

   # Iterate through the list of ranges until no
   # more changes are made.
   changes = True
   while changes:
      changes = False

      # Iterate through list of ranges and create
      # a new list of ranges made by combining
      # overlapping ranges.
      new_ranges = list()
      length_ranges = len(ranges)
      i = 0
      while i < length_ranges:
         low1, high1 = ranges[i]
         combined = False
         # Compare range with subsequent ranges
         for j in range(i + 1, length_ranges):
            low2, high2 = ranges[j]
            # If overlap is found, combine them
            # and add new range to new_ranges
            if withinRange(low1, high1, low2, high2):
               new_ranges.append((min(low1, low2), max(high1, high2)))

               # Remove the second range from the
               # list and decrement the range
               # length
               ranges.pop(j)
               length_ranges -= 1
               combined = True
               changes = True
               break

         # Increment the index
         i += 1

         # If the original range is not modified,
         # add it to new_ranges
         if not combined:
            new_ranges.append((low1, high1))

      # Reset ranges for the next round
      ranges = new_ranges

   # Count the number of good ingredient IDs
   # within the combined ID ranges
   count = 0
   for r in ranges:
      count += (r[1] - r[0])
   print('fresh ingredient IDs = ' + str(count))
      

   
   
