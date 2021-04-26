import pydot
import networkx as nx
from pathlib import Path
import matplotlib.pyplot as plt

path = Path(__file__).parent / "out"


def visualize_graph(graph, weight="capacity", node_weight=None, filename="graph_out.png"):

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_color="tab:blue")

    # edges
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist= [(u, v) for (u, v) in graph.edges() if graph[u][v]["capacity"] != 0],
        width=2,
        alpha=0.5,
        edge_color="tab:red",
    )

    edge_labels = { (u, v): graph[u][v][weight] for (u, v) in graph.edges() if graph[u][v]["capacity"] != 0}

    if node_weight:
        node_weight = { u: graph.nodes[u][node_weight] for u in graph }
        nx.draw_networkx_labels(graph, pos, node_weight)
    # some math labels
    nx.draw_networkx_edge_labels(graph, pos, edge_labels, font_size=22, font_color="tab:blue")

    plt.tight_layout()
    plt.axis("off")
    plt.savefig(path / filename)






