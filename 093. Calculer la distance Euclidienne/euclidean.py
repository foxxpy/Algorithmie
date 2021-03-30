from math import sqrt

def distance_euclidienne(pt1, pt2):
    """Calcule la distance euclidienne entre deux points pour n'importe quelle dimension"""

    if len(pt1) != len(pt2):
        return None

    pt_zip = zip(pt1, pt2)
    pt_sum_difference = [(x[0] - x[1])**2 for x in pt_zip]
    pt_sum = sum(pt_sum_difference)
    distance = sqrt(pt_sum)
    return distance
