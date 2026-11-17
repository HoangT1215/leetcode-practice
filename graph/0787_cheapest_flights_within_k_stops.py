"""LeetCode 787: Cheapest Flights Within K Stops.

Problem: https://leetcode.com/problems/cheapest-flights-within-k-stops/

Let m = len(flights).
All space bounds below exclude the input.

Active Bellman-Ford solution:
    Time: O(k(m+n)) for k >= 1. Each round copies n costs and scans m flights.
    When k = 0, the single round takes O(m+n) time.
    The copy matters: the precise bound includes n, not just the edge count m.
    Auxiliary space: O(n). Only cost and next_cost are stored; rounds do not
    accumulate separate arrays.

Commented naive route-enumeration solution:
    Let b be the maximum outgoing degree and W = 1 + b + ... + b**(k + 1).
    There can be up to W route states, since the same city can be revisited
    through many different routes without deduplication.
    Time: O(n + m + k + W), including adjacency construction and the cost array.
    Auxiliary space: O(n + m + k + W). Advancing head does not remove processed
    queue entries, so the list retains all enqueued route states.
    For b >= 2, W = O(b**(k + 1)): the worst-case growth is exponential in k.
"""


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: list[list[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        # --- Naive approach
        # adjacency_list = [[] for _ in range(n)]

        # for start, end, price in flights:
        #     adjacency_list[start].append((end, price))

        # # cost[e] = cheapest route to dst using exactly e flights
        # cost = [float("inf")] * (k + 2)

        # # (current city, total cost, flights already used)
        # queue = [(src, 0, 0)]
        # head = 0

        # while head < len(queue):
        #     node, current_cost, flights_used = queue[head]
        #     head += 1

        #     # At most k stops means at most k + 1 flights.
        #     if flights_used == k + 1:
        #         continue

        #     for neighbor, edge_cost in adjacency_list[node]:
        #         new_cost = current_cost + edge_cost
        #         new_flights_used = flights_used + 1

        #         if neighbor == dst:
        #             cost[new_flights_used] = min(
        #                 cost[new_flights_used],
        #                 new_cost,
        #             )
        #         else:
        #             queue.append(
        #                 (neighbor, new_cost, new_flights_used)
        #             )

        # answer = min(cost)
        # return answer if answer < float("inf") else -1

        # --- Bellman-Ford algorithm
        # cost[v] is the cheapest cost to reach v using at most the number of
        # flights allowed by the completed relaxation rounds.
        cost = [float("inf")] * n
        cost[src] = 0

        # At most k stops means at most k + 1 flights.
        for _ in range(k + 1):
            # Read from cost and write to a copy so that one round adds at
            # most one flight to a route.
            next_cost = cost.copy()

            for start, end, price in flights:
                if cost[start] != float("inf"):
                    next_cost[end] = min(
                        next_cost[end],
                        cost[start] + price,
                    )

            cost = next_cost

        return cost[dst] if cost[dst] != float("inf") else -1
