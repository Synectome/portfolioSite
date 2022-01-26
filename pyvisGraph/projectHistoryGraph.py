from pyvis.network import Network

#https://towardsdatascience.com/pyvis-visualize-interactive-network-graphs-in-python-77e059791f01

net = Network()

# Generate Nodes
net.add_node(1, label="Web Dev", title='Web Development', value=200, color='#d37427')
net.add_node(2, label="Game Dev", title='Game Development', value=200, color='#d37427')
net.add_node(3, label="Data Science", title='Data Science', value=200, color='#d37427')
net.add_node(4, label="Software Dev", title='Software Development', value=200, color='#d37427')

net.add_node(5, shape='circularImage', image='https://www.python.org/static/community_logos/python-logo-master-v3-TM.png', label="Python", value=50, color='#adb5bd')
net.add_node(6, label="Java", value=50, color='#adb5bd')
net.add_node(7, label="C++", value=50, color='#adb5bd')
net.add_node(8, label="C", value=50, color='#adb5bd')
net.add_node(9, label="R", value=50, color='#adb5bd')
net.add_node(10, label="JavaScript", value=50, color='#adb5bd')
net.add_node(11, label="SQL", value=50, color='#adb5bd')
net.add_node(12, label="HTML", value=50, color='#adb5bd')
net.add_node(13, label="CSS", value=50, color='#adb5bd')
net.add_node(14, label="GDScript", value=50, color='#adb5bd')

net.add_node(15, label="Godot", value=50, color='#1cabc4')
net.add_node(16, label="Blender", value=50, color='#1cabc4')
net.add_node(17, label="REDCap", value=50, color='#1cabc4')







# Generate Edges
net.add_edges([(1, 5, 5), (1, 12, 2), (1, 13, 1), (1, 10, 2), (1, 11, 3)]) #WebDEV ---Add a rel to R/shiny
net.add_edges([(2, 14, 5), (2, 15, 5), (2, 16, 3)]) # GameDEV
net.add_edges([(3, 5, 5), (3, 9, 5), (3, 17, 2)]) # Data Science
net.add_edges([(4, 5, 4), (4, 6, 2), (4, 7, 4), (4, 8, 3)]) # SoftwareDEV

net.show('nodes.html')
