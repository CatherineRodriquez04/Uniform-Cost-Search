# Catherine Rodriquez - CSC 4444
# uniform cost function
# returns the minimum cost (Bonus: returns path to minimum cost as well)
def  uniform_cost_search(start, goal, graph, cost):
    answer = {node: {'cost': float('inf'), 'path': []} for node in goal}
    #create a priority queue
    queue = []
    #set queue: cost, location, path
    #cost begins at 0, location begins at start, path begins empty
    queue.append([0, start, []])

    #queue is not empty
    while (len(queue)>0):
        #pop the elements
        currentCost, currentNode, currentPath = queue.pop();

        #checks if currentNode is the goal and if currentCost costs less
        #adjusts answer
        if currentNode in goal and currentCost < answer[currentNode]['cost']:
            answer[currentNode]['cost'] = currentCost
            answer[currentNode]['path'] = currentPath + [currentNode]

        #checks with adjacent nodes
        #adjusts cost and path
        for neighbor in graph[currentNode]:
            #set updated cost, location, and path
            queue.append((currentCost + cost[(currentNode, neighbor)], neighbor, currentPath + [currentNode]))
            
    return answer
 
# main function
if __name__ == '__main__':
     
    # create a graph with no more than 30 nodes
    graph, cost = [[] for i in range(30)], {}
 
    # add edges to the graph
    graph[0].append(4)
    graph[0].append(5)
    graph[0].append(16)
    graph[2].append(1)
    graph[3].append(1)
    graph[4].append(2)
    graph[4].append(3)
    graph[4].append(5)
    graph[5].append(8)
    graph[5].append(18)
    graph[6].append(3)
    graph[6].append(7)
    graph[8].append(16)
    graph[8].append(17)
    graph[16].append(17)
    graph[18].append(6)
    
 
    # add cost to each edge
    cost[(0, 4)] = 3
    cost[(0, 5)] = 9
    cost[(0, 16)] = 1
    cost[(2, 1)] = 2
    cost[(3, 1)] = 2
    cost[(4, 2)] = 1
    cost[(4, 3)] = 8
    cost[(4, 5)] = 2
    cost[(5, 8)] = 3
    cost[(5, 18)] = 2
    cost[(6, 3)] = 3
    cost[(6, 7)] = 2
    cost[(8, 16)] = 4
    cost[(8, 17)] = 4
    cost[(16, 17)] = 15
    cost[(18, 6)] = 1
    
    # set start state 
    start = 0
    
    # set goal state, there can be multiple goal states
    goal = [7, 0, 4, 32]
    
    # call uniform_search_cost function to get the minimum cost to reach gaol. Bonus points for path
    # ****** You have to implement this function *****
    min_cost_info = uniform_cost_search(start, goal, graph, cost)

    for node, info in min_cost_info.items():
        print(f'Minimum cost from {start} to {node} is {info["cost"]}')
        print(f'Path: {info["path"]}')