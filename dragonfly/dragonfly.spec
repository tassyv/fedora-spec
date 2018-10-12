# Global variables for github repository
%global commit0 e2f9940fe922eed9ec7c1aedf6fcd2e3c2e63e66
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:          dragonfly-reverb
Version:       0.9.2
Release:       1%{?dist}
Summary:       DragonFly reverberation plugin

Group:         Applications/Multimedia
License:       GPLv2+
URL:           https://github.com/michaelwillis/dragonfly-reverb/
# git clone --recurse https://github.com/michaelwillis/dragonfly-reverb/
# cp -r dragonfly-reverb /tmp/dragonfly-reverb
# cd /tmp/dragonfly-reverb
# rm -rf .git dpf/.git
# cd ..
# tar cvfz dragonfly-reverb.tar.gz dragonfly-reverb/*

Source0:       dragonfly-reverb.tar.gz
#Source0:       https://github.com/michaelwillis/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel

%description
A free hall-style reverb based on freeverb3 algorithms

%prep
# %setup -qn %{name}-%{commit0}
%setup -qn %{name}

%build
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} all

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyReverb.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/vst

cp bin/DragonflyReverb %{buildroot}/%{_bindir}/
cp -r bin/DragonflyReverb.lv2/* %{buildroot}/%{_libdir}/lv2/DragonflyReverb.lv2/
cp bin/DragonflyReverb-vst.so %{buildroot}/%{_libdir}/vst/

%files
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Fri Oct 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-1
- Initial build
