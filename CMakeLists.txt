cmake_minimum_required(VERSION 3.5)

project(drone_sim LANGUAGES C)

set(INC ${PROJECT_SOURCE_DIR}/Inc/)

set(SOURCES    Src/quadrotor.c
               Src/attitude_control.c
               Src/kalman_backend.c
               Src/kalman_filter.c
               Src/mathlib.c
               Src/matrix_lib.c
               Src/pid.c
               Src/position_control.c
               Src/state_estimation.c
               Src/timer.c
               Src/logger.c)

set(HEADERS   Inc/quadrotor.h
              Inc/attitude_control.h
              Inc/kalman_backend.h
              Inc/kalman_filter.h
              Inc/kalman_filter_types.h
              Inc/mathlib.h
              Inc/matrix_lib.h
              Inc/pid.h
              Inc/position_control.h
              Inc/state_estimation.h
              Inc/timer.h
              Inc/logger.h)

if(WIN32)
    add_custom_target(headers SOURCES ${HEADERS} Inc/win/blender_socket.h)
    add_executable(drone_sim Src/main.c ${SOURCES} Src/win/blender_socket.c)
    target_include_directories(drone_sim PUBLIC ${INC}/win)
else()
    add_custom_target(headers SOURCES ${HEADERS} Inc/linux/blender_socket.h)
    add_executable(drone_sim Src/main.c ${SOURCES} Src/linux/blender_socket.c)
    target_include_directories(drone_sim PUBLIC ${INC}/linux)
endif()

target_include_directories(drone_sim PUBLIC ${INC})

target_link_libraries(drone_sim PUBLIC m)

if(WIN32)
    target_link_libraries(drone_sim PUBLIC wsock32)
endif()

