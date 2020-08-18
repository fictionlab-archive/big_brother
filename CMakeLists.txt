cmake_minimum_required(VERSION 2.8.3)
project(leo_big_brother)

find_package(catkin REQUIRED COMPONENTS
  message_generation
)

add_message_files(
  DIRECTORY msg
  FILES
  BigBrother.msg
)

generate_messages()

catkin_package(
	CATKIN_DEPENDS message_runtime
)

catkin_install_python(PROGRAMS 
  scripts/control.py
  scripts/watch.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

install(DIRECTORY config/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
)