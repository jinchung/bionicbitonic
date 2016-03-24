import math
import copy

'''
bitonic if it is monotonically increasing and 
then decreasing or it can be circular shifted to such

idea: count peaks or "changes"
if there are 1: true
if there are 2: test if the last value is greater / less than first depending on peak types
else: false
'''
def is_bitonic(xs):
    print('TBI')

def bitonic_split(random_input):
    n = len(random_input)
    max_k = int(math.log(n, 2))
    splits = [2**x for x in reversed(range(max_k))]
    for k in splits:
        for i in range(k):
            jump = int(n / k)
            start_idx = i*jump
            increasing = i % 2 == 0
            random_input[start_idx:start_idx+jump] = bitonic_merge(
                    random_input[start_idx:start_idx+jump], increasing)
    return random_input

def bitonic_merge(bitonic_seq, increasing):
    if len(bitonic_seq) <= 1:
        return bitonic_seq
    corr_idx_jump = int(len(bitonic_seq) / 2)
    for i in range(corr_idx_jump):
        corr_idx = i + corr_idx_jump
        if ((bitonic_seq[i] > bitonic_seq[corr_idx]) == increasing): 
           swap(bitonic_seq, i, corr_idx)  
    s1 = bitonic_merge(bitonic_seq[:corr_idx_jump], increasing)
    s2 = bitonic_merge(bitonic_seq[corr_idx_jump:], increasing)
    bitonic_seq = s1 + s2
    return bitonic_seq 

def swap(bitonic_seq, a, b):
    holder = bitonic_seq[a]
    bitonic_seq[a] = bitonic_seq[b]
    bitonic_seq[b] = holder

if __name__ == "__main__":
    # test bitonic merge
    bm = [2, 4, 6, 8, 7, 5, 3, 1]
    res = bitonic_merge(bm, True)
    print("testing bitonic merge: {}...{}".format(bm, res))

    # test bitonic split 
    bs = [1, 4, 2, 3, 6, 7, 5, 0]
    bs_cpy = copy.copy(bs)
    res = bitonic_split(bs)
    print("testing bitonic split: {}...{}".format(bs_cpy, res))

    # TODO: 
    # need to be able to support input that aren't divisible by 4
    # how would this be made parallelizable on a GPU
    # include more test cases
    # do comparisons with other sorts
