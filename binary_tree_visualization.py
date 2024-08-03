import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Adds edges to the graph based on the given node and its children.
    
    Parameters:
        graph (Graph): The graph to add edges to.
        node (Node): The current node.
        pos (dict): A dictionary to store the positions of the nodes.
        x (float): The x-coordinate of the current node.
        y (float): The y-coordinate of the current node.
        layer (int): The current layer of the tree.
    
    Returns:
        Graph: The updated graph with added edges.
    """
    ...
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
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
    """
    Recursively builds a binary tree up to a specified maximum depth.
    Parameters:
    - node: The current node in the binary tree.
    - depth: The current depth of the node in the binary tree.
    - max_depth: The maximum depth of the binary tree.
    Returns:
    None
    """
    if depth == max_depth:
        return

    node.left = Node(node.val * 2 + 1)
    node.right = Node(node.val * 2 + 2)

    build_binary_tree(node.left, depth + 1, max_depth)
    build_binary_tree(node.right, depth + 1, max_depth)

# Create a binary heap
root = Node(0)
build_binary_tree(root, 0, 3)  # Change the max_depth value as needed

# Display the tree
draw_tree(root)
