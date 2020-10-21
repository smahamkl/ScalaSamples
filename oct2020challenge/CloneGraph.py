from typing import List

'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test 
case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of 
neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference 
to the cloned graph.
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. 
The graph consists of only one node with val = 1 and it does not have any neighbors.
'''
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.dfs(node, {})
    
    def dfs(self, node:Node, nodeDict:dict)->Node:
        if node == None:
            return node

        if nodeDict.get(node.val, None) != None:
            return nodeDict[node.val]
        cur = Node(node.val)
        nodeDict[cur.val] = cur
        
        cur.neighbors = [self.dfs(x, nodeDict) for x in node.neighbors]
        return cur

sol = Solution()
n1 = Node(2)
n2 = Node(3)
n = Node(1, [n1,n2])
clonedList = sol.cloneGraph(n)
print(clonedList.val)
print(len(clonedList.neighbors))
print(clonedList.neighbors[0].val)
print(clonedList.neighbors[1].val)


    