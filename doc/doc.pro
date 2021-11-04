TEMPLATE = aux

CONFIG += sailfish-qdoc-template
SAILFISH_QDOC.project = nemo-qml-plugin-notifications
SAILFISH_QDOC.config = nemo-qml-plugin-notifications.qdocconf
SAILFISH_QDOC.style = offline
SAILFISH_QDOC.path = /usr/share/doc/nemo-qml-plugin-notifications-qt5

OTHER_FILES += \
    $$PWD/src/nemo-qml-plugin-notifications.qdoc
