import argparse
import sys


def solution_2(f):
    
    rules_dic = {
        'A': {
            # lose - cissor
            'X': 3,
            # draw - rock
            'Y': 4,
            # win - paper
            'Z': 8
        },
        #paper
        'B': {
            # lose - rock
            'X': 1,
            # draw - paper
            'Y': 5,
            # win - cissor
            'Z': 9
        },
        #cissor
        'C': {
            # lose - paper
            'X': 2,
            # draw - cissor
            'Y': 6,
            # win - rock
            'Z': 7
        },
        
    }
    sum_points = 0
    for line in f:
        choiches = line.strip().split(' ')
        adv_choice = choiches[0]
        my_choice = choiches[1]
        
        sum_points += rules_dic[adv_choice][my_choice]
    return sum_points
            


def solution_1(f):
    points_dic = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    rules_dic = {
        'X': {
            'A': 3,
            'B': 0,
            'C': 6
        },
        'Y': {
            'A': 6,
            'B': 3,
            'C': 0
        },
        'Z': {
            'A': 0,
            'B': 6,
            'C': 3
        }
    }
    return solution_1_calculation(f, points_dic, rules_dic)




def solution_1_calculation(f, points_dic, rules_dic):
    sum_points = 0
    for line in f:
        choiches = line.strip().split(' ')
        adv_choice = choiches[0]
        my_choice = choiches[1]
        sum_points += (points_dic[my_choice] + rules_dic[my_choice][adv_choice])
    return sum_points


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
