#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
12 Feb 2017

Store corpus in CSV format
Run with python dstc1_to_csv.py --dataset=train3.half2 --dataroot=../data
'''

import sys,os,argparse,shutil,glob,json,copy,time, csv
install_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
utils_dirname = os.path.join(install_path,'lib')
sys.path.append(utils_dirname)
from dataset_walker import dataset_walker


SLOTS = ['route','from.desc','from.neighborhood','from.monument','to.desc','to.neighborhood','to.monument','date','time']
DATASETS = ['test1', 'test2', 'test3', 'test4', 'train1a', 'train1b', 'train1c', 'train2', 'train3']

def parse_data(csv_writer, dataroot='../data'):
    for dataset in DATASETS:
        sessions = dataset_walker(dataset, dataroot=dataroot, labels=False)
        
        for session in sessions:
            print session.log['session-id']
            for turn_index, (log_turn, scratch) in enumerate(session):
                # systems's utterance
                acts = [{u'slots': None, u'act': None}]
                transcript = None
                start_time = None
                end_time = None
                if 'start-time' in log_turn['output'].keys():
                    start_time = log_turn['output']['start-time']
                if 'end-time' in log_turn['output'].keys():
                    end_time = log_turn['output']['end-time']
                if 'transcript' in log_turn['output'].keys():
                    transcript = log_turn['output']['transcript']
                if 'dialog-acts' in log_turn['output'].keys():
                    acts = log_turn['output']['dialog-acts']
                for act in acts:
                    # conversation id, role id, turn id, act, slots, transcript, start time
                    csv_writer.writerow([session.log['session-id'], 'S', turn_index, act['act'], act['slots'], transcript, start_time, end_time])

                # user's utterance
                slu_hyp = [{u'slots': None, u'act': None}]
                asr_hyp = None
                asr_hyps = log_turn['input']['live']['asr-hyps']
                if asr_hyps:
                    asr_hyp = asr_hyps[0]['asr-hyp']
                start_time = None
                end_time = None
                if 'start-time' in log_turn['input'].keys():
                    start_time = log_turn['input']['start-time']
                if 'end-time' in log_turn['input'].keys():
                    end_time = log_turn['input']['end-time']
                slu_hyps = log_turn['input']['live']['slu-hyps']
                if slu_hyps:
                    slu_hyp = slu_hyps[0]['slu-hyp']
                for act in slu_hyp:
                    # conversation id, role id, turn id, act, slots, transcript, start time
                    csv_writer.writerow([session.log['session-id'], 'U', turn_index, act['act'], act['slots'], asr_hyp, start_time, end_time])

if (__name__ == '__main__'):
    with open('dstc1.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)
        parse_data(csv_writer)
