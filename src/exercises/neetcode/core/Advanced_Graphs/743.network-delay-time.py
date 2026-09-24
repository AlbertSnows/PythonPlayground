"""
743. Network Delay Time
Difficulty: Medium
https://leetcode.com/problems/network-delay-time/

──────────────────────────────────────────────────

You are given a network of n nodes, labeled from 1 to n. You are also
given times, a list of travel times as directed edges times[i] = (ui,
vi, wi), where ui is the source node, vi is the target node, and wi is
the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it
takes for all the n nodes to receive the signal. If it is impossible
for all the n nodes to receive the signal, return -1.

 

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

 

Constraints:

	• 1 <= k <= n <= 100

	• 1 <= times.length <= 6000

	• times[i].length == 3

	• 1 <= ui, vi <= n

	• ui != vi

	• 0 <= wi <= 100

	• All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
# todo! revisit
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # You are given a network of n nodes, labeled from 1 to n. You are also
        # given times, a list of travel times as directed edges times[i] = (ui,
        # vi, wi), where ui is the source node, vi is the target node, and wi is
        # the time it takes for a signal to travel from source to target.

        # We will send a signal from a given node k. Return the minimum time it
        # takes for all the n nodes to receive the signal. If it is impossible
        # for all the n nodes to receive the signal, return -1.
        # 2 1 1
        # source node = 2
        # target node = 1
        # duration = 1
        # k = starting node

        path_to_fastest: dict[(int, int), int] = {}
        source_to_dests: dict[int, set[int]] = {}
        for node_info in times:
            source = node_info[0]
            dest = node_info[1]
            dur = node_info[2]
            # populate path to fastest
            pair = (source, dest)
            path_to_fastest[pair] = max(path_to_fastest.get(pair, 0), dur)

            if source not in source_to_dests:
                source_to_dests[source] = {dest}
            else: 
                source_to_dests[source].add(dest)




        remaining = set(range(n))
        if k not in remaining:
            return -1

        remaining.remove(k)
        outcome = find_fastest_path(remaining, k, source_to_dests, path_to_fastest)
        return outcome



def find_fastest_path(
    remaining: set[int], 
    source: int, 
    source_to_dests: dict[int, set[int]],
    path_to_fastest: dict[(int, int), int]):

    if len(remaining) == 0:
        return 0

    possible_paths = source_to_dests.get(source, -1)
    if possible_paths == -1:
        return -1
    paths_to_check: set[int] = set(filter(lambda p: p in remaining, possible_paths))
    if len(paths_to_check) == 0:
        return -1

    fastest = -1
    for dest in paths_to_check:
        pair = (source, dest)
        path_exists = pair in path_to_fastest
        if path_exists:
            local_remaining = remaining.copy()
            local_remaining.remove(dest)
            local_fastest = find_fastest_path(local_remaining, dest, source_to_dests, path_to_fastest)

            if local_fastest != -1:
                fastest = max(fastest, local_fastest)
    return fastest

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
        (([[1, 2, 1]], 2, 1), 1),
        (([[1, 2, 1]], 2, 2), -1),
    ]
    for (args, expected) in tests:
        result = sol.networkDelayTime(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: networkDelayTime{args} -> {result} (expected {expected})")
