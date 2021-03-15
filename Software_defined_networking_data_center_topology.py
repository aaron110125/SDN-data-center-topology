from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.link import TCLink

class MyTopo( Topo ):

    def build( self ):
        "Create custom topo."

        # Add hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )
        # Add Switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        s7 = self.addSwitch( 's7' )

        # Add links hosts--switches
        self.addLink(h1, s3 ,cls = TCLink,bw=40)
        self.addLink(h2, s3 ,cls = TCLink,bw=40)
        self.addLink(h3, s4 ,cls = TCLink,bw=40)
        self.addLink(h3, s4 ,cls = TCLink,bw=40)
        self.addLink(h4, s4 ,cls = TCLink,bw=40)
        self.addLink(h5, s5 ,cls = TCLink,bw=40)
        self.addLink(h6, s5 ,cls = TCLink,bw=40)
        self.addLink(h7, s6 ,cls = TCLink,bw=40)
        self.addLink(h8, s6 ,cls = TCLink,bw=40)

        #add links s1--All Switches
        self.addLink(s1, s3 ,cls = TCLink,bw=80)
        self.addLink(s1, s4 ,cls = TCLink,bw=80)

        #addlinks s2--All Switches
        self.addLink(s2, s5 ,cls = TCLink,bw=80)
        self.addLink(s2, s6 ,cls = TCLink,bw=80)

        #addlinks s7--All Switches
        self.addLink(s7, s1 ,cls = TCLink,bw=120)
        self.addLink(s7, s2, cls = TCLink,bw=120)

def bootFatTree():
    "Start a fatree topology using mininet"

    #instance of the topology
    topo = MyTopo()

    #network creation using ovs and using a remote controller
    net = Mininet(topo=topo, controller=lambda name: RemoteController( name, ip='127.0.0.1'), switch = OVSSwitch, autoSetMacs=True)

    #start the network
    net.start()

    #user in cli to run the commands
    CLI(net)

    #shut the network after CLI usage by user
    net.stop()

if __name__ == '__main__':
    #this function will run if executed directly
    setLogLevel('info')
    bootFatTree()
