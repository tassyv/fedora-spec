# 
# Pure Data vanilla build
#

%define pdver 0.52-1
%define pkgver 0.52.1

Summary: Pure Data
Name:    puredata
Version: %{pkgver}
Release: 2%{?dist}
License: BSD
URL:     https://puredata.info/

Vendor:       Audinux
Distribution: Audinux

Source0: http://msp.ucsd.edu/Software/pd-%{pdver}.src.tar.gz

# additional files for the gui package
# desktop file
Source10: puredata.desktop
# icon
Source11: puredata.xpm
# /usr/bin/pd-gui
Source12: pd-gui
# pd-gui man page
Source13: pd-gui.1
# pd-gui plugin (needs python3)
Source14: pd-gui-plugin
# pd gui plugins readme
Source15: pd-README
# mime stuff
Source16: puredata-gui.sharedmimeinfo

# add relevant debian patches
Patch1: pd-patch-pd2puredata.patch
%ifarch x86_64
Patch2: pd-patch-usrlib64pd_path.patch
%else
Patch2: pd-patch-usrlibpd_path.patch
%endif
Patch3: pd-patch-helpbrowser_puredata-doc.patch
Patch4: pd-patch-etc-gui-plugins.patch
Patch5: pd-patch-fixmanpage.patch
Patch6: pd-patch-privacy.patch

BuildRequires: gcc gcc-c++ perl
BuildRequires: autoconf automake libtool
BuildRequires: alsa-lib-devel jack-audio-connection-kit-devel portaudio-devel
BuildRequires: gettext-devel desktop-file-utils

# the main package requires everything else by default (except -devel)
Requires: puredata-core puredata-doc puredata-extra 
Requires: puredata-gui puredata-utils
# for the gui plugin
Requires: python3

%description
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing. Pd's audio functions
are built-in; graphical computations require separate packages such as
gem (Graphics Environment for Multimedia) or pd-pdp (Pd Packet).

%package core
Summary: Pure Data Core

%description core
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package only provides the core infrastructure. Most likely you
will want to install the puredata-gui as well

%package devel
Summary: Pure Data Development files
Requires: puredata-core

%description devel
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package provides the header-files for compiling externals
(plugins) for puredata.

%package doc
Summary: Pure Data documentation
Requires: puredata-core

%description doc
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package provides the documentation for Pure Data. Most likely you
will want to install "puredata" as well.

%package extra
Summary: Pure Data extra
Requires: puredata-core

%description extra
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package provides extra objects that come with Pd, e.g. for signal
analysis (fiddle~, sigmund~, bonk~), expression evaluation (expr~) and
more

%package gui
Summary: Pure Data GUI
Requires: puredata-core

%description gui
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package provides the graphical user-interface for Pure Data. Most
likely you will want to install "puredata-core" (or even "puredata")
as well.

%package utils
Summary: Pure Data utilities
Requires: puredata-core

%description utils
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package provides utility applications for puredata, namely pdsend
and pdreceive, for sending and receiving FUDI over the net.

%prep
%autosetup -p1 -n pd-%{pdver}

# fix hardwired lib dir in startup file (why the heck is this hardwired?)
perl -p -i -e "s|\"/lib|\"/%{_lib}|g" src/s_main.c
# fix path of pd-externals
perl -p -i -e "s|/usr/local/lib|%{_libdir}|g" src/s_path.c

%build

%set_build_flags

# now do the build, use "puredata" as the program name
./autogen.sh
%configure --enable-alsa --enable-jack --program-transform-name 's/pd$$/puredata/'

%make_build

%install

%make_install

# add additional stuff needed by the gui package
# create plugins enabled directory
mkdir -p %{buildroot}%{_sysconfdir}/pd/plugins-enabled
# add desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install  --dir %{buildroot}%{_datadir}/applications %{SOURCE10}
perl -p -i -e "s|/lib/|/%{_lib}/|g" %{buildroot}%{_datadir}/applications/puredata.desktop

