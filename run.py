# Search methods

import search

routes = {
    "ab": search.GPSProblem('A', 'B', search.romania),
    "bf": search.GPSProblem('B', 'F', search.romania),
    "ch": search.GPSProblem('C', 'H', search.romania),
    "eg": search.GPSProblem('E', 'G', search.romania),
    "ba": search.GPSProblem('B', 'A', search.romania)
}

for route in routes.iterkeys():
    print " --------- ",route, "-----------"

    print "---- Anchura ----"
    search.breadth_first_graph_search(routes[route]).path()
    print "---- Profundidad ----"
    search.depth_first_graph_search(routes[route]).path()
    print "---- Ramificacion y poda no informada ----"
    search.branch_and_bound(routes[route]).path()
    print "---- Ramificacion y salto informado ----"
    search.informed_branch_and_bound(routes[route]).path()


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
