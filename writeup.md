
# 8.14

## Summary

The summary of this problem is that two friends live in different cities and want to minimize time to see eachother in person. These people are going to drive to a middle city.

## My solution

I think this problem is pretty simple. We can represent the cities and roads as a weighted graph with edges. It wouldn't make sense for the graph to have negative edges as you can't have negative travel time. We take in a graph, and a starting vertex for each of our friends. My solution would be to run Dijkstra's algorithm twice, one for one friends vertex, one for the other, then find the minimum sum for all vertexes in both given graphs. 

## Analysis of Correctness

We already know dijkstra's algorithm will give us the minimum cost it takes to get from a source node to each other node. The problem is asking for the minimum travel time from both starting nodes. All our algorithm is doing is finding the shortest path from both of our nodes to all other nodes, then finding the node which both vertexes travel time sums up to be the least.

## Analysis of Runtime

We know we run Dijkstra's algorithm twice, each time the algorithm is called the runtime is the same, O(ElogV) where E is the number of edges and V is the number of vertecies. The other part of the algorithm is finding the minimum sum. This loop loops through every node so the runtime is O(V). O(ElogV) dominates O(V) so the runtime is O(ElogV).