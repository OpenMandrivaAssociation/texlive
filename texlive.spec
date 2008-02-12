%bcond_with     obsolete_tetex

%define default_letter_paper 1
%define disable_lcdf_typetools 1

%define _localstatedir %{_var}
%{!?_texmf_main: %global _texmf_main %{_datadir}/texmf}
%{!?_texmf_conf: %global _texmf_conf %{_sysconfdir}/texmf}
%{!?_texmf_var:  %global _texmf_var %{_var}/lib/texmf}
%{!?_texmf_vendor: %global _texmf_vendor %{_datadir}/texmf-texlive}

%define kpathsea_version_major 4
%define libkpathsea %mklibname kpathsea %{kpathsea_version_major}
%define libkpathsea_o %mklibname kpathsea
%define libkpathsea_d %mklibname kpathsea -d
%define libkpathsea_d_s %mklibname kpathsea -d -s

%define svn_rev r6295

Name:           texlive
Version:        2007
Release:        %mkrel 20.%{svn_rev}.2
Epoch:          0
Summary:        Binaries for the TeX formatting system
Group:          Publishing
License:        Distributable
URL:            http://tug.org/texlive/
# svn export -%{svn_rev} svn://tug.org/texlive/trunk/Build/source
# tar cvYf source-%{svn_rev}.tar.lzma source
Source0:        http://tug.org/svn/texlive/branches/branch2007/Master/source/source-%{svn_rev}.tar.lzma
Source10:       texlive.cron
# Source30 is http://xdvi.sourceforge.net/xdvi48x48.gif converted to png
Source30:       xdvi48x48.png
# Fedora
Patch5:         texlive-2007-browser.patch
Patch8:         texlive-2007-xprint.patch
Patch10:        texlive-2007-dvipdfm-security.patch
Patch11:        texlive-2007-makej.patch
Patch15:        texlive-2007-xdvi-keepflag.patch
# mpeters contributed patches
# fixes man pages to utf-8
Patch41:        texlive-2007-kuesterei-man.patch
Patch42:        texlive-2007-copyright-utf8-man.patch
# Debian
Patch100:       texlive-Build_script.patch
Patch101:       texlive-mktexlsr_fixes.patch
Patch102:       texlive-fix_pkfix_invocation.patch
Patch103:       texlive-fix_epstopdf_invocation.patch
Patch104:       texlive-12a_fix_thumbpdf_invocation.patch
Patch105:       texlive-12b_fix_a2ping_invocation.patch
Patch106:       texlive-12c_fix_pdfcrop_invocation.patch
Patch107:       texlive-12d_fix_ebong_invocation.patch
Patch108:       texlive-12e_fix_vpe_invocation.patch
Patch109:       texlive-texdoc.patch
Patch111:       texlive-xdvi.patch
Patch112:       texlive-use_xdvi.bin.patch
Patch113:       texlive-libpoppler_new.patch
Patch115:       texlive-maketexmf.patch
Patch117:       texlive-fmtutil_keep_failedlog.patch
Patch118:       texlive-builtin-searchpath-fix.patch
Patch119:       texlive-checklib_fixes.patch
Patch120:       texlive-dvipdfm_timezone.patch
# Mandriva
Patch200:       texlive-paths.patch
Patch201:       texlive-ttf2pk-freetype.patch
Patch202:       texlive-pdftex.patch
Patch203:       texlive-xetex.patch
Patch204:       texlive-build.patch
Patch205:       texlive-no-lzma.patch
# Suse
Patch300:       texlive-source-icu.patch
Patch301:       texlive-source-t1lib.patch
Patch302:       texlive-source-warns.patch
Patch303:       texlive-source-x11r7.patch
Patch304:       texlive-source-xdvi-numlock.patch
Patch305:       texlive-source-xdvizilla.patch
%if %with obsolete_tetex
Obsoletes:      tetex < 1:3.0
%else
Conflicts:      tetex < 1:3.0
%endif
Provides:       tetex = 1:3.0
# XXX
Provides:       perl(Htex::dimen)
Provides:       perl(Htex::papers)
Provides:       perl(Pts::string)
Requires(post): rpm-helper
Requires:       bison
Requires:       ed
Requires:       flex
Requires(post): texlive-texmf = %{version}
Requires:       texlive-texmf = %{version}
# make sure fonts package installed before running post - since
# fmtutil-sys is symlink to fmtutil
Requires(post): texlive-fonts = %{epoch}:%{version}-%{release}
Requires:       texlive-fonts = %{epoch}:%{version}-%{release}
BuildRequires:  bison
BuildRequires:  ed
BuildRequires:  flex
BuildRequires:  desktop-file-utils
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  gd-devel
BuildRequires:  lesstif-devel
BuildRequires:  t1lib-devel
BuildRequires:  libsm-devel
BuildRequires:  libice-devel
BuildRequires:  xaw-devel
BuildRequires:  Xaw3d-devel
BuildRequires:  teckit-devel
# for non modular xorg - use xorg-devel instead for above
BuildRequires:  lesstif
BuildRequires:  texlive-texmf = %{version}
BuildRequires:  chrpath
BuildRequires:  freetype-devel
BuildRequires:  freetype2-devel
BuildRequires:  libpoppler-devel
BuildRequires:  tiff-devel
#BuildRequires: w3c-libwww-devel
BuildRequires:  texinfo
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Conflicts:      tetex-doc < 2007

# This description based on Fedora tetex package, modified for texlive.
%description
texlive is an implementation of TeX for Linux or UNIX systems. TeX takes
a text file and a set of formatting commands as input and creates a
typesetter-independent .dvi (DeVice Independent) file as output.
Usually, TeX is used in conjunction with a higher level formatting
package like LaTeX or PlainTeX, since TeX by itself is not very
user-friendly. The output format needn't to be DVI, but also PDF,
when using pdflatex or similar tools.

Install texlive if you want to use the TeX text formatting system. Consider
to install texlive-latex (a higher level formatting package which provides
an easier-to-use interface for TeX). Unless you are an expert at using TeX,
you should also install the texlive-texmf-doc package, which includes the
documentation for TeX.

