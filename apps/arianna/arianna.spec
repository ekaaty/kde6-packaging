Name:          arianna
Version:       24.01.95
Release:       1%{?dist}
Summary:       EPub Reader for mobile devices
# Complete license breakdown can be found in the "LICENSE-BREAKDOWN" file.
License:       GPLv3
URL:           https://invent.kde.org/graphics/%{name}
%apps_source

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Baloo)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(KF6QuickCharts)
BuildRequires: cmake(KF6WindowSystem)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6HttpServer)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6WebChannel)
BuildRequires: cmake(Qt6WebSockets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6WebEngineQuick)

# QML module dependencies
Requires: kf6-kirigami%{?_isa}
Requires: kf6-kirigami-addons%{?_isa}
Requires: kf6-kitemmodels%{?_isa}
Requires: kf6-kquickcharts%{?_isa}
Requires: kf6-qqc2-desktop-style%{?_isa}
Requires: qt6-qtwebchannel%{?_isa}
Requires: qt6-qtwebengine%{?_isa}

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch: %{qt6_qtwebengine_arches}

%description
An ebook reader and library management app


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.arianna.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.arianna.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/arianna
%{_kf6_datadir}/applications/org.kde.arianna.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.arianna.svg
%{_kf6_datadir}/qlogging-categories6/arianna.categories
%{_kf6_metainfodir}/org.kde.arianna.appdata.xml

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Sun Dec 03 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.80-1
- 24.01.80

* Thu Nov 23 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 24.01.75-1
- 24.01.75

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 11 2023 Steve Cossette <farchord@gmail.com> - 1.1.0-1
- This release adds a table of content overview as well as a book detail dialog.

* Mon May 29 2023 Steve Cossette <farchord@gmail.com> - 1.0.1-2
- Added more install dependancies
- Cleaned up the licensing text by moving the license breakdown to a separate file

* Sun May 21 2023 Steve Cossette <farchord@gmail.com> - 1.0.1-1
- Initial release
