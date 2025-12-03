# Given a safe has a dial with only an arrow on it;
# around the dial are the numbers 0 through 99 in
# order. and an input of a sequence of rotations,
# one per line, which tell you how to open the safe.
# A rotation starts with an L or R which indicates
# whether the rotation should be to the left (toward
# lower numbers) or to the right (toward higher
# numbers). Then, the rotation has a distance value
# which indicates how many clicks the dial should be
# rotated in that direction.
#
# The dial starts by pointing at 50.
#
# Calculate the number of times the dial is left
# pointing at 0 after any rotation in the sequence.

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
