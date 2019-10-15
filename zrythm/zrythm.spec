%global debug_package %{nil}

Name:    zrythm
Version: 0.6.502
Release: 2%{?dist}
Summary: Zrythm is a highly automated Digital Audio Workstation (DAW) designed to be featureful and intuitive to use.

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://git.zrythm.org/git/zrythm

Source0: https://download-mirror.savannah.gnu.org/releases/zrythm/zrythm-%{version}.tar.xz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: libyaml-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: gtk3-devel
BuildRequires: portaudio-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: fftw-devel
BuildRequires: libgtop2-devel
BuildRequires: meson
BuildRequires: help2man
BuildRequires: python3-sphinx
BuildRequires: desktop-file-utils
BuildRequires: gtk-update-icon-cache

%description
Zrythm is a highly automated Digital Audio Workstation (DAW) designed to be featureful and intuitive to use. Zrythm sets itself apart from other DAWs by allowing extensive automation via built-in LFOs and envelopes and intuitive MIDI or audio editing and arranging via clips.
In the usual Composing -> Mixing -> Mastering workflow, Zrythm puts the most focus on the Composing part. It allows musicians to quickly lay down and process their musical ideas without taking too much time for unnecessary work.
It is written in C and uses the GTK+3 toolkit, with bits and pieces taken from other programs like Ardour and Jalv.
More info at https://www.zrythm.org

%prep
%setup -qn zrythm-%{version}

sed -i -e "s/'sphinx-build'/'sphinx-build-3'/g" meson.build
sed -i -e '/meson.add_install_script/,+3d' meson.build

%build

mkdir build
DESTDIR=%{buildroot} VERBOSE=1 meson -Dmanpage=true -Duser_manual=true --buildtype release --prefix=/usr build

cd build
DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install 

cd build
DESTDIR=%{buildroot} VERBOSE=1 ninja install

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/zrythm.desktop

%post
touch --no-create %{_datadir}/mime/packages &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
update-desktop-database -q

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%posttrans
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc AUTHORS COPYING README.md THANKS CHANGELOG.md CONTRIBUTING.md
%{_bindir}/*
%{_datadir}/*

%changelog
* Sun Oct 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.502-2
- update to 0.6.502

* Wed Oct 2 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.479-2
- update to 0.6.479

* Fri Sep 20 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.422-2
- update to 0.6.422

* Sun Sep 8 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.384-2
- update to 0.6.384

* Sun Sep 8 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.323-1
- update to 0.6.323

* Wed Aug 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.039-1
- update to 0.6.039

* Sun Jul 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.162-1
- Initial build