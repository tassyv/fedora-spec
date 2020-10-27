Fedora 33 - To be fixed:

BespokeSynth -> JUCE was missing + lto-wrapper -> to fix directly on fedora 33 ... wait until gcc update
performer	 -> cmake + ui_setlist.h missing - pb cmake 3.18 ...
qscintilla	 -> fail to build for qt4
miniaudicle	 -> qscintilla was missing
sonic-pi	 -> cmake - check ruby version

Add new packages:
 Dplug                -> https://github.com/AuburnSounds/Dplug
 SmartGuitarAmp       -> https://github.com/keyth72/SmartGuitarAmp
 improviz-performance -> https://github.com/rumblesan/improviz-performance
 osmid                -> https://github.com/llloret/osmid
 Squeezer             -> https://github.com/mzuther/Squeezer
 DAFx19-Gamelanizer/  -> https://github.com/lukemcraig/DAFx19-Gamelanizer
 ladspa-t5-plugins    -> https://gitlab.com/t-5/ladspa-t5-plugins
 OwlSim               -> https://github.com/pingdynasty/OwlSim
 DeLooper             -> https://github.com/sonejostudios/DeLooper
 morphex              -> https://github.com/MarcSM/morphex
 CF3                  -> https://github.com/MtnViewJohn/context-free.git
 minicomputer         -> http://minicomputer.sourceforge.net/
 freqtweak            -> https://github.com/essej/freqtweak
 dexed                -> https://github.com/asb2m10/dexed
 mephisto             -> https://open-music-kontrollers.ch/lv2/mephisto/
 xmonk                -> https://github.com/brummer10/Xmonk.lv2
 xpolymonk            -> https://github.com/brummer10/XPolyMonk.lv2
 littlefly            -> https://github.com/brummer10/LittleFly.lv2
 fatgrog              -> https://github.com/brummer10/FatFrog.lv2
 zrythm - reproc      -> https://github.com/DaanDeMeyer/reproc (for zrythm)
 zrythm - lsp-dsp     -> add a devel package for zrythm
 emissioncontrol2     -> https://github.com/EmissionControl2/EmissionControl2
 regrader             -> https://github.com/igorski/regrader
 
 supercollider-study  -> https://github.com/rumblesan/super-collider-study
 
** Add source.sh file in spec file:
Source1: source.sh

** Add check section:
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

** Fix debug generation:

purr-data/purr-data.spec       -> has a pure binary dependency
improviz/improviz.spec         -> (Cabal ...)
processing/processing.spec     -> precompiled java package
rack				           -> fail with some fedora flags
ams-lv2/lvtk.spec              -> (???)
psi-plugins                    -> error with fedora 33 + lv2-devel
picoloop/picoloop.spec         -> complex ...
orca/orca.spec                 -> really special build system
ryukau/ryukau.spec             -> gcc hangs during compilation of parameter.cpp
performer/performer.spec       -> ui_setlist.h missing - cmake 3.18 pb probably
socallab/SocaLabs-plugins.spec -> build fails because of a default juce path / maybe use juce 5.4 ...
surge/stochas.spec             -> jucaid compilation pb - maybe due tu %set_build_flags ...

zrythm/zrythm.spec
ossia/ossia-score.spec