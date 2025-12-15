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
# Determine the the fewest button presses required
# to correctly configure the joltage level
# counters on all of the machines.

import math        # Used for math.inf
import itertools   # Used for product function

# A dictionary for memoization
found_states = dict()

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
                    
      # Final light scheme is not needed for this.
      configs.append((tuple(wiring), tuple(joltages)))
   
   return configs



# Perform a recursive search for the fewest button
# pushes to reach the desired joltage state. This
# is done by determining the button pushes needed
# to reach the parity joltage, divide resulting
# joltage by two (for each joltage state) and then
# recursing on the resulting joltage until all
# remaining joltages are zero.
def findFewest(configuration):
   # First check the memoization store.
   if configuration in found_states:
      print(found)
      return found_states[configuration]
   
   # Break apart the configuration.
   wiring, final_joltages = configuration

   # If remaining joltages are zero, return zero.
   if all([ j == 0 for j in final_joltages ]):
      return 0

   # Determine the light configuration based on
   # joltage parity
   final_lights = [ (j % 2) != 0 for j in final_joltages ]   

   # Iterate through all combinations of button
   # presses (in which each button can be pressed
   # either once or not at all. Only save those
   # that lead to final light configuration.
   possible_presses = list(itertools.product([True, False], repeat=len(wiring)))   
   presses = list()
   for sequence in possible_presses:
      current_lights = [ False for _ in final_joltages ]
      for s in range(len(sequence)):
         if sequence[s]:
            for w in wiring[s]:
               current_lights[w] = not current_lights[w]
      if current_lights == final_lights:
         presses.append(sequence)

   # Iterate through all button press sequences
   # that lead to the final light configuration.
   min_presses = math.inf
   for sequence in presses:
      # If no combination of button presses exists
      # to reach the final state, then skip
      if len(sequence) == 0:
         total_presses = math.inf
         
      # Otherwise, reduce joltages according to
      # button pushes.
      else:
         num_presses = sequence.count(True)
         next_joltages = [ j for j in final_joltages ]
         for s in range(len(sequence)):
            if sequence[s]:
               for w in wiring[s]:
                  next_joltages[w] -= 1

         # Skip if any joltage residues are
         # negative.
         if all([ j >= 0 for j in next_joltages ]):
            # All joltages are even; divide by two.
            if all([ (j % 2) == 0 for j in next_joltages ]):
               next_joltages = [ j // 2 for j in next_joltages ]

            # Recurse to find remaining joltages.
            # Total presses are 2x the results of
            # the recursive call plus the current
            # number of button pushes.
            next_config = (wiring, tuple(next_joltages))
            if next_config in found_states:
               total_presses = (2 * found_states[next_config]) + num_presses
            else:
               total_presses = (2 * findFewest(next_config)) + num_presses

            # Keep track of the minimum number of
            # button pushes.
            if total_presses < min_presses:
               min_presses = total_presses

   # Return the minimum number of button pushes.
   found_states[configuration] = min_presses
   return min_presses
         
         

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

   # Received help from Reddit on this one.
   
