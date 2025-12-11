# The puzzle input is a list of coordinates where
# red tiles are located in the grid.
#
# Choosing any two red tiles as the opposite
# corners of a rectangle; the goal of the program
# is to find the largest rectangle possible.

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

   return coords


# Calculate the number of tiles that would be red
# given the coordinates of the two corner tiles.
def calcArea(coords1, coords2):
   x1, y1 = coords1
   x2, y2 = coords2

   return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


if __name__ == '__main__':
   values = readFile("input9b.txt")
   coords = parseInput(values)

   # Iterate through each pair of tiles and
   # determine the largest area resulting from
   # using these coordinates as the corners.
   max_area = 0
   for c1 in range(len(coords)):
      for c2 in range(c1 + 1, len(coords)):
         area = calcArea(coords[c1], coords[c2])
         if area > max_area:
            max_area = area

   # Display the result
   print('largest area is ' + str(max_area))
   
