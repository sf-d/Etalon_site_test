import osmnx as ox
import networkx as nx
from matplotlib import pyplot
from shapely.geometry import Point, Polygon, LineString, MultiLineString


class GoalPolygon:
    def __init__(self, name):
        self.name = name
        self.frame = ox.geocode_to_gdf(name)
        self.frameproj = ox.project_gdf(ox.geocode_to_gdf(name))
        self.polygon = self.coordinates_poly()
        self.network = self.surrounding_net()

    def coordinates_poly(self):
        coordinates = []
        polygon = self.frameproj.boundary[0]
        # coordinates = list(polygon.coords)
        for i in polygon.coords:
            coordinates.append(list(i))
        return Polygon(coordinates)

    def surrounding_net(self):
        network_lines = []
        network = ox.graph_from_place(self.name, network_type="all", buffer_dist=50)
        network = ox.project_graph(network)
        gdf_nodes, gdf_edges = ox.graph_to_gdfs(network)
        for i in gdf_edges.geometry.keys():
            network_lines.append(list(gdf_edges.geometry[i].coords))
        return network_lines


place = GoalPolygon(['Бизнес-парк "Ростех-Сити"'])
print(place.network)
