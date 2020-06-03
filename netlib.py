import stdnetlib

class size2D():
    def __init__(self, height, width):
        self.height = height
        self.width = width

class size3D():
    def __init__(self, height, width, layers):
        self.height = height
        self.width  = width

        self.layers = layers

class matrix2D():
    def __init__(self, name):
        self.name = name
        self.matrixContent = []

        self.size2D = size2D(0,0)

    def getElement(self, elementPos):
        # ElementPos is a tuple in form (row, column)
        
        try:
            return self.matrixContent[elementPos[1]][elementPos[0]]
        except IndexError:
            print("ERROR - Matrix2D Content not big enough for indexes given.")
            print("Debug Dump: ")
            print("Matrix Content = " + str(self.matrixContent))
            print("Matrix Maximum Row = " + str(len(self.matrixContent)))

            if self.matrixContent == []:
                print("Matrix Maximum Column = 0")
            else:
                print("Matrix Maximum Column = " + str(len(self.matrixContent[0])))

            print("Row Index = " + str(elementPos[0]))
            print("Column Index = " + str(elementPos[1]))
            print("")

            return "Error 1-1"

    
    def updateElement(self, elementPos, data):
        try:
            self.matrixContent[elementPos[1]][elementPos[0]] = data
        except IndexError:
            print("ERROR - Matrix2D Content not big enough for indexes given.")
            print("Debug Dump: ")
            print("Matrix Content = " + str(self.matrixContent))
            print("Matrix Maximum Row = " + str(len(self.matrixContent)))

            if self.matrixContent == []:
                print("Matrix Maximum Column = 0")
            else:
                print("Matrix Maximum Column = " + str(len(self.matrixContent[0])))

            print("Row Index = " + str(elementPos[0]))
            print("Column Index = " + str(elementPos[1]))
            print("")

            return "Error 1-1"

    def getRow(self, rowNumber):
        try:
            return self.matrixContent[rowNumber]
        except IndexError:
            print("ERROR - Matrix2D Content not big enough for index given.")
            print("Debug Dump: ")
            print("Matrix Content = " + str(self.matrixContent))
            print("Matrix Maximum Row = " + str(len(self.matrixContent)))

            print("Row Index = " + str(rowNumber))
            print("")

            return "Error 1-2"
    
    def getColumn(self, columnNumber):
        column = []

        for rowCounter in range(len(self.matrixContent)):
            try:
                column.append(self.matrixContent[rowCounter][columnNumber])
            except IndexError:
                print("ERROR - Matrix2D Content not big enough for index given.")
                print("Debug Dump: ")
                print("Matrix Content = " + str(self.matrixContent))

                if self.matrixContent == []:
                    print("Matrix Maximum Column = 0")
                else:
                    print("Matrix Maximum Column = " + str(len(self.matrixContent[0])))
                    print("Column Index = " + str(columnNumber))
                
                print("")

                return "Error 1-3"

        return column

    def setMatrix(self, matrix):
        self.matrixContent = matrix
    
    def generateNullMatrix(self, dimensions):
        self.size2D.height = dimensions[0]
        self.size2D.width  = dimensions[1]

        # dimensions is also a tuple in form (row, column)
        for rowCounter in range(dimensions[0]):
            matrixRow = []

            for columnCounter in range(dimensions[1]):
                matrixRow.append(0)
        
            self.matrixContent.append(matrixRow)
    
    def outputMatrixContent(self):
        print("Outputing Matrix2D (Name: " + self.name + ")")
        print(self.matrixContent)
        print("")



class matrix3D():
    def __init__(self, name):
        self.name = name
        self.matrixContent = []

    def getSheet(self, layerNum):
        try:
            return self.matrixContent[layerNum]
        except IndexError:
            print("ERROR - Matrix3D Content not big enough for indexes given.")
            print("Debug Dump: ")
            print("Matrix Content = " + str(self.matrixContent))
            print("Matrix Maximum Layer = " + str(len(self.matrixContent)))

            print("Matrix Layer Index = " + str(layerNum))
            print("")
          
            return "Error 2-1"
    
    def updateSheet(self, layerNoPos, dataSheet):
        try:
            self.matrixContent[layerNoPos] = dataSheet
        except IndexError:
            print("ERROR - Matrix3D Content not big enough for indexes given.")
            print("Debug Dump: ")
            print("Matrix Content = " + str(self.matrixContent))
            print("Matrix Maximum Layer = " + str(len(self.matrixContent)))

            print("Matrix Layer Index = " + str(layerNoPos))
            print("")
          
            return "Error 2-1"
    def getElement(self, elementPos):
        # ElementPos is an array in form [Layer, Row, Column]
        # Error handling not needed here as self.getSheet() deals with that.
        
        return self.getSheet(elementPos[0]).getElement((elementPos[1], elementPos[2]))

    def getColumn(self, elementPos):
        # ElementPos is a tuple in the form (Layer, Column)

        return self.getSheet(elementPos[0]).getColumn(elementPos[1])

    def getRow(self, elementPos):
        # ElementPos is a tuple in the form (Layer, Row)

        return self.getSheet(elementPos[0]).getRow(elementPos[1])

    def setMatrix(self, matrix):
        self.matrixContent = matrix
    
    def generateNullMatrix(self, dimensions):
        # dimensions is also an array in form [Layer, Row, Column]

        self.matrixContent = []

        for layerCounter in range(dimensions[0]):
            newMatrix = matrix2D(self.name + " Layer " + str(layerCounter + 1))

            newMatrix.generateNullMatrix((dimensions[1], dimensions[2]))

            self.matrixContent.append(newMatrix)

    def outputMatrixContent(self):
        content = "Outputing Full Matrix3D (Name: " + self.name + ")"
        lines = len(content) * "-"

        print(content)
        print(lines)
        print("")
        for matrix in self.matrixContent:
            matrix.outputMatrixContent()


