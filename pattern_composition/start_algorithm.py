import csv

#this file takes the frequent patterns as the output
# and produces
from pattern_composition.compose_patterns_optimised_pairs import composePatternOptPairs

csvfile = open('sample_input2.csv', 'r')
#csvfile = open('method_mining_input.csv', 'r')


csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')

Pns = next(csv_reader, None)
Yns = [int(i) for i in next(csv_reader, None)]

CoupledPY = [(i,j) for i,j in zip(Pns, Yns)]
# Pns is the set of patterns after the frequency mining, Pn is a particular pattern
# Yn is the frequency of patterns to happen, from the set Yns
# Cn is the predefined numbers of components we want to get
# K numbers of patterns given

print (sum(Yns))

# the problem that we are trying to solve is how to distribute the available patterns into
# Cn components
Cn = 40
# that will represent behaviour of the whole original input log

#TODO see these requirements
# length is the number of symbols allowed in the pattern
Length = 8
LoopsK = 1

# one of the ways to look at this problem is to solve the optimization problem
# MAX(sum_{on all components Cn} ( sum_{over all patterns in each component} ( Yi ) ) )
# where we look for maximum sum of all the Yi scores that compose Cn best patterns

#for that we need to define some rules on how to match the sequences

# it should have < and >, and the shortest length

# Constraints the  script if build to adhere to:
# 3. aggregate frequent sequences
# https://en.wikipedia.org/wiki/Knapsack_problem LP or greedy optimization
# Constraints: (1) size - at most n patterns;
# (2) length (tree depth) - at most k symbols per pattern;
# (3) completeness - each component must begin with a start symbol and end with the end symbol;
# (4) at most k loops per component


from itertools import chain, combinations
from compose_patterns import composePattern


# composePattern(CoupledPY, max_pattern_len=Length, max_loops_number= LoopsK)
composePatternOptPairs(CoupledPY, max_pattern_len=Length, max_loops_number= LoopsK , number_of_patterns_out=Cn)

# for the input from the file './sample_input.csv'
# the resulting patterns are:

# ---looking for patterns with a max pattern len: 6
# ---max loops allowed: 1
# ---number of patterns we are looking for: 5

# <QAF*> 11813 ['<Q', 'Q', 'QA', 'A', 'AF', 'QAF', 'F', 'F*', '*', 'QAF*', 'AF*', '*>']
# <1FAQ> 3718 ['<1', '1', '1F', 'FA', 'AQ', 'FAQ', 'Q>']
# <QA*A> 3203 ['<QA', 'A*', 'QA*', '*A', 'A>']
# <QR*2> 2117 ['<QR', 'QR', 'R', 'QR*', 'R*', '*2', '2', '2>']
# <Q*QF> 1009 ['<Q*', 'Q*', '*Q', 'QF', 'F>']

# Total score patternalized: 21860 / 34697
