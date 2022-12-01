import argparse
import sys

def insert_ordered(list, number):
    if number > list[2]:
        if number >= list[1]:
            if number >= list[0]:
                list[2] = list[1]
                list[1] = list[0]
                list[0] = number
                
            else:
                list[2] = list[1]
                list[1] = number
        else:
            list[2] = number
    
        
                
def solution_2(file):

    three_best = [0] * 3
    deer_sum = 0
    
    for line in file:
        if line == '\n':
            insert_ordered(three_best, deer_sum)
            deer_sum = 0
        else:
            deer_sum += int(line)
    
    insert_ordered(three_best, deer_sum)
    deer_sum = 0
    
    print(three_best)
    return sum(three_best)


def solution_1(file):
    
    deer_sum = 0
    max_sum = 0
    
    for line in file:
        if line == '\n':
            max_sum = max(deer_sum, max_sum)
            deer_sum = 0
        else:
            deer_sum += int(line)
    
    # end of file
    max_sum = max(deer_sum, max_sum)
    deer_sum = 0
                
    return max_sum
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        required=True,
        help='Input file to process.')
    parser.add_argument(
        '--prob',
        dest='prob',
        required=True,
        help='Problem number')

    argv = sys.argv[1:]
    known_args, _ = parser.parse_known_args(argv)
    f = open(known_args.input, "r")
    problem = int(known_args.prob)
    solution_func = solution_1 if problem == 1 else solution_2
    print(solution_func(f))