%package afm
Summary:        A converter for PostScript(TM) font metric files, for use with TeX
Group:          Publishing
%if %with obsolete_tetex
Obsoletes:      tetex-afm < 1:3.0
%else
Conflicts:      tetex-afm < 1:3.0
%endif
Provides:       tetex-afm = 1:3.0
Requires(post): texlive-texmf-afm = %{version}
Requires:       texlive-texmf-afm = %{version}
BuildRequires:  texlive-texmf-afm = %{version}

# This description based on Fedora tetex package, modified for texlive.
%description afm
texlive-afm provides afm2tfm, a converter for PostScript font metric
files. PostScript fonts are accompanied by .afm font metric files
which describe the characteristics of each font. To use PostScript
fonts with TeX, TeX needs .tfm files that contain similar information.
Afm2tfm will convert .afm files to .tfm files.

If you are installing texlive in order to use the TeX text formatting
system and PostScript(TM) files, you will need to install texlive-afm. You will
also need to install texlive-dvips (for converting .dvi files to PostScript
format for printing on PostScript printers), texlive-latex (a higher level
formatting package which provides an easier-to-use interface for TeX), and
texlive-xdvi (for previewing .dvi files in X). Unless you are an expert at
using TeX, you should also install the texlive-texmf-doc package, which
includes documentation for TeX.

%package context
Summary:        Document engineering system based on TeX
Group:          Publishing
Requires:       texlive-texmf-context = %{version}
Requires(post): texlive-texmf-context = %{version}
%if %with obsolete_tetex
Obsoletes:      tetex-context < 1:3.0
%else
Conflicts:      tetex-context < 1:3.0
%endif
Provides:       tetex-context = 1:3.0

%description context
CONTeXT is a document engineering system based on TeX. TeX is a
typesetting system and a program to typeset and produce documents.
CONTeXT is easy to use and enables you to make complex paper and
electronic documents.

%package dvipdfm
Group:          Publishing
Summary:        A DVI to PDF converter
BuildRequires:  texlive-texmf-dvipdfm = %{version}
Requires:       texlive-texmf-dvipdfm = %{version}
Requires(post): texlive-texmf-dvipdfm = %{version}
%if %with obsolete_tetex
Obsoletes:      tetex-dvipdfm < 1:3.0
%else
Conflicts:      tetex-dvipdfm < 1:3.0
%endif
Provides:       tetex-dvipdfm = 1:3.0

%description dvipdfm
dvidpfm is a DVI to PDF translator for use with TeX.

%package dvips
Summary:        A DVI to PostScript converter for the TeX text formatting system
Group:          Publishing
Requires:       texlive-fonts = %{epoch}:%{version}-%{release}
Requires:       psutils
Requires(post): texlive-fonts = %{epoch}:%{version}-%{release}
Requires(post): psutils
%if %with obsolete_tetex
Obsoletes:      tetex-dvips < 1:3.0
%else
Conflicts:      tetex-dvips < 1:3.0
%endif
Provides:       tetex-dvips = 1:3.0
Requires:       texlive-texmf-dvips = %{version}
Requires(post): texlive-texmf-dvips = %{version}
BuildRequires:  texlive-texmf-dvips = %{version}

# This description based on Fedora tetex package, modified for texlive.
%description dvips
Dvips converts .dvi files produced by the TeX text formatting system
(or by another processor like GFtoDVI) to PostScript(TM) format.
Normally the PostScript file is sent directly to your printer.

If you are installing texlive, so that you can use the TeX text
formatting system without direct PDF compilation, consider to install
texlive-dvips. In addition, you will need to install texlive-afm (for
converting PostScript font description files), texlive-latex (a higher level
1formatting package which provides an easier-to-use interface for TeX), and
texlive-xdvi (for previewing .dvi files in X). If you are installing TeX and
you are not an expert at it, you should also install the texlive-texmf-doc
package which contains documentation for the TeX system.

%package dvilj
Summary:        A DVI to HP PCL (Printer Control Language) converter
Group:          Publishing
Requires:       texlive-fonts = %{epoch}:%{version}-%{release}
Requires(post): texlive-fonts = %{epoch}:%{version}-%{release}
%if %with obsolete_tetex
Obsoletes:      tetex-dvilj < 1:3.0
%else
Conflicts:      tetex-dvilj < 1:3.0
%endif
Provides:       tetex-dvilj = 1:3.0

%description dvilj
Dvilj and dvilj's siblings (included in this package) will convert TeX
text formatting system output .dvi files to HP PCL (HP Printer Control
Language) commands. Using dvilj, you can print TeX files to HP
LaserJet+ and fully compatible printers. With dvilj2p, you can print
to HP LaserJet IIP and fully compatible printers. And with dvilj4, you
can print to HP LaserJet4 and fully compatible printers.

If you are installing teTeX, so that you can use the TeX text formatting
system, you will also need to install texlive-dvilj. In addition, you will
need to install texlive-afm (for converting PostScript font description
files), texlive-dvips (for converting .dvi files to PostScript format for
printing on PostScript printers), texlive-latex (a higher level formatting
package which provides an easier-to-use interface for TeX) and texlive-xdvi
(for previewing .dvi files in X). If you're installing TeX and you're
not a TeX expert, you'll also want to install the texlive-texmf-doc package,
which contains documentation for TeX.

%package dviutils
Summary:        A collection of utilities for working with dvi files
Group:          Publishing
# not positive about this requires, pretty sure though
Requires:       texlive-fonts = %{epoch}:%{version}-%{release}
Requires(post): texlive-fonts = %{epoch}:%{version}-%{release}

%description dviutils
The texlive-dviutils package includes a set of tools for working with dvi
files. You only need this package if you plan to manipulate existing dvi files.

%package fonts
Summary:        The font files for the TeX text formatting system
Group:          Publishing
%if %with obsolete_tetex
Obsoletes:      tetex-fonts < 1:3.0
%else
Conflicts:      tetex-fonts < 1:3.0
%endif
Provides:       tetex-fonts = 1:3.0
Provides:       kpathsea
Requires:       texlive-texmf-fonts = %{version}
Requires(post): texlive-texmf-fonts = %{version}
BuildRequires:  texlive-texmf-fonts = %{version}
Conflicts:      tetex < 1:3.0

