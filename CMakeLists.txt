cmake_minimum_required(VERSION 2.8.3)
project(leo_big_brother)

find_package(catkin REQUIRED COMPONENTS
  ar_track_alvar
  geometry_msgs
  usb_cam
  message_generation
)


add_message_files(
  DIRECTORY msg
  FILES
  BigBrother.msg
)

# install(DIRECTORY msg/
#     DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/msg
# )

generate_messages()

catkin_package(
	CATKIN_DEPENDS message_runtime
)

