import stdnetlib
import random

class size2D():
    def __init__(self, height, width):
        self.height = height
        self.width = width

class size3D():
    def __init__(self, height, width, layers):
        self.height = height
        self.width  = width

        self.layers = layers

class vector():
    def __init__(self, name):
        self.name = name
        self.vectorContent = []

        self.size = 0

    def offsetVectorByVector(self, offsetVector):
        for counter in range(self.size):
            self.updateElement(counter, self.getElement(counter) - offsetVector.getElement(counter))

    def getElement(self, elementPos):
        # elementPos is just the index 

        try:
            return self.vectorContent[elementPos]
        except IndexError:
            print("ERROR - Vector Content not big enough for indexes given.")
            print("Debug Dump: ")
            print("Vector Content = " + str(self.vectorContent))
            print("Vector Maximum Index = " + str(len(self.vectorContent)))

            print("Given Index = " + str(elementPos))
            print("")

            return "Error 5-1"
    
    def updateElement(self, elementPos, data):
        try:
            self.vectorContent[elementPos] = data
        except IndexError:
            print("ERROR - Vector Content not big enough for indexes given.")
            print("Debug Dump: ")
            print("Vector Content = " + str(self.vectorContent))
            print("Vector Maximum Index = " + str(len(self.vectorContent)))

            print("Given Index = " + str(elementPos))
            print("")

            return "Error 5-1"

    def setVector(self, vector):
        self.vectorContent = vector
    
    def generateNullVector(self, dimension):
        self.size = dimension

        # dimensions is also a tuple in form (row, column)
        for counter in range(dimension):
            self.vectorContent.append(0)
    
    def outputVectorContent(self):
        print("Outputing Vector (Name: " + self.name + ")")
        print(self.vectorContent)
        print("")

