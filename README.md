1. clone package into your workspace
2. build package
3. plug usb camera
4. use camera calibration package to generate calibration file for your camera- replace default file in /config directory
5. source your workspace
6. remap topic /cmd_vel to big_brother/cmd_vel in /opt/ros/kinetic/share/leo_bringup/launch/leo_bringup.launch
7. launch test.launch
