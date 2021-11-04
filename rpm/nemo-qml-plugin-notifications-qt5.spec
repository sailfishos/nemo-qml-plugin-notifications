Name:       nemo-qml-plugin-notifications-qt5
Summary:    Notifications plugin for Nemo Mobile
Version:    1.2.0
Release:    1
License:    BSD
URL:        https://github.com/sailfishos/nemo-qml-plugin-notifications/
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  sailfish-qdoc-template

%description
%{summary}.

%package devel
Summary:    Notifications support for C++ applications
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%package doc
Summary: Documentation for %{name}
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

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake_install
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -R doc/html/* %{buildroot}/%{_docdir}/%{name}/

# org.nemomobile.notifications legacy import
mkdir -p %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/notifications/
ln -sf %{_libdir}/qt5/qml/Nemo/Notifications/libnemonotifications.so %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/notifications/
sed 's/Nemo.Notifications/org.nemomobile.notifications/' < src/plugin/qmldir > %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/notifications/qmldir

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE
%{_libdir}/libnemonotifications-qt5.so.*
%{_libdir}/qt5/qml/Nemo/Notifications

# org.nemomobile.notifications legacy import
%{_libdir}/qt5/qml/org/nemomobile/notifications

%files devel
%defattr(-,root,root,-)
%{_libdir}/libnemonotifications-qt5.so
%{_libdir}/libnemonotifications-qt5.prl
%{_includedir}/nemonotifications-qt5
%{_libdir}/pkgconfig/nemonotifications-qt5.pc

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}
