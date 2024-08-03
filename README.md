# Data Structures and Algorithms Final Project

## Table of Contents
- [Data Structures and Algorithms Final Project](#data-structures-and-algorithms-final-project)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Tasks Overview](#tasks-overview)
  - [Task Implementations](#task-implementations)
    - [Task 1: Singly Linked Lists](#task-1-singly-linked-lists)
    - [Task 2: Pythagorean Tree Fractal](#task-2-pythagorean-tree-fractal)
    - [Task 3: Dijkstra's Algorithm](#task-3-dijkstras-algorithm)
    - [Task 4: Binary Tree Visualization](#task-4-binary-tree-visualization)
    - [Task 5: Tree Traversal Visualization](#task-5-tree-traversal-visualization)
    - [Task 6: Greedy Algorithms and Dynamic Programming](#task-6-greedy-algorithms-and-dynamic-programming)
    - [Task 7: Monte Carlo Simulation](#task-7-monte-carlo-simulation)
  - [Results](#results)
  - [Conclusion](#conclusion)

## Introduction
This project involves a series of tasks aimed at demonstrating proficiency in various data structures and algorithms, including linked lists, recursion, graph algorithms, and more. Each task is implemented in Python and includes visualizations and analyses to support the solutions.

## Tasks Overview
The project consists of the following tasks:
1. **Task 1**: Implement and manipulate singly linked lists, including reversing, sorting, and merging.
2. **Task 2**: Use recursion to create and visualize the Pythagorean tree fractal.
3. **Task 3**: Implement Dijkstra's algorithm using a binary heap for finding the shortest paths in a weighted graph.
4. **Task 4**: Visualize a binary tree using the provided Python code.
5. **Task 5**: Implement and visualize tree traversal algorithms (DFS and BFS) using stack and queue.
6. **Task 6**: Solve a food selection problem using greedy and dynamic programming approaches.
7. **Task 7**: Simulate dice rolls using the Monte Carlo method and compare results with analytical probabilities.

## Task Implementations

### Task 1: Singly Linked Lists
Three operations on singly linked lists:
1. **Reversing a Singly Linked List**: Develop a function that reverses the order of nodes in a singly linked list by changing the links between nodes.
2. **Sorting a Singly Linked List**: Implement a sorting algorithm (e.g., merge sort) for singly linked lists. This requires functions to split the list, merge sorted sublists, and recursively sort the sublists.
3. **Merging Two Sorted Singly Linked Lists**: Create a function that merges two sorted singly linked lists into a single sorted list. This will involve comparing nodes from both lists and linking them in the correct order.

### Task 2: Pythagorean Tree Fractal

1. **Implement Recursion for Fractal Generation**: Write a recursive function to create the Pythagorean tree fractal. The function should draw each branch and recursively call itself to draw the smaller branches.
2. **Visualize the Fractal**: Use a plotting library (e.g., Matplotlib) to visualize the fractal. The user should be able to specify the recursion depth to see different levels of the fractal.

### Task 3: Dijkstra's Algorithm

1. **Implement Dijkstra's Algorithm**: Develop the algorithm to find the shortest paths from a starting vertex to all other vertices in a weighted graph using a priority queue (heapq).
2. **Graph Representation**: Represent the graph using a dictionary where keys are vertices and values are dictionaries of neighbors and edge weights.
3. **Calculate Distances**: Calculate and return the shortest distances from the starting vertex to all other vertices.

### Task 4: Binary Tree Visualization

1. **Build a Binary Tree**: Write a function to construct a binary tree up to a specified depth.
2. **Visualize the Tree**: Use the provided code to visualize the binary tree. Each node should be represented with a unique identifier and visually arranged to reflect the tree structure.

### Task 5: Tree Traversal Visualization

1. **Implement DFS and BFS Traversals**: Write functions to perform depth-first search (DFS) and breadth-first search (BFS) on the binary tree. Use a stack for DFS and a queue for BFS.
2. **Color Nodes Based on Traversal Order**: Assign a unique color to each node based on its position in the traversal order. Use a gradient of colors to represent the traversal sequence from start to finish.
3. **Visualize Traversals**: Modify the tree visualization to show the nodes with their assigned colors, reflecting the traversal order.

### Task 6: Greedy Algorithms and Dynamic Programming

1. **Solve the Food Selection Problem Using a Greedy Algorithm**: Implement a greedy algorithm that selects food items to maximize the calorie-to-cost ratio without exceeding the budget.
2. **Solve the Same Problem Using Dynamic Programming**: Develop a dynamic programming solution to find the optimal set of food items that maximizes the total calories within the given budget.
3. **Compare Results**: Compare the solutions obtained from the greedy algorithm and the dynamic programming approach.

### Task 7: Monte Carlo Simulation

1. **Simulate Dice Rolls**: Write a program to simulate rolling two dice a large number of times. Record the sum of the numbers rolled.
2. **Calculate Probabilities**: Determine the probability of each possible sum (from 2 to 12) based on the simulation results.
3. **Compare with Analytical Probabilities**: Compare the simulated probabilities with the analytical probabilities provided. Visualize the results using a plot to show how closely the simulation matches the theoretical values.



## Results
The results include:
- Correct implementation of linked list operations.
- Visualization of the Pythagorean tree fractal at different recursion depths.
- Successful calculation of shortest paths using Dijkstra's algorithm.
- Visualization of the binary tree and traversal orders.
- Comparison of solutions from greedy and dynamic programming algorithms for the food selection problem.
- Probability distribution of dice roll sums from the Monte Carlo simulation compared with analytical probabilities.

## Conclusion
This project demonstrates various data structures and algorithms, including their implementation, visualization, and analysis. Each task provides a practical application of these concepts, showcasing their utility and performance in different scenarios.
