#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print("{:d}: {:d}".format(key, a_dictionary[key]))