# This description based on Fedora tetex package, modified for texlive.
%description fonts
The texlive-fonts package contains fonts used by both the Xdvi previewer and
the TeX text formatting system.

You will need to install texlive-fonts if you wish to use either texlive-xdvi
(for previewing .dvi files in X) or the texlive package (the core of the TeX
text formatting system).

%package latex
Summary:        The LaTeX front end for the TeX text formatting system
Group:          Publishing
Requires:       texlive = %{epoch}:%{version}-%{release}
Requires:       texlive-dvips = %{epoch}:%{version}-%{release}
Requires:       netpbm
# (Anssi 01/2008) Are these two really req'd by post?
Requires(post): texlive-dvips = %{epoch}:%{version}-%{release}
Requires(post): netpbm
# make sure main and fonts package installed before running post
Requires(post): texlive-fonts = %{epoch}:%{version}-%{release}
Requires(post): texlive = %{epoch}:%{version}-%{release}
BuildRequires:  ghostscript
BuildRequires:  netpbm
%if %with obsolete_tetex
Obsoletes:      tetex-latex < 1:3.0
%else
Conflicts:      tetex-latex < 1:3.0
%endif
Provides:       tetex-latex = 1:3.0
Requires:       texlive-texmf-latex = %{version}
Requires(post): texlive-texmf-latex = %{version}
BuildRequires:  texlive-texmf-latex = %{version}

# This description based on Fedora tetex package, modified for texlive.
%description latex
LaTeX is a front end for the TeX text formatting system. Easier to
use than TeX. LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users. It also allows to
compile LaTeX files directly to PDF format.

If you are installing texlive, so that you can use the TeX text
formatting system, consider to install texlive-latex.
If you are not an expert at TeX, you should also install
the texlive-texmf-doc package, which contains documentation for TeX.

%package mfwin
Summary:        Metafont with output window
Group:          Publishing
%if %with obsolete_tetex
Obsoletes:      tetex-mfwin < 1:3.0
%else
Conflicts:      tetex-mfwin < 1:3.0
%endif
Provides:       tetex-mfwin = 1:3.0
Conflicts:      tetex < 1:3.0

%description mfwin
This package contains METAFONT with window support. Install this
package if you plan to run METAFONT interactively and would like to see
the font building in a output window.

%package xdvi
Summary:        An X viewer for DVI files
Group:          Publishing
Requires:       texlive-dvips = %{epoch}:%{version}-%{release}
Requires(post): texlive-dvips = %{epoch}:%{version}-%{release}
Requires(post): desktop-file-utils
%if %with obsolete_tetex
Obsoletes:      tetex-xdvi < 1:3.0
%else
Conflicts:      tetex-xdvi < 1:3.0
%endif
Provides:       tetex-xdvi = 1:3.0
Conflicts:      xdvv

# This description based on Fedora tetex package, modified for texlive.
%description xdvi
Xdvi allows you to preview the TeX text formatting system's output
.dvi files on an X Window System.

If you are installing texlive and you use PlainTeX or you are using DVI files,
you will also need to install texlive-xdvi which allows you to view DVI files.
Consider installing texlive-dvips (for converting .dvi files to PostScript
format for printing on PostScript printers), and texlive-latex (a higher level
formatting package which provides an easier-to-use interface for TeX). If you
are not a TeX expert, you will probably also want to install the
texlive-texmf-doc package which contains documentation for the TeX text
formatting system.

%package jadetex
Summary:        TeX macros used by Jade TeX output
Group:          Publishing
Requires:       texlive-texmf-jadetex = %{version}
Requires(post): texlive-texmf-jadetex = %{version}
%if %with obsolete_tetex
Obsoletes:      jadetex < 1:3.0
%else
Conflicts:      jadetex < 1:3.0
%endif
Provides:       jadetex = 1:3.0
Requires:       sgml-common
Requires:       openjade
Requires:       texlive-latex = %{epoch}:%{version}-%{release}
# (Anssi 01/2008) Are all of these really (post)?
Requires(post): sgml-common
Requires(post): openjade
Requires(post): texlive-latex = %{epoch}:%{version}-%{release}

%description jadetex
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as TeX files, to obtain DVI, Postscript
or PDF files for example.

%package xmltex
Summary:        Namespace-aware XML parser written in TeX
Group:          Publishing
Requires:       texlive-latex = %{epoch}:%{version}-%{release}
Requires:       texlive-texmf-xmltex = %{version}
Requires(post): texlive-latex = %{epoch}:%{version}-%{release}
Requires(post): texlive-texmf-xmltex = %{version}
%if %with obsolete_tetex
Obsoletes:      xmltex < 1:3.0
%else
Conflicts:      xmltex < 1:3.0
%endif
Provides:       xmltex = 1:3.0

%description xmltex
Namespace-aware XML parser written in TeX. This package
also includes passivetex macros, which can be used to process an XML
document which results from an XSL trasformation to formatting objects.

%package -n %{libkpathsea}
Summary:        Main library for kpathsea
Group:          System/Libraries
Provides:       %{libkpathsea_o} = %{epoch}:%{version}-%{release}

%description -n %{libkpathsea}
Main library for kpathsea.

%package -n %{libkpathsea_d}
Summary:        Development files for kpathsea
Group:          Development/C
Requires:       %{libkpathsea} = %{epoch}:%{version}-%{release}
%if %with obsolete_tetex
Obsoletes:      tetex-devel < 1:3.0
%else
Conflicts:      tetex-devel < 1:3.0
%endif
Provides:       tetex-devel = 1:3.0
Provides:       kpathsea-devel = %{epoch}:%{version}-%{release}

%description -n %{libkpathsea_d}
This package contains the development files for kpathsea.

%package -n %{libkpathsea_d_s}
Summary:        Static development files for kpathsea
Group:          Development/C
Requires:       %{libkpathsea_d} = %{epoch}:%{version}-%{release}
Provides:       kpathsea-static-devel = %{epoch}:%{version}-%{release}

