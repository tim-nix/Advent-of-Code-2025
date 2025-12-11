# The program input consists of a list of devices
# and their outputs. Starting at the device
# labeled 'you', find the number of different
# paths to the device labeled 'out' be following
# the output cable from each device to the next.
#
# How many different paths lead from 'you' to
# 'out'?

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


# Convert each line of input into an entry in a
# dictionary with the first entry of the line
# being the key and the outputs stored as a tuple
# for the dictionary value.
def parseInput(values):
   wiring = dict()
   for line in values:
      parts = line.split()
      wiring[parts[0][:-1]] = tuple(parts[1:])

   return wiring


# Perform a BFS using the wiring diagram and a
# starting device of 'you'.  Count the number of
# different paths that lead to the device labeled
# 'out'.
def searchWiring(wiring):
   start = 'you'
   end = 'out'
   count = 0
   toVisit = [ start ]
   while len(toVisit) > 0:
      current = toVisit.pop(0)
      # If the output leads to 'out', increment
      # count.
      if current == end:
         count += 1
      # Otherwise, add each of the output paths to
      # the list of devices to visit.
      else:
         for next_device in wiring[current]:
            toVisit.append(next_device)

   # Return the number of paths found.
   return count


if __name__ == '__main__':
   values = readFile("input11b.txt")
   wiring = parseInput(values)

   # Find the number of different paths.
   count = searchWiring(wiring)

   # Display the results.
   print(count)

   
