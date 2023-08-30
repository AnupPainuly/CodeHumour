'''
Input : 
A = [4, 2, 7]
B = [5, 6, 3]
Output : 
1 2

'''
def scoresCard(a,b):
    score_a, score_b = 0, 0
    for i,j in zip(a,b):
        if i > j:
            score_a += 1
        elif i < j:
            score_b += 1
    return score_a, score_b


if __name__ == "__main__":
    a = [4, 2, 7]
    b = [5, 6, 3]
    print(scoresCard(a,b))

