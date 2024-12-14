#!/usr/local/bin/python3
import sys
# import re
# import math
# from collections import defaultdict
# from collections import Counter
# import itertools
# from copy import deepcopy
# import numpy as np


def main(input_file, _):
    lines = input_file.read().splitlines()


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
