LeetCode Patterns
========

![Language](https://img.shields.io/badge/language-Python%20%2F%20Modern%20C++-orange.svg)&nbsp;
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)

When prepare for coding interviews, I find that practicing by topics is usually more efficient that randomly tackling problems.

I summarized some typical questions under their respective topics and made sure all the code is as clean as possible. I hope this list will help more people like myself better understand data structures and grasp algorithmic patterns.

(Please consider leaving a star if you find this repo helpful &#9733; )

------

### Topics

- [Binary Indexed Tree](#binary-indexed-tree)
- [Binary Search](#binary-search)
- [Binary Search by Value](#binary-search-by-value)
- [BFS](#bfs)
- [DFS](#dfs)
- [DP - bitmask](#dp---bitmask)
- [Topological Sort](#topological-sort)



------

### Binary Indexed Tree

| #    | Title                                                        | Solution                                        | Difficulty |
| ---- | ------------------------------------------------------------ | ----------------------------------------------- | ---------- |
| 0   | [Template](https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/) | [Python](./python/template/binary_indexed_trees.py), [C++](./cpp/template/binary_indexed_trees.cpp) | :gift: |
| 307   | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | [Python](./python/_307.py), [C++](./cpp/_307.cpp) | Medium |
| 315   | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | [Python](./python/_315.py), [C++](./cpp/_315.cpp) | Hard |
| 327   | [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) | [Python](./python/_327.py), [C++](./cpp/_327.cpp) | Hard |
| 493   | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | [Python](./python/_493.py), [C++](./cpp/_493.cpp) | Hard |
| 1649   | [Create Sorted Array through Instructions](https://leetcode.com/problems/create-sorted-array-through-instructions/) | [Python](./python/_1649.py), [C++](./cpp/_1649.cpp) | Hard |



### Binary Search

| #    | Title                                                        | Solution                                        | Difficulty |
| ---- | ------------------------------------------------------------ | ----------------------------------------------- | ---------- |
| 0   | [Template](https://www.geeksforgeeks.org/binary-search/) | [Python](./python/template/binary_search.py), [C++](./cpp/template/binary_search.cpp) | :gift: |
| 33   | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python](./python/_33.py), [C++](./cpp/_33.cpp) | Medium |
| 34   | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Python](./python/_34.py), [C++](./cpp/_34.cpp) | Medium |
| 35   | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [Python](./python/_35.py), [C++](./cpp/_35.cpp) | Easy |
| 81   | [ Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | [Python](./python/_81.py), [C++](./cpp/_81.cpp) | Medium |
| 153   | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Python](./python/_153.py), [C++](./cpp/_153.cpp) | Medium |
| 154   | [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | [Python](./python/_154.py), [C++](./cpp/_154.cpp) | Hard |
| 162   | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | [Python](./python/_162.py), [C++](./cpp/_162.cpp) | Medium |



### Binary Search by Value

| #    | Title                                                        | Solution                                            | Difficulty |
| ---- | ------------------------------------------------------------ | --------------------------------------------------- | ---------- |
| 0   | [Template](https://www.geeksforgeeks.org/binary-search/) | [Python](./python/template/binary_search_by_value.py), [C++](./cpp/template/binary_search_by_value.cpp) | :gift: |
| 410  | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | [Python](./python/_410.py), [C++](./cpp/_410.cpp)   | Hard       |
| 774  | [Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/) | [Python](./python/_774.py), [C++](./cpp/_774.cpp)   | Hard       |
| 875  | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | [Python](./python/_875.py), [C++](./cpp/_875.cpp)   | Medium     |
| 1011 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | [Python](./python/_1011.py), [C++](./cpp/_1011.cpp) | Medium     |
| 1231 | [Divide Chocolate](https://leetcode.com/problems/divide-chocolate/) | [Python](./python/_1231.py), [C++](./cpp/_1231.cpp) | Hard       |
| 1552 | [Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/) | [Python](./python/_1552.py), [C++](./cpp/_1552.cpp) | Medium     |



### BFS

| #    | Title                                                        | Solution                                        | Difficulty |
| ---- | ------------------------------------------------------------ | ----------------------------------------------- | ---------- |
| 0   | [Template](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/) | [Python](./python/template/bfs.py), [C++](./cpp/template/bfs.cpp) | :gift: |
| 102   | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Python](./python/_102.py), [C++](./cpp/_102.cpp) | Medium |
| 103   | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [Python](./python/_103.py), [C++](./cpp/_103.cpp) | Medium |
| 107   | [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | [Python](./python/_107.py), [C++](./cpp/_107.cpp) | Easy |
| 127   | [Word Ladder](https://leetcode.com/problems/word-ladder/) | [Python](./python/_127.py), [C++](./cpp/_127.cpp) | Hard |
| 200   | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python](./python/_200.py), [C++](./cpp/_200.cpp) | Medium |
| 752   | [Open the Lock](https://leetcode.com/problems/open-the-lock/) | [Python](./python/_752.py), [C++](./cpp/_752.cpp) | Medium |



### DFS

| #    | Title                                                        | Solution                                        | Difficulty |
| ---- | ------------------------------------------------------------ | ----------------------------------------------- | ---------- |
| 0   | [Template](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/) | [Python](./python/template/dfs.py), [C++](./cpp/template/dfs.cpp) | :gift: |
| 46   | [Permutations](https://leetcode.com/problems/permutations/) | [Python](./python/_46.py), [C++](./cpp/_46.cpp) | Medium |
| 77   | [Combinations](https://leetcode.com/problems/combinations/) | [Python](./python/_77.py), [C++](./cpp/_77.cpp) | Medium |
| 94   | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [Python](./python/_94.py), [C++](./cpp/_94.cpp) | Medium |
| 144   | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [Python](./python/_144.py), [C++](./cpp/_144.cpp) | Medium |
| 145   | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [Python](./python/_145.py), [C++](./cpp/_145.cpp) | Medium |
| 200   | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python](./python/_200.py), [C++](./cpp/_200.cpp) | Medium |



### DP - bitmask

| #    | Title                                                        | Solution                                        | Difficulty |
| ---- | ------------------------------------------------------------ | ----------------------------------------------- | ---------- |
| 0   | [Template](https://www.geeksforgeeks.org/bitmasking-and-dynamic-programming-set-1-count-ways-to-assign-unique-cap-to-every-person/) |  | :gift: |
| 1125   | [Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/) | [Python](./python/_1125.py), [C++](./cpp/_1125.cpp) | Hard |
| 1349   | [Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/) | [Python](./python/_1349.py), [C++](./cpp/_1349.cpp) | Hard |
| 1434   | [Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) | [Python](./python/_1434.py), [C++](./cpp/_1434.cpp) | Hard |
| 1595   | [Minimum Cost to Connect Two Groups of Points](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/) | [Python](./python/_1595.py), [C++](./cpp/_1595.cpp) | Hard |



### Topological Sort

| #    | Title                                                        | Solution                                        | Difficulty |
| ---- | ------------------------------------------------------------ | ----------------------------------------------- | ---------- |
| 0   | [Template](https://www.geeksforgeeks.org/topological-sorting/) | [Python](./python/template/topo_sort.py), [C++](./cpp/template/topo_sort.cpp) | :gift: |
| 207   | [Course Schedule](https://leetcode.com/problems/course-schedule/) | [Python](./python/_207.py), [C++](./cpp/_207.cpp) | Medium |



### Tree

| #    | Title                                                        | Solution                                        | Difficulty |
| ---- | ------------------------------------------------------------ | ----------------------------------------------- | ---------- |
| 100   | [Same Tree](https://leetcode.com/problems/same-tree/) | [Python](./python/_100.py), [C++](./cpp/_100.cpp) | Easy |
| 236   | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Python](./python/_236.py), [C++](./cpp/_236.cpp) | Medium |

