# Tag:  Jack
# Type: Standalone
# Category: Audio, Tool

Summary: Measure the round-trip latency of a soundcard.
Name:    jack_delay
Version: 0.4.2
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel

%description
Measure the round-trip latency of a soundcard.

%prep
%autosetup

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile
sed -i 's|-lasound||' source/Makefile

pushd source
make PREFIX=%{_prefix}
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}/

pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README
%license COPYING
%{_bindir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- update for Fedora 29

* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- initial release
