import networkx as nx


def parse_input(source):
    cons = []
    with open(source, 'r') as f:
        lines = f.read().split('\n')
    for line in lines:
        line = line.split(': ')
        matches = line[1].split()
        for m in matches:
            cons.append((line[0], m))
    return cons


def solve(source):
    G = nx.Graph()
    G.add_edges_from(parse_input(source))
    nx.minimum_edge_cut(G)
    G.remove_edges_from(list(nx.minimum_edge_cut(G)))
    res = list(nx.connected_components(G))
    print(len(res[0]) * len(res[1]))


def main(source):
    solve(source)


main('input.txt')
