import pandas as pd
from scipy.spatial import cKDTree

class SwarmSpatialIndexer:
    def __init__(self, nodes_df: pd.DataFrame):
        self.nodes_df = nodes_df.reset_index(drop=True)
        self.coords = self.nodes_df[['lat', 'lon']].values
        self.tree = cKDTree(self.coords)

    def snap_to_graph(self, lat: float, lon: float):
        distance, index = self.tree.query([lat, lon], k=1)
        return self.nodes_df.iloc[index]['node_id'], distance