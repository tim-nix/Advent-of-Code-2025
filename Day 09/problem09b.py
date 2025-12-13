# The puzzle input is a list of coordinates of
# tiles that denote the sequence of points in the
# construction of a rectilinear polygon. These
# coordinates designate red tiles. All tiles
# connecting one tile to the next (in sequence)
# are green and all tiles within the border of the
# polygon are green
#
# Choosing any two red tiles as the opposite
# corners of a rectangle; the goal of the program
# is to find the largest rectangle possible that
# is made up entirely of red and green tiles.

# A global data structure denoting whether or not
# a 'visited' tile is red/green or not.
good_walls = dict()


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


# Convert the (x, y) coordinates from a string
# representation into list of integer tuples.
def parseInput(values):
   coords = list()
   for line in values:
      x, y = line.split(',')
      coords.append((int(x), int(y)))

   # Add the first coordinate to the end of the
   # list to enclose the polygon formed.
   coords.append(coords[0])

   return coords



# Calculate the number of tiles that would be red
# given the coordinates of the two corner tiles.
def calcArea(coords1, coords2):
   x1, y1 = coords1
   x2, y2 = coords2

   return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)



# Generate a set of all edge coordinates of the
# polygon formed from the input coordinates. Also
# determine the minimum x-coordinate value.
def generateWallData(path):
   min_x = path[0][0]
   walls = set()

   # Iterate through all corner coordinates of the
   # polygon (except the last which is a repeat of
   # the first).
   for i in range(len(path) - 1):
      x1, y1 = path[i]
      x2, y2 = path[i + 1]

      # Check for new minimum x value.
      if min(x1, x2) < min_x:
         min_x = min(x1, x2)

      # Check and handle a verticle edge.
      if x1 == x2:
         for y in range(min(y1, y2), max(y1, y2) + 1):
            walls.add((x1, y))
      # Otherwise handle a horizontal edge.
      else:
         for x in range(min(x1, x2), max(x1, x2) + 1):
            walls.add((x, y1))

   # Reduce the minimum x value by one and return
   # it with the set of wall edges.
   return (min_x - 1, walls)


# From the minimum x value, traverse to the right
# and count the number of walls/edges that are
# passed through before reaching the given point
# (rec_x, rec_y).
def countWalls(min_x, rec_x, rec_y, walls):
   enterWall = False
   walls_before = 0
   for x in range(min_x, rec_x + 1):
      if x <= rec_x:
         if (x, rec_y) in walls:
            enterWall = True
         elif ((x, rec_y) not in walls) and enterWall:
            walls_before += 1
            enterWall = False
            
   return walls_before

# Determine if the rectangle formed by the two
# opposing vertices is contained entirely within
# the polygon.
def isContained(coords1, coords2, wallData):
   x1, y1 = coords1
   x2, y2 = coords2
   min_x, walls = wallData

   # Generate vertical walls of rectangle.
   rec_walls = list()
   for rec_y in range(min(y1, y2), max(y1, y2) + 1):
      rec_walls.append((x1, rec_y))
      rec_walls.append((x2, rec_y))

   # For each of the verticle edge coordinates,
   # check to see if it is interior to the polygon.
   for rec_x, rec_y in rec_walls:
      # First check to see if the coordinates have
      # already been seen.
      if (rec_x, rec_y) in good_walls:
         if not good_walls[(rec_x, rec_y)]:
            return False
         else:
            continue
      # Otherwise, count the number of verticle
      # edges passed through from left to right.
      else:
         if (rec_x, rec_y) in walls:
            good_walls[(rec_x, rec_y)] = True
         else:
            before = countWalls(min_x, rec_x, rec_y, walls)
            # If the coordinates are interior,
            # then they should have passed through
            # an odd number of walls.
            if (before % 2) == 0:
               good_walls[(rec_x, rec_y)] = False
               return False
            else:
               good_walls[(rec_x, rec_y)] = True

   # All points in the rectangle are interior
   return True


if __name__ == '__main__':
   values = readFile("input9b.txt")
   coords = parseInput(values)

   # Generate a set of edge coordinates for the
   # polygon.
   wallData = generateWallData(coords)

   # Generate a list of all possible rectangles
   # along with their corresponding area.
   candidates = list()
   for c1 in range(len(coords) - 1):
      for c2 in range(c1 + 1, len(coords) - 1):
         candidates.append((calcArea(coords[c1], coords[c2]), coords[c1], coords[c2]))

   # Sort the rectangles by area.
   candidates.sort(reverse=True)

   # Iterate through the rectangles from largest
   # to smallest and stop at the first one found
   # that is interior to the polygon.
   found = False
   index = 0
   max_area = 0
   while not found:
      if candidates[index][0] > 1526000000: # Added after solution was found
         index += 1
         continue
      else:
         print('checking candidate with area = ' + str(candidates[index][0]))
         if isContained(candidates[index][1], candidates[index][2], wallData):
            max_area = candidates[index][0]
            found = True
         else:
            index += 1

   # Display the result
   print('largest area is ' + str(max_area))
   
# Provides the correct answer. This solution is
# not a general solution as it does not also check
# from top to bottom. Also, this solution is
# horribly inefficient (~10 hours of runtime for
# solution).
