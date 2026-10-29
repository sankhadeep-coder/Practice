This is a massive, ambitious, and highly effective way to master Data Structures and Algorithms (DSA). By committing to one problem per day for a year, you transition from "memorizing solutions" to "recognizing patterns."

To make this project successful, you need a **systematic roadmap**. If you jump around randomly, you will lose momentum. Below is the professional documentation and framework for your **"365 Days of Python DSA"** project.

---

# 🚀 Project Roadmap: 365 Days of Python DSA

## 📋 Project Overview
The goal of this project is to solve 365 DSA problems using Python, organized into a GitHub repository. Each problem will reside in its own `.py` file, named according to the problem title.

**Core Principles:**
1.  **Consistency:** One file, one day, no excuses.
2.  **Readability:** Use Pythonic conventions (PEP 8), type hinting, and clear docstrings.
3.  **Complexity Analysis:** Every file must include a Big O notation for Time and Space complexity.
4.  **Pattern Recognition:** Group problems by patterns (e.g., Two Pointers, Sliding Window, BFS/DFS).

---

## 📂 Repository Structure
To keep the repository organized as it grows to 365 files, use a folder-based structure:

```text
365-days-python-dsa/
├── Day_001_to_030_Arrays/
│   ├── 2sum.py
│   ├── contains_duplicate.py
│   └── ...
├── Day_031_to_090_Linked_Lists/
│   ├── reverse_linked_list.py
│   └── ...
├── Day_091_to_150_Trees_and_Graphs/
│   ├── invert_binary_tree.py
│   └── ...
├── Day_151_to_250_Dynamic_Programming/
│   ├── climbing_stairs.py
│   └── ...
└── README.md
```

---

## 🛠 The "Gold Standard" File Template
Every `.py` file should follow this structure to ensure it is portfolio-ready.

**Example: `2sum.py`**
```python
"""
Problem: 2Sum
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Source: LeetCode #1
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Solves the 2Sum problem using a Hash Map (Dictionary).
    
    Args:
        nums: A list of integers.
        target: The target sum.
        
    Returns:
        A list containing the indices of the two numbers.
    """
    # Dictionary to store: {value: index}
    prev_map = {} 

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []

# --- Complexity Analysis ---
# Time Complexity: O(n) - We traverse the list containing n elements only once.
# Space Complexity: O(n) - In the worst case, we store all elements in the map.

# --- Test Cases ---
if __name__ == "__main__":
    test_1 = two_sum([2, 7, 11, 15], 9)
    print(f"Test 1: {test_1}")  # Expected: [0, 1]

    test_2 = two_sum([3, 2, 4], 6)
    print(f"Test 2: {test_2}")  # Expected: [1, 2]
```

---

## 🗺 365-Day Curriculum Strategy
To ensure you cover everything, divide the year into phases:

### Phase 1: The Fundamentals (Days 1–90)
*   **Arrays & Strings:** Two Pointers, Sliding Window, Prefix Sums.
*   **Hashing:** Frequency counting, Hash Maps, Sets.
*   **Linked Lists:** Singly, Doubly, Circular, Fast/Slow pointers.
*   **Stacks & Queues:** Monotonic stacks, BFS/DFS basics.
*   **Recursion:** Backtracking basics (Permutations, Subsets).

### Phase 2: Trees & Graphs (Days 91–180)
*   **Trees:** Binary Trees, BSTs, AVL Trees, Traversals (Pre/In/Post-order).
*   **Heaps/Priority Queues:** K-th largest element, Merging sorted lists.
*   **Graphs:** Adjacency Lists, BFS, DFS, Dijkstra’s, Bellman-Ford.
*   **Tries:** Prefix trees, Autocomplete logic.

### Phase 3: Advanced Algorithms (Days 181–300)
*   **Dynamic Programming:** 1D DP, 2D DP, Knapsack, Longest Common Subsequence.
*   **Greedy Algorithms:** Interval scheduling, Huffman coding.
*   **Bit Manipulation:** XOR tricks, Bitmasking.
*   **Segment Trees & Fenwick Trees:** Range queries.

### Phase 4: Mastery & Mock Interviews (Days 301–365)
*   **Hard LeetCode problems.**
*   **System Design-related DSA.**
*   **Time-pressured Mock Interviews.**
*   **Reviewing "Hard" problems from previous months.**

---

## 💡 Expert Tips for Success

1.  **Don't spend > 1 hour on one problem:** If you are stuck, look at the solution, understand the *logic*, close the solution, and then write the code from scratch in your file.
2.  **The "Why" over the "How":** In your docstrings, briefly explain *why* you chose a specific data structure (e.g., "Used a Hash Map because we need O(1) lookup time").
3.  **Use Type Hinting:** Always use `List[int]`, `Dict[str, int]`, etc. It makes your code look professional and helps with IDE autocompletion.
4.  **GitHub Streak:** Commit your file every single day. The "Green Square" streak is a powerful psychological motivator and a great signal to recruiters.
5.  **Review:** Every Sunday, go back and re-solve 3 problems from the previous month without looking