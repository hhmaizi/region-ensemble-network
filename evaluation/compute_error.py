import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from util import get_errors


def print_usage():
    print('usage: {} icvl/nyu in_file'.format(sys.argv[0]))
    exit(-1)


def draw_error(dataset, errs):
    if dataset == 'icvl':
        joint_idx = [0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16]
        names = ['Palm', 'Thumb.R', 'Thumb.T', 'Index.R', 'Index.T', 'Mid.R', 'Mid.T', 'Ring.R', 'Ring.T', 'Pinky.R', 'Pinky.T', 'Mean']
    elif dataset == 'nyu':
        joint_idx = [0, 1, 2, 5, 3, 13, 12, 11, 10, 9, 8, 7, 6, 14];
        names = ['Palm', 'Wrist1', 'Wrist2', 'Thumb.R', 'Thumb.T', 'Index.R', 'Index.T', 'Mid.R', 'Mid.T', 'Ring.R', 'Ring.T', 'Pinky.R', 'Pinky.T', 'Mean'];

    fig = plt.figure()
    x = np.arange(len(joint_idx))
    plt.bar(x, errs[joint_idx])
    # plt.xlim([0.4, len(joint_idx) + 0.6])
    plt.xticks(x + 0.5, names, rotation='vertical')
    plt.ylabel('Mean Error (mm)')
    plt.show()
    

def main():
    if len(sys.argv) < 3:
        print_usage()

    dataset = sys.argv[1]
    in_file = sys.argv[2]

    errs = get_errors(dataset, in_file)
    mean_errs = np.mean(errs, axis=0)
    mean_errs = np.append(mean_errs, np.mean(mean_errs))
    print('mean error: {:.2f}mm'.format(mean_errs[-1]))

    draw_error(dataset, mean_errs)


if __name__ == '__main__':
    main()
