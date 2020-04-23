cmake_minimum_required(VERSION 2.8.3)
project(leo_big_brother)

find_package(catkin REQUIRED COMPONENTS
  ar_track_alvar
  geometry_msgs
  usb_cam
)

catkin_package(

)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

