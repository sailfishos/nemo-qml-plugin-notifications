system($$[QT_HOST_BINS]/qdbusxml2cpp org.freedesktop.Notifications.xml -p notificationmanagerproxy -c NotificationManagerProxy -i notification_p.h)

TEMPLATE = lib
TARGET = nemonotifications-qt5
CONFIG += qt hide_symbols create_pc create_prl
QT += dbus

SOURCES += notification.cpp \
    notificationmanagerproxy.cpp

HEADERS += \
    notification.h \
    notification_p.h \
    notificationmanagerproxy.h

target.path = $$[QT_INSTALL_LIBS]
pkgconfig.files = $$TARGET.pc
pkgconfig.path = $$target.path/pkgconfig
headers.files = notification.h notification_p.h
headers.path = /usr/include/nemonotifications-qt5

QMAKE_PKGCONFIG_NAME = lib$$TARGET
QMAKE_PKGCONFIG_DESCRIPTION = Convenience library or sending notifications
QMAKE_PKGCONFIG_LIBDIR = $$target.path
QMAKE_PKGCONFIG_INCDIR = $$headers.path
QMAKE_PKGCONFIG_DESTDIR = pkgconfig

INSTALLS += target headers pkgconfig
