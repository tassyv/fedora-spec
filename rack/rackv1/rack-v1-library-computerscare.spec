# Global variables for github repository
%global commit0 c1d03abafa454cc357abab7fb0aaf5a9491691de

%global gittag0 1.3.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-v1-computerscare
Version: 1.3.0
Release: 3%{?dist}
Summary: computerscare plugin for Rack

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/freddyz/computerscare-vcv-modules

# git clone https://github.com/VCVRack/Rack.git Rack
# cd Rack
# git checkout v1.1.6
# git submodule init
# git submodule update
# find . -name ".git" -exec rm -rf {} \;
# cd dep
# wget https://bitbucket.org/jpommier/pffft/get/29e4f76ac53b.zip
# unzip 29e4f76ac53b.zip
# mkdir include
# cp jpommier-pffft-29e4f76ac53b/*.h include/
# rm  29e4f76ac53b.zip
# cd ../..
# tar cvfz Rack.tar.gz Rack/*

Source0: Rack.tar.gz
Source1: https://github.com/freddyz/computerscare-vcv-modules/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source2: computerscare_plugin.json

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: cmake sed
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel
BuildRequires: libzip-devel
BuildRequires: glew-devel
BuildRequires: glfw-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: jansson-devel
BuildRequires: gtk2-devel
BuildRequires: rtaudio-devel
BuildRequires: rtmidi-devel
BuildRequires: speex-devel
BuildRequires: speexdsp-devel
BuildRequires: jq

%description
computerscare plugin for Rack.

%prep
%setup -qn Rack

CURRENT_PATH=`pwd`

sed -i -e "s/-march=core2//g" compile.mk
sed -i -e "s/-march=nocona//g" compile.mk
sed -i -e "s/-ffast-math//g" compile.mk
sed -i -e "s/-fno-finite-math-only//g" compile.mk
sed -i -e "s/-O3/-O2/g" compile.mk

# %{build_cxxflags}
echo "CXXFLAGS += -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I$CURRENT_PATH/dep/nanosvg/src -I/usr/include/rtaudio -I/usr/include/rtmidi -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/jpommier-pffft-29e4f76ac53b -I$CURRENT_PATH/dep/include" >> compile.mk

sed -i -e "s/-Wl,-Bstatic//g" Makefile
sed -i -e "s/-lglfw3/dep\/lib\/libglfw3.a/g" Makefile

sed -i -e "s/dep\/lib\/libGLEW.a/-lGLEW/g" Makefile
sed -i -e "s/dep\/lib\/libglfw3.a/dep\/%{_lib}\/libglfw3.a/g" Makefile
sed -i -e "s/dep\/lib\/libjansson.a/-ljansson/g" Makefile
sed -i -e "s/dep\/lib\/libcurl.a/-lcurl/g" Makefile
sed -i -e "s/dep\/lib\/libssl.a/-lssl/g" Makefile
sed -i -e "s/dep\/lib\/libcrypto.a/-lcrypto/g" Makefile
sed -i -e "s/dep\/lib\/libzip.a/-lzip/g" Makefile
sed -i -e "s/dep\/lib\/libz.a/-lz/g" Makefile
sed -i -e "s/dep\/lib\/libspeexdsp.a/-lspeexdsp/g" Makefile
sed -i -e "s/dep\/lib\/libsamplerate.a/-lsamplerate/g" Makefile
sed -i -e "s/dep\/lib\/librtmidi.a/-lrtmidi/g" Makefile
sed -i -e "s/dep\/lib\/librtaudio.a/-lrtaudio/g" Makefile

mkdir computerscare_plugin
tar xvfz %{SOURCE1} --directory=computerscare_plugin --strip-components=1 

cp -n %{SOURCE2} computerscare_plugin/plugin.json

%build

cd computerscare_plugin
make RACK_DIR=.. DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} dist

%install 

mkdir -p %{buildroot}%{_libexecdir}/Rack1/plugins-v1/computerscare/
cp -r computerscare_plugin/dist/computerscare/* %{buildroot}%{_libexecdir}/Rack1/plugins-v1/computerscare/

%files
%{_libexecdir}/*

%changelog
* Tue Feb 11 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-3
- initial specfile