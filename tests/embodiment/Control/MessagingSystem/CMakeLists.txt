ADD_DEFINITIONS(-D_REENTRANT -DTEST_CONFIG_FILE=\\"${CMAKE_CURRENT_SOURCE_DIR}/config.cfg\\")

SET(CMAKE_BUILD_TYPE Debug)

ADD_CXXTEST(RouterMessageUTest)
TARGET_LINK_LIBRARIES(RouterMessageUTest Control)

ADD_CXXTEST(FileMessageCentralUTest)
TARGET_LINK_LIBRARIES(FileMessageCentralUTest Control)

ADD_CXXTEST(MemoryMessageCentralUTest)
TARGET_LINK_LIBRARIES(MemoryMessageCentralUTest Control)

ADD_CXXTEST(StringMessageUTest)
TARGET_LINK_LIBRARIES(StringMessageUTest Control)
