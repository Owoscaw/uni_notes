def divisors(n):
    return [i for i in range(1,n) if n%i == 0]

def aliquot_succ(n):
    return sum(divisors(n))

def aliquot_sequence(n):
    aliseq = [n]
    while (n != aliseq[-1] and aliseq[-1] != 0) or len(aliseq) == 1:
        aliseq.append(aliquot_succ(aliseq[-1]))
        
    return aliseq

def aliquot_pairs(alst):
    aliquot_pairs_lst = []
    for i in alst:
        aliseq_n = aliquot_sequence(i)

        for j in aliseq_n:
            new_pair = [j, aliquot_succ(j)]
            if new_pair not in aliquot_pairs_lst:
                aliquot_pairs_lst.append(new_pair)

    return aliquot_pairs_lst


print(aliquot_pairs([6, 8, 10, 18]))