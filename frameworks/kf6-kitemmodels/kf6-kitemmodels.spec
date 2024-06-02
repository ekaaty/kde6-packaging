%global		framework kitemmodels

Name:		kf6-%{framework}
Version:	6.2.0
Release:	1%{?dist}.1
Summary:	KDE Frameworks 6 Tier 1 addon with item models

License:	CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Qml)

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with item models.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%qch_package

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6ItemModels.so.6
%{_kf6_libdir}/libKF6ItemModels.so.%{version}
%{_kf6_qmldir}/org/kde/kitemmodels/

%files devel
%{_qt6_docdir}/*.tags
%doc README.md
%license LICENSES/*.txt
%{_kf6_includedir}/KItemModels/
%{_kf6_libdir}/cmake/KF6ItemModels/
%{_kf6_libdir}/libKF6ItemModels.so


%changelog
* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1.1
- rebuild for f40

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Sep 26 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230914.113622.4c5c663-1
- Initial Release
