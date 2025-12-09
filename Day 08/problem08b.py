# The program input consists of a list of
# coordinates (x, y, z) for junction boxes.
# Connect pairs of junction boxes that are as
# close together as possible according to
# straight-line distance. By connecting two
# junction boxes together, because electricity can
# flow between them, they become part of the same
# circuit.
#
# Continue connecting the closest unconnected
# pairs of junction boxes together until they're
# all in the same circuit. Calculate the product
# resulting if you multiply together the X
# coordinates of the last two junction boxes you
# need to connect.

import math  # Needed for the sqrt function

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


# Convert the input into a list of (x, y, z)
# tuples of integers.
def parseInput(values):
   jBoxes = list()
   for line in values:
      x, y, z = line.split(',')
      jBoxes.append((int(x), int(y), int(z)))

   return jBoxes


# Find the straight-line distance between two
# junctions.
def findDistance(coords1, coords2):
   x1, y1, z1 = coords1
   x2, y2, z2 = coords2

   distance = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

   return math.sqrt(distance)


# Generate a sorted list of the shortest connections
# between junctions.
def calcDistances(jBoxes):
   shortest = list()
   for j in range(len(jBoxes)):
      for k in range(j + 1, len(jBoxes)):
         shortest.append((round(findDistance(jBoxes[j], jBoxes[k]), 4), jBoxes[j], jBoxes[k]))

   shortest.sort()
   
   return shortest


if __name__ == '__main__':
   values = readFile("input8b.txt")
   jBoxes = parseInput(values)

   shortest = calcDistances(jBoxes)
   
   # Generate a list of sets with each set
   # containing a single junction.
   circuits = list()
   for j in jBoxes:
      new_set = set()
      new_set.add(j)
      circuits.append(new_set)

   # Continue to iterate through the shortest
   # edges until a single circuit is formed.
   while len(circuits) > 1:
      distance, j1, j2 = shortest.pop(0)
      # Find the set containing the first junction
      found_index1 = -1
      for i in range(len(circuits)):
         if j1 in circuits[i]:
            found_index1 = i
            break

      # Find the set containing the second junction
      found_index2 = -1
      for i in range(len(circuits)):
         if j2 in circuits[i]:
            found_index2 = i
            break

      # Combine the two circuits
      if found_index1 != found_index2:
         circuits[found_index1] = circuits[found_index1].union(circuits[found_index2])
         circuits.pop(found_index2)

   # Display the results
   product = j1[0] * j2[0]
   print('Product of the last edge x-coordinates = ' + str(product))
