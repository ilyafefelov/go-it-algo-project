import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_binary_tree(node, depth, max_depth):
    if depth == max_depth:
        return

    node.left = Node(node.val * 2 + 1)
    node.right = Node(node.val * 2 + 2)

    build_binary_tree(node.left, depth + 1, max_depth)
    build_binary_tree(node.right, depth + 1, max_depth)

def get_color_gradient(n, start_color="#00008B", end_color="#87CEFA"):
    """
    Generates a list of n colors that form a gradient between start_color and end_color.
    """
    import matplotlib.colors as mcolors
    start_rgb = mcolors.hex2color(start_color)
    end_rgb = mcolors.hex2color(end_color)
    return [mcolors.to_hex((start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / (n - 1),
                            start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / (n - 1),
                            start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / (n - 1)))
            for i in range(n)]

def bfs_visualization(root):
    """
    Perform breadth-first search traversal on a binary tree and visualize the traversal process.
    Args:
        root: The root node of the binary tree.
    Returns:
        None
    Raises:
        None
    """
    if root is None:
        return

    queue = deque([root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    colors = get_color_gradient(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]

    draw_tree(root)

def dfs_visualization(root):
    """
    Perform depth-first search traversal on a binary tree and visualize the traversal process.
    Args:
        root (TreeNode): The root node of the binary tree.
    Returns:
        None
    Raises:
        None
    """
    if root is None:
        return

    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    colors = get_color_gradient(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]

    draw_tree(root)

# Create a binary tree
root = Node(0)
build_binary_tree(root, 0, 3)  # Change the max_depth value as needed

# BFS visualization
bfs_visualization(root)

# Resetting colors for DFS visualization
root = Node(0)
build_binary_tree(root, 0, 3)  # Change the max_depth value as needed

# DFS visualization
dfs_visualization(root)