# add desktop icon
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -m 644 %{SOURCE11} %{buildroot}%{_datadir}/pixmaps/
# pd-gui script and plugin
install -m 755 %{SOURCE12} %{buildroot}%{_bindir}/pd-gui
perl -p -i -e "s|/lib/|/%{_lib}/|g" %{buildroot}%{_bindir}/pd-gui
install -m 755 %{SOURCE14} %{buildroot}%{_bindir}/pd-gui-plugin
# pd-gui man page
install -m 644 %{SOURCE13} %{buildroot}%{_mandir}/man1/pd-gui.1
# REAMDE for plugins
install -m 644 %{SOURCE15} %{buildroot}%{_sysconfdir}/pd/plugins-enabled/README
# documentation, intro
mkdir -p %{buildroot}%{_datadir}/puredata-gui
install -m 644 doc/1.manual/1.introduction.txt %{buildroot}%{_datadir}/puredata-gui
# mime stuff
mkdir -p %{buildroot}%{_datadir}/mime/packages/
install -m 644 %{SOURCE16} %{buildroot}%{_datadir}/mime/packages/puredata.xml

# hardlink pd-* binaries
rm -f %{buildroot}%{_bindir}/pd
rm -f %{buildroot}%{_bindir}/pd-watchdog
rm -r %{buildroot}%{_libdir}/puredata/bin/pd
rm -f %{buildroot}%{_libdir}/puredata/bin/pd-watchdog

cp src/pd-watchdog %{buildroot}%{_libdir}/puredata/bin/pd-watchdog
cp src/pd          %{buildroot}%{_libdir}/puredata/bin/pd
ln -s %{_libdir}/puredata/bin/pd          %{buildroot}%{_bindir}/pd
ln -s %{_libdir}/puredata/bin/pd-watchdog %{buildroot}%{_bindir}/pd-watchdog

rm -f %{buildroot}%{_libdir}/puredata/doc/Makefile.am

%ifarch x86_64
sed -i -e "s/lib/lib64/g" %{buildroot}%{_bindir}/pd-gui
%endif

%files
%doc README.txt INSTALL.txt
%license LICENSE.txt

%files core
%{_bindir}/pd
%{_bindir}/pd-watchdog
%{_libdir}/puredata/bin/pd
%{_libdir}/puredata/bin/pd-watchdog
%{_sysconfdir}/pd/plugins-enabled
%{_libdir}/puredata/doc/5.reference
%{_libdir}/puredata/doc/7.stuff
%{_mandir}/man1/pd.1*
%{_datadir}/pixmaps/puredata.xpm

%files doc
%{_libdir}/puredata/doc/1.manual/
%{_libdir}/puredata/doc/2.control.examples/
%{_libdir}/puredata/doc/3.audio.examples/
%{_libdir}/puredata/doc/4.data.structures/
%{_libdir}/puredata/doc/6.externs/
%{_libdir}/puredata/doc/8.topics/
%{_libdir}/puredata/doc/sound/

%files devel
%{_includedir}/m_pd.h
%{_includedir}/puredata/
%{_libdir}/pkgconfig/pd.pc

%files extra
%{_libdir}/puredata/extra/

%files gui
%{_bindir}/pd-gui
%{_bindir}/pd-gui-plugin
%{_libdir}/puredata/tcl/
%{_libdir}/puredata/po
%{_datadir}/applications/puredata.desktop
%{_mandir}/man1/pd-gui*
%{_sysconfdir}/pd/plugins-enabled
%{_datadir}/puredata-gui
%{_datadir}/mime/packages/puredata.xml

%files utils
%{_bindir}/pdreceive
%{_bindir}/pdsend
%{_mandir}/man1/pdreceive.1.gz
%{_mandir}/man1/pdsend.1.gz

%changelog
* Tue Dec 21 2021 Yann Collette <ycollette.nospam@free.fr> - 0.52.1-2
- update to 0.52.1-2

* Sun Jan 3 2021 Yann Collette <ycollette.nospam@free.fr> - 0.51.4-2
- update to 0.51.4

* Mon Dec 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.51.3-2
- update to 0.51.3

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.51.2-2
- fix debug build

* Thu Sep 24 2020 Yann Collette <ycollette.nospam@free.fr> - 0.51.2-1
- update to 0.51.2-1

* Sun Aug 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.51.1-1
- update to 0.51.1-1

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 0.50.2-1
- update to 0.50.2-1

* Sat Oct 5 2019 Yann Collette <ycollette.nospam@free.fr> - 0.50.0-1
- update to 0.50.0-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> -
- update for Fedora 29

* Wed Nov 23 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 
- do not create symlinks to documentation
- finish adding all the pd-gui stuff from Debian
- borrow pre/post scripts from ardour5 spec file

* Tue Nov 22 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.47.1-1
- initial build, start from scratch with pd vanilla
- replicate Debian package structure, add most patches, many thanks
  to IOhannes m zmolnig (Debian/GNU)