class FCLayer():
    def __init__(self, name):
        self.name = name
        self.nodes = matrix2D(name)                 # The node layer will be computed as a matrix (well, a vector - 1xn matrix)

        self.weights = matrix3D("Empty")
        self.bias = 0

    def getNode(self, nodeNum):
        return self.nodes.getElement((1, nodeNum))

    def setWeight(self, weights):
        self.weights = weights
    
    def forwardPass(self, nextLayer):
        for rowCounter in range(nextLayer.size2D.height):
            for columnCounter in range(nextLayer.size2D.width):
                # So the idea here that they're all fully connected. That means that each input has a weight
                # connecting to the relative output. Output is then sigmoid(sum(inputs * weights) + bias).

                # The weights belong to the output in this case, the output offering a matrix2D of weights. 
                # Two pointers, row_pointer and column_pointer cycle through both matricies simulataniously
                # computing said output

                for row_pointer in range(self.nodes.size2D.height):
                    for column_ptr in range(self.nodes.size2D.width):
                        nextLayer.nodes.matrixContent[rowCounter][columnCounter] += (self.nodes.getElement((row_pointer, column_ptr)) * nextLayer.weights.getElement([rowCounter * columnCounter, row_pointer, column_ptr]))
                
                # Adding the bias
                nextLayer.nodes.matrixContent[rowCounter][columnCounter] += nextLayer.bias

                # Sigmoid Squish
                nextLayer.nodes.matrixContent[rowCounter][columnCounter] = stdnetlib.sigmoid(nextLayer.nodes.matrixContent[rowCounter][columnCounter])

    def backPropagation(self, nextLayer, previousSet):
        # Note previousSet should be a tuple/array with two elements. The elements are in the form:
        # [previousDerivative, desiredOutputMatrix]

        # "previousDerivative  = None" when nextLayer is the last layer of the network

        # "desiredOutputMatrix = None" when nextLayer is any other, relying on a previously computed derivative (pretty much
        # handled by the parent class 'Network')

        weightDerivativeCubeForOutputs = matrix3D("Weight Deriv Multi Output")

        # just a key note here for future mila: 
        # This is *just* the weight deriv cube. Nothing more - for the next layer you want a cube (preferably organised)
        # which is multiplied by the weight for the current node deriv (see paper)
        weightDerivativeCubeForOutputs.generateNullMatrix([nextLayer.size2D.height * nextLayer.size2D.width, self.nodes.size2D.height, self.nodes.size2D.width])
        
        for rowCounter in range(nextLayer.size2D.height):
            for columnCounter in range(nextLayer.size2D.width):

                if previousSet[0] == None:
                    # So first during backpropogation, one should form the base
                    backpropBase = 2 * (stdnetlib.sigmoidInverse(nextLayer.nodes.getElement((rowCounter, columnCounter)))) * (nextLayer.nodes.getElement((rowCounter, columnCounter)) - previousSet[1].nodes.getElement((rowCounter, columnCounter)))
                    
                    # List of weight derivatives
                    weightDerivativesTotal = matrix2D("Weight Deriv Single Output")


                    # Weight Deriv Matrix
                    weightDerivativesTotal.generateNullMatrix((self.nodes.size2D.height, self.nodes.size2D.width))

                    # Second to last layer, so no extensions. Just multiplying by table mentioned in paper.
                    for row_pointer in range(self.nodes.size2D.height):
                        for column_pointer in range(self.nodes.size2D.width):
                            finalMultiplier = self.nodes.getElement((row_pointer, column_pointer))

                            weightDerivativesTotal.updateElement((row_pointer, column_pointer), backpropBase * finalMultiplier)
                        
                elif previousSet[1] == None:
                    pass
                else:
                    # some oopsie happened
                    return "Error 4-1"






