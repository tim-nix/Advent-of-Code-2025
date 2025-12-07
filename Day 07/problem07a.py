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
# Analyze the manifold diagram and calculate how
# many times the beam will be split.


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


if __name__ == '__main__':
   values = readFile("input7b.txt")
   manifold = parseInput(values)

   # Iterate through each location of the manifold
   split_count = 0
   for y in range(1, len(manifold)):
      for x in range(1, len(manifold[y])):
         # If the current position is empty and
         # the position above is either 'S' or '|'
         # then current position becomes '|'
         if (manifold[y][x] == '.') and (manifold[y - 1][x] in ('S', '|')):
            manifold[y][x] = '|'
         # If the current posistion is a splitter
         # ('^') then the position before and
         # after becomes '|' and increment split
         # count
         elif (manifold[y][x] == '^') and (manifold[y - 1][x] == '|'):
            split_count += 1
            manifold[y][x - 1] = '|'
            manifold[y][x + 1] = '|'

   # Display the split count
   print('The tachyon beam is split ' + str(split_count) + ' times.')
         
   
