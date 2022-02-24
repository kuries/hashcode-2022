#!/usr/bin/env pypy
import argparse
from pickle import TRUE
import solutions.template as solution


def scorer(num_of_customers, likes_dislikes, ingredients_list):
    score = 0
    ingredients_list = set(ingredients_list)
    for i in range(int(num_of_customers)):
        like = likes_dislikes[2*i]
        dislike = likes_dislikes[2*i+1]
        l_cnt, l_ing = like.split(" ")[0], like.split(" ")[1:]
        d_cnt, d_ing = dislike.split(" ")[0], dislike.split(" ")[1:]
        
        if len(set(l_ing)) != 0 and not set(l_ing).issubset(ingredients_list) and set(l_ing):
            continue
        if len(set(d_ing)) != 0 and set(d_ing).issubset(ingredients_list):
            continue
        
        score += 1
    return score
            

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('testcase')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    file = open(args.testcase, "r")
    lines = file.read().splitlines()
    num_of_customers = lines[0]
    likes_dislikes = lines[1:]
    ingredients_list = solution.solution(num_of_customers, likes_dislikes)
    score = scorer(num_of_customers, likes_dislikes, ingredients_list)
    print(score)
    