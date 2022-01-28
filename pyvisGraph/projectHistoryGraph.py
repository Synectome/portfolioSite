from pyvis.network import Network

#https://towardsdatascience.com/pyvis-visualize-interactive-network-graphs-in-python-77e059791f01

net = Network()

# Generate Nodes
net.add_node(1, shape='image', image='static/assets/img/WebDevNode.png', label="Web Dev", title='Web Development', value=200, color='#d37427')
net.add_node(2, shape='image', image='static/assets/img/GameDevNode.png', label="Game Dev", title='Game Development', value=200, color='#1cabc4')
net.add_node(3, shape='image', image='static/assets/img/DataSciNode.png', label="Data Science", title='Data Science', value=200, color='#6610f2')
net.add_node(4, shape='image', image='static/assets/img/SoftDevNode.png', label="Software Dev", title='Software Development', value=200, color='#399136')

net.add_node(5, shape='image', image='static/assets/img/python(250px).png', title="Python", value=120, color='#adb5bd')
net.add_node(6, shape='image', image='static/assets/img/Java(250px).png', title="Java", value=55, color='#adb5bd')
net.add_node(7, shape='image', image='static/assets/img/Cpp(250px).png', title="C++", value=100, color='#adb5bd')
net.add_node(8, shape='image', image='static/assets/img/Clang(250px).png', title="C", value=80, color='#adb5bd')
net.add_node(9, shape='image', image='static/assets/img/R(250px).png', title="R", value=100, color='#adb5bd')
net.add_node(10, shape='image', image='static/assets/img/javascript(250px).png', title="JavaScript", value=60, color='#adb5bd')
net.add_node(11, shape='image', image='static/assets/img/MySQL(250px).png', label="SQL", value=65, color='#adb5bd')
net.add_node(12, shape='image', image='static/assets/img/HTML(apx.250px).png', title="HTML", value=70, color='#adb5bd')
net.add_node(13, shape='image', image='static/assets/img/css(apx.250px).png', title="CSS", value=60, color='#adb5bd')
net.add_node(14, shape='image', image='static/assets/img/GDscript(250px).png', title="GDScript", value=100, color='#adb5bd')

net.add_node(15, shape='image', image='static/assets/img/Godot(250px).png', title="Godot", value=90, color='#1cabc4')
net.add_node(16, shape='image', image='static/assets/img/blender(250px).png', title="Blender", value=60, color='#1cabc4')
net.add_node(17, shape='image', image='static/assets/img/REDCap(250px).png', title="REDCap", value=50, color='#1cabc4')



# Generate Edges
net.add_edges([(1, 5, 5), (1, 12, 2), (1, 13, 1), (1, 10, 2), (1, 11, 3)]) #WebDEV ---Add a rel to R/shiny
net.add_edges([(2, 14, 5), (2, 15, 5), (2, 16, 3)]) # GameDEV
net.add_edges([(3, 5, 5), (3, 9, 5), (3, 17, 2)]) # Data Science
net.add_edges([(4, 5, 4), (4, 6, 2), (4, 7, 4), (4, 8, 3)]) # SoftwareDEV

net.show('nodes.html')
