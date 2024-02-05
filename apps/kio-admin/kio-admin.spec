Name:           kio-admin
Version:        24.02.0
Release:        1%{?dist}
Summary:        Manage files as administrator using the admin:// KIO protocol
License:        (GPL-2.0-only or GPL-3.0-only) and BSD-3-Clause and CC0-1.0 and FSFAP
URL:            https://invent.kde.org/system/kio-admin
%apps_source

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)

BuildRequires:  cmake(Qt6Core)

BuildRequires:  cmake(PolkitQt6-1)


%description
kio-admin implements a new protocol "admin:///" 
which gives administrative access
to the entire system. This is achieved by talking, 
over dbus, with a root-level
helper binary that in turn uses 
existing KIO infrastructure to run file://
operations in root-scope.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE
%cmake_build


%install
%cmake_install
%find_lang kio5_admin %{name}.lang


%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_metainfodir}/org.kde.kio.admin.metainfo.xml
%dir %{_kf6_plugindir}/kfileitemaction/
%{_kf6_plugindir}/kfileitemaction/kio-admin.so
%dir %{_kf6_plugindir}/kio/
%{_kf6_plugindir}/kio/admin.so
%{_kf6_libexecdir}/kio-admin-helper
%{_kf6_datadir}/dbus-1/system.d/org.kde.kio.admin.conf
%{_kf6_datadir}/dbus-1/system-services/org.kde.kio.admin.service
%{_kf6_datadir}/polkit-1/actions/org.kde.kio.admin.policy


%changelog	
* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Thu Apr 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Mon Jan 23 2023 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 1.0.0-1
- initial kio-admin package
