from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        graph = defaultdict(set)
        indegree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break

        queue = deque([char for char in indegree if indegree[char] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(indegree):
            return ""

        return "".join(result)
