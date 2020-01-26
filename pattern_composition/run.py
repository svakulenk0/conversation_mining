#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 23, 2019
.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Run traces through pattern extraction and combination.
'''

import csv
import argparse
import requests

from itertools import chain, combinations
from compose_patterns import composePattern

# this file takes the frequent patterns as the output
from pattern_composition.compose_patterns_optimised_pairs import composePatternOptPairs
from pattern_composition.count_ngrams import frequent_loops

data_path = "../data/"


def compose_model(traces_path, length, LoopsK=1, vocabulary_path=None, Cn=40):
    vocabulary = {'<': 'START', '>': 'END'}
    if not vocabulary_path:
        # look-up default location
        vocabulary_path = traces_path.split('.')[0] + '.vocabulary.txt'
    with open(data_path+vocabulary_path) as v:
        for line in v.readlines():
            # print(line)
            symbol = line[0]
            label = line.strip('\n')[2:]
            vocabulary[symbol] = label

    # 1. load traces
    with open(data_path+traces_path) as t:
        log_string = t.read()
    traces = ["<%s>" % t for t in log_string.split('\n')]
    print("%d traces" % len(traces))
    print(traces[0])

    Pns, Yns, loop_ids = frequent_loops(traces, topn=250)
    # add loops to our vocabulary
    for k, v in loop_ids.items():
        loop_pattern = ' -> '.join([vocabulary[symbol] for symbol in k])
        vocabulary[str(v)] = '(%s)'%loop_pattern
    # print(vocabulary['1'])

    # input is a list of tuples (pattern, count)
    CoupledPY = [(i,j) for i,j in zip(Pns, Yns)]

    patterns = {}
    # print('loops', loop_ids.values())
    loop_symbols = [str(l) for l in loop_ids.values()]
    
    for l in range(2, length+1):
        print(l)
        solution_patterns = composePatternOptPairs(CoupledPY, max_pattern_len=l, max_loops_number=LoopsK , number_of_patterns_out=Cn)

        for i in solution_patterns:
            if i[2] < 1:
                break
            loop = False
            decoded_model = []
            for symbol in i[0].pattern_composed_now:
                if symbol in loop_symbols:
                    loop = True
                decoded_model.append(vocabulary[symbol])

            # report only patterns with loops
            if loop:
                decoded_model = ' -> '.join(decoded_model)
                decoded_patterns = []
                for pattern in i[1]:
                    decoded_patterns.append(' -> '.join([vocabulary[symbol]  for symbol in pattern]))
                patterns[decoded_model] = (i[2], decoded_patterns)

    sorted_patterns_keys = sorted(patterns, reverse=True, key=patterns.get)
    with open(data_path+traces_path.split('.')[0] + '.output.txt', 'w') as out_file:
        out_file.writelines([' '.join([str(patterns[pattern]), pattern])+'\n' for pattern in sorted_patterns_keys])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to the file with traces")
    parser.add_argument("l", help="pattern length", default=5)
    args = parser.parse_args()
    compose_model(args.path, int(args.l))
