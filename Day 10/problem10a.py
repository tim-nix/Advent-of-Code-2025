# Each line of program input contains a single
# indicator light diagram in [square brackets],
# one or more button wiring schematics in
# (parentheses), and joltage requirements in
# {curly braces}. You can toggle the state of
# indicator lights by pushing any of the listed
# buttons. Each button lists which indicator
# lights it toggles, where 0 means the first
# light, 1 means the second light, and so on. When
# you push a button, each listed indicator light
# either turns on (if it was off) or turns off (if
# it was on).
#
# Determine the fewest total presses required to
# correctly configure all indicator lights for all
# machines in your list. What is the fewest button
# presses required to correctly configure the
# indicator lights on all of the machines?

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


# Split each line of input into a final state (a
# list of Boolean values), a list of button press
# options (a list of tuples with each tuple
# toggling one or more lights), and a list of
# joltages (not used for this problem).
def parseInput(values):
   configs = list()
   for line in values:
      config = line.split()
      final = list(config[0][1:-1])
      final = [ True if x == '#' else False for x in final ]
      
      wiring = [ scheme[1:-1].split(',') for scheme in config[1:-1] ]
      wiring = [ tuple([ int(i) for i in s ]) for s in wiring ]

      joltages = config[-1][1:-1].split(',')
      joltages = [ int(j) for j in joltages ]
                    

      configs.append((final, wiring, joltages))
   
   return configs



# Conduct a BFS starting with an initial
# configuration of all lights OFF (False). Explore
# using each button press to change the current
# state. Find the fewest number of button presses
# needed to reach the final configuration.
def findFewest(configuration):
   final, wiring, joltages = configuration

   # Configure initial state (level is the number
   # of button presses to reach the configuration)
   states = [(0, [ False for i in range(len(final)) ])]
   visited = set()

   # Keep searching until the current state matches
   # the final state
   while states[0][1] != final:
      level, current = states.pop(0)
      # Iterate through each of the button presses
      for w in wiring:
         # Configure the updated state
         next_state = [ s for s in current ]
         for i in range(len(next_state)):
            if i in w:
               next_state[i] = not next_state[i]

         # Ignore configurations already seen and
         # update the states queue
         t_state = tuple(next_state)
         if t_state not in visited:
            visited.add(t_state)
            states.append((level + 1, next_state))

   # return the 'level' of the found final state
   return states[0][0]
   



if __name__ == '__main__':
   values = readFile("input10b.txt")
   configs = parseInput(values)

   # Initial count and iterate through each
   # configuration, find the fewest button presses
   # to reach the final state and increment count
   button_presses = 0
   for c in configs:
      button_presses += findFewest(c)

   # Display result
   print('total button presses = ' + str(button_presses))
   
   
