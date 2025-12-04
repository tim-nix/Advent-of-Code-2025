# The program input consists of rolls of paper (@)
# arranged on a large grid. The forklifts can only
# access a roll of paper if there are fewer than
# four rolls of paper in the eight adjacent
# positions. Calculate the number of rolls of paper
# the forklifts can access and then remove in
# multiple passes.


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

# Turn the list of strings into a list of lists
# characters. This step is not really needed for
# this problem.
def parseInput(values):
   rows = list()
   for v in values:
      rows.append(list(v))

   return rows


# Given a location (x, y), determine if the value
# is a legal location on the grid (rows).
def isInBounds(x, y, rows):
   length = len(rows)
   width  = len(rows[0])
   
   if (x >= 0) and (y >= 0):
      if (x < width) and (y < length):
         return True

   return False


# If the given location (x, y) contains a roll
# of paper, then count the number rolls of paper
# that are adjacent to the given location. If
# less than four rolls of paper are adjecent,
# return True. Otherwise, return False.
def isLowAdjacent(x, y, rows):
   if rows[x][y] != '@':
      return False
   
   count = 0
   if isInBounds(x - 1, y - 1, rows) and (rows[x - 1][y - 1] == '@'):
      count += 1
   if isInBounds(x, y - 1, rows) and (rows[x][y - 1] == '@'):
      count += 1
   if isInBounds(x + 1, y - 1, rows) and (rows[x + 1][y - 1] == '@'):
      count += 1
   if isInBounds(x - 1, y, rows) and (rows[x - 1][y] == '@'):
      count += 1
   if isInBounds(x + 1, y, rows) and (rows[x + 1][y] == '@'):
      count += 1
   if isInBounds(x - 1, y + 1, rows) and (rows[x - 1][y + 1] == '@'):
      count += 1
   if isInBounds(x, y + 1, rows) and (rows[x][y + 1] == '@'):
      count += 1
   if isInBounds(x + 1, y + 1, rows) and (rows[x + 1][y + 1] == '@'):
      count += 1

   return count < 4


if __name__ == '__main__':
   values = readFile("input4b.txt")
   paper_rolls = parseInput(values)

   # Identify the paper rolls that can be removed
   # and remove them. Removed paper rolls may make
   # more paper rolls accessible so make multiple
   # passes until no rolls are removed.
   still_removing = True
   accessible = 0
   while still_removing:
      # Identify rolls that are accessible and
      # mark them for removal
      to_remove = list()
      for x in range(len(paper_rolls)):
         for y in range(len(paper_rolls[x])):
            if isLowAdjacent(x, y, paper_rolls):
               to_remove.append((x, y))

      # If no paper rolls are accessible, then
      # done with removing them
      if len(to_remove) == 0:
         still_removing = False
      else:
         # Increase the count of paper rolls
         # that can be removed
         accessible += len(to_remove)

         # Remove the rolls
         for s, t in to_remove:
            paper_rolls[s][t] = '.'

   # Display the resulting count
   print('rolls accessible = ' + str(accessible))