class matrix2D():
    def __init__(self, name):
        self.name = name
        self.matrixContent = []

        self.size2D = size2D(0,0)

    def offsetMatrixByMatrix(self, offsetMatrix):
        for counter in range(self.size2D.height):
            newVector = self.getRow(counter)
            offsetMatrixVector = offsetMatrix.getRow(counter)

            newVector.offsetVectorByVector(offsetMatrixVector)
            self.insertVector(counter, newVector)

    def getElement(self, elementPos):
        # ElementPos is a tuple in form (row, column)
        
        try:
            return self.matrixContent[elementPos[0]].getElement(elementPos[1])
        except IndexError as e:
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
            raise(e)

            return "Error 1-1"

    
    def updateElement(self, elementPos, data):
        try:
            self.matrixContent[elementPos[0]].updateElement(elementPos[1], data)
        except IndexError as e:
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
            raise(e)

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
    
    def insertVector(self, rowNumber, vector):
        try:
            self.matrixContent[rowNumber] = vector
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
            matrixRow = vector("Matrix 2D (Name: " + self.name + ") Vector")

            matrixRow.generateNullVector(dimensions[1])
        
            self.matrixContent.append(matrixRow)
    
    def outputMatrixContent(self):
        print("Outputing Matrix2D (Name: " + self.name + ")")
        for vectorCounter in range(self.size2D.height):
            self.getRow(vectorCounter).outputVectorContent()
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
    def __init__(self, name, nodes):
        self.name = name
        self.nodes = nodes                 # The node layer will be computed as a vector

        self.weights = matrix2D("Empty")
        self.bias = vector("Empty")

        self.weightDeriv = matrix2D("Empty")
        self.biasDeriv = vector("Empty")

        self.unprimedSheet = vector("Empty")

    def getNode(self, nodeNum):
        return self.nodes.getElement(nodeNum)

    def setWeight(self, weights):
        self.weights = weights
    
    def forwardPass(self, nextLayer):
        for nextLayerNodeCounter in range(nextLayer.nodes.size):
            # So the idea here that they're all fully connected. That means that each input has a weight
            # connecting to the relative output. Output is then sigmoid(sum(inputs * weights) + bias).

            # The weights belong to the output in this case, the output offering a matrix2D of weights. 
            # Two pointers, row_pointer and column_pointer cycle through both matricies simulataniously
            # computing said output

            for thisLayerNodeCounter in range(self.nodes.size):

                nextLayer.nodes.vectorContent[nextLayerNodeCounter] += (self.nodes.getElement(thisLayerNodeCounter) * nextLayer.weights.getElement((nextLayerNodeCounter, thisLayerNodeCounter)))
            
            # Adding the bias
            nextLayer.nodes.vectorContent[nextLayerNodeCounter] += nextLayer.bias.getElement(nextLayerNodeCounter)

            # Sigmoid Squish
            nextLayer.nodes.vectorContent[nextLayerNodeCounter] = stdnetlib.sigmoid(nextLayer.nodes.vectorContent[nextLayerNodeCounter])

    def backPropagation(self, nextLayer, previousSet):
        # Note previousSet should be a tuple/array with two elements. The elements are in the form:
        # [previousDerivative, desiredOutputMatrix]
        previousDerivative = previousSet[0]

        # "previousDerivative  = None" when nextLayer is the last layer of the network

        # "desiredOutputMatrix = None" when nextLayer is any other, relying on a previously computed derivative (pretty much
        # handled by the parent class 'Network')

        # previousDerviative should essentially be a vector() containing the averaged out activation derviatives for each
        # of the respective weights (because it's weight * backpropBase, and there are tons of weights sometimes). every element 
        # in the previous derivative can be mapped to the element in nextLayer.nodes and used from there. We just have to prime it by 
        # multiplying by sigma_derivative(sigma_inverse(node in next layer we're using)) then finding our derivative by multiplying
        # by the picked multiplier.

        weightDerivSheetForOutputs = matrix2D("Weight Deriv Multi Output")

        # just a key note here for future mila: 
        # This is *just* the weight deriv sheet. Nothing more - for the next layer you want a sheet (preferably organised)
        # which is multiplied by the weight for the current node deriv (see paper)
        weightDerivSheetForOutputs.generateNullMatrix((nextLayer.nodes.size, self.nodes.size))

        # This here is the unprimed derivative vector
        unprimedSheet = vector("Unprimed Derivatives For Next Layer")

        unprimedSheet.generateNullVector(self.nodes.size)

        # Bias Derivatives
        self.biasDeriv = vector("Derivates for Biases")
        self.biasDeriv.generateNullVector(nextLayer.nodes.size)
        
        if previousSet[0] == None:
            for nextLayerCounter in range(nextLayer.nodes.size):
                # So first during backpropogation, one should form the base
                backpropBase = 2 * stdnetlib.sigmoidDerivative(stdnetlib.sigmoidInverse(nextLayer.nodes.getElement((nextLayerCounter)))) * (nextLayer.nodes.getElement(nextLayerCounter) - previousSet[1].getElement(nextLayerCounter))
                
                # bias is just * 1
                self.biasDeriv.updateElement(nextLayerCounter, backpropBase)

                # List of weight derivatives
                weightDerivativesTotal = vector("Weight Deriv Single Output")

                # Weight Deriv Matrix
                weightDerivativesTotal.generateNullVector(self.nodes.size)

                
                # Second to last layer, so no extensions. Just multiplying by table mentioned in paper.
                for thisLayerCounter in range(self.nodes.size):
                    finalMultiplier = self.nodes.getElement(thisLayerCounter)

                    weightDerivativesTotal.updateElement(thisLayerCounter, backpropBase * finalMultiplier)
                
                weightDerivSheetForOutputs.insertVector(nextLayerCounter, weightDerivativesTotal)     

            # Yes, I know making another loop is inefficent. But honestly, it should be fairly okay to reimplement and refactor 
            # so that'll be okiedokie hopefully. It's just the switching of loop direction to have more code readability

            for thisLayerCounter in range(self.nodes.size):                
                # Activation sum scalar
                acitvationSumScalar = 0

                for nextLayerCounter in range(nextLayer.nodes.size):
                    backpropBase = 2 * stdnetlib.sigmoidDerivative(stdnetlib.sigmoidInverse(nextLayer.nodes.getElement((nextLayerCounter)))) * (nextLayer.nodes.getElement(nextLayerCounter) - previousSet[1].getElement(nextLayerCounter))
                    
                    # Here the idea is that the row axis is the output index, the columns are the weights for the input for that single output
                    # In coords, it'd look like (x, a), where we loop through "x" being our outputs for our single input "a".

                    # x = nextLayerCounter
                    # a = thisLayerCounter

                    # The usage of another loop comes from the fact the majority of this works with row-first-column-second (maybe i'll call it
                    # RFCS) and this is column-first-row-second (CFRS)
                    acitvationSumScalar += backpropBase * nextLayer.weights.getElement((nextLayerCounter, thisLayerCounter))
                
                # Average it out
                acitvationSumScalar = acitvationSumScalar / nextLayer.nodes.size

                # Add it to the unprimed sheet (to be primed later)
                unprimedSheet.updateElement(thisLayerCounter, acitvationSumScalar)


        elif previousSet[1] == None:
            for nextLayerCounter in range(nextLayer.nodes.size):
                # So although this isn't the second-to-last layer, we'll form a pseudobase by priming the derivatives

                backpropBase = stdnetlib.sigmoidDerivative(stdnetlib.sigmoidInverse(nextLayer.nodes.getElement(nextLayerCounter))) * previousDerivative.getElement(nextLayerCounter)

                # then just as previousSet[0] == None

                # bias is just * 1
                self.biasDeriv.updateElement(nextLayerCounter, backpropBase)

                # List of weight derivatives
                weightDerivativesTotal = vector("Weight Deriv Single Output")

                # Weight Deriv Matrix
                weightDerivativesTotal.generateNullVector(self.nodes.size)

                # Multiplier as per paper table
                for thisLayerCounter in range(self.nodes.size):
                    finalMultiplier = self.nodes.getElement(thisLayerCounter)

                    weightDerivativesTotal.updateElement(thisLayerCounter, backpropBase * finalMultiplier)
                
                weightDerivSheetForOutputs.insertVector(nextLayerCounter, weightDerivativesTotal)     

            for thisLayerCounter in range(self.nodes.size):
                
                # Activation sum scalar
                activationSumScalar = 0

                for nextLayerCounter in range(nextLayer.nodes.size):
                    backpropBase = stdnetlib.sigmoidDerivative(stdnetlib.sigmoidInverse(nextLayer.nodes.getElement(nextLayerCounter))) * previousDerivative.getElement(nextLayerCounter)
                    
                    # Here the idea is that the row axis is the output index, the columns are the weights for the input for that single output
                    # In coords, it'd look like (x, a), where we loop through "x" being our outputs for our single input "a".

                    # x = nextLayerCounter
                    # a = thisLayerCounter

                    # The usage of another loop comes from the fact the majority of this works with row-first-column-second (maybe i'll call it
                    # RFCS) and this is column-first-row-second (CFRS)
                    activationSumScalar += backpropBase * nextLayer.weights.getElement((nextLayerCounter, thisLayerCounter))
                
                # Average it out
                activationSumScalar = activationSumScalar / nextLayer.nodes.size

                # Add it to the unprimed sheet (to be primed later)
                unprimedSheet.updateElement(thisLayerCounter, activationSumScalar)
        else:
            # some oopsie happened
            return "Error 4-1"
        
        self.weightDeriv = weightDerivSheetForOutputs
        self.unprimedSheet = unprimedSheet

