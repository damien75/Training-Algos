from typing import Dict, List


class CutTheTreeIn2(object):
    """
    Source Hackerrank / Algorithms / Search / Cut the Tree

    Input: tree with weights

    Goal: cut in 2 trees with minimal total weight difference

    Idea: keep a dict of the connected nodes and a list of the weights
    Using DFS with a set of visited nodes and a stack of nodes to visit,
    Add the weight of the current subtree to the parent so that sutTotals gives the weight of the subtree
    when we move up
    subTotals : node => weight of its subtree with node as root
    and the best difference so far
    """

    @staticmethod
    def min_diff_cut(graph: Dict[int, List[int]], weights: List[int], vertex: int) -> int:
        total = sum(weights)
        visited = set()
        best_diff = total
        to_visit = [vertex]
        to_visit_set = set()
        # Adding this set instead of just having the toVisit list increases speed drastically when checking if next_vtx
        # has already been seen and is in the toVisit
        to_visit_set.add(vertex)
        sub_totals = {vertex: weights[vertex] for vertex in graph.keys()}
        while len(to_visit) > 0:
            curr_vertex = to_visit[-1]
            has_children_not_visited = False
            for next_vtx in graph[curr_vertex]:
                if next_vtx in visited or next_vtx in to_visit_set:
                    # we need to check if it is in the list to visit but is not yet considered visited,
                    # even if it's in the list
                    continue
                to_visit.append(next_vtx)
                to_visit_set.add(next_vtx)
                has_children_not_visited = True
            if not has_children_not_visited:
                visited.add(curr_vertex)
                to_visit.pop()  # we have visited all its children, we can now remove this node from the list to visit
                for next_vtx in graph[curr_vertex]:
                    if next_vtx not in visited:
                        sub_totals[next_vtx] += sub_totals[curr_vertex]  # we update the weight of its parent
                best_diff = min(best_diff, abs(2 * sub_totals[curr_vertex] - total))
        return best_diff

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        nb_nodes = int(input())
        weights = list(map(int, input().split()))
        tree = {i: [] for i in range(nb_nodes)}
        for _ in range(nb_nodes - 1):
            parent, child = map(int, input().split())
            tree[parent - 1].append(child - 1)
            tree[child - 1].append(parent - 1)
        print(self.min_diff_cut(tree, weights, 0))
