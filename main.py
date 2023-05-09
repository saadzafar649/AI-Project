import networkx as nx
import matplotlib.pyplot as plt


from PyQt5.QtWidgets import *
import sys
from BFS import *
from DFS import *
from UCS import *
from DLS import *
from BestFS import *


graph = {}
weights = {}
heuristic = {}

graphUnDir = {}
weightsUnDir = {}


graph = {
    'a': ['c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['a', 'b'],
    'e': ['b', 'c'],
}

weights = {
    ('a','c'):1,
    ('b','d'):1,
    ('c','e'):1,
    ('d','a'):1,
    ('d','b'):1,
    ('e','b'):1,
    ('e','c'):1,
}


graphUnDir = {
    '1':['2','3'],
    '2':['4','5','1'],
    '3':['6','7','1'],
    '4' :['2','7'],
    '5' :['2'],
    '6' :['3'],
    '7' :['3','4'],
}

weightsUnDir = {
    ('1','2'):1,
    ('1','3'):1,
    ('2','4'):7,
    ('2','5'):1,
    ('6','3'):1,
    ('7','3'):1,
    ('7', '4'): 1,

    ('2','1'): 1,
    ('3','1'): 1,
    ('4','2'): 7,
    ('5','2'): 1,
    ('3','6'): 1,
    ('3','7'): 1,
    ('4','7'): 1,
}

heuristic = {
    '1': 1,
    '2': 2,
    '3': 2,
    '4': 4,
    '5': 0,
    '6': 1,
    '7': 3
}

class AILabProject:

    def showerror(self,error):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(error)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    def load_gui(self, window):
        #to add nodes

        node1_label = QLabel('Node1:', window)
        node1_label.move(20, 20)
        self.node1_input = QLineEdit(window)
        self.node1_input.move(80, 20)

        node2_label = QLabel('Node2:', window)
        node2_label.move(200, 20)
        self.node2_input = QLineEdit(window)
        self.node2_input.move(260, 20)

        weight_label = QLabel('Edge Weight:', window)
        weight_label.move(380, 20)
        self.weight_input = QLineEdit(window)
        self.weight_input.move(470, 20)

        add_button = QPushButton('Add Nodes', window)
        add_button.move(600, 20)
        add_button.clicked.connect(self.add_nodes)

        # to add heuristic
        node1_label = QLabel('Node:', window)
        node1_label.move(20, 60)
        self.node = QLineEdit(window)
        self.node.move(80, 60)

        node2_label = QLabel('Node Heuristic:', window)
        node2_label.move(200, 60)
        self.nodeHeuristic = QLineEdit(window)
        self.nodeHeuristic.move(290, 60)

        add_button = QPushButton('Add Node Heuristic', window)
        button_size = add_button.sizeHint()
        add_button.resize(button_size)
        add_button.move(400, 60)
        add_button.clicked.connect(self.add_node_heuristic)


        # to add heuristic
        node1_label = QLabel('Start Node:', window)
        node1_label.move(20, 100)
        self.start = QLineEdit(window)
        self.start.move(100, 100)

        node2_label = QLabel('Goal Node:', window)
        node2_label.move(200, 100)
        self.goal = QLineEdit(window)
        self.goal.move(290, 100)

        node2_label = QLabel('Depth Limit:', window)
        node2_label.move(400, 100)
        self.depth_limit = QLineEdit(window)
        self.depth_limit.move(500, 100)

        add_button = QPushButton('Submit', window)
        button_size = add_button.sizeHint()
        add_button.resize(button_size)
        add_button.move(600, 100)
        add_button.clicked.connect(self.apply_algorithm)

        #Algo DropDown
        self.algorithms = QComboBox(window)
        self.algorithms.addItems(['BFS', 'UCS', 'DFS', 'DLS', 'IDFS', 'BDS', 'BestFS', 'A*'])
        self.algorithms.setGeometry(20, 140, 100, 30)

        #Graph Type DropDown
        self.graphtype = QComboBox(window)
        self.graphtype.addItems(['Undirected Graph','Directed Graph'])
        self.graphtype.setGeometry(180, 140, 200, 30)


        add_button = QPushButton('Show Graph', window)
        button_size = add_button.sizeHint()
        add_button.resize(button_size)
        add_button.move(400, 140)
        add_button.clicked.connect(self.drawGraph)

    def apply_algorithm(self):
        algo = self.algorithms.currentText()
        start = self.start.text()
        goal = self.goal.text()
        limit = 0
        if self.depth_limit.text() != "":
            limit = int(self.depth_limit.text())

        graphType = self.graphtype.currentText()
        # nodesList = graph.keys()

        if graphType == "Directed Graph":
            if start not in graph or goal not in graph:
                print("select valid nodes")
                return
        else:
            if start not in graphUnDir or goal not in graphUnDir:
                print("select valid nodes")
                return

        self.start.clear()
        self.goal.clear()
        output = (0,"No output")
        if graphType == 'Undirected Graph':
            if algo == 'BFS':
                output = BFS(start,goal, graphUnDir, False)
            elif algo == 'DFS':
                output = DFS(start,goal, graphUnDir, False)
            elif algo == 'UCS':
                output = UCS(graphUnDir,weightsUnDir,start,goal, False)
            elif algo == 'BestFS':
                output = BestFS(graphUnDir,heuristic,start,goal, False)
            elif algo == 'DLS':
                output = DLS(graphUnDir,limit,start,goal, False)
        else:
            if algo == 'BFS':
                output = BFS(start, goal, graph, True)
            elif algo == 'DFS':
                output = DFS(start,goal, graph, True)
            elif algo == 'UCS':
                output = UCS(graph,weights,start,goal, True)
            elif algo == 'BestFS':
                output = BestFS(graph,heuristic,start,goal, True)
            elif algo == 'DLS':
                output = DLS(graph,limit,start,goal, True)

        if output[0] == 0:
            self.showerror(output[1])
        else:
            print(output[1])



    def add_nodes(self):
        node1 = self.node1_input.text()
        node2 = self.node2_input.text()
        weight = self.weight_input.text()
        graphType = self.graphtype.currentText()
        self.node1_input.clear()
        self.node2_input.clear()
        self.weight_input.clear()

        print(graphType)

        if node1 not in graphUnDir:
            graph[node1]=[]
            graphUnDir[node1]=[]

        if node2 not in graphUnDir:
            graph[node2]=[]
            graphUnDir[node2] = []

        if node2 not in graph[node1]:
            graph[node1].append(node2)
            graphUnDir[node1].append(node2)

        # if node1 not in graphUnDir[node2]:
        #     graphUnDir[node2].append(node1)

        # if graphType == "Undirected Graph":
        if node1 not in graphUnDir[node2]:
            graphUnDir[node2].append(node1)

        weightsUnDir[(node2, node1)] = int(weight)
        weightsUnDir[(node1,node2)] = int(weight)

        weights[(node1,node2)] = int(weight)


        print(graphUnDir)
        print(weightsUnDir)
        print(f"Node1: {node1}, Node2: {node2}, Weight: {weight}")

    def add_node_heuristic(self):
        node = self.node.text()
        nodeHeuristic = self.nodeHeuristic.text()
        self.node.clear()
        self.nodeHeuristic.clear()

        if node in graph and nodeHeuristic != '':
            heuristic[node]=int(nodeHeuristic)
            print(heuristic)


    def drawGraph(self):

        graphType = self.graphtype.currentText()
        # nodesList = graph.keys()

        if graphType == "Directed Graph":
            nodesList = graph.keys()
            weightList = weights.keys()
            DG = nx.DiGraph()
            DG.add_nodes_from(nodesList)
            DG.add_edges_from(weightList)
            pos1 = nx.spring_layout(DG)

            pos_attrs = {}
            for node, coords in pos1.items():
                pos_attrs[node] = (coords[0], coords[1] + 0.19)

            nx.draw(DG, pos1, with_labels=True, node_color="blue", node_size=1000, font_color="white", font_size=20,
                    font_family="Times New Roman", font_weight="bold", width=5, edge_color="black")
            nx.draw_networkx_edge_labels(DG, pos1, font_size=26, edge_labels=weights, font_color='red')

            nx.draw_networkx_labels(DG, pos_attrs, labels=heuristic, font_size=12, font_color='k',
                                    font_family='sans-serif', font_weight='normal', alpha=None, bbox=None,
                                    horizontalalignment='center', verticalalignment='center', ax=None, clip_on=True)

            # nx.draw(DG, pos1, with_labels=True)
            # nx.draw_networkx_edge_labels(DG, pos1)
            #
            # nx.draw_networkx_labels(DG, pos_attrs, labels=custom_node_attrs)

            plt.margins(0.2)
            plt.show()
        else:
            nodesList = graphUnDir.keys()
            weightList = weightsUnDir.keys()
            G = nx.Graph()
            G.add_nodes_from(nodesList)
            G.add_edges_from(weightList)
            pos = nx.spring_layout(G)

            pos_attrs = {}
            for node, coords in pos.items():
                pos_attrs[node] = (coords[0], coords[1] + 0.19)

            nx.draw(G, pos, with_labels=True, node_color="blue", node_size=1000, font_color="white", font_size=20,
                    font_family="Times New Roman", font_weight="bold", width=5, edge_color="black")
            nx.draw_networkx_edge_labels(G, pos, font_size=26, edge_labels=weightsUnDir, font_color='red')

            nx.draw_networkx_labels(G, pos_attrs, labels=heuristic, font_size=12, font_color='k',
                                    font_family='sans-serif', font_weight='normal', alpha=None, bbox=None,
                                    horizontalalignment='center', verticalalignment='center', ax=None, clip_on=True)

            plt.margins(0.2)
            plt.show()








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle('Input Field Example')
    window.resize(779, 790)
    ui = AILabProject()
    ui.load_gui(window)
    window.show()
    sys.exit(app.exec_())

