import networkx as nx
import matplotlib.pyplot as plt

def create_network_map(data):
    # Create an empty graph
    graph = nx.Graph()

    # Add nodes (IP addresses and domains) to the graph
    for node in data['nodes']:
        graph.add_node(node['id'], label=node['label'])

    # Add edges (relationships between nodes) to the graph
    for edge in data['edges']:
        graph.add_edge(edge['source'], edge['target'])

    return graph

# Prompt the user to input network data
data = {}
data['nodes'] = []
data['edges'] = []

num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    node_id = input(f"Enter ID for node {i+1}: ")
    node_label = input(f"Enter label for node {i+1}: ")
    data['nodes'].append({'id': node_id, 'label': node_label})

num_edges = int(input("Enter the number of edges: "))

for i in range(num_edges):
    source = input(f"Enter source node for edge {i+1}: ")
    target = input(f"Enter target node for edge {i+1}: ")
    data['edges'].append({'source': source, 'target': target})

# Set the title for the network mapping
title = input("Enter the title for the network mapping: ")

# Create the network map
network_map = create_network_map(data)

# Draw the network map
pos = nx.spring_layout(network_map)
labels = nx.get_node_attributes(network_map, 'label')
nx.draw(network_map, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, labels=labels)
plt.title(title)
plt.show()
