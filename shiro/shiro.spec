# Tag: Effect
# Type: LV2
# Category: Effect

Name:    shiro
Version: 0.1
Release: 1%{?dist}
Summary: SHIRO LV2 plugin collection
License: GPLv2+
URL:     https://github.com/ninodewit/SHIRO-Plugins

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./shiro-source.sh <tag>
# ./shiro-source.sh master

Source0: SHIRO-Plugins.tar.gz
Source1: shiro-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: ladspa-devel

%description
SHIRO LV2 plugin collection

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n ladspa-%{name}
Summary:  LADSPA version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n ladspa-%{name}
LADSPA version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst-%{name}
LV2 version of %{name}

%prep
%autosetup -n SHIRO-Plugins

sed -i -e "s/-Wl,--strip-all//g" Makefile.mk

%build

%set_build_flags

%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/ladspa/

cd bin
cp -a Harmless Larynx Modulay Shiroverb %{buildroot}/%{_bindir}/
cp -a Harmless-vst.so Larynx-vst.so Modulay-vst.so Shiroverb-vst.so %{buildroot}/%{_libdir}/vst/
cp -a Harmless-ladspa.so Larynx-ladspa.so Modulay-ladspa.so Shiroverb-ladspa.so %{buildroot}/%{_libdir}/ladspa/
cp -ra Harmless.lv2 Larynx.lv2 Modulay.lv2 Shiroverb.lv2 %{buildroot}/%{_libdir}/lv2/
cd ..

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Fri Nov 06 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
