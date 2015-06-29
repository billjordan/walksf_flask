import json
import os
from flask import Flask
import pickle
# from intersections import loadIntersections
# from graph import SF_graph
from dijkstra_search import *

app = Flask(__name__)

# intersections = None
# graph = None

@app.route("/")
@app.route("/WalkSF_api/")
def api_home():
    return "WalkSF api homepage"

@app.route("/walksf/least_work/<start_cnn>/<end_cnn>/")
#CNNs are uids for intersections from data.sf.gov
def least_work(start_cnn, end_cnn):
    implemented = False
    path = None
    start_intersection_valid = start_cnn in valid_cnns
    end_intersection_valid = end_cnn in valid_cnns
    if start_intersection_valid and end_intersection_valid:
        path = dijkstra_search(graph, intersections[start_cnn], intersections[end_cnn])
    result = {
        "start_intersection_valid": start_intersection_valid,
        "end_intersection_valid": end_intersection_valid,
        "path": get_list_of_ints_from_path(path)
    }
    return json.dumps(result)

    # return json.dumps(implemented)


def get_list_of_ints_from_path(path):
    int_path = []
    for intersection in path:
        int_path.append(int(intersection.get_cnn()))

    return int_path


if __name__ == "__main__":
    graph_file = os.path.dirname(__file__) + "/sf_graph.pickle"
    gragh_pickle_in = open(graph_file, "rb")
    graph = pickle.load(gragh_pickle_in)
    valid_cnns = set([])    #set of cnns (strings)
    intersections = {}
    for node in graph.get_nodes():
        valid_cnns.add(node.get_id())
        intersections[node.get_id()] = node
    app.debug = True
    app.run(host="0.0.0.0", port=8080)
