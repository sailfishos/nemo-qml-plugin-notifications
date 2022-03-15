TEMPLATE = subdirs

SUBDIRS += src doc

no-qml {
    message(Building without QML dependency.)
} else {
    message(Building with QML dependency.)
    src_plugins.subdir = src/plugin
    src_plugins.target = sub-plugins
    src_plugins.depends = src
    SUBDIRS += src_plugins
}
