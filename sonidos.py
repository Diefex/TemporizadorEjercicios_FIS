from pyo import *
server = Server().boot()
server.start()
sf = SfPlayer("komodo.mp3", mul=0.1).out()
input()   # raw_input() en Python 2
server.stop()