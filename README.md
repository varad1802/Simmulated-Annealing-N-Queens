# Simmulated-Annealing-N-Queens
Solving N-Queens Problem by Simmulated Annealing. This Project was submitted as a part of Intelligent Systems Coursework un Dr. Dewan Ahmed at UNC, Charlotte

## Summary of the Program
* The simulated annealing program begins with the user entering the no of queens required on board and the no of iterations on which the program should iterate.
* An initial board configuration is selected at random by placing one queen in each row. 
* The heuristic value is calculated based on the no of attacks present on the board.
* The initial temperature is set to a high value(4000 in the code)
* A random new state is selected and its heuristic value is calculated.
* The heuristic values of current state and new state are compared and accepted based on the following criteria:
  * The heuristic value of the new state is less than the current state.
  * The heuristic is greater than the current state but is within the bounds of the temperature.
* If these requirements are satisfied, we move to the new state and continue.
* We continue this process till the heuristic of the current state is zero, i.e., we have found a solution or the no of iterations are completed.
* For every iteration, we decrease the temperature. The temperature thus decreases exponentially as the algorithm progresses.
* By doing this, we avoid getting trapped in local minima early on in the algorithm but start to hone in on a viable solution by the time the algorithm ends.

## Parameters to run the Program
* Download the code NQueen_Simulated_Annealing.py
* Run the code by typing the following command on terminal:<br />
	**```py NQueen_Simulated_Annealing.py```**
* The program will run and ask for the no of queens. Enter any value above 3 as the queen problem cannot be solved for boards less than 4.
* Then the program will ask for the no of iterations for which you want to run the algorithm. Simulated annealing will most likely give a solution for 150000 iterations and above.

## Output
### Case 1: Successful run for 8 Queens
```
Enter number of Queens:
8
Enter number of iterations:
170000
Initial Board Configuration:
[['-' '-' '-' '-' '-' '-' 'Q' '-']
 ['-' '-' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' '-' '-']
 ['-' 'Q' 'Q' '-' 'Q' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' '-' 'Q']
 ['Q' '-' '-' 'Q' '-' 'Q' '-' '-']]
Solution found!
[['-' 'Q' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' '-' 'Q']
 ['-' '-' '-' '-' '-' 'Q' '-' '-']
 ['Q' '-' '-' '-' '-' '-' '-' '-']
 ['-' '-' 'Q' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' 'Q' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' 'Q' '-']
 ['-' '-' '-' 'Q' '-' '-' '-' '-']]
 ```
 
### Case 2: Unsuccessful run for 8 Queens
```
Enter number of Queens:
8
Enter number of iterations:
150000
Initial Board Configuration:
[['-' '-' '-' '-' '-' '-' '-' '-']
 ['Q' '-' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' 'Q' 'Q' '-' '-' '-']
 ['-' 'Q' '-' '-' '-' '-' '-' 'Q']
 ['-' '-' '-' '-' '-' 'Q' '-' '-']
 ['-' '-' '-' '-' '-' '-' '-' '-']
 ['-' '-' 'Q' '-' '-' '-' 'Q' '-']]
The algorithm was unsuccessful in finding any solution!
```
