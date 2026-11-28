def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    sum = {}
    cnt = {}
    for cat, t in zip(categories, targets):
        sum[cat] = sum.get(cat, 0.0) + t 
        cnt[cat] = cnt.get(cat, 0) + 1
    mean = {cat: sum[cat] / cnt[cat] for cat in sum}
    return [mean[cat] for cat in categories]
    