def allocate(total:int, weights: list[int]) -> list[int]:
    if not weights:
        raise ValueError("need at least one weight")
    if any(w<0 for w in weights):
        raise ValueError("weight has to be positive")

    weight_sum = sum(weights)
    shares = [total*w//weight_sum for w in weights]
    remainder = total - sum(shares)

    order = sorted(range(len(weights)), key =lambda i: (-(total*weights[i])%weight_sum, i))
    for i in order[:remainder]:
        shares[i]+=1
    return shares


