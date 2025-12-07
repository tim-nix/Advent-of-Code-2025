# The program input is a diagram of the tachyon
# manifold. A tachyon beam enters the manifold at
# the location marked S; tachyon beams always move
# downward. Tachyon beams pass freely through
# empty space (.). However, if a tachyon beam
# encounters a splitter (^), the beam is stopped;
# instead, a new tachyon beam continues from the
# immediate left and from the immediate right of
# the splitter.
#
# Analyze the manifold diagram and calculate the
# number of timelines active after a single
# particle completes all of its possible journeys
# through the manifold.

# Global variable for tracking found paths to
# prevent rewalking recursive paths multiple times.
splits = dict()

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


# Convert the input, consisting of a list of
# strings, to a list containing lists of
# characters (allows for reassignment of character
# values.
def parseInput(values):
   manifold = list()
   for line in values:
      manifold.append(list(line))

   return manifold


# Perform a recursive DFS search of all possible
# paths through the manifold
def searchManifold(y, above, manifold):
   #print('recursive depth = ' + str(y))
   if y >= len(manifold):
      return 1

   split_count = 0
   current = [ i for i in manifold[y] ]
   for x in range(len(current)):
      # If the current position is empty and
      # the position above is either 'S' or '|'
      # then current position becomes '|' and
      # recursively search this path
      if (manifold[y][x] == '.') and (above[x] in ('S', '|')):
         # If path has been walked before, look up
         # previous split count
         if (y, x) in splits:
            split_count += splits[(y, x)]
         # Otherwise walk the recursive path
         else:
            current[x] = '|'
            splits[(y, x)] = searchManifold(y + 1, current, manifold)
            split_count += splits[(y, x)]
            current[x] = manifold[y][x]
         
      # If the current posistion is a splitter
      # ('^') then the position before and
      # after becomes '|' then recursively search
      # this path
      elif (manifold[y][x] == '^') and (above[x] == '|'):
         # If path has been walked before, look up
         # previous split count
         if (y, x - 1) in splits:
            split_count += splits[(y, x - 1)]
         # Otherwise walk the recursive path
         else:
            current[x - 1] = '|'
            splits[(y, x - 1)] = searchManifold(y + 1, current, manifold)
            split_count += splits[(y, x - 1)]
            current[x - 1] = manifold[y][x - 1]

         # If path has been walked before, look up
         # previous split count
         if (y, x + 1) in splits:
            split_count += splits[(y, x + 1)]
         # Otherwise walk the recursive path
         else:
            current[x + 1] = '|'
            splits[(y, x + 1)] = searchManifold(y + 1, current, manifold)
            split_count += splits[(y, x + 1)]
            current[x + 1] = manifold[y][x + 1]

   #print(split_count)
   return split_count


if __name__ == '__main__':
   values = readFile("input7b.txt")
   manifold = parseInput(values)

   # Recursively search the manifold for all
   # possible tachyon paths
   above = [ i for i in manifold[0] ]
   split_count = searchManifold(1, above, manifold)
   
   # Display the split count
   print('The tachyon beam is split ' + str(split_count) + ' times.')
         
   
