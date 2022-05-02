import matplotlib.pyplot as plt
import osmnx as ox
import networkx as nx
class GoalPolygon:
    def __init__(self, name):
        self.name = name
        self.frame = ox.geocode_to_gdf(name)
        self.frameproj = ox.project_gdf(ox.geocode_to_gdf(name))
        self.center = self.center_point()
        self.coor = self.coordinates_poly()
        self.network = self.surrounding()

    def center_point(self):
        c_point = self.frame.centroid
        center = (float(c_point.y), float(c_point.x))
        return center

    def coordinates_poly(self):
        polygon = self.frameproj.boundary[0]
        coordinates = list(polygon.coords)
        return coordinates

    def surrounding(self):
        network = ox.graph_from_point(self.center, dist_type="network", dist=500, network_type="all")
        network = ox.project_graph(network)
        return list(network.nodes)




place = GoalPolygon(['Бизнес-парк "Ростех-Сити"'])
print(place.network)
