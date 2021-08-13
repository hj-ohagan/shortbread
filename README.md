# shortbread problem
### Toy problem given by my first company:
Given a file with a list of English words seperated by '/n', starting from the word "short" find a sequence of words that end in the word 'bread' by changing one letter at a time such that the changed word is still a valid word. 

E.g: (short -> shoot -> shoat) etc... is a valid sequence.

After getting a valid path, what about shortest path? What optimisations can be done?

This repo contains my initial solution written in 2016 as a fledgling software developer as well as my latest solution after coming back to the problem. Execution time improved from 95 +/- 1.6 ms to 19.70 +/- 0.44 ms (1 stdv over 100 trials).