%description -n %{libkpathsea_d_s}
This package contains the static development files for kpathsea.

%prep
%setup -q -n source
%{_bindir}/find . -name autom4te.cache | %{_bindir}/xargs -t %{__rm} -r || :

# fix for debuginfo rpmlint happiness
chmod -x texk/dvipdfm/macglyphs.h
chmod -x texk/dvipdfm/ttf.c
chmod -x texk/dvipdfm/encodings.c

# Red Hat-specific TeX configuration patches
# Use htmlview first
%patch5 -p1 -b .browser
%patch8 -p1 -b .xprint
# TeX patches
# Don't use tmpnam() in dvipdfm.
%patch10 -p1 -b .dvipdfm-security
# Fix parallel builds.
%patch11 -p1 -b .makej
# Fix xdvi - navigation with a spacebar does not keep position (RH bug #168124)
%patch15 -p1 -b .xdvi-keepflag

# fix non utf man pages
%patch41 -p1 -b .notutf8
%patch42 -p1 -b .notutf8-2

%patch100 -p1
%patch101 -p3
%patch102 -p3
%patch103 -p3
%patch104 -p3
%patch105 -p3
%patch106 -p3
%patch107 -p3
%patch108 -p3
%patch109 -p3
%patch111 -p3
%patch112 -p3
%patch113 -p3
%patch115 -p3
%patch117 -p3
%patch118 -p3
%patch119 -p3
%patch120 -p3

%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1

%patch300 -p0
%patch301 -p0
%patch302 -p0
%patch303 -p0
%patch304 -p0
%patch305 -p0

pushd texk/kpathsea
%{__sed} -i 's?^TEXMF =.*?TEXMF = {\$TEXMFCONFIG,\$TEXMFVAR,\$TEXMFHOME,\$TEXMFSYSCONFIG,\!\!\$TEXMFSYSVAR,\!\!\$TEXMFLOCAL,\!\!\$TEXMFMAIN,\!\!\$TEXMFDIST}?' texmf.in
%{__sed} -i 's?^TEXMFMAIN =.*?TEXMFMAIN = %{_texmf_main}?' texmf.in
%{__sed} -i 's?^TEXMFDIST =.*?TEXMFDIST = %{_texmf_vendor}?' texmf.in
%{__sed} -i 's?^TEXMFLOCAL =.*?TEXMFLOCAL = %{_usr}/local/share/texmf?' texmf.in
%{__sed} -i 's?^TEXMFSYSVAR =.*?TEXMFSYSVAR = %{_texmf_var}?' texmf.in
%{__sed} -i 's?^TEXMFSYSCONFIG =.*?TEXMFSYSCONFIG = %{_texmf_conf}?' texmf.in
popd

%if %{disable_lcdf_typetools}
pushd utils
rm -rf lcdf-typetools
popd
%endif

# Remove everything except:
# icu: includes some changes
# md5: the aladdin md5 code (not a library)
# type1: a library, but created specifically for ttf2pk
%{__rm} -r libs/{curl,expat,freetype,freetype2,gd,howto,jpeg,libgnuw32,libgsw32,libpng,libttf,ncurses,obsdcompat,regex,t1lib,teckit,unzip,xpdf,zlib}/

%build
set -x
unset TEXINPUTS || :
export CCACHE_DIR=$HOME/.ccache
unset HOME || :

# XXX: check these options (from Debian)
# --without-dvipng --without-dvipdfmx
# --without-musixflx 
# --without-ps2eps --without-sam2p
# --without-cjkutils --without-dvidvi
# --without-lacheck --without-ttf2pk
# --with-system-wwwlib

%{configure2_5x} \
        --cache-file=/dev/null \
        --enable-shared=default \
%if %{default_letter_paper}
        --disable-a4 \
%endif
        --with-system-freetype \
        --with-freetype-include=%{_includedir}/freetype \
        --with-system-freetype2 \
        --with-freetype2-include=%{_includedir}/freetype2 \
        --with-system-t1lib \
        --without-texlive \
        --without-t1utils \
        --without-psutils \
        --without-pdfopen \
        --disable-multiplatform \
        --without-dialog --without-texinfo --without-texi2html \
        --without-tex4htk \
%if %{disable_lcdf_typetools}
        --with-lcdf-typetools=no \
%endif
        --with-mf-x-toolkit=yes \
        --with-xdvi-x-toolkit=xaw3d \
        --with-editor="xdg-open %s" \
        --enable-ipc \
        --with-x \
        --without-install-extra \
        --with-system-zlib \
        --with-system-pnglib \
        --with-pnglib-libdir=%{_libdir} \
        --with-system-tifflib \
        --with-system-gd \
        --without-system-icu \
        --with-icu-include=%{_includedir}/unicode
%{__make}

%install
rm -rf %{buildroot}
unset TEXINPUTS || :
export CCACHE_DIR=$HOME/.ccache
unset HOME || :

mkdir -p %{buildroot}%{_texmf_main}
mkdir -p %{buildroot}%{_texmf_var}/web2c
mkdir -p %{buildroot}%{_texmf_var}
mkdir -p %{buildroot}%{_texmf_conf}

#export TEXMFSYSVAR=%{buildroot}%{_texmf_var}
#export TEXMFSYSCONFIG=%{buildroot}%{_texmf_conf}

export LD_LIBRARY_PATH=`pwd`/texk/kpathsea/.libs

%{makeinstall} \
        texmf=%{buildroot}%{_texmf_main} \
        texmfmain=%{buildroot}%{_texmf_main}

rm -f %{buildroot}%{_infodir}/dir*

%if 0
# jadetex
rm -f %{buildroot}%{_bindir}/jadetex
rm -f %{buildroot}%{_bindir}/pdfjadetex
# xmltex
rm -f %{buildroot}%{_bindir}/xmltex
rm -f %{buildroot}%{_bindir}/pdfxmltex
%endif

