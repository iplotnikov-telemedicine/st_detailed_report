from nodes import NODES


nodes = NODES
for node in nodes:
    all = node.get('children')
    for section in all:
        print(section)