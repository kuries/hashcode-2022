from main import scorer
import random

def solution(num_of_customers, likes_dislikes):
    ing_likes = {}
    ing_dislikes = {}
    dis_ing = []
    for i in range(int(num_of_customers)):
        like = likes_dislikes[2*i]
        dislike = likes_dislikes[2*i+1]
        l_cnt, l_ing = like.split(" ")[0], like.split(" ")[1:]
        d_cnt, d_ing = dislike.split(" ")[0], dislike.split(" ")[1:]
        l_ing = list(l_ing)
        d_ing = list(d_ing)
        for j in range(int(l_cnt)):
            if l_ing[j] not in dis_ing:
                dis_ing.append(l_ing[j])
            if l_ing[j] in ing_likes.keys():
                ing_likes[l_ing[j]] += 1
            else:
                ing_likes.update({l_ing[j]:1})

        for j in range(int(d_cnt)):
            if d_ing[j] not in dis_ing:
                dis_ing.append(d_ing[j])
            if d_ing[j] in ing_dislikes.keys():
                ing_dislikes[d_ing[j]] += 1
            else:
                ing_dislikes.update({d_ing[j]:1})
    
    ldd = {}
    for ing in dis_ing:
        ldd.update({ing:0})
        if ing in ing_likes.keys():
            ldd[ing] += ing_likes[ing]
        if ing in ing_dislikes.keys():
            ldd[ing] -= ing_dislikes[ing]
        if ldd[ing] < 0:
            del ldd[ing]
    ldd = dict(reversed(sorted(ldd.items(), key = lambda item: item[1])))
    max_score = 0
    all_scores = []
    ans = []
    for i in range(100):
        n_rand = random.randint(int(len(ldd) / 2), len(ldd) - 1)
        keys = random.sample(list(ldd), n_rand)
        score = scorer(num_of_customers, likes_dislikes, keys)
        all_scores.append(score)
        if score > max_score:
            max_score = score
            ans = keys
    # print(all_scores, "\nMax Score:",max_score)
    return ans