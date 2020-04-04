from random import randrange
import random
import math

class Grid:
    def __init__(self, row, col, inputString, covid):
        self.row = row
        self.col = col
        self.inputString = inputString
        self.covid = covid
        self.grid = self.buildGrid(row, col, inputString)
        self.traversePath = []

    @staticmethod
    def buildGrid(row, col, inputString):
        cells = list(inputString)

        grid = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                grid[i][j] = cells[i * col + j]

        return grid

    @staticmethod
    def findMaxConnectedCell(grid):

        visitedNodes = []

        for node in grid.covid:
            i = int(node.split("-")[1])
            j = int(node.split("-")[0])

            if (i, j) in visitedNodes or grid.grid[i][j] == '0':
                nodeVisit = dict({
                    "node": (i, j),
                    "path": [],
                    "pathSize": 0,
                })
                grid.traversePath.append(nodeVisit)
                continue

            nodeList = []

            grid.DFS(grid, (i, j), visitedNodes, nodeList)

            # added to traverse path
            nodeVisit = dict({
                "node": (i, j),
                "path": nodeList,
                "pathSize": len(nodeList),
            })
            grid.traversePath.append(nodeVisit)

        return grid

    @staticmethod
    def BFS(grid):

        visitedNodes = []

        for node in grid.covid:
            i = int(node.split("-")[1])
            j = int(node.split("-")[0])

            if (i, j) in visitedNodes or grid.grid[i][j] == '0':
                nodeVisit = dict({
                    "node": (i, j),
                    "path": [],
                    "pathSize": 0,
                })
                grid.traversePath.append(nodeVisit)
                continue

            queue = [(i, j)]
            path = []
            while len(queue) > 0:
                currentNode = queue.pop(0)

                if currentNode not in path:
                    path.append(currentNode)

                neighbors = Grid.findNeighbor(grid, currentNode)

                for neighbor in neighbors:
                    if neighbor not in visitedNodes:
                        queue.append(neighbor)
                        visitedNodes.append(neighbor)

            nodeVisit = dict({
                "node": (i, j),
                "path": path,
                "pathSize": len(path),
            })
            grid.traversePath.append(nodeVisit)

        return grid

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

    @staticmethod
    def randomInputStringAndCovidNoSocialDistance():
        strLen = 880
        binaryStr = ""
        ones = []
        covidStr = ""

        for i in range(strLen):
            binaryNum = randrange(2)
            binaryStr += str(binaryNum)
            if binaryNum == 1:
                ones.append(len(binaryStr)-1)

        # random number of covid position
        covidPosition = []
        for i in range(2):
            ranNum = ones[randrange(len(ones))]
            covidPosition.append(ranNum)

        # convert ones position into grid position
        for i in covidPosition:
            localCol = i % 40;
            localRow = math.ceil((i - localCol) / 40)
            localCell = str(localCol)+"-"+str(localRow)
            covidStr += localCell+"_"

        covidStr = covidStr[:-1]

        return covidStr+"|"+binaryStr

    @staticmethod
    def randomInputStringAndCovidSocialDistance():
        strLen = 880
        col = 40
        binaryStr = ""
        ones = []
        prohibittedCell = []
        covidStr = ""

        for i in range(strLen):
            binaryNum = randrange(2)
            if binaryNum == 1 and i not in prohibittedCell:

                binaryStr += str(binaryNum)
                ones.append(len(binaryStr) - 1)

                # addProhibitedCell:
                prohibittedCell.append(i + 1)
                prohibittedCell.append(i + col + 1)
                prohibittedCell.append(i + col)
                prohibittedCell.append(i + col - 1)
                prohibittedCell.append(i - 1)
                prohibittedCell.append(i - col)
                prohibittedCell.append(i - col - 1)
                prohibittedCell.append(i - col + 1)
            else:
                binaryStr += str(0)

        # random number of covid position
        iter = 7 if len(ones) > 7 else len(ones)
        covidPosition = []
        for i in range(iter):
            ranNum = ones[randrange(len(ones))]
            covidPosition.append(ranNum)

        # convert ones position into grid position
        for i in covidPosition:
            localCol = i % 40;
            localRow = math.ceil((i - localCol) / 40)
            localCell = str(localCol) + "-" + str(localRow)
            covidStr += localCell + "_"

        covidStr = covidStr[:-1]

        return covidStr + "|" + binaryStr

    def __str__(self):
        gridString = ""
        for i in range(self.row):
            for j in range(self.col):
                gridString += self.grid[i][j] + " "
            gridString += "\n"

        return gridString


if __name__ == '__main__':
    # string = Grid.randomInputStringAndCovidNoSocialDistance()
    # string = Grid.randomInputStringAndCovidSocialDistance()
    # print(string)
    pass
    # inputString = "1100000000" \
    #               "1111000000" \
    #               "0110000000" \
    #               "0100000000" \
    #               "0000000000" \
                  # "0000000000" \
                  # "0000000000" \
                  # "0000000000" \
                  # "0000000000" \
                  # "0000000000"
    # row = 5
    # col = 10
    #
    # # build grid
    # grid = Grid(row, col, inputString)
    #
    # # print grid
    # print(grid)
    #
    # # find connected cells
    # result = Grid.findMaxConnectedCell(grid)
    #
    # print(result)

    # print(randrange(10))

