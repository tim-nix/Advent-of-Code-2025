# The problem input consists of several sections.
# The first section lists the standard present
# shapes as 3x3 grids. For convenience, each shape
# starts with its index and a colon; then, the
# shape is displayed visually, where # is part of
# the shape and . is not.
#
# The second section lists the regions under the
# trees. Each line starts with the width and
# length of the region. The rest of the line
# describes the presents that need to fit into
# that region by listing the quantity of each
# shape of present
#
# Presents can be rotated and flipped as necessary
# to make them fit in the available space, but
# they have to always be placed perfectly on the
# grid.
#
# Determine how many of the regions can fit the
# presents listed. 

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


# 
def parseInput(values):
   shapes = list()
   grid_sizes = list()
   num_presents = list()
   for line in values:
      if len(line) == 2:
         read_shape = True
         shape = list()
      elif read_shape and (line == ''):
         read_shape = False
         shapes.append(shape)
      elif read_shape:
         shape.append(list(line))
      else:
         size, nums = line.split(':')
         width, length = size.split('x')
         grid_sizes.append((int(width), int(length)))
         num_presents.append([int(i) for i in nums.split()])

   return (shapes, grid_sizes, num_presents)
         
      
      



if __name__ == '__main__':
   values = readFile("input12b.txt")
   shapes, grid_sizes, num_presents = parseInput(values)

   # Find general and precise present sizes. The
   # general size is the full grid (3x3) while the
   # precise size is the count of '#' characters
   # within the grid.
   present_sizes = list()
   precise_sizes = list()
   for p in shapes:
      present_sizes.append(len(p) * len(p[0]))
      count = 0
      for y in range(len(p)):
         for x in range(len(p[y])):
            if p[y][x] == '#':
               count += 1
      precise_sizes.append(count)   

   # For each region, determine if the presents
   # can absolutely fit, maybe fit, or absolutely
   # can't fit
   can_fit = 0
   maybe_fit = 0
   no_fit = 0
   for i in range(len(num_presents)):
      # Calculate the maximum size and the minimum
      # size needed for the layout.
      max_space = 0
      min_space = 0
      for n in range(len(num_presents[i])):
         max_space += (num_presents[i][n] * present_sizes[n])
         min_space += (num_presents[i][n] * precise_sizes[n])

      # If all presents can fit regardless of the
      # layout, increment can_fit.
      if max_space <= (grid_sizes[i][0] * grid_sizes[i][1]):
         can_fit += 1
      # If all presents might fit depending on the
      # layout, increment maybe_fit.
      elif min_space <= (grid_sizes[i][0] * grid_sizes[i][1]):
         maybe_fit += 1
      # If the region is too small under any
      # circumstances, then increment no_fit.
      else:
         no_fit += 1

   # Display the results
   print('Can fit   = ' + str(can_fit))
   print('Might fit = ' + str(maybe_fit))
   print("Can't fit = " + str(no_fit))

   # The general solution to this problem is the
   # bin packing problem which (for the decision
   # problem) is NP-complete. Any configuration
   # resulting in a "might fit" will need a more
   # complex solution than implemented here.
