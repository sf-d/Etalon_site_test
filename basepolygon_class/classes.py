import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString, MultiLineString


class GoalPolygon:
    def __init__(self, osm_name):
        self.osm_name = osm_name
        self.frame = ox.geocode_to_gdf(self.osm_name)
        self.frameproj = ox.project_gdf(ox.geocode_to_gdf(self.osm_name))
        self.polygon = self.coordinates_poly()

    def coordinates_poly(self):
        coordinates = []
        polygon = self.frameproj.boundary[0]
        # coordinates = list(polygon.coords)
        for i in polygon.coords:
            coordinates.append(list(i))
        return Polygon(coordinates)

    def network_clean(self, key='all', num=50):
        network = ox.graph_from_place(self.osm_name, network_type=key, buffer_dist=num)
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

    def network_node_coors(self, **kwargs):
        nn_coords = []
        network, edges, nodes = self.network_clean(**kwargs)
        for n in edges.geometry:
            try:
                iterator = iter(n)
                for ii in range(len(n)):
                    nn_coords.append(list(n[ii].coords))
            except TypeError:
                nn_coords.append(list(n.coords))
        return nn_coords

    def get_osmid(self, **kwargs):
        network, edges, nodes = self.network_clean(**kwargs)
        ed_id = list(edges.geometry.keys())
        n_id = list(nodes.geometry.keys())
        return ed_id, n_id
