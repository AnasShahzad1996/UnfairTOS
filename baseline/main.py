import numpy as np
import torch

import datasets


def main():
    '''Main function starts baseline'''
    print ("Start conducting the baseline experiment")
    new_dataset = datasets.load_dataset('lex_glue','unfair_tos')

    

if __name__ == '__main__':
    main()
