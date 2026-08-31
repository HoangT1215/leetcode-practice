"""LeetCode 127: Word Ladder.

Problem: https://leetcode.com/problems/word-ladder/

Let N be the number of words and L be their common length.
Time complexity: O(N * L^2 * alphabet_size)
Space complexity: O(N)
"""

from typing import List


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        # --- Naive BFS implementation: explicitly construct the graph.
        # if endWord not in wordList:
        #     return 0
        # n = len(beginWord)
        # graph = {}
        # word_set = set(wordList)

        # for word in [beginWord] + wordList:
        #     graph[word] = []
        #     for i in range(n):
        #         for char in "abcdefghijklmnopqrstuvwxyz":
        #             if char == word[i]:
        #                 continue

        #             neighbor = word[:i] + char + word[i + 1:]

        #             # This is key: `neighbor in wordList` would cost O(N).
        #             if neighbor in word_set:
        #                 graph[word].append(neighbor)

        # # --- BFS step.
        # queue = [(beginWord, 1)]
        # head = 0
        # visited = {beginWord}
        # print(graph)

        # while head < len(queue):
        #     word = queue[head]
        #     head += 1

        #     for neighbor in graph[word[0]]:
        #         if neighbor == endWord:
        #             return word[1] + 1
        #         if neighbor not in visited:
        #             word_tuple = (neighbor, word[1] + 1)
        #             queue.append(word_tuple)
        #             visited.add(neighbor)
        # return 0

        # --- Generate neighbors on demand instead of storing the graph.
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        word_length = len(beginWord)
        queue = [(beginWord, 1)]
        head = 0

        # Removing a word when it is discovered marks it as visited.
        word_set.discard(beginWord)

        while head < len(queue):
            word, distance = queue[head]
            head += 1

            for i in range(word_length):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char == word[i]:
                        continue

                    neighbor = word[:i] + char + word[i + 1:]

                    if neighbor == endWord:
                        return distance + 1

                    if neighbor in word_set:
                        # Mark the neighbor visited when enqueuing it so no
                        # other word can add the same neighbor again.
                        word_set.remove(neighbor)
                        queue.append((neighbor, distance + 1))

        return 0
