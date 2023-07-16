TARGET = nemonotifications
PLUGIN_IMPORT_PATH = Nemo/Notifications
QT += dbus
QT -= gui

TEMPLATE = lib
CONFIG += qt plugin hide_symbols
QT += qml

INCLUDEPATH += ..
LIBS += -L.. -lnemonotifications-qt$${QT_MAJOR_VERSION}
SOURCES += plugin.cpp

target.path = $$[QT_INSTALL_QML]/$$PLUGIN_IMPORT_PATH
qmldir.files += \
        qmldir \
        plugins.qmltypes
qmldir.path +=  $$target.path
INSTALLS += target qmldir

qmltypes.commands = qmlplugindump -nonrelocatable Nemo.Notifications 1.0 > $$PWD/plugins.qmltypes
QMAKE_EXTRA_TARGETS += qmltypes

OTHER_FILES += qmldir
