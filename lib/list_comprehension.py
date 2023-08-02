#!/usr/bin/env python3

def return_evens(num_list):
    nums = []
    for num in num_list:
        if num % 2 == 0:
            nums.append(num)
    return nums

def make_exclamation(sentence_list):
    ex_list = [sentence + "!" for sentence in sentence_list]
    return ex_list