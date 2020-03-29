class Grid:
    def __init__(self, row, col, inputString):
        self.row = row
        self.col = col
        self.inputString = inputString
        self.grid = self.buildGrid(row, col, inputString)

    @staticmethod
    def buildGrid(row, col, inputString):
        cells = list(inputString)

        grid = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                grid[i][j] = cells[i * 4 + j]

        return grid

    @staticmethod
    def findMaxConnectedCell(grid):
        visitedNodes = []
        maxNodeList = []
        for i in range(grid.row):
            for j in range(grid.col):

                if (i, j) in visitedNodes or grid.grid[i][j] == '0':
                    continue

                nodeList = []

                grid.DFS(grid, (i, j), visitedNodes, nodeList)
                maxNodeList = maxNodeList if len(maxNodeList) > len(nodeList) else nodeList

        return [len(maxNodeList), maxNodeList]

    @staticmethod
    def DFS(grid, currentNode, visitedNodes, nodeList):

        visitedNodes.append(currentNode)
        nodeList.append(currentNode)

        neighbors = Grid.findNeighbor(grid, currentNode)

        for neighbor in neighbors:
            if neighbor not in visitedNodes:
                Grid.DFS(grid, neighbor, visitedNodes, nodeList)

    @staticmethod
    def findNeighbor(grid, currentNodePos):
        direction = [-1, 0, 1]
        neighbors = []
        for i in direction:
            for j in direction:
                if i == 0 and j == 0:
                    continue
                neighborPosition = (currentNodePos[0] + i, currentNodePos[1] + j)

                if Grid.checkValidPosition(grid, neighborPosition) and grid.grid[neighborPosition[0]][
                    neighborPosition[1]] == '1':
                    neighbors.append((neighborPosition[0], neighborPosition[1]))

        return neighbors

    @staticmethod
    def checkValidPosition(grid, currentNodePos):
        return True if (0 <= currentNodePos[0] < grid.row and 0 <= currentNodePos[1] < grid.col) else False

    def __str__(self):
        gridString = ""
        for i in range(self.row):
            for j in range(self.col):
                gridString += self.grid[i][j] + " "
            gridString += "\n"

        return gridString


if __name__ == '__main__':
    inputString = "1100011000101000"
    row = 4
    col = 4

    # build grid
    grid = Grid(row, col, inputString)

    # print grid
    print(grid)

    # find connected cells
    result = Grid.findMaxConnectedCell(grid)

    print(result)
