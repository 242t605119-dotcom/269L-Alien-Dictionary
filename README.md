# Alien Dictionary

**LeetCode Problem:** 269
**Language:** Python

## Problem

You are given a list of words written in an unknown alien language.

The words are already sorted according to the rules of that language.

The task is to determine the order of the characters in the alien alphabet.

If there are multiple valid orders, any valid order can be returned.

If no valid ordering exists, return an empty string.

## Example

Input:

```text id="k7w2ps"
words = ["wrt", "wrf", "er", "ett", "rftt"]
```

By comparing adjacent words, we can determine relationships such as:

```text id="f1m6qa"
t < f
w < e
r < t
e < r
```

One valid character ordering is:

```text id="z8c3nv"
"wertf"
```

Output:

```text id="b4y7hx"
"wertf"
```

## Approach

This problem can be represented as a directed graph.

Each character is treated as a node.

When comparing two adjacent words, the first position where they differ gives us an ordering relationship.

For example:

```text id="s5d9ke"
word1 = "wrt"
word2 = "wrf"
```

The first two characters are the same:

```text id="q2a7lm"
w = w
r = r
```

The first different characters are:

```text id="h6v1px"
t and f
```

Therefore:

```text id="j3n8yc"
t → f
```

This means `t` must appear before `f`.

## Topological Sorting

After building the graph, we use **topological sorting** to determine a valid ordering of the characters.

The `indegree` of a character tells us how many characters must come before it.

Characters with an indegree of `0` can be processed first.

A queue is used to process these characters.

Whenever a character is processed, its outgoing edges are removed by decreasing the indegree of its neighboring characters.

When a neighbor reaches indegree `0`, it can be added to the queue.

## Invalid Cases

There are two important invalid situations.

### Prefix Case

For example:

```text id="y4r8qa"
["abc", "ab"]
```

The second word is a prefix of the first word, but it appears after the longer word.

This ordering is invalid.

### Cycle Case

If the character relationships form a cycle, there is no valid alphabet order.

For example:

```text id="p6x2md"
a → b
b → c
c → a
```

A topological ordering is impossible.

The solution detects this by checking whether all characters were processed.

## Complexity

* **Time:** O(C)
* **Space:** O(C)

Here, `C` represents the total number of characters in the input words.

## Key Learning

This problem helped me practice:

* Graphs
* Directed edges
* Indegree
* Topological sorting
* BFS
* Queue
* Cycle detection
* Comparing strings

## Conclusion

The solution builds a directed graph from the ordering relationships between adjacent words. It then uses BFS-based topological sorting to find a valid alien alphabet order and detects invalid cases such as cycles and incorrect prefix ordering.

**Author: T. Nandhini**
