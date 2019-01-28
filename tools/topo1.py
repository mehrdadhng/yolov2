#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')
info('*** Adding docker containers\n')
d1 = net.addDocker('decoder', ip='10.0.0.251', dimage="containernet:ubuntu1604")
d2 = net.addDocker('server', ip='10.0.0.252', dimage="containernet:ubuntu1604")
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
info('*** Creating links\n')
net.addLink(d1, s1)
net.addLink(d2, s1)
info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([d1, d2])
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()