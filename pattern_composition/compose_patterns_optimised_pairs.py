import copy

class Node:
    def __init__(self, pattern_composed_now = '', patterns_used = {}, score_composed_now = 0):
        self.pattern_composed_now = pattern_composed_now
        self.patterns_used = patterns_used

        self.score_composed_now = score_composed_now # the more the better


def composePatternOptPairs(patterns, max_pattern_len = 6, number_of_patterns_out = 5, max_loops_number = 1):
    print ("---looking for patterns with a max pattern len: " + str(max_pattern_len))
    print ("---max loops allowed: " + str(max_loops_number))
    print ("---number of patterns we are looking for: " + str(number_of_patterns_out))

    print (patterns)

    p_other = {}
    p_pairs = {}
    p_start = []
    MAX_pattern_length = 0
    for pattern in patterns:
        if len(pattern[0]) == 2:
            if pattern[0][0] == '<':
                p_start.append((pattern[0][1], pattern[1]))
            else:
                if not pattern[0][0] in p_pairs:
                    p_pairs[pattern[0][0]] = []
                p_pairs[pattern[0][0]].append((pattern[0][1], pattern[1]))
        else:
            # this set is only to add the points to overall solution
            # possible to set to higher points for longer patterns
            p_other[pattern[0]] = pattern[1]
            if len(pattern[0]) > MAX_pattern_length:
                print(pattern[0])
                MAX_pattern_length = len(pattern[0])
    if '<' in p_other:
        del p_other['<']
    if '>' in p_other:
        del p_other['>']

    roots = set([Node(pattern_composed_now=i[0], patterns_used={'<' + i[0]: i[1]}, score_composed_now=i[1]) for i in p_start])

    ######################################################################################
    ######################################################################################
    ## This first step finds all patterns
    ######################################################################################

    composed_patterns = list()
    new_set = set()

    def too_much_loops(patt,max_loops_number):
        count = 0
        for i in patt:
            if i.isdigit():
                count += 1
        return count > max_loops_number

    count_steps = 1
    while(roots):
        print ("Step #: " + str(count_steps))
        count_steps+=1

        for patt in roots:
            if patt.pattern_composed_now[-1] == '>':
                patt.pattern_composed_now = patt.pattern_composed_now[0:-1]
                composed_patterns.append(patt)
            elif (len(patt.pattern_composed_now) <= max_pattern_len) and patt.pattern_composed_now[-1] in p_pairs:
                matching_pairs = p_pairs[patt.pattern_composed_now[-1]]
                for p in matching_pairs:

#                    if not too_much_loops(patt.pattern_composed_now[-1]+p[0], max_loops_number):
                   if not too_much_loops(patt.pattern_composed_now+p[0], max_loops_number):
                        pattern_composed_now = (patt.pattern_composed_now + p[0])
                        patterns_used = patt.patterns_used.copy()
                        patterns_used[patt.pattern_composed_now[-1] + p[0]] = p[1]
                        #score_composed_now = patt.score_composed_now + p[1]

                        # here we add any other patterns and their score to the overall pattern
                        for i in range(1, MAX_pattern_length):
                            if pattern_composed_now[-i:] in  p_other:
                                patterns_used[pattern_composed_now[-i:]] = p_other[pattern_composed_now[-i:]]
                                #score_composed_now += p_other[pattern_composed_now[-i:]]


                        new_set.add(Node(pattern_composed_now=pattern_composed_now,
                                     patterns_used=patterns_used))
                                    # ,score_composed_now=score_composed_now))
        roots = new_set
        new_set = set()


    ######################################################################################
    ######################################################################################
    ## This step is used to find "number_of_patterns_out" best patterns
    ######################################################################################

    print(" Finding " + str(number_of_patterns_out) + " best patterns now")
    solution_patterns = []
    patterns_used_in_solution = set()

    max_val = 0
    pat_candidate = None

    for i in range(number_of_patterns_out):
        score_tem = 0
        for pat in composed_patterns:
            for fp in pat.patterns_used:
                if not fp in patterns_used_in_solution:
                    score_tem += pat.patterns_used[fp]
            pat.score_composed_now = score_tem
            if score_tem > max_val:
                max_val = score_tem
                pat_candidate = pat
            score_tem = 0

        solution_patterns.append([copy.deepcopy(pat_candidate), set(pat_candidate.patterns_used.keys()).difference(patterns_used_in_solution), max_val])
        patterns_used_in_solution.update(pat_candidate.patterns_used.keys())

        max_val = 0

    #print(solution_patterns)

    for i in solution_patterns:
        # print(i[0].pattern_composed_now + " : " + str(i[1]) + ' : ' + str(i[2]))
        print(str([i[0].pattern_composed_now, i[1],i[2]])+ ',')

    print ("End of the calculations")

    return solution_patterns