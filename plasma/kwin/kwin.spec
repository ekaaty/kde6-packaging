%bcond x11 1

Name:    kwin
Version: 6.1.4
Release: 1%{?dist}
Summary: KDE Window manager

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL AND MIT
URL:     https://userbase.kde.org/KWin
%plasma_source

# Base
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros

# Qt
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  qt6-qtbase-devel
# KWinQpaPlugin (and others?)
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires:  qt6-qtsensors-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  cmake(Qt6Core5Compat)

# X11/OpenGL
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libxcb-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libXcursor-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libcap-devel

BuildRequires:  lcms2-devel
BuildRequires:  glib2-devel
BuildRequires:  pipewire-devel

# Wayland
BuildRequires:  cmake(KWayland)
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  libxkbcommon-devel >= 0.4
BuildRequires:  pkgconfig(libinput) >= 0.10
BuildRequires:  pkgconfig(libudev)

# KF6
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(KDecoration2)
BuildRequires:  kscreenlocker-devel
BuildRequires:  plasma-breeze-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  cmake(KGlobalAccelD)
BuildRequires:  libdisplay-info-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libeis-1.0)

## Runtime deps
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       kf6-kdeclarative%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       kscreenlocker%{?_isa} >= %{basever}
Requires:       libplasma%{?_isa} >= %{basever}
Requires:       qt6-qt5compat%{?_isa}
Requires:       qt6-qtdeclarative%{?_isa}
Requires:       qt6-qtmultimedia%{?_isa}

# http://bugzilla.redhat.com/605675
# until initial-setup is fixed... (#1197135)
Provides: firstboot(windowmanager) = kwin

Requires:   %{name}-wayland = %{version}-%{release}

%description
%{summary}.

%package        wayland
Summary:        KDE Window Manager with Wayland support
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       kwayland-integration%{?_isa} >= %{basever}
BuildRequires:  pkgconfig(xwayland)
Requires:       xorg-x11-server-Xwayland
# http://bugzilla.redhat.com/605675
Provides:       firstboot(windowmanager) = kwin_wayland
%if ! %{with x11}
# Obsolete kwin-x11 as we are dropping the package
Obsoletes:      %{name}-x11 < %{version}-%{release}
%endif
%description    wayland
%{summary}.

%if %{with x11}
%package        x11
Summary:        KDE Window Manager with X11 support
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       xorg-x11-server-Xorg
# http://bugzilla.redhat.com/605675
Provides:       firstboot(windowmanager) = kwin_x11
# KWinX11Platform (and others?)

%description    x11
%{summary}.
%endif

%package        common
Summary:        Common files for KWin X11 and KWin Wayland
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kwayland%{?_isa} >= %{basever}
%description    common
%{summary}.

%package        libs
Summary:        KWin runtime libraries
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Quick)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6WindowSystem)
Requires:       pkgconfig(wayland-server)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        User manual for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-html --all-name
grep "%{_kf6_docdir}" %{name}.lang > %{name}-doc.lang
cat %{name}.lang %{name}-doc.lang | sort | uniq -u > kwin6.lang

# temporary(?) hack to allow initial-setup to use /usr/bin/kwin too
ln -sr %{buildroot}%{_kf6_bindir}/kwin_wayland %{buildroot}%{_bindir}/kwin

%if ! %{with x11}
# Delete x11 session stuff
rm -v %{buildroot}%{_kf6_bindir}/kwin_x11 %{buildroot}%{_userunitdir}/plasma-kwin_x11.service
%endif


%files
%{_bindir}/kwin

