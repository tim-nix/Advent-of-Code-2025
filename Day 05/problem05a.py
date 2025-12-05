# The program input consists of a list of fresh
# ingredient ID ranges, a blank line, and a list
# of available ingredient IDs. The fresh ID ranges
# are inclusive: the range 3-5 means that
# ingredient IDs 3, 4, and 5 are all fresh. The
# ranges can also overlap; an ingredient ID is
# fresh if it is in any range.
#
# Count how many of the available ingredient IDs
# are fresh.


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


# Convert the list of strings into two lists. The
# first list contains a tuple for each range; the
# low and high value of the range. The second list
# are the integer values associated with each
# ingredient.
def parseInput(values):
   cut_point = values.index('')
   ranges_str = values[:cut_point]
   ingredients_str = values[cut_point + 1:]
   
   ranges = list()
   for r in ranges_str:
      a, b = r.split('-')
      ranges.append((int(a), int(b)))
                    
   ingredients = [ int(i) for i in ingredients_str ]
   
   return (ranges, ingredients)


if __name__ == '__main__':
   values = readFile("input5b.txt")
   ranges, ingredients = parseInput(values)

   # Iterate through the list of ingredients and
   # count how many are fresh; that is, how many
   # fall within at least one of the ranges.
   count = 0
   for i in ingredients:
      bad = True
      # Iterate through the ranges and break out
      # if the ingredient is found to be within
      # a given range.
      for low, high in ranges:
         if i in range(low, high + 1):
            bad = False
            break

      # If ingredient is good, increment count
      if not bad:
         count += 1

   # Display the results
   print('good ingredients = ' + str(count))
   
   
