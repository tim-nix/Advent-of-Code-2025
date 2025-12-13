# The program input consists of a list of devices
# and their outputs. Starting at the device
# labeled 'svr', find the number of different
# paths to the device labeled 'out' by following
# the output cable from each device to the next.
#
# Find the number of paths that lead from 'svr' to
# 'out' that also visit both 'dac' and 'fft'?

# Global variable for keeping track of the number
# of paths to 'out' from a given device.
path_count = dict()



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


# Perform a recursive BFS using the wiring diagram 
# from the current device to the end device. Count
# the number of different paths that lead to the
# end device. Use the global path_count variable
# to minimize searching paths already found.
def searchWiring(current, end, wiring):
   # If path count is stored, then return it.
   if current in path_count:
      return path_count[current]

   # If the 'out' device is found but is not the
   # end device, then stop this path search but
   # don't count it.
   if (end != 'out') and (current == 'out'):
      return 0

   # If the current device is the end device, then
   # stop this path search but count it.
   if current == end:
      return 1

   # Search all output paths, sum the count, and
   # store in path_count.
   count = 0         
   for next_device in wiring[current]:
      count += searchWiring(next_device, end, wiring)
   path_count[current] = count

   # Return the number of paths found.
   return count


if __name__ == '__main__':
   values = readFile("input11b.txt")
   wiring = parseInput(values)

   # Find the number of different paths.
   # First find the number of different paths from
   # 'svr' to 'fft'.
   count1 = searchWiring('svr', 'fft', wiring)

   # Reset path_count and find the number of paths
   # from 'fft' to 'dac'.
   path_count = dict()
   count2 = searchWiring('fft', 'dac', wiring)

   # Reset path_count and find the number of paths
   # from 'dac' to 'out'.
   path_count = dict()
   count3 = searchWiring('dac', 'out', wiring)

   # Calculate the number of unique paths from
   # 'svr' to 'out' that pass through both 'fft'
   # and 'dac' by multiplying count1, count2, and
   # count3.
   total = count1 * count2 * count3
   
   # Display the results.
   print('The total paths = ' + str(total))
   