%files common -f kwin6.lang
%{_kf6_datadir}/applications/*.desktop
%{_kf6_datadir}/config.kcfg/kwin.kcfg
%{_kf6_datadir}/config.kcfg/kwindecorationsettings.kcfg
%{_kf6_datadir}/config.kcfg/nightlightsettings.kcfg
%{_kf6_datadir}/config.kcfg/virtualdesktopssettings.kcfg
%{_kf6_datadir}/icons/hicolor/*/apps/kwin.*
%{_kf6_datadir}/kconf_update/kwin.upd
%{_kf6_datadir}/knotifications6/kwin.notifyrc
%{_kf6_datadir}/knsrcfiles/*.knsrc
%{_kf6_datadir}/krunner/dbusplugins/kwin-runner-windows.desktop
%{_kf6_datadir}/kwin/
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen
%{_kf6_libdir}/kconf_update_bin/kwin-6.1-remove-gridview-expose-shortcuts
%{_kf6_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_kf6_qtplugindir}/kf6/packagestructure/kwin_*.so
%{_kf6_qtplugindir}/kwin/
%{_kf6_qtplugindir}/org.kde.kdecoration2/*.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/*.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/*.so
%{_libexecdir}/kwin_killer_helper
%{_libexecdir}/kwin-applywindowdecoration
%{_qt6_plugindir}/org.kde.kdecoration2.kcm/kcm_auroraedecoration.so
%{_qt6_qmldir}/org/kde/kwin/

%files wayland
%caps(cap_sys_nice=ep) %{_kf6_bindir}/kwin_wayland
%{_kf6_bindir}/kwin_wayland_wrapper
%{_userunitdir}/plasma-kwin_wayland.service

%if %{with x11}
%files x11
%{_kf6_bindir}/kwin_x11
%{_userunitdir}/plasma-kwin_x11.service
%endif

%files libs
%{_kf6_datadir}/qlogging-categories6/org_kde_kwin.categories
%{_kf6_libdir}/libkcmkwincommon.so.%{basever}
%{_kf6_libdir}/libkcmkwincommon.so.6
%{_kf6_libdir}/libkwin.so.%{basever}
%{_kf6_libdir}/libkwin.so.6

%files devel
%{_includedir}/kwin/
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_kf6_libdir}/cmake/KWin
%{_kf6_libdir}/cmake/KWinDBusInterface
%{_kf6_libdir}/libkwin.so

%files doc -f %{name}-doc.lang
%license LICENSES/*.txt


%changelog
* Tue Aug 06 2024 Pavel Solovev <daron439@gmail.com> - 6.1.4-1
- Update to 6.1.4

* Fri Jul 26 2024 Pavel Solovev <daron439@gmail.com> - 6.1.3-3
- pick upstream commits

* Wed Jul 17 2024 Pavel Solovev <daron439@gmail.com> - 6.1.3-2
- pick upstream commit

* Tue Jul 16 2024 Pavel Solovev <daron439@gmail.com> - 6.1.3-1
- Update to 6.1.3

* Tue Jul 02 2024 Pavel Solovev <daron439@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Tue Jun 25 2024 Pavel Solovev <daron439@gmail.com> - 6.1.1-1
- Update to 6.1.1

* Tue Jun 18 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Fri May 24 2024 Pavel Solovev <daron439@gmail.com> - 6.0.90-1
- Update to 6.0.90

* Tue May 21 2024 Pavel Solovev <daron439@gmail.com> - 6.0.5-3
- drop explicit sync

* Tue May 21 2024 Pavel Solovev <daron439@gmail.com> - 6.0.5-1
- Update to 6.0.5

* Tue May 21 2024 Pavel Solovev <daron439@gmail.com> - 6.0.4.1-3
- backport explicit sync, fix dnd in chromium

* Sat May 04 2024 Neal Gompa <ngompa@fedoraproject.org> - 6.0.4.1-2
- Persist CAP_SYS_NICE capability for kwin_wayland binary

* Tue Apr 16 2024 Pavel Solovev <daron439@gmail.com> - 6.0.4-1
- Update to 6.0.4

* Wed Mar 27 2024 Pavel Solovev <daron439@gmail.com> - 6.0.3.1-1
- Update to 6.0.3.1

* Tue Mar 26 2024 Pavel Solovev <daron439@gmail.com> - 6.0.3-1
- Update to 6.0.3

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.2-2
- qmlcache rebuild

* Fri Nov 24 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-5
- Explicit QML runtime dependencies

* Fri Nov 24 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-4
- plasma-framework was renamed

* Fri Nov 17 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.27.80-3
- Drop -x11 subpackage and have -wayland subpackage obsolete it

* Wed Nov 15 2023 Steve Cossette <farchord@gmail.com> - 5.27.80-2
- Updated -common requirement mistake

* Mon Nov 13 2023 Steve Cossette <farchord@gmail.com> - 5.27.80-1
- 5.27.80

* Fri Nov 03 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.27.9-2
- Mark kwin-x11 as deprecated

* Tue Oct 24 2023 Steve Cossette <farchord@gmail.com> - 5.27.9-1
- 5.27.9

* Tue Sep 12 2023 justin.zobel@gmail.com - 5.27.8-1
- 5.27.8

* Tue Aug 01 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.7-1
- 5.27.7

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.6-1
- 5.27.6

* Wed May 10 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.5-1
- 5.27.5

* Wed Apr 12 2023 Marc Deop marcdeop@fedoraproject.org - 5.27.4.1-1
- Re-spin from upstream

* Tue Apr 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.4-1
- 5.27.4

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.3-2
- Add patch from upstream
- Fixes BZ#2180100

* Tue Mar 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.3-1
- 5.27.3

* Tue Feb 28 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-1
- 5.27.2

* Sun Feb 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.1-3
- Add missing BuildRequires
- Clean up commented code

* Wed Feb 22 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.1-2
- Add patch to fix BZ#2168034

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.1-1
- 5.27.1

* Mon Feb 20 2023 Adam Williamson <awilliam@redhat.com> - 5.27.0-2
- Allow VT switching even if global shortcuts are disabled

* Thu Feb 09 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Thu Jan 19 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- 5.26.90

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Justin Zobel <justin@1707.io> - 5.26.5-1
- Update to 5.26.5

* Tue Nov 29 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.4-1
- 5.26.4

* Wed Nov 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.3-1
- 5.26.3

* Wed Oct 26 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.2-1
- 5.26.2

* Tue Oct 18 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.1-1
- 5.26.1

* Thu Oct 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.0-1
- 5.26.0

* Sat Sep 17 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.90-1
- 5.25.90

* Wed Sep 07 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.5-1
- 5.25.5

* Wed Aug 03 2022 Justin Zobel <justin@1707.io> - 5.25.4-1
- Update to 5.25.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.25.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 5.25.3-2
- Rebuild (qt5)

* Tue Jul 12 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.3-1
- 5.25.3

* Tue Jun 28 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.2-1
- 5.25.2

* Tue Jun 21 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.1-1
- 5.25.1

* Thu Jun 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.0-1
- 5.25.0

* Fri May 20 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.90-1
- 5.24.90
- remove kwayland-server dependency

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 5.24.5-2
- Rebuild (qt5)

* Tue May 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.5-1
- 5.24.5

* Thu Mar 31 2022 Justin Zobel <justin@1707.io> - 5.24.4-1
- Update to 5.24.4 and remove patch

* Mon Mar 21 2022 Adam Williamson <awilliam@redhat.com> - 5.24.3-3
- Backport MR #2163 (edited to cover vbox) to fix VM cursor offset (#2063969)

* Thu Mar 10 2022 Marc Deop <marcdeop@fedoraproejct.org> - 5.24.3-2
- Rebuild (qt5)

* Tue Mar 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.3-1
- 5.24.3

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 5.24.2-3
- Rebuild (qt5)

* Wed Feb 23 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.24.2-2
- pull in upstream fix for https://bugs.kde.org/show_bug.cgi?id=449273

* Tue Feb 22 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.24.2-1
- 5.24.2

* Tue Feb 15 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.1-1
- 5.24.1

* Fri Feb 11 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.0-2
- Rebuild due to tarball re-spin

* Thu Feb 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.0-1
- 5.24.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.23.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.23.90-1
- 5.23.90

* Tue Jan 04 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.23.5-1
- 5.23.5

* Tue Dec 14 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.4-1
- 5.23.4

* Wed Nov 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.23.3-1
- 5.23.3

* Tue Oct 26 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.23.2-1
- 5.23.2

* Sat Oct 23 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.1-1
- 5.23.1

* Fri Oct 08 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.0-1
- 5.23.0

* Sun Sep 19 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.22.90-2
- Remove patch already applied upstream
- Add BuildRequires plasma-wayland-protocols-devel
- Adjust files section

* Fri Sep 17 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.22.90-1
- 5.22.90

* Fri Sep 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.22.5-2
- pull in proposed libglvnd-1.3.4 FTBFS fix (kde#440372, rh#2002431)

* Tue Aug 31 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.5-1
- 5.22.5

* Tue Jul 27 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.4-1
- 5.22.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.3-1
- 5.22.3

* Tue Jun 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.2.1-1
- 5.22.2.1

* Tue Jun 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.2-1
- 5.22.2

* Tue Jun 15 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.1-1
- 5.22.1

* Sun Jun 06 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.0-1
- 5.22.0

* Fri May 14 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.21.90-1
- 5.21.90

* Thu May 13 2021 Jonathan Wakely <jwakely@redhat.com> - 5.21.5-3
- Add patch to fix focus follows mouse (#1960208)

* Wed May 05 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.5-2
- Use dma-bufs for screensharing only when client asks for it

* Tue May 04 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.5-1
- 5.21.5

* Tue Apr 06 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.4-1
- 5.21.4

* Tue Mar 16 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.3-1
- 5.21.3

* Tue Mar 02 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.2-1
- 5.21.2

* Tue Feb 23 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.1-1
- 5.21.1

* Mon Feb 15 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.0-2
- Tarball respin

* Thu Feb 11 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.0-1
- 5.21.0

* Mon Feb 08 2021 Neal Gompa <ngompa13@gmail.com> - 5.20.90-4
- Add patch to ensure Xauthority file is generated for Wayland (rhbz#1921947)

* Thu Jan 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.20.90-3
- pull in upstream wayland fix (kde#432189)
- .spec cosmetics
- revert BR: make (not needed)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Jan Grulich <jgrulich@redhat.com> - 5.20.90-1
- 5.20.90 (beta)

* Tue Jan  5 16:03:31 CET 2021 Jan Grulich <jgrulich@redhat.com> - 5.20.5-1
- 5.20.5

* Fri Jan 01 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.20.4-3
- -wayland: add explicit versioned dep on kwayland-server

* Thu Dec 10 10:57:46 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.4-2
- Fix screensharing on Wayland with Chromium

* Tue Dec  1 09:42:59 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.4-1
- 5.20.4

* Mon Nov 30 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.3-3
- Fix screensharing for xwayland apps

* Mon Nov 23 07:53:19 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.3-2
- rebuild (qt5)

* Wed Nov 11 08:33:06 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.3-1
- 5.20.3

* Thu Nov  5 07:55:10 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.2-3
- Backport upstream fix for clipboard issue

* Sat Oct 31 10:01:51 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 5.20.2-2
- Obsolete kwin-wayland-nvidia package by kwin-wayland since kwin now
  automatically supports NVIDIA graphics correctly on Wayland

* Tue Oct 27 14:23:03 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.2-1
- 5.20.2

* Tue Oct 20 15:28:57 CEST 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.1-1
- 5.20.1

* Tue Oct 13 14:51:44 CEST 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.0-2
- Updated sources

* Sun Oct 11 19:50:03 CEST 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.0-1
- 5.20.0

* Sat Oct 03 2020 Neal Gompa <ngompa13@gmail.com> - 5.19.90-2
- Use Wayland by default for F34+
  https://fedoraproject.org/wiki/Changes/WaylandByDefaultForPlasma

* Fri Sep 18 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.90-1
- 5.19.90

* Thu Sep 17 2020 Neal Gompa <ngompa13@gmail.com> - 5.19.5-3
- Split out X11 support and set up conditional for Wayland by default
- Add kwin-wayland-nvidia package for NVIDIA driver configuration

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.5-2
- rebuild (qt5)

* Tue Sep 01 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.5-1
- 5.19.5

* Tue Jul 28 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.4-1
- 5.19.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.3-2
- Don't perform MouseActivateRaiseAndPassClick for topmost windows

* Tue Jul 07 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.3-1
- 5.19.3

* Tue Jun 23 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.2-1
- 5.19.2

* Wed Jun 17 2020 Martin Kyral <martin.kyral@gmail.com> - 5.19.1-1
- 5.19.1

* Tue Jun 9 2020 Martin Kyral <martin.kyral@gmail.com> - 5.19.0-1
- 5.19.0

* Fri May 15 2020 Martin Kyral <martin.kyral@gmail.com> - 5.18.90-1
- 5.18.90

* Tue May 05 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.5-1
- 5.18.5

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.18.4.1-2
- rebuild (qt5)

* Sat Apr 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.18.4.1-1
- 5.18.4.1

* Tue Mar 31 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.4-1
- 5.18.4

* Tue Mar 10 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.3-1
- 5.18.3

* Tue Feb 25 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.2-1
- 5.18.2

* Tue Feb 18 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.1-1
- 5.18.1

* Tue Feb 11 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.0-1
- 5.18.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.17.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Jan Grulich <jgrulich@redhat.com> - 5.17.90-1
- 5.17.90

* Wed Jan 08 2020 Jan Grulich <jgrulich@redhat.com> - 5.17.5-1
- 5.17.5

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.4-2
- rebuild (qt5)

* Thu Dec 05 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.4-1
- 5.17.4

* Wed Nov 13 2019 Martin Kyral <martin.kyral@gmail.com> - 5.17.3-1
- 5.17.3

* Wed Oct 30 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.2-1
- 5.17.2

* Wed Oct 23 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.1-1
- 5.17.1

* Wed Oct 16 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.0-2
- Updated tarball

* Thu Oct 10 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.0-1
- 5.17.0

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 5.16.90-2
- rebuild (qt5)

* Fri Sep 20 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.90-1
- 5.16.90

* Fri Sep 06 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.5-1
- 5.16.5

* Tue Jul 30 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.4-1
- 5.16.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.3-1
- 5.16.3

* Wed Jun 26 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.2-1
- 5.16.2

* Tue Jun 25 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.16.1-3
- rebuild (qt5)

* Wed Jun 19 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.16.1-2
- pull in 5.16 branch fix

* Tue Jun 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.16.1-1
- 5.16.1

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 5.16.0-2
- rebuild (qt5)

* Tue Jun 11 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.0-1
- 5.16.0

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 5.15.90-2
- rebuild (qt5)

* Thu May 16 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.90-1
- 5.15.90

* Thu May 09 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.5-1
- 5.15.5

* Wed Apr 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.15.4-1
- 5.15.4

* Wed Mar 13 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.3.2-1
- 5.15.3.2
- tarball respun to remove docs causing build issues with KDocTools < 5.57

* Tue Mar 12 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.3-1
- 5.15.3

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.15.2-3
- rebuild (qt5)

* Thu Feb 28 2019 Pete Walter <pwalter@fedoraproject.org> - 5.15.2-2
- Update wayland deps

* Tue Feb 26 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.15.2-1
- 5.15.2

* Tue Feb 19 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.15.1-1
- 5.15.1

* Wed Feb 13 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.0-1
- 5.15.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Martin Kyral <martin.kyral@gmail.com> - 5.14.90-1
- 5.14.90

* Wed Dec 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.14.4-2
- rebuild (qt5)

* Tue Nov 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.14.4-1
- 5.14.4

* Thu Nov 08 2018 Martin Kyral <martin.kyral@gmail.com> - 5.14.3-1
- 5.14.3

* Wed Oct 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.14.2-1
- 5.14.2

* Tue Oct 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.14.1-1
- 5.14.1

* Fri Oct 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.14.0-1
- 5.14.0

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.13.90-2
- rebuild (qt5)

* Fri Sep 14 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.90-1
- 5.13.90

* Tue Sep 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.5-1
- 5.13.5

* Fri Aug 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.4-2
- rebuild

* Thu Aug 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.4-1
- 5.13.4

* Fri Jul 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.3-4
- use %%_qt5_qmldir (#1604528)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.3-1
- 5.13.3

* Mon Jul 09 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.2-1
- 5.13.2

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.1-2
- rebuild (qt5)

* Tue Jun 19 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.1-1
- 5.13.1

* Sat Jun 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.0-1
- 5.13.0

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.12.90-2
- rebuild (qt5)

* Fri May 18 2018 Martin Kyral <martin.kyral@gmail.com> - 5.12.90-1
- 5.12.90

* Tue May 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.12.5-1
- 5.12.5

* Tue Mar 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.12.4-1
- 5.12.4

* Thu Mar 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.12.3-2
- -common: add versioned dep on kf5-kwayland (no longer optional)
- use %%make_build %%ldconfig_scriptlets
- BR: libcap-devel

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.12.3-1
- 5.12.3

* Wed Feb 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.12.2-1
- 5.12.2

* Tue Feb 13 2018 Jan Grulich <jgrulich@redhat.com> - 5.12.1-1
- 5.12.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.12.0-2
- respin

* Fri Feb 02 2018 Jan Grulich <jgrulich@redhat.com> - 5.12.0-1
- 5.12.0

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.11.95-2
- Remove obsolete scriptlets

* Mon Jan 15 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.95-1
- 5.11.95

* Tue Jan 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.5-1
- 5.11.5

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 5.11.4-2
- rebuild (qt5)

* Thu Nov 30 2017 Martin Kyral <martin.kyral@gmail.com> - 5.11.4-1
- 5.11.4

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.11.3-2
- rebuild (qt5)

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.11.3-1
- 5.11.3

* Wed Oct 25 2017 Martin Kyral <martin.kyral@gmail.com> - 5.11.2-1
- 5.11.2

* Tue Oct 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.11.1-1
- 5.11.1

* Wed Oct 11 2017 Martin Kyral <martin.kyral@gmail.com> - 5.11.0-1
- 5.11.0

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.5-3
- confirmed only -wayland uses private api

* Tue Oct 10 2017 Jan Grulich <jgrulich@redhat.com> - 5.10.5-2
- rebuild (qt5)

* Thu Aug 24 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.5-1
- 5.10.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.4-1
- 5.10.4

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.3.1-2
- rebuild (qt5)

* Mon Jul 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.3.1-1
- kwin-5.10.3.1

* Mon Jul 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.3-3
- respin

* Sun Jul 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.3-2
- enable tests, support %%bootstrap, update URL

* Tue Jun 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.3-1
- 5.10.3

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.2-1
- 5.10.2

* Tue Jun 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.1-1
- 5.10.1

* Wed May 31 2017 Jan Grulich <jgrulich@redhat.com> - 5.10.0-1
- 5.10.0

* Thu May 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.5-3
- rebuild (qt5)

* Wed Apr 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.5-2
- -doc: use %%find_lang --with-html

* Wed Apr 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.5-1
- 5.9.5

* Fri Mar 31 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.4-2
- rebuild (qt5), update URL

* Thu Mar 23 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.4-1
- 5.9.4

* Sat Mar 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.3-2
- rebuild

* Wed Mar 01 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.3-1
- 5.9.3

* Tue Feb 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.8.6-1
- 5.8.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.5-1
- 5.8.5

* Thu Dec 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.4-3
- rebuild (qt5)

* Sat Dec 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.4-2
- rebuild (qt5)

* Tue Nov 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.4-1
- 5.8.4

* Thu Nov 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.3-2
- release++

* Thu Nov 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.3-1.2
- branch rebuild (qt5)

* Tue Nov 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.3-1
- 5.8.3

* Mon Oct 31 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.2-2
- pull in upstream fixes

* Tue Oct 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.2-1
- 5.8.2

* Tue Oct 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.1-1
- 5.8.1

* Thu Sep 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.8.0-1
- 5.8.0

* Thu Sep 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.95-1
- 5.7.95

* Tue Sep 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.5-1
- 5.7.5

* Tue Aug 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.4-1
- 5.7.4

* Tue Aug 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.3-2
- patch-n-relax breeze verision

* Tue Aug 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.3-1
- 5.7.3

* Fri Jul 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.2-2
- BR: plasma-breeze-devel

* Tue Jul 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.2-1
- 5.7.2

* Tue Jul 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-5
- rebuild (qt5)

* Fri Jul 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-4
- add versioned qt5 dep in main pkg too

* Thu Jul 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-3
- -wayland: Requires: xorg-x11-server-Xwayland

* Thu Jul 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-2
- -wayland: KWinQpaPlugin uses private Qt5 apis, BR: qt5-qtbase-private-devel

* Tue Jul 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-1
- 5.7.1

* Thu Jun 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-1
- 5.7.0

* Sat Jun 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.95-1
- 5.6.95

* Tue Jun 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.5-1
- 5.6.5

* Sat May 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.4-1
- 5.6.4

* Wed Apr 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.3-2
- tighten kscreenlocker, kdecoration runtime deps (#1328942)
- -wayland: relax kwayland-integration runtime dep

* Tue Apr 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.3-1
- 5.6.3

* Sat Apr 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.2-1
- 5.6.2

* Fri Apr 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.1-1
- 5.6.1

* Tue Mar 01 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.5-1
- Plasma 5.5.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.4-1
- Plasma 5.5.4

* Thu Jan 14 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.3-2
- -BR: cmake, use %%license

* Thu Jan 07 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.3-1
- Plasma 5.5.3

* Thu Dec 31 2015 Rex Dieter <rdieter@fedoraproject.org> 5.5.2-2
- update URL, use %%majmin_ver for more plasma-related deps

* Thu Dec 31 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.5.2-1
- 5.5.2

* Fri Dec 18 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.1-1
- Plasma 5.5.1

* Thu Dec 03 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.0-1
- Plasma 5.5.0

* Wed Nov 25 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.4.95-1
- Plasma 5.4.95

* Thu Nov 05 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.4.3-1
- Plasma 5.4.3

* Sat Oct 24 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-4
- respin (rawhide)

* Fri Oct 23 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-3
- latest batch of upstream fixes (kde#344278,kde#354164,kde#351763,kde#354090)

* Tue Oct 20 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-2
- .spec cosmetics, backport kwin/aurorae crasher fix (kde#346857)

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.2-1
- 5.4.2

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-3
- tigthen kdecorration-devel dep

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-2
- -devel: move dbus xml interface files here

* Wed Sep 09 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.1-1
- 5.4.1

* Wed Sep 02 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-4
- versioned kf5-kwayland dep too
- make kwayland-integration dep arch'd

* Wed Sep 02 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-3
- add versioned Requires: kwin-libs dep to main pkg

* Tue Aug 25 2015 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-2
- add upstream patch to fix crash
- make sure kwayland-integration is installed for kwin-wayland

* Fri Aug 21 2015 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-1
- Plasma 5.4.0

* Thu Aug 13 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.95-1
- Plasma 5.3.95

* Thu Jun 25 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.2-1
- Plasma 5.3.2

* Wed Jun 17 2015 Rex Dieter <rdieter@fedoraproject.org> 5.3.1-4
- BR: kf5-kcompletion-devel kf5-kiconthemes-devel kf5-kio-devel

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.1-1
- Plasma 5.3.1

* Tue May 19 2015 Rex Dieter <rdieter@fedoraproject.org> 5.3.0-5
- move dbus xml files to -libs (so present for -devel)

* Sun May 17 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.3.0-4
- followup SM fix, discard support (kde#341930)
- note qt5-qtmultimedia dep is runtime-only

* Thu May 14 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.3.0-3
- test candidate SM fixes (reviewboard#123580,kde#341930)
- move libkdeinit bits out of -libs
- move dbus interface xml to runtime pkg
- drop %%config from knsrc files
- enable wayland support (f21+)
- .spec cosmetics

* Wed Apr 29 2015 Jan Grulich <jgrulich@redhat.com> - 5.3.0-2
- BR xcb-util-cursor-devel

* Mon Apr 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- Plasma 5.3.0

* Wed Apr 22 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.95-1
- Plasma 5.2.95

* Tue Apr 07 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.2-2
- tarball respin

* Fri Mar 20 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.2-1
- Plasma 5.2.2

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-4
- Rebuild (GCC 5)

* Fri Feb 27 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.2.1-3
- Provide /usr/bin/kwin too (#1197135)
- bump plasma_version macro

* Fri Feb 27 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-2
- Provides: firstboot(windowmanager) = kwin_x11  (#605675)

* Tue Feb 24 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-1
- Plasma 5.2.1

* Sun Feb 08 2015 Daniel Vrátil <dvratli@redhat.com> - 5.2.0.1-2
- Obsoletes: kwin-gles, kwin-gles-libs

* Wed Jan 28 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0.1-1
- Update to upstream hotfix release 5.2.0.1 (kwindeco KCM bugfix)

* Wed Jan 28 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-3
- add upstream patch for bug #341971 - fixes Window decorations KCM

* Tue Jan 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-2
- -doc: Don't require arch-specific kwin in noarch package

* Mon Jan 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- Plasma 5.2.0

* Mon Jan 12 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-1.beta
- Plasma 5.1.95 Beta

* Wed Dec 17 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-2
- Plasma 5.1.2

* Tue Nov 18 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-3
- Fixed license
- Fixed scriptlets
- Fixed Conflicts in -devel
- -docs is noarch

* Wed Nov 12 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-2
- added optional Wayland support

* Fri Nov 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-1
- Plasma 5.1.1

* Tue Oct 14 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0.1-1
- Plasma 5.1.0.1

* Thu Oct 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- Plasma 5.1.0

* Tue Sep 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.2-1
- Plasma 5.0.2

* Sun Aug 10 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.1-1
- Plasma 5.0.1

* Wed Jul 16 2014 Daniel Vrátil <dvratil@redhat.com> 5.0.0-1
- Plasma 5.0.0

* Wed May 14 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-1.20140514git61c631c
- Update to latest upstream git snapshot

* Fri Apr 25 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1.20140425gitb92f4a6
- Initial package
