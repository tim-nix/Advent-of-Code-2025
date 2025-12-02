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

# Convert each instruction (line of input) into
# a direction (a single character: 'R' or 'L')
# and a distance (integer value between 0 and 99).
# Store as a tuple within a list.
def parseInput(values):
   rotations = []
   for line in values:
      direction = line[0]
      distance = int(line[1:])
      rotations.append((direction, distance))

   return rotations

if __name__ == '__main__':
   values = readFile("input1b.txt")
   rotations = parseInput(values)

   # The dial starts by pointing at 50
   dial = 50

   # Iterate through the rotations. Adjust
   # the dial and count the number of times
   # that '0' occurs.
   count = 0
   for direction, distance in rotations:
      if direction == 'R':
         dial = (dial + distance) % 100
      else:
         dial = (dial - distance) % 100
      
      if dial == 0:
         count += 1

   # Display the number of times that '0'
   # occurred; that is, the count.
   print('count = ' + str(count))
