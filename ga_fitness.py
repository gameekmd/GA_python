def calc_fitness( trial_genome ):
 import numpy, random
###
##
## Calculate fitness of "genes", passed from genetic algorithm in "ga.py"
##
## Fitness = EXP [ - SUM_i ( target_V - trial_V ) ^ 2 ]
##
## 0 <= i <= len(r_list)
##
###
 scaling_factor=1000.0 # used to sensitize fitness function
# define values of "r" for which to calculate "V"
 r_list=[2.0,2.5,3.0,3.5,4.0,4.5,5.0]
 best_genome=[12.0,9.0,6.0]
 exp_argument=0.0
 exact_V=[0.0 for i in range(len(r_list))]
 trial_V=[0.0 for i in range(len(r_list))]
 for i in range(len(r_list)):
# define the argument of the exponential in the fitness function
  trial_V=0.0
  exact_V=0.0
# Define the ratio of the r coordinates
  for j in range(len(trial_genome)):
   V = trial_genome[j] * r_list[i] ** (j+1)
   trial_V = trial_V + V
  for j in range(len(best_genome)):
   V = best_genome[j] * r_list[i] ** (j+1)
   exact_V = exact_V + V

# define the argument of the exponential in the fitness function
  exp_argument = exp_argument + ( exact_V - trial_V ) ** 2.0

 fitness=numpy.exp( - ( 1.0 / exp_argument ) / scaling_factor )
# print "fitness=",fitness

 return fitness
