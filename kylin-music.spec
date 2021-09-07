%define debug_package %{nil}
Name:           kylin-music
Version:        1.0.44
Release:        2
Summary:        kylin-music
License:        GPL-3.0 License
URL:            https://github.com/UbuntuKylin/kylin-music
Source0:        %{name}-%{version}.tar.gz
Source1:        kylin-music_zh_CN.qm


patch0:	      	0001-modify-kylin-music-complier-error.patch
patch1:         0001_fix_chinese_translation_issue.patch

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  zlib-devel
BuildRequires:  libX11-devel
BuildRequires:  libcrystalhd-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  libXext-devel
BuildRequires:  taglib-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  gsettings-qt-devel
BuildRequires:  kf5-kwindowsystem-devel


Requires:  gstreamer1
Requires:  gstreamer1-plugins-bad-free
Requires:  gstreamer1-plugins-good
%description
kylin-music


%prep

%setup -q
%patch0 -p1
%patch1 -p1

%build

export PATH=%{_qt5_bindir}:$PATH
sed -i 's|/usr/lib/libtag.so|/usr/lib64/libtag.so|g' kylin-music.pro
sed -i 's|/usr/lib/libtag_c.so|/usr/lib64/libtag_c.so|g' kylin-music.pro

mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build}
popd 

%install

pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 

mkdir -p %{buildroot}/usr/share/kylin-music/data/

cp -r %{_builddir}/%{name}-%{version}/data/kylin-music %{buildroot}/usr/share/kylin-music/data
cp -r %{_builddir}/%{name}-%{version}/translations/* %{buildroot}/usr/share/kylin-music
cp -r %{SOURCE1} %{buildroot}/usr/share/kylin-music

%files
%doc debian/changelog
%license  debian/copyright 
%{_bindir}/kylin-music
%{_datadir}/applications/kylin-music.desktop
%{_datadir}/glib-2.0/schemas/org.kylin-music-data.gschema.xml
%{_datadir}/pixmaps/kylin-music.png
%{_datadir}/kylin-music/

%changelog
* Mon Sep 06 2021 douyan <douyan@kylinos.cn> - 1.0.44-2
- add missing translation

* Thu Aug 19 2021 peijiankang <peijiankang@kylinos.cn> - 1.0.44-1
- Init kylin-music package for openEuler

