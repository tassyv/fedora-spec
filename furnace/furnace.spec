# Tag: Tracker, MIDI, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name:    furnace
Version: 0.5.8
Release: 2%{?dist}
Summary: A multi-system chiptune tracker compatible with DefleMask modules
License: GPLv2
URL:     https://github.com/tildearrow/furnace

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-furnace.sh v0.5.8

Source0: furnace.tar.gz
Source1: source-furnace.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: flac-devel
BuildRequires: opus-devel
BuildRequires: lame-devel
BuildRequires: mpg123-devel
BuildRequires: speex-devel
BuildRequires: sqlite-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libxcb-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libXrender-devel
BuildRequires: wayland-devel
BuildRequires: libsndfile-devel
BuildRequires: rtmidi-devel
BuildRequires: zlib-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: libglvnd-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: patchelf

%description
A multi-system chiptune tracker compatible with DefleMask modules

%prep
%autosetup -n %{name}

sed -i -e "s/DEPENDENCIES_LIBRARIES SDL2-static/DEPENDENCIES_LIBRARIES SDL2/" CMakeLists.txt

%build

%cmake
%cmake_build

%install 

%cmake_install

install -m 755 -d %{buildroot}/%{_libdir}/%{name}/
[ -d %{__cmake_builddir}/extern/fmt ] && cp %{__cmake_builddir}/extern/fmt/libfmt.so.? %{buildroot}/%{_libdir}/%{name}/
[ -d %{__cmake_builddir}/extern/libsndfile ] && cp %{__cmake_builddir}/extern/libsndfile/libsndfile.so.? %{buildroot}/%{_libdir}/%{name}/
[ -d %{__cmake_builddir}/extern/SDL ] && cp %{__cmake_builddir}/extern/SDL/libSDL2-2.0.so.? %{buildroot}/%{_libdir}/%{name}/

patchelf --set-rpath '$ORIGIN/../%{_lib}/%{name}/' %{buildroot}/%{_bindir}/%{name}

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_libdir}/furnace/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/furnace/papers/*
%{_datadir}/furnace/demos/*
%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Tue Mar 08 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.8-1
- Initial spec file
