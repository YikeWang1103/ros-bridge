import lcm
import sys
sys.path.insert(0,'/home/yike/Workspace/ros-bridge/carla_ros_bridge/protocol/lcm')
from lcmPointCloud import LcmPointCloud

def sub_handler(channel, data):
	msg = LcmPointCloud.decode(data)
	print("Receive lidar data = %d" %(msg.numPtdCld))
	#print(msg.ptdCld)


lc = lcm.LCM()
subscription = lc.subscribe("POINT_CLOUD", sub_handler)

try:
	while True:
		lc.handle()
except KeyboardInterrupt:
	pass

