Name:       nemo-qml-plugin-notifications-qt5
Summary:    Notifications plugin for Nemo Mobile
Version:    1.1.2
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://git.merproject.org/mer-core/nemo-qml-plugin-notifications
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  mer-qdoc-template

%description
%{summary}.

%package devel
Summary:    Notifications support for C++ applications
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%package doc
Summary: Documentation for %{name}
Group: Documentation
BuildRequires: qt5-qttools-qthelp-devel
BuildRequires: qt5-tools
BuildRequires: qt5-plugin-platform-minimal
BuildRequires: qt5-plugin-sqldriver-sqlite

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5 VERSION=%{version}

make %{?jobs:-j%jobs}
make docs

%install
rm -rf %{buildroot}
%qmake_install
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -R html/* %{buildroot}/%{_docdir}/%{name}/

# org.nemomobile.notifications legacy import
mkdir -p %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/notifications/
ln -sf %{_libdir}/qt5/qml/Nemo/Notifications/libnemonotifications.so %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/notifications/
sed 's/Nemo.Notifications/org.nemomobile.notifications/' < src/plugin/qmldir > %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/notifications/qmldir

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libnemonotifications-qt5.so.*
%dir %{_libdir}/qt5/qml/Nemo/Notifications
%{_libdir}/qt5/qml/Nemo/Notifications/libnemonotifications.so
%{_libdir}/qt5/qml/Nemo/Notifications/qmldir
%{_libdir}/qt5/qml/Nemo/Notifications/plugins.qmltypes

# org.nemomobile.notifications legacy import
%dir %{_libdir}/qt5/qml/org/nemomobile/notifications
%{_libdir}/qt5/qml/org/nemomobile/notifications/libnemonotifications.so
%{_libdir}/qt5/qml/org/nemomobile/notifications/qmldir

%files devel
%defattr(-,root,root,-)
%{_libdir}/libnemonotifications-qt5.so
%{_libdir}/libnemonotifications-qt5.prl
%{_includedir}/nemonotifications-qt5/*.h
%{_libdir}/pkgconfig/nemonotifications-qt5.pc

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}