# install cron file
install -D -m755 %{SOURCE10} %{buildroot}%{_sysconfdir}/cron.daily/tetex.cron

# these are owned by texmf-fonts package
rm -f %{buildroot}%{_texmf_main}/ls-R
rm -f %{buildroot}%{_texmf_var}/ls-R
rm -f %{buildroot}%{_texmf_conf}/ls-R
rm -f %{buildroot}%{_texmf_main}/web2c/texmf.cnf
rm -f %{buildroot}%{_texmf_main}/web2c/fmtutil.cnf

# these are owned by texmf-doc package
rm -rf %{buildroot}%{_texmf_main}/doc/tetex

# desktop entry things
cat > xdvi.desktop << EOF
[Desktop Entry]
Name=DVI Viewer
Type=Application
Comment=DVI viewer for TeX DVI files
Icon=xdvi48x48
#MiniIcon=mini-doc1.xpm
Exec=%{_bindir}/xdvi
MimeType=application/x-dvi;
NoDisplay=true
Categories=Office;Publishing;
EOF

# install the xdvi desktop file
install -d -m755 %{buildroot}%{_datadir}/{applications,pixmaps}
install -m644 %{SOURCE30} %{buildroot}%{_datadir}/pixmaps/
%{_bindir}/desktop-file-install --vendor "" --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  xdvi.desktop

# (tv) fix xdvi not working (#35288):
ln -s xdvi-xaw3d.bin %{buildroot}/%{_bindir}/xdvi.bin

for file in afm2pl afm2tfm aleph bibtex bibtex8 ctangle ctie cweave detex dmp disdvi dvi2tty dvibook dviconcat dvicopy dvilj dvilj2p dvilj4 dvilj4l dvipdfm dvipos dvips dviselect dvitodvi dvitomp dvitype ebb gftodvi gftopk gftype gsftopk hbf2gf kpsewhich mag makeindex makempx mf mf-nowin mft mpost odvicopy odvitype omega omfonts otangle otp2ocp outocp patgen pdftex pfb2pfa pk2bm pktogf pktype pltotf pooltype ps2pk tangle tex tftopl tie ttf2afm ttf2pk ttf2tfm vftovp vptovf weave xdvi-xaw3d.bin xetex xdvipdfmx; do
  %{_bindir}/test -x %{buildroot}/%{_bindir}/${file} && %{_bindir}/chrpath -d %{buildroot}/%{_bindir}/${file}
done

%clean
rm -rf %{buildroot}

%post
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :
%_install_info dvipng.info
# fmtutil
[ -x %{_bindir}/fmtutil-sys ] && LC_ALL=C %{_bindir}/fmtutil-sys --all > /dev/null 2>&1 || :

%post afm
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post context
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post dvilj
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post dvipdfm
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post dvips
%_install_info dvips.info
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post fonts
%_install_info web2c.info
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :
%{__rm} -f %{_texmf_conf}/web2c/updmap.cfg
%{__rm} -f %{_texmf_conf}/web2c/updmap.log
[ -x %{_bindir}/updmap-sys ] && LC_ALL=C %{_bindir}/updmap-sys --syncwithtrees > /dev/null 2>&1 || :

%post latex
%_install_info latex.info
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys init >/dev/null 2>&1 || :
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :
[ -x %{_bindir}/fmtutil-sys ] && LC_ALL=C %{_bindir}/fmtutil-sys --all > /dev/null 2>&1 || :

%post xdvi
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :
%{_bindir}/update-desktop-database %{_datadir}/applications || :

%post jadetex
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post xmltex
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post -n %{libkpathsea} -p /sbin/ldconfig

%postun -n %{libkpathsea} -p /sbin/ldconfig

%post -n %{libkpathsea_d}
%_install_info kpathsea.info

%preun
%_remove_install_info dvipng.info

%preun dvips
%_remove_install_info dvips.info

%preun latex
%_remove_install_info latex.info

%preun fonts
%_remove_install_info web2c.info

%preun -n %{libkpathsea_d}
%_remove_install_info kpathsea.info

