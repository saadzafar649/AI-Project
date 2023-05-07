from PyQt5.QtWidgets import *
import sys


class AILabProject():

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
        add_button.clicked.connect(self.add_nodes)


        # to add heuristic
        node1_label = QLabel('Start Node:', window)
        node1_label.move(20, 100)
        self.start = QLineEdit(window)
        self.start.move(100, 100)

        node2_label = QLabel('Goal Node:', window)
        node2_label.move(200, 100)
        self.goal = QLineEdit(window)
        self.goal.move(290, 100)

        add_button = QPushButton('Submit', window)
        button_size = add_button.sizeHint()
        add_button.resize(button_size)
        add_button.move(400, 100)
        add_button.clicked.connect(self.add_nodes)

        #Algo DropDown
        self.algorithms = QComboBox(window)
        self.algorithms.addItems(['BFS', 'UCS', 'DFS', 'DLS', 'IDFS', 'BDS', 'BestFS', 'A*'])
        self.algorithms.setGeometry(20, 140, 100, 30)

        #Graph Type DropDown
        self.graphtype = QComboBox(window)
        self.graphtype.addItems(['Directed Graph', 'Undirected Graph'])
        self.graphtype.setGeometry(180, 140, 200, 30)

    def add_nodes(self):
        node1 = self.node1_input.text()
        node2 = self.node2_input.text()
        weight = self.weight_input.text()
        self.node1_input.clear()
        self.node2_input.clear()
        self.weight_input.clear()
        print(f"Node1: {node1}, Node2: {node2}, Weight: {weight}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle('Input Field Example')
    window.resize(779, 790)
    ui = AILabProject()
    ui.load_gui(window)
    window.show()
    sys.exit(app.exec_())
