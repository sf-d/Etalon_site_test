import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString, MultiLineString


class GoalPolygon:
    def __init__(self, name):
        self.name = name
        self.frame = ox.geocode_to_gdf(name)
        self.frameproj = ox.project_gdf(ox.geocode_to_gdf(name))
        self.polygon = self.coordinates_poly()


    def coordinates_poly(self):
        coordinates = []
        polygon = self.frameproj.boundary[0]
        # coordinates = list(polygon.coords)
        for i in polygon.coords:
            coordinates.append(list(i))
        return Polygon(coordinates)

    def network_clean(self, key, num):
        network = ox.graph_from_place(self.name, network_type=key, buffer_dist=num)
        network = ox.project_graph(network)
        gdf_nodes, gdf_edges = ox.graph_to_gdfs(network)

        for i in gdf_edges.geometry.keys():
            if gdf_edges.geometry[i].crosses(self.polygon) or self.polygon.covers(gdf_edges.geometry[i]):
                network.remove_edge(*i)
            else:
                pass
        network = ox.utils_graph.remove_isolated_nodes(network)
        nodes, edges = ox.graph_to_gdfs(network)
        return network, edges, nodes


def network_node_coors(network):
    nn_coords = []
    for n in network.geometry:
        try:
            iterator = iter(n)
            for ii in range(len(n)):
                nn_coords.append(list(n[ii].coords))
        except TypeError:
            nn_coords.append(list(n.coords))
    return nn_coords


place = GoalPolygon(['Бизнес-парк "Ростех-Сити"'])


n_d, e_one, n_one = place.network_clean('drive', 25)
print(list(n_one.geometry.keys()))
a_d, e_two, n_two = place.network_clean('walk',25)
all_d, e_three, n_three = place.network_clean('all',300)

fig, ax = plt.subplots(figsize=(12, 12))
ax.set_facecolor('black')


x,y = place.polygon.exterior.xy
xs = [point.x for point in n_one.geometry.values]
ys = [point.y for point in n_one.geometry.values]

plt.plot(x,y,linewidth=4,color='#9c00ff')
e_three.plot(ax=ax, linewidth=1, edgecolor='#b2b2b2')
e_two.plot(ax=ax, linewidth=2, edgecolor='#fef96c')
e_one.plot(ax=ax, linewidth=2, edgecolor='#00ffb4')
plt.scatter(xs, ys, s=200, marker='o', c='red')
plt.show()
