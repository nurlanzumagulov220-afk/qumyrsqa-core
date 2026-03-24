import networkx as nx

class SwarmBiddingEngine:
    def __init__(self, road_graph: nx.Graph):
        self.graph = road_graph
        # Коэффициенты Алгоритма Бейсекенова
        self.W_DISTANCE = 0.4
        self.W_TIME = 0.5
        self.W_AMANAT = 0.1

    def solve_best_unit(self, fleet, target_node, priority):
        valid_bids = []
        for unit in fleet:
            # Расчет по графу NetworkX
            path = nx.shortest_path(self.graph, unit['node'], target_node, weight='length')
            dist = nx.shortest_path_length(self.graph, unit['node'], target_node, weight='length')
            
            # Формула Score (чем меньше, тем лучше)
            penalty = (dist * self.W_DISTANCE)
            if priority == "HIGH": penalty *= 0.5 # Срочность важнее пробега
            
            valid_bids.append({
                "unit_id": unit['id'],
                "score": round(penalty, 2),
                "dist": dist,
                "path": path
            })
        
        valid_bids.sort(key=lambda x: x['score'])
        return valid_bids[0]