%postun
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun afm
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun context
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun dvilj
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun dvipdfm
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun dvips
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun fonts
/sbin/ldconfig
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun latex
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun xdvi
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun jadetex
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun xmltex
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%files
%defattr(0755,root,root,0755)
#%{_bindir}/*mex*
%{_bindir}/a2ping
%{_bindir}/aleph
%{_bindir}/allcm
%{_bindir}/allec
%{_bindir}/allneeded
%{_bindir}/amstex
%{_bindir}/bibtex
%{_bindir}/ctangle
%{_bindir}/ctie
%{_bindir}/cweave
%{_bindir}/dmp
%{_bindir}/dvicopy
%{_bindir}/dvihp
%{_bindir}/dvipng
%{_bindir}/dvitomp
%{_bindir}/dvitype
%{_bindir}/e2pall
%{_bindir}/epstopdf
%{_bindir}/etex
%{_bindir}/fmtutil-sys
%{_bindir}/fontinst
#%{_bindir}/jbibtex
%{_bindir}/kpsereadlink
%{_bindir}/kpsewhere
%{_bindir}/lambda
%{_bindir}/lamed
%{_bindir}/mag
%{_bindir}/makeindex
%{_bindir}/makempx
%{_bindir}/makempy
%{_bindir}/mex
%{_bindir}/pdfmex
%{_bindir}/utf8mex
#%{_bindir}/mendex
%{_bindir}/mkindex
%{_bindir}/mkocp
%{_bindir}/mkofm
%{_bindir}/mpost
%{_bindir}/mpto
# in context
#%{_bindir}/mptopdf
%{_bindir}/newer
%{_bindir}/odvicopy
%{_bindir}/odvitype
%{_bindir}/ofm2opl
%{_bindir}/omega
%{_bindir}/omfonts
%{_bindir}/opl2ofm
%{_bindir}/otangle
%{_bindir}/otp2ocp
%{_bindir}/outocp
%{_bindir}/ovf2ovp
%{_bindir}/ovp2ovf
%{_bindir}/patgen
%{_bindir}/pdfcrop
%{_bindir}/pdfetex
%{_bindir}/pdftex
#%{_bindir}/pdfxtex
#%{_bindir}/pdvitype
%{_bindir}/pfb2pfa
%{_bindir}/pk2bm
%{_bindir}/pktogf
%{_bindir}/pktype
%{_bindir}/pltotf
%{_bindir}/pooltype
%{_bindir}/ps2frag
%{_bindir}/ps4pdf
#%{_bindir}/ptex
%{_bindir}/rubibtex
%{_bindir}/rumakeindex
%{_bindir}/tangle
%{_bindir}/tex
%{_bindir}/texconfig
%{_bindir}/texconfig-dialog
%{_bindir}/texconfig-sys
%{_bindir}/texdoc
%{_bindir}/texdoctk
%{_bindir}/texexec
%{_bindir}/texfont
%{_bindir}/texlinks
%{_bindir}/texutil
%{_bindir}/tftopl
%{_bindir}/thumbpdf
%{_bindir}/tie
%{_bindir}/updmap
%{_bindir}/updmap-sys
%{_bindir}/vftovp
%{_bindir}/vptovf
%{_bindir}/weave
# new files not in Fedora tetex
%{_bindir}/bibtex8
%{_bindir}/csplain
%{_bindir}/detex
%{_bindir}/mltex
%{_bindir}/pdfcsplain
# not positive these belong here
%{_bindir}/bg5conv
%{_bindir}/cef5conv
%{_bindir}/cefconv
%{_bindir}/cefsconv
%{_bindir}/devnag
%{_bindir}/disdvi
%{_bindir}/eplain
%{_bindir}/extconv
%{_bindir}/musixflx
%{_bindir}/physe
%{_bindir}/phyzzx
%{_bindir}/sjisconv
%{_bindir}/texsis
# other utilities
%{_bindir}/bbox
%{_bindir}/ctxtools
%{_bindir}/dvipos
%{_bindir}/exatools
%{_bindir}/luatools
%{_bindir}/mpstools
%{_bindir}/mtxtools
%{_bindir}/pdftools
# FIXME: currently (incorrectly?) disabled by Ubuntu patch
#%{_bindir}/pdftosrc
%{_bindir}/ps2eps
%{_bindir}/pstopdf
%{_bindir}/rlxtools
%{_bindir}/runtools
%{_bindir}/texmfstart
%{_bindir}/textools
%{_bindir}/tmftools
%{_bindir}/xdvi-xaw3d.bin
%{_bindir}/xelatex
%{_bindir}/xetex
%{_bindir}/xmltools
%defattr(0644,root,root,0755)
# man pages
#%{_mandir}/ja/man1/mendex.1*
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/amstex.1*
%{_mandir}/man1/bibtex.1*
%{_mandir}/man1/ctangle.1*
%{_mandir}/man1/ctie.1*
%{_mandir}/man1/cweave.1*
%{_mandir}/man1/cweb.1*
%{_mandir}/man1/dmp.1*
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvihp.1*
%{_mandir}/man1/dvipng.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/dvitype.1*
%{_mandir}/man1/e2pall.1*
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/etex.1*
%{_mandir}/man1/fdf2tex.1*
%{_mandir}/man1/fmtutil-sys.1*
%{_mandir}/man1/fontinst.1*
%{_mandir}/man1/kpsereadlink.1*
%{_mandir}/man1/kpsewhere.1*
%{_mandir}/man1/lambda.1*
%{_mandir}/man1/mag.1*
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/makempx.1*
%{_mandir}/man1/makempy.1*
%{_mandir}/man1/mkindex.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
%{_mandir}/man1/mktexfmt.1*
%{_mandir}/man1/mpost.1*
%{_mandir}/man1/mpto.1*
%{_mandir}/man1/newer.1*
%{_mandir}/man1/odvicopy.1*
%{_mandir}/man1/odvitype.1*
%{_mandir}/man1/ofm2opl.1*
%{_mandir}/man1/omega.1*
%{_mandir}/man1/opl2ofm.1*
%{_mandir}/man1/otp2ocp.1*
%{_mandir}/man1/outocp.1*
%{_mandir}/man1/ovf2ovp.1*
%{_mandir}/man1/ovp2ovf.1*
%{_mandir}/man1/patgen.1*
%{_mandir}/man1/pdfetex.1*
%{_mandir}/man1/pdftex.1*
#%{_mandir}/man1/pdfxtex.1*
%{_mandir}/man1/pfb2pfa.1*
%{_mandir}/man1/pk2bm.1*
%{_mandir}/man1/pktogf.1*
%{_mandir}/man1/pktype.1*
%{_mandir}/man1/pltotf.1*
%{_mandir}/man1/pooltype.1*
%{_mandir}/man1/ps2frag.1*
%{_mandir}/man1/rubibtex.1*
%{_mandir}/man1/rumakeindex.1*
%{_mandir}/man1/tangle.1*
%{_mandir}/man1/tex.1*
%{_mandir}/man1/texconfig.1*
%{_mandir}/man1/texconfig-sys.1*
%{_mandir}/man1/texdoc.1*
%{_mandir}/man1/texdoctk.1*
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texfind.1*
%{_mandir}/man1/texfont.1*
%{_mandir}/man1/texlinks.1*
%{_mandir}/man1/texutil.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/thumbpdf.1*
%{_mandir}/man1/tie.1*
%{_mandir}/man1/updmap.1*
%{_mandir}/man1/updmap-sys.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/vptovf.1*
%{_mandir}/man1/weave.1*
# new files not in Fedora tetex
%{_mandir}/man1/detex.1*
%{_mandir}/man5/updmap.cfg.*
# man pages for other utilities
%{_mandir}/man1/bbox.1*
%{_mandir}/man1/ctxtools.1*
%{_mandir}/man1/dvipos.1*
# in context
#%{_mandir}/man1/mptopdf.1*
%{_mandir}/man1/pdftools.1*
%{_mandir}/man1/pdftosrc.1*
%{_mandir}/man1/ps2eps.1*
%{_mandir}/man1/pstopdf.1*
%{_mandir}/man1/texmfstart.1*
%{_mandir}/man1/textools.1*
%dir %{_texmf_main}/web2c
%defattr(-,root,root,0755)
%{_texmf_main}/texconfig/
%{_texmf_main}/bibtex/
%{_texmf_main}/web2c/aleph.pool
%{_texmf_main}/web2c/mf.pool
%{_texmf_main}/web2c/omega.pool
%{_texmf_main}/web2c/pdftex.pool
%{_texmf_main}/web2c/tex.pool
#%{_texmf_main}/web2c/xetex.pool
%{_infodir}/dvipng.info*
%doc %{_texmf_main}/doc/bibtex8/
%dir /var/lib/texmf
%dir %{_texmf_var}/web2c/
%if 0
%{_texmf_var}/web2c/updmap.log
%dir %{_texmf_var}/web2c/aleph
%ghost %{_texmf_var}/web2c/aleph/aleph.fmt
%ghost %{_texmf_var}/web2c/aleph/aleph.log
%ghost %{_texmf_var}/web2c/aleph/lamed.fmt
%ghost %{_texmf_var}/web2c/aleph/lamed.log
%dir %{_texmf_var}/web2c/metafont
%ghost %{_texmf_var}/web2c/metafont/mf.base
%ghost %{_texmf_var}/web2c/metafont/mf.log
%dir %{_texmf_var}/web2c/metapost
%ghost %{_texmf_var}/web2c/metapost/mpost.log
%ghost %{_texmf_var}/web2c/metapost/mpost.mem
#
%dir %{_texmf_var}/web2c/omega
%ghost %{_texmf_var}/web2c/omega/lambda.fmt
%ghost %{_texmf_var}/web2c/omega/lambda.log
%ghost %{_texmf_var}/web2c/omega/omega.fmt
%ghost %{_texmf_var}/web2c/omega/omega.log
%dir %{_texmf_var}/web2c/tex
%ghost %{_texmf_var}/web2c/tex/tex.fmt
%ghost %{_texmf_var}/web2c/tex/tex.log
%dir %{_texmf_var}/web2c/pdftex
%ghost %{_texmf_var}/web2c/pdftex/*
%endif

%files afm
%defattr(0755,root,root,0755)
%{_bindir}/afm2tfm
%{_bindir}/ttf2afm
%{_bindir}/afm2pl
%defattr(0644,root,root,0755)
%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/ttf2afm.1*
# not in fedora tetex
%{_mandir}/man1/afm2pl.1*

%files context
%defattr(0755,root,root,0755)
%{_bindir}/mptopdf
%defattr(-,root,root,0755)
%{_mandir}/man1/mptopdf.1*
#
%if 0
%ghost %{_texmf_var}/web2c/metapost/metafun.log
%ghost %{_texmf_var}/web2c/metapost/metafun.mem
%ghost %{_texmf_var}/web2c/xetex/cont-en.fmt
%ghost %{_texmf_var}/web2c/xetex/cont-en.log
%endif

%files dvilj
%defattr(0644,root,root,0755)
%doc texk/dviljk/{AUTHORS,ChangeLog,INSTALL,NEWS,README}
%defattr(0755,root,root,0755)
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6
%defattr(0644,root,root,0755)
%{_mandir}/man1/dvilj.1*
%{_mandir}/man1/dvilj2p.1*
%{_mandir}/man1/dvilj4.1*
%{_mandir}/man1/dvilj4l.1*
%{_mandir}/man1/dvilj6.1*

%files dvipdfm
%defattr(0644,root,root,0755)
%doc texk/dvipdfm/{AUTHORS,COPYING,Credits,INSTALL*,NEWS,OBTAINING,README*,TODO,doc/}
%defattr(0755,root,root,0755)
%{_bindir}/ebb
%{_bindir}/dvipdfm
%{_bindir}/dvipdfmx
%{_bindir}/dvipdft
%{_bindir}/xdvipdfmx
%defattr(0644,root,root,0755)
%{_mandir}/man1/ebb.1*
%{_mandir}/man1/dvipdfm.1*
%{_mandir}/man1/dvipdft.1*
%{_texmf_main}/dvipdfm/
%exclude %{_texmf_main}/dvipdfm/dvipdfmx.cfg
%if 0
%{_texmf_var}/fonts/map/dvipdfm/updmap/dvipdfm.map
%{_texmf_var}/fonts/map/dvipdfm/updmap/dvipdfm_dl14.map
%{_texmf_var}/fonts/map/dvipdfm/updmap/dvipdfm_ndl14.map
%endif

%files dvips
%defattr(0644,root,root,0755)
%doc texk/dvipsk/{AUTHORS,README}
%defattr(0755,root,root,0755)
%{_bindir}/dvi2fax
%{_bindir}/dvips
%{_bindir}/dvired
%{_bindir}/odvips
#%{_bindir}/opdvips
#%{_bindir}/pdvips
%defattr(-,root,root,0755)
%{_texmf_main}/dvips/
%defattr(0644,root,root,0755)
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/odvips.1*
%{_infodir}/dvips.info*
#
#%{_mandir}/man1/opdvips.1*
#%{_mandir}/man1/pdvips.1*
#

%files dviutils
%defattr(0755,root,root,0755)
%{_bindir}/dt2dv
%{_bindir}/dv2dt
%{_bindir}/dvi2tty
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dvidvi
%{_bindir}/dviselect
%{_bindir}/dvitodvi
%defattr(0644,root,root,0755)
%{_mandir}/man1/dt2dv.1*
%{_mandir}/man1/dv2dt.1*
%{_mandir}/man1/dvi2tty.1*
%{_mandir}/man1/dvibook.1*
%{_mandir}/man1/dviconcat.1*
%{_mandir}/man1/dvidvi.1*
%{_mandir}/man1/dviselect.1*
%{_mandir}/man1/dvitodvi.1*

%files fonts
%defattr(0755,root,root,0755)
%{_bindir}/fmtutil
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/gsftopk
%{_bindir}/kpseaccess
%{_bindir}/kpsepath
%{_bindir}/kpsestat
%{_bindir}/kpsetool
%{_bindir}/kpsewhich
%{_bindir}/kpsexpand
%{_bindir}/mft
%{_bindir}/mktexfmt
%{_bindir}/mktexlsr
%{_bindir}/mktexmf
%{_bindir}/mktexpk
%{_bindir}/mktextfm
%{_bindir}/ps2pk
%{_bindir}/texhash
# new files (not in fedora tetex)
%{_bindir}/hbf2gf
%{_bindir}/ttf2pk
%{_bindir}/ttf2tfm
%defattr(0644,root,root,0755)
# man pages
%{_mandir}/man1/fmtutil.1*
%{_mandir}/man1/gftodvi.1*
%{_mandir}/man1/gftopk.1*
%{_mandir}/man1/gftype.1*
%{_mandir}/man1/gsftopk.1*
%{_mandir}/man1/kpseaccess.1*
%{_mandir}/man1/kpsepath.1*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhich.1*
%{_mandir}/man1/kpsexpand.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/ps2pk.1*
%{_mandir}/man1/texhash.1*
%{_mandir}/man5/fmtutil.cnf.5*
# man pages for new files (not in Fedora tetex)
%{_mandir}/man1/hbf2gf.1*
%{_mandir}/man1/ttf2pk.1*
%{_mandir}/man1/ttf2tfm.1*
# other stuff
%{_infodir}/web2c.info*
%defattr(-,root,root,0755)
%{_sysconfdir}/cron.daily/tetex.cron
%{_texmf_main}/web2c/mf.pool
%{_texmf_main}/web2c/*.opt
%{_texmf_main}/web2c/mktexdir
%{_texmf_main}/web2c/mktexnam
%{_texmf_main}/web2c/mktexupd
#
%if 0
%{_texmf_var}/web2c/xetex/xelatex.fmt
%{_texmf_var}/web2c/xetex/xelatex.log
%{_texmf_var}/web2c/xetex/xetex.fmt
%{_texmf_var}/web2c/xetex/xetex.log
%endif
#
%if 0
%{_texmf_var}/fonts/map/dvips/updmap/builtin35.map
%{_texmf_var}/fonts/map/dvips/updmap/download35.map
%{_texmf_var}/fonts/map/dvips/updmap/ps2pk.map
%{_texmf_var}/fonts/map/dvips/updmap/psfonts.map
%{_texmf_var}/fonts/map/dvips/updmap/psfonts_pk.map
%{_texmf_var}/fonts/map/dvips/updmap/psfonts_t1.map
%{_texmf_var}/fonts/map/pdftex/updmap/pdftex.map
%{_texmf_var}/fonts/map/pdftex/updmap/pdftex_dl14.map
%{_texmf_var}/fonts/map/pdftex/updmap/pdftex_ndl14.map
%endif

%files latex
%defattr(0755,root,root,0755)
%{_bindir}/latex
%{_bindir}/pdflatex
#%{_bindir}/platex
%{_bindir}/pslatex
#%{_bindir}/platex209
# not in fedora tetex
%{_bindir}/bg5+latex
%{_bindir}/bg5+pdflatex
%{_bindir}/bg5latex
%{_bindir}/bg5pdflatex
%{_bindir}/cef5latex
%{_bindir}/cef5pdflatex
%{_bindir}/ceflatex
%{_bindir}/cefpdflatex
%{_bindir}/cefslatex
%{_bindir}/cefspdflatex
%{_bindir}/cslatex
%{_bindir}/gbklatex
%{_bindir}/gbkpdflatex
%{_bindir}/lacheck
%{_bindir}/mkjobtexmf
%{_bindir}/mllatex
%{_bindir}/pdfcslatex
#%{_bindir}/pdfplatex
%{_bindir}/sjislatex
%{_bindir}/sjispdflatex
%{_bindir}/texcount
%{_bindir}/tpic2pdftex
%defattr(0644,root,root,0755)
%{_mandir}/man1/lacheck.1*
%{_mandir}/man1/latex.1*
%{_mandir}/man1/mkjobtexmf.1*
%{_mandir}/man1/pdflatex.1*
%{_mandir}/man1/pslatex.1*
%{_infodir}/latex.info*

%files mfwin
%defattr(0755,root,root,0755)
%{_bindir}/mf
%{_bindir}/mf-nowin
%defattr(0644,root,root,0755)
%{_mandir}/man1/mf.1*
%{_mandir}/man1/mf-nowin.1*

%files xdvi
%defattr(0644,root,root,0755)
%doc texk/xdvik/{BUGS,CHANGES,INSTALL,LESSTIF-BUGS,README*}
%defattr(0755,root,root,0755)
%{_bindir}/oxdvi
%{_bindir}/xdvi
%{_bindir}/xdvi.bin
%{_bindir}/xdvizilla
%defattr(-,root,root,0755)
%{_texmf_main}/xdvi/
%defattr(0644,root,root,0755)
%{_mandir}/man1/oxdvi.1*
%{_mandir}/man1/xdvi.1*
%{_mandir}/man1/xdvizilla.1*
%{_datadir}/pixmaps/xdvi48x48.png
%{_datadir}/applications/*xdvi.desktop

%files jadetex
%defattr(0755,root,root,0755)
%{_bindir}/jadetex
%{_bindir}/pdfjadetex

%files xmltex
%defattr(0755,root,root,0755)
%{_bindir}/xmltex
%{_bindir}/pdfxmltex

%files -n %{libkpathsea}
%defattr(0644,root,root,0755)
%doc texk/kpathsea/{AUTHORS,BUGS,HIER,PROJECTS,README*}
%defattr(0755,root,root,0755)
%{_libdir}/libkpathsea.so.*

%files -n %{libkpathsea_d}
%defattr(0644,root,root,0755)
%{_includedir}/kpathsea/
%{_infodir}/kpathsea.info*
%defattr(0755,root,root,0755)
%{_libdir}/libkpathsea.la
%{_libdir}/libkpathsea.so

%files -n %{libkpathsea_d_s}
%defattr(0644,root,root,0755)
%{_libdir}/libkpathsea.a
