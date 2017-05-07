#!/usr/bin/env python
#import docker
from subprocess import call
nodes = {
    "node1": 8801,
    "node2": 8802,
    "node3": 8803,
    "node4": 8804,
    "node5": 8805
}

#client = docker.DockerClient(base_url='unix://var/run/docker.sock')

"""
for running on local processes
"""


def shellStart():
    for port in nodes.values():
        call(['congredi', '-p', port, 'peer'])


def shellStop():
    call(['pkill', 'congredi'])

"""
For running test networks on the local machine. If running via
docker-machine, see the examples in delegito.
"""

"""
def dockerStart():
    print('starting')
    for name, port in nodes.items():
        args = {'exposeport': str(port)}
        ports = {port: port}
        print("building {0} as {1}".format(name, ports))
        img = client.images.build(
            path='.', nocache=False, tag=name, buildargs=args, rm=True)
        print("running {0} as {1}".format(name, ports))
        client.containers.run(img, ports=ports, detach=True, name=name)
    print('done')


def dockerStop():
    print('stopping')
    for name in nodes.keys():
        print("stopping {0}".format(name))
        client.containers.stop(name)
    print('done')

dockerStart()
"""
