%define debug_package %{nil}
Name:           kylin-music
Version:        1.1.2
Release:        1
Summary:        kylin-music
License:        GPL-3.0-or-later and MIT
URL:            https://github.com/UbuntuKylin/kylin-music
Source0:        %{name}-%{version}.tar.gz


patch0:	      	0001-fix-compile-error-of-kylin-music.patch

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qtchooser
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  taglib-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  ukui-interface libpeony3 libpeony-dev
BuildRequires:  mpv-libs-devel
BuildRequires:  sqlite-devel libXtst-devel


%description
kylin-music


%prep

%setup -q
%patch0 -p1

%build

export PATH=%{_qt5_bindir}:$PATH

mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build}
popd 

%install

pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 

mkdir -p %{buildroot}/usr/share/kylin-user-guide/data/guide

cp -r %{_builddir}/%{name}-%{version}/data/kylin-music %{buildroot}/usr/share/kylin-user-guide/data/guide/

%files
%doc debian/changelog
%license  debian/copyright 
%{_bindir}/kylin-music
%{_datadir}/applications/kylin-music.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pixmaps/kylin-music.png
%{_datadir}/kylin-music/
%{_datadir}/kylin-user-guide/data/guide/*

%changelog
* Tue Jun 14 2022 peijiankang <peijiankang@kylinos.cn> - 1.1.2-1
- update version to 1.1.2

* Tue Jun 7 2022 peijiankang <peijiankang@kylinos.cn> - 1.0.44-6
- add kylin-user-guide file

* Wed May 18 2022 tanyulong<tanyulong@kylinos.cn> - 1.0.44-5
- Improve the project according to the requirements of compliance improvement

* Thu Apr 7 2022 peijiankang <peijiankang@kylinos.cn> - 1.0.44-4
- modify version is error

* Wed Sep 08 2021 douyan <douyan@kylinos.cn> - 1.0.44-3
- fix_title_bar_issue.patch

* Mon Sep 06 2021 douyan <douyan@kylinos.cn> - 1.0.44-2
- add missing translation

* Thu Aug 19 2021 peijiankang <peijiankang@kylinos.cn> - 1.0.44-1
- Init kylin-music package for openEuler

