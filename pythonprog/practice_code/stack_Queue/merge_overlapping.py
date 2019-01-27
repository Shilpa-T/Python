"""
Merge Overlapping Intervals

Given a set of time intervals in any order, merge all overlapping intervals into one and output the result
which should have only mutually exclusive intervals. Let the intervals be represented as pairs of integers for simplicity.
For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8} }.
The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}.
Similarly {5, 7} and {6, 8} should be merged and become {5, 8}

"""

def merge_intervals(intervals):
    """
    A simple algorithm can be used:
    1. Sort the intervals in increasing order
    2. Push the first interval on the stack
    3. Iterate through intervals and for each one compare current interval
       with the top of the stack and:
       A. If current interval does not overlap, push on to stack
       B. If current interval does overlap, merge both intervals in to one
          and push on to stack
    4. At the end return stack
    """
    si = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for tup in si:
        if not merged:
            merged.append(tup)
        else:
            b = merged.pop()
            if b[1] >= tup[0]:
                new_tup = tuple([b[0], tup[1]])
                merged.append(new_tup)
            else:
                merged.append(b)
                merged.append(tup)
    return merged

if __name__ == '__main__':

    l = [(5, 7), (11, 116), (3, 4), (10, 12), (6, 12)]
    l1=[ (5,7),(6,8), (1,3),(2,4)]
    l2 = [ (5,10),(3,6)]
    print "Original list of ranges: {}".format(l)
    merged_list = merge_intervals(l)
    print "List of ranges after merge_ranges: {}".format(merged_list)
    print "*********************************************"
    print "Original list of ranges: {}".format(l1)
    merged_list = merge_intervals(l1)
    print "List of ranges after merge_ranges: {}".format(merged_list)
    print "*********************************************"
    print "Original list of ranges: {}".format(l2)
    merged_list = merge_intervals(l2)
    print "List of ranges after merge_ranges: {}".format(merged_list)
