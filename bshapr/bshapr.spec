# Global variables for github repository
%global commit0 ac3ce0372f93d23b29d4d6b6d2328429dce30603
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Beat / envelope shaper LV2 plugin
Name:    lv2-BShapr
Version: 0.8.0
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/sjaehn/BShapr

Source0: https://github.com/sjaehn/BShapr/archive/%{commit0}.tar.gz#/BShapr-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
Beat / envelope shaper LV2 plugin

%prep
%setup -qn BShapr-%{commit0}

%build

make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install
%{__rm} -rf %{buildroot}
make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC" install

%clean
%{__rm} -rf %{buildroot}

%files
%doc LICENSE README.md
%{_libdir}/lv2/*

%changelog
* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 0.8.0-1
- update to 0.8.0-1

* Thu Jan 16 2020 Yann Collette <ycollette dot nospam at free.fr> 0.7.0-1
- update to 0.7.0-1

* Sat Nov 30 2019 Yann Collette <ycollette dot nospam at free.fr> 0.6.0-1
- update to 0.6.0-1

* Sun Oct 13 2019 Yann Collette <ycollette dot nospam at free.fr> 0.4.0-1
- update to 0.4.0-1

* Sat Aug 24 2019 Yann Collette <ycollette dot nospam at free.fr> 0.3.2-1
- initial release 
