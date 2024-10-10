# alist => [T, T, F, F, F]

{
    "T": 2,
    "F": 3
}
def solution(alist):
    collect = {}
    for light in alist:
        if light in collect:
            collect[light] += 1
        else:
            collect[light] = 1

    if collect["F"] >= 2:
        return "Outage"
    else:
        return "Power"
