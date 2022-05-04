import osmnx as ox
import networkx as nx
from matplotlib import pyplot
from shapely.geometry import Point, Polygon, LineString, MultiLineString


class GoalPolygonfff:
    def __init__(self, name):
        self.name = name
        self.frame = ox.geocode_to_gdf(name)
        self.frameproj = ox.project_gdf(ox.geocode_to_gdf(name))
        self.center = self.center_point()
        self.polygon = self.coordinates_poly()
        self.network = self.surrounding_net()

    def center_point(self):
        c_point = self.frame.centroid
        center = (float(c_point.y), float(c_point.x))
        return center

    def coordinates_poly(self):
        coordinates = []
        polygon = self.frameproj.boundary[0]
        # coordinates = list(polygon.coords)
        for i in polygon.coords:
            coordinates.append(list(i))
        return Polygon(coordinates)

    def surrounding_net(self, buffer):
        network_lines = []
        network = ox.graph_from_place(self.name, network_type="all", buffer_dist=buffer)
        network = ox.project_graph(network)
        gdf_nodes, gdf_edges = ox.graph_to_gdfs(network)
        for i in gdf_nodes.geometry.keys():
            network_lines.append(list(gdf_nodes.geometry[i].coords))
        return network_lines


'''def network_substract(lines, contour):
    new_network = []
    nn_coords = []
    for i in lines:
        new_network.append(i.difference(contour))
    for n in new_network:
        try:
            iterator = iter(n)
            for ii in range(len(n)):
                nn_coords.append(list(n[ii].coords))
        except TypeError:
            nn_coords.append(list(n.coords))
    return nn_coords'''


place = GoalPolygon(['Бизнес-парк "Ростех-Сити"'], 50)
#new_n = network_substract(place.network, place.polygon)
print(place.network)
