# 

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
   coords = list()
   for line in values:
      x, y = line.split(',')
      coords.append((int(x), int(y)))

   coords.append(coords[0])

   return coords



# Calculate the number of tiles that would be red
# given the coordinates of the two corner tiles.
def calcArea(coords1, coords2):
   x1, y1 = coords1
   x2, y2 = coords2

   return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)



# 
def generateWallData(path):
   min_x = path[0][0]
   max_x = path[0][1]
   walls = set()
   for i in range(len(path) - 1):
      x1, y1 = path[i]
      x2, y2 = path[i + 1]

      if min(x1, x2) < min_x:
         min_x = min(x1, x2)

      if max(x1, x2) > max_x:
         max_x = max(x1, x2)

      if x1 == x2:
         for y in range(min(y1, y2), max(y1, y2) + 1):
            walls.add((x1, y))
      else:
         for x in range(min(x1, x2), max(x1, x2) + 1):
            walls.add((x, y1))

   return (min_x - 1, walls)


#
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

#
def isContained(coords1, coords2, wallData):
   x1, y1 = coords1
   x2, y2 = coords2
   min_x, walls = wallData

   for rec_y in range(min(y1, y2), max(y1, y2) + 1):
      for rec_x in range(min(x1, x2), max(x1, x2) + 1):
         if (rec_x, rec_y) not in walls:
            before = countWalls(min_x, rec_x, rec_y, walls)
            if (before % 2) == 0:
               return False

   return True


if __name__ == '__main__':
   values = readFile("input9b.txt")
   coords = parseInput(values)

   wallData = generateWallData(coords)
   print('walls generated')
   # 
   max_area = 0
   for c1 in range(len(coords) - 1):
      for c2 in range(c1 + 1, len(coords) - 1):
         if isContained(coords[c1], coords[c2], wallData):
            area = calcArea(coords[c1], coords[c2])
            if area > max_area:
               max_area = area
               print('new max area = ' + str(max_area))

   # Display the result
   print('largest area is ' + str(max_area))

   
