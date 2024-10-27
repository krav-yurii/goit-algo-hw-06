import networkx as nx
import matplotlib.pyplot as plt


#Firts
G = nx.Graph()

stops = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(stops)

routes = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'),
          ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H'), ('E', 'H')]
G.add_edges_from(routes)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500)
plt.title("Транспортна мережа міста")
plt.show()

print(f"Кількість вузлів: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")

degrees = dict(G.degree())
print("Ступені вузлів:")
for node, degree in degrees.items():
    print(f"Вузол {node}: ступінь {degree}")

#Second

# Функція для пошуку шляху за допомогою DFS
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs_paths(graph, neighbor, goal, path + [neighbor])
            if new_path:
                return new_path
    return None

# Функція для пошуку шляху за допомогою BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex == goal:
            return path
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited and neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    return None

# Пошук шляхів між вузлами 'A' та 'H'
dfs_path = dfs_paths(G, 'A', 'H')
bfs_path = bfs_paths(G, 'A', 'H')

print(f"Шлях DFS від 'A' до 'H': {dfs_path}")
print(f"Шлях BFS від 'A' до 'H': {bfs_path}")


#Third

# Додаємо ваги до ребер
weighted_routes = [
    ('A', 'B', 2), ('A', 'C', 5), ('B', 'D', 1), ('C', 'D', 2),
    ('D', 'E', 3), ('E', 'F', 1), ('F', 'G', 2), ('G', 'H', 3), ('E', 'H', 4)
]

G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from(weighted_routes)

# Знаходимо найкоротші шляхи між усіма парами вузлів
shortest_paths = dict(nx.all_pairs_dijkstra_path(G_weighted))

# Виводимо найкоротші шляхи
for source in G_weighted.nodes():
    for target in G_weighted.nodes():
        if source != target:
            path = shortest_paths[source][target]
            print(f"Найкоротший шлях від {source} до {target}: {path}")