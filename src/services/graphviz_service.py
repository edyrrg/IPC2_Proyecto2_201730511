import graphviz


class GraphvizService:
    def __init__(self, name):
        self.name = name
        self.graph = graphviz.Digraph(f'resolve-{self.name}', comment=f'The Graph to MockUp: {self.name}')
        self.graph.attr('node', shape='box')
        self.graph.node("Hello")
        self.graph.node("World")
        self.graph.edge("Hello", "World")
        self.graph.view()


if __name__ == '__main__':
    graphviz_service = GraphvizService('Prueba')