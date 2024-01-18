Name:       kwayland
Version:    5.92.0
Release:    1%{?dist}
Summary:    KDE Frameworks 6 library that wraps Client and Server Wayland libraries

License:    BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT-CMU AND MIT
URL:        https://invent.kde.org/plasma/%{name}

%plasma_source

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  appstream
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires:  qt6-qttools-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6WaylandClient)

Requires:   kf6-filesystem

# Renamed from kf6-kwayland
Obsoletes:      kf6-kwayland < 1:%{version}-%{release}
Provides:       kf6-kwayland = 1:%{version}-%{release}

%description
%{summary}.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   qt6-qtbase-devel
Obsoletes:  kf6-kwayland-devel < 1:%{version}-%{release}
Provides:   kf6-kwayland-devel = 1:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKWaylandClient.so.%{version}
%{_kf6_libdir}/libKWaylandClient.so.6

%files devel
%doc README.md
%license LICENSES/*.txt
%{_includedir}/KWayland/
%{_kf6_libdir}/cmake/KWayland/
%{_kf6_libdir}/libKWaylandClient.so
%{_kf6_libdir}/pkgconfig/KWaylandClient.pc

%changelog
* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- Renamed from kf6-kwayland
- 5.27.80

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230922.150947.770e361-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230922.150947.770e361-2
- Rebuild for Qt Private API

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230922.150947.770e361-1
- Initial release
