# Tag: Library
# Type: Devel
# Category: Audio

Summary: LinuxSampler Control Protocol library
Name:    liblscp
Version: 0.9.3
Release: 1%{?dist}
License: GPL
URL:     https://www.linuxsampler.org

Distribution: Planet CCRMA
Vendor:       Planet CCRMA

Source0: http://download.linuxsampler.org/packages/liblscp-%{version}.tar.gz

BuildRequires: automake autoconf libtool make
BuildRequires: linuxsampler-devel
BuildRequires: gcc gcc-c++

%description
LinuxSampler Control Protocol library

%package devel
Summary:  LinuxSampler Control Protocol library developer resources
Requires: %{name} = %{version}-%{release}

%description devel
LinuxSampler Control Protocol library developer resources

%prep
%autosetup
if [ -f Makefile.cvs ]; then make -f Makefile.cvs; fi

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/liblscp.so.*

%files devel
%{_includedir}/lscp
%{_libdir}/liblscp.so
%{_libdir}/liblscp.a
%exclude %{_libdir}/liblscp.la
%{_libdir}/pkgconfig/lscp.pc

%changelog
* Sun May 23 2021 Yann Collette <ycollette.nospam@free.fr> 0.9.3-1
- update to 0.9.3-1

* Thu Nov 5 2020 Yann Collette <ycollette.nospam@free.fr> 0.6.8-1
- update to 0.6.0-1

* Mon Nov 5 2018 Yann Collette <ycollette.nospam@free.fr> 0.5.8-1
- update to 0.5.8-1

* Sun Aug 28 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.7-1
- update to 0.5.7

* Sat Nov  7 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.6-1
- updated to 0.5.6

* Tue Jul  3 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.5-1
- updated to 0.5.5

* Tue Jul  3 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.3-1
- updated to 0.5.3

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.2-1
- updated to 0.4.2

* Mon Jun 20 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.3-1
- updated to 0.3.3

* Wed Jun 29 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.0-1
- updated to 0.3.0

* Thu May 26 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.9-1
- updated to 0.2.9

* Thu Jan 20 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.4-1
- initial build.
