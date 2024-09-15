import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/utabot/Desktop/UTABOT/ros2_ws/install/utabot_controller'