# TODO: Develop parent network class. That needs to be properly done (fancy functions and all) to ensure it all works in tandem
# + Linking of layers by generating respective random weights
# + Smooth forward passing
# + Smooth backprop
# + After all is completed, all resets done as needed, the parent should hand back to the child their respective derivatives, and edits made
# 
# ++ Potentially:
# ++ Learning rates
# ++ Saving of most cost-effective weights
# ++ Reload of most cost-effective weights

testNodes = vector("Test")
testHiddenNodes = vector("Test Hidden")
outputTestNodes = vector("Test Output")
desiredOutputTest = vector("Desired Output Test")

testNodes.generateNullVector(3)
testHiddenNodes.generateNullVector(5)
outputTestNodes.generateNullVector(2)
desiredOutputTest.generateNullVector(1)




# So this here is the key thing that the AI is trying to predict. Basically testNode's inputs should match to desiredOutputTest's outputs
testNodes.setVector([0.2, 0.2, 0.3])

desiredOutputTest.setVector([0.1, 0.5])





test = FCLayer("Test", testNodes)
testHidden = FCLayer("Test Hidden", testHiddenNodes)
testOutput = FCLayer("Test Output", outputTestNodes)

testHidden.weights.generateNullMatrix((5, 3))
testHidden.bias.generateNullVector(5)

testOutput.weights.generateNullMatrix((2, 5))
testOutput.bias.generateNullVector(2)

for foo in range(5):
    for bar in range(3):
        testHidden.weights.updateElement((foo, bar), 2 / random.randint(1, 200))
    
    testHidden.bias.updateElement(foo, 2 / random.randint(1, 200))


for foo in range(2):
    for bar in range(5):
        testOutput.weights.updateElement((foo, bar), 2 / random.randint(1, 200))
    
    testOutput.bias.updateElement(foo, 2 / random.randint(1, 200))


test.forwardPass(testHidden)
testHidden.forwardPass(testOutput)


print("===== FIRST RUN =====")
testOutput.nodes.outputVectorContent()


for x in range(10000):
    test.forwardPass(testHidden)
    testHidden.forwardPass(testOutput)

    testHidden.backPropagation(testOutput, [None, desiredOutputTest])
    test.backPropagation(testHidden, [testHidden.unprimedSheet, None])

    testOutput.weights.offsetMatrixByMatrix(testHidden.weightDeriv)
    testOutput.bias.offsetVectorByVector(testHidden.biasDeriv)

    testHidden.weights.offsetMatrixByMatrix(test.weightDeriv)
    testHidden.bias.offsetVectorByVector(test.biasDeriv)



test.forwardPass(testHidden)
testHidden.forwardPass(testOutput)


print("==== LAST RUN ====")
testOutput.nodes.outputVectorContent()
