from collections import defaultdict, deque

def earliest_ancestor(ancestors, starting_node):
    parents = defaultdict(set)

    for parent, child in ancestors:
        parents[child].add(parent)

    if len(parents[starting_node]) == 0:
        return -1

    def earliest_recur(node, depth=0):
        neighbors = parents[node]
        if len(neighbors) == 0:
            return node, depth
        else:
            ancestors = [
                earliest_recur(parent, depth=depth + 1) for parent in neighbors
                ]
            print('ancestors', ancestors)
            max_depth = max(ancestors, key = lambda pair: pair[1])[1]
            print(max_depth)
            oldest = [a for a in ancestors if a[1] == max_depth]
            return min(oldest, key = lambda pair: pair[0])

    return earliest_recur(starting_node)[0]
'''
    deepest_depth = 0
    oldest_ancestor = starting_node
    queue = deque()
    queue.appendleft(starting_node)
    visited = set()
    while len(queue) > 0:
        node = queue.pop()
        visited.add(node)
        neighbors = parents[node]
        if len(neighbors) == 0 and len(queue) == 0:
            return node
        else:
            queue.extendleft(neighbors)
'''
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))