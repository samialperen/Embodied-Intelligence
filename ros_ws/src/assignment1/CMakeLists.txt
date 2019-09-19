cmake_minimum_required(VERSION 2.8.3)
project(assignment1)
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
  geometry_msgs
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_package()

add_executable(scan_listener src/main.cpp)
target_link_libraries(scan_listener ${catkin_LIBRARIES})


