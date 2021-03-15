# SDN-data-center-topology
A data center topology using Mininet emulator on SDN VM 

![image](https://user-images.githubusercontent.com/22559413/111225882-bb6da800-85b6-11eb-9c8c-f91822c1370a.png)

Run it with the command: cd /home/ubuntu/ryu && ./bin/ryu-manager --verbose ryu/app/simple_switch_13.py /home/ryu/ryu/ryu/app/ofctl_rest.py

cd /home/ubuntu/ryu && ./bin/ryu-manager --verbose ryu/app/simple_switch_stp.py /home/ryu/ryu/ryu/app/ofctl_rest.py
	To check the transmission bandwidth on a host: iperf -c 10.0.0.1 -i 1 -t 5

