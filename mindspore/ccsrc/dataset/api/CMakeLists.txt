file(GLOB_RECURSE _CURRENT_SRC_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "*.cc")
set_property(SOURCE ${_CURRENT_SRC_FILES} PROPERTY COMPILE_DEFINITIONS SUBMODULE_ID=mindspore::SubModuleId::SM_MD)
add_library(APItoPython OBJECT
  de_pipeline.cc
  python_bindings.cc
  )
target_include_directories(APItoPython PRIVATE ${pybind11_INCLUDE_DIRS})
