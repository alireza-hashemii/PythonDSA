# 2- Three-Way Set Disjointness - O(N^3)
def three_set_disjoint(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a ==b==c:
                    return False
    return True


# 2- Three-Way Set Disjointness . An alternative - O(N^2)
def three_set_disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a ==c:
                        return False
    return True