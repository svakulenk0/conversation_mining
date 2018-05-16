#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
16 May 2017

Pick indices at random to generate process log splits for model validation.
'''
import numpy as np

n_dialogues = 15866
test_split = 0.2
n_samples = int(n_dialogues * 0.2)
print n_samples, 'test samples out of', n_dialogues


all_indices = range(n_dialogues)
assert len(all_indices) == n_dialogues
test_indices = np.random.choice(n_dialogues, n_samples, replace=False)
assert len(test_indices) == n_samples
development_indices = [i for i in all_indices if i not in test_indices]
assert len(development_indices) == n_dialogues - n_samples
