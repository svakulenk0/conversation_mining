#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 23, 2019
.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Extract sequences frequent across traces
after https://stackoverflow.com/questions/40556491/how-to-find-the-longest-common-substring-of-multiple-strings
'''
from functools import partial, reduce
from itertools import chain
from typing import Iterator

from collections import Counter


def ngram(seq: str, n: int) -> Iterator[str]:
    return (seq[i: i+n] for i in range(0, len(seq)-n+1))


def allngram(seq: str, minn=1, maxn=None) -> Iterator[str]:
    lengths = range(minn, maxn) if maxn else range(minn, len(seq))
    ngrams = map(partial(ngram, seq), lengths)
    return set(chain.from_iterable(ngrams))


def frequent_ngrams(strings, min_support=None, topn=5):
    
    # 1.split traces into ngrams
    seqs_ngrams = map(allngram, strings)
    # 2.count ngram frequencies
    counts = Counter(chain.from_iterable(seqs_ngrams))
    
#     return counts.most_common(topn)
    # 3.filter frequent substrings
    # set frequency threshold if not specified
    if not min_support:
        most_frequent_s = [s for s, count in counts.most_common(topn)]
        # maximum frequency
#         most_frequent1 = counts.most_common(1)[0]
#         min_support = most_frequent1[1]
    else:
#         print(min_support)
        most_frequent={string: count for string, count in counts.items() if count >= min_support}
    #     print(most_frequent)
        most_frequent_s = list(most_frequent.keys())
    
    return most_frequent_s, [counts[s] for s in most_frequent_s]
    
# group repeating chars into loops with () symbols
from collections import defaultdict


def frequent_loops(traces, topn=500):
    '''
    collect frequent patterns with loops
    '''
    # get frequent ngram patterns
    patterns, counts = frequent_ngrams(traces, topn=topn)
    
    loop_patterns = Counter()
    loop_patterns_num = {}
    loops = defaultdict(int)
    loop_ids = {}
    n_loops = 0
    for i, pattern in enumerate(patterns):
        loop_pattern, loop_pattern_num = "", ""
        for c in pattern:
            if c not in loop_pattern:
                loop_pattern += c
                loop_pattern_num += c
            else:
                loop_start_idx = loop_pattern.index(c)
                loop = ''.join([c for c in loop_pattern[loop_start_idx:] if c not in '()'])
                if len(loop) > 1:
                    loop_set = loop
    #                 loop_set = "".join(set(loop))
                    if loop_set not in loops:
                        n_loops += 1
                        loops[loop_set] += counts[i]
                        loop_ids[loop_set] = n_loops
                    loop_pattern = ''.join([c for c in loop_pattern[:loop_start_idx] if c not in '()']) + "(%s)" % loop
                    loop_pattern_num = ''.join([c for c in loop_pattern[:loop_start_idx] if c not in '()']) + str(loop_ids[loop_set])
    #     if not numeric and loop_pattern != pattern:
    #         print(pattern)
    #         print (loop_pattern)
    #         print('\n')
    #     if loop_pattern_num:
        loop_patterns_num[loop_pattern] = loop_pattern_num
        loop_patterns[loop_pattern] += counts[i]
#     print((list(loop_patterns.keys()), list(loop_patterns.values())))
#     print(loops)

    # show loop encoding
    # print(loop_ids)
    patterns_w_loop_ids = [loop_patterns_num[p] if p in loop_patterns_num else p for p, c in loop_patterns.most_common()]
    counts = [c for p, c in loop_patterns.most_common()]
    return patterns_w_loop_ids, counts, loop_ids


if __name__ == '__main__':
    a, b = frequent_loops(traces, topn=250)
    # show extracted patterns
    ptns = ''
    cnts = ''
    for i in a:
        ptns += i + ','
    for i in b:
        cnts += str(i) + ','
        
    print (ptns)
    print (cnts)