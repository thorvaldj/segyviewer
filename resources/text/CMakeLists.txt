set(RESOURCES
    help_dialog_text
)

add_custom_target(install_resources ALL)

foreach (file ${RESOURCES})
    add_custom_command(TARGET install_resources
            COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_BINARY_DIR}/resources
            COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_SOURCE_DIR}/${file} ${CMAKE_BINARY_DIR}/resources/text
            )
endforeach ()
get_target_property(INSTALL_PATH package_segyviewlib PACKAGE_INSTALL_PATH)
install(FILES ${RESOURCES} DESTINATION ${INSTALL_PATH}/resources/img)
