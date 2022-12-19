%define _binary_payload w9.gzdio
%define _disable_lto 1

%define _texmf_enable_asymptote 0
%define _texmf_enable_biber 0
%define _texmf_enable_xindy 0
%bcond_without dvik
%define _texmf_with_system_dialog 1
%define _texmf_with_system_icu 1
%define _texmf_with_system_lcdf 0
%define _texmf_with_system_poppler 1
%define _texmf_with_system_psutils 1
%define _texmf_with_system_t1lib 1
%define _texmf_with_system_tex4ht 0
%define _texmf_with_system_teckit 1
%define enable_shared 1
%define historic 0

#-----------------------------------------------------------------------
Name:		texlive
Version:	20220321
Release:	13
Summary:	The TeX formatting system
Group:		Publishing
License:	http://www.tug.org/texlive/LICENSE.TL
URL:		http://tug.org/texlive/
%if %{historic}
Source0:	ftp://tug.org/historic/systems/texlive/%(echo %{version}|cut -b1-4)/texlive-%{version}-source.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/%(echo %{version}|cut -b1-4)/texlive-%{version}-source.tar.xz.sha512
%else
# svn co svn://tug.org/texlive/branches/branch2019/Build/source texlive-source
# cd texlive-source
# svn export . /tmp/texlive-$(date +%Y%m%d)-source
# cd /tmp
# tar cJf texlive-$(date +%Y%m%d)-source.tar.xz texlive-$(date +%Y%m%d)-source/
Source0:	https://ctan.org/tex-archive/systems/texlive/Source/texlive-%{version}-source.tar.xz
# sha512sum texlive-$(date +%Y%m%d)-source.tar.xz > texlive-$(date +%Y%m%d)-source.tar.xz.sha512
Source1:	texlive-%{version}-source.tar.xz.sha512
%endif
Source100:	%{name}.rpmlintrc
Obsoletes:	tetex-usrlocal < 3.0-1
Obsoletes:	texlive-fixmsxpart.bin < %{EVRD}

#-----------------------------------------------------------------------
Provides:	task-texlive = %{EVRD}
Requires:	ghostscript
%if %{_texmf_enable_asymptote}
Requires:	gv
Requires:	tkinter
%endif
%if %{_texmf_with_system_teckit}
Requires:	teckit >= 0:2.5.3-1
%endif

Requires:	texlive-collection-latexextra
Requires:	texlive-latex.bin
# Make sure the triggers are there
Requires(pre,post):	texlive-tlpkg
BuildRequires:	texlive-tlpkg

#-----------------------------------------------------------------------
BuildRequires:	bison
%if %{_texmf_enable_xindy}
BuildRequires:	clisp
BuildRequires:	ffcall-devel
%endif
%if %{_texmf_enable_asymptote}
BuildRequires:	fftw-devel
BuildRequires:	flex
%endif
BuildRequires:	freetype-devel
BuildRequires:	fontconfig-devel
%if %{_texmf_enable_asymptote}
BuildRequires:	libgc-devel
BuildRequires:	libsigsegv-devel
BuildRequires:	ghostscript-dvipdf
BuildRequires:	gsl-devel
BuildRequires:	GL-devel
%endif
BuildRequires:	gd-devel
%if %{_texmf_with_system_icu}
BuildRequires:	icu-devel >= 49
%endif
%if %{_texmf_with_system_poppler}
BuildRequires:	pkgconfig(poppler) >= 22.04.0
%endif
BuildRequires:	ghostscript-devel
BuildRequires:	glibc-static-devel stdc++-static-devel
BuildRequires:	gmp-devel
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	xaw-devel
BuildRequires:	pkgconfig(xaw3d)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
%if !%{_texmf_with_system_dialog}
BuildRequires:	ncurses-devel
%endif
BuildRequires:	png-devel
%if %{_texmf_with_system_t1lib}
BuildRequires:	t1lib-devel
%endif
%if %{_texmf_with_system_teckit}
BuildRequires:	teckit-devel
%endif
%if %{_texmf_enable_xindy}
BuildRequires:	texlive
%endif
%if %{_texmf_enable_asymptote}
BuildRequires:	texinfo
%endif
BuildRequires:	zziplib-devel
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(graphite2)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	libpaper-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

#-----------------------------------------------------------------------
Patch1:		texlive-asymptote.patch
Patch2:		texlive-xdvi.patch
# New definition only misses default location...
Patch3:		texlive-texmfcnf.patch
Patch4:		texlive-20150521-clang-3.8.patch
Patch5:		texlive-20180414-compile.patch
Patch6:		texlive-2018-libdl-linkage.patch
Patch7:		texlive-20210324-restore-poppler-support.patch
Patch8:		texlive-poppler-21.09.patch
Patch9:		texlive-20210324-poppler-22.03.patch
Patch10:	texlive-20210324-poppler-22.04.patch
Patch11:	texlive-20220321-poppler-22.09.patch
Patch12:	texlive-20220321-clang-15.patch
Patch13:	texlive-20220321-fix-m4-syntax-errors.patch
Patch14:	texlive-20220321-ghostscript-10.patch
# LFS sometimes (not yet for 2021) has useful patches at
# http://www.linuxfromscratch.org/patches/blfs/svn
#-----------------------------------------------------------------------

%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files
%dir %{_texmfvardir}
%dir %{_texmfconfdir}

#-----------------------------------------------------------------------
%if %{enable_shared}
########################################################################
%define kpathsea %{mklibname kpathsea 6}

%package -n %{kpathsea}
Summary:	Path searching library for TeX-related files
Group:		System/Libraries
Provides:	kpathsea = %{version}-%{release}

%description -n %{kpathsea}
Kpathsea implements generic path searching, configuration,
and TeX-specific file searching.

%files -n %{kpathsea}
%{_libdir}/libkpathsea.so.*

#-----------------------------------------------------------------------
%define kpathsea_devel %{mklibname -d kpathsea}

%package -n %{kpathsea_devel}
Summary:	Kpathsea development files
Group:		Development/C
Requires:	kpathsea = %{version}-%{release}
Provides:	kpathsea-devel = %{version}-%{release}

%description -n %{kpathsea_devel}
Kpathsea implements generic path searching, configuration,
and TeX-specific file searching.
This package includes the kpathsea development files.

%files -n %{kpathsea_devel}
%{_includedir}/kpathsea
%{_libdir}/libkpathsea.so
%{_libdir}/pkgconfig/kpathsea.pc

#-----------------------------------------------------------------------
%define ptexenc %{mklibname ptexenc 1}

%package -n %{ptexenc}
Summary:	Library for Japanese pTeX
Group:		System/Libraries
Provides:	ptexenc = %{version}-%{release}

%description -n %{ptexenc}
ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.

%files -n %{ptexenc}
%{_libdir}/libptexenc.so.*

#-----------------------------------------------------------------------
%define ptexenc_devel %{mklibname -d ptexenc}

%package -n %{ptexenc_devel}
Summary:	Library for Japanese pTeX
Group:		Development/C
Requires:	ptexenc = %{version}-%{release}
Provides:	ptexenc-devel = %{version}-%{release}

%description -n %{ptexenc_devel}
ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.
This package includes the ptexenc development files.

%files -n %{ptexenc_devel}
%{_includedir}/ptexenc/
%{_libdir}/libptexenc.so
%{_libdir}/pkgconfig/ptexenc.pc
########################################################################
# enable_shared
%endif

#-----------------------------------------------------------------------
%package -n texlive-afm2pl.bin
Summary:	Binary files of afm2pl
Group:		System/Libraries

%description -n texlive-afm2pl.bin
texlive afm2pl.bin package.

%files -n texlive-afm2pl.bin
%{_bindir}/afm2pl

#-----------------------------------------------------------------------
%package -n texlive-aleph.bin
Summary:	Binary files of aleph
Group:		System/Libraries

%description -n texlive-aleph.bin
texlive aleph.bin package.

%files -n texlive-aleph.bin
%{_bindir}/aleph
%{_bindir}/lamed

#-----------------------------------------------------------------------
%package -n texlive-axohelp.bin
Summary:	Binary files of axohelp
Group:		System/Libraries

%description -n texlive-axohelp.bin
texlive axohelp.bin package.

%files -n texlive-axohelp.bin
%{_bindir}/axohelp

#-----------------------------------------------------------------------
%if %{_texmf_enable_biber}
%package -n texlive-biber.bin
Summary:	Binary files of biber
Group:		System/Libraries

%description -n texlive-biber.bin
texlive biber.bin package.

%files -n texlive-biber.bin
%{_bindir}/biber
%endif

#-----------------------------------------------------------------------
%package -n texlive-bibtex.bin
Summary:	Binary files of bibtex
Group:		System/Libraries

%description -n texlive-bibtex.bin
texlive bibtex.bin package.

%files -n texlive-bibtex.bin
%{_bindir}/bibtex

#-----------------------------------------------------------------------
%package -n texlive-bibtex8.bin
Summary:	Binary files of bibtex8
Group:		System/Libraries

%description -n texlive-bibtex8.bin
texlive bibtex8.bin package.

%files -n texlive-bibtex8.bin
%{_bindir}/bibtex8

#-----------------------------------------------------------------------
%package -n texlive-bibtexu.bin
Summary:	Binary files of bibtexu
Group:		System/Libraries

%description -n texlive-bibtexu.bin
texlive bibtexu.bin package.

%files -n texlive-bibtexu.bin
%{_bindir}/bibtexu

#-----------------------------------------------------------------------
%package -n texlive-chktex.bin
Summary:	Binary files of chktex
Group:		System/Libraries

%description -n texlive-chktex.bin
texlive chktex.bin package.

%files -n texlive-chktex.bin
%{_bindir}/chktex

#-----------------------------------------------------------------------
%package -n texlive-chkdvifont.bin
Summary:	Binary files of chkdvifont
Group:		System/Libraries

%description -n texlive-chkdvifont.bin
texlive chkdvifont.bin package.

%files -n texlive-chkdvifont.bin
%{_bindir}/chkdvifont

#-----------------------------------------------------------------------
%package -n texlive-cjkutils.bin
Summary:	Binary files of cjkutils
Group:		System/Libraries

%description -n texlive-cjkutils.bin
texlive cjkutils.bin package.

%files -n texlive-cjkutils.bin
%{_bindir}/bg5+latex
%{_bindir}/bg5+pdflatex
%{_bindir}/bg5conv
%{_bindir}/bg5latex
%{_bindir}/bg5pdflatex
%{_bindir}/cef5conv
%{_bindir}/cef5latex
%{_bindir}/cef5pdflatex
%{_bindir}/cefconv
%{_bindir}/ceflatex
%{_bindir}/cefpdflatex
%{_bindir}/cefsconv
%{_bindir}/cefslatex
%{_bindir}/cefspdflatex
%{_bindir}/extconv
%{_bindir}/gbklatex
%{_bindir}/gbkpdflatex
%{_bindir}/hbf2gf
%{_bindir}/sjisconv
%{_bindir}/sjislatex
%{_bindir}/sjispdflatex

#-----------------------------------------------------------------------
%package -n texlive-cluttex.bin
Summary:	Binary files of cluttex
Group:		System/Libraries

%description -n texlive-cluttex.bin
texlive cluttex.bin package.

%files -n texlive-cluttex.bin
%{_bindir}/cluttex

#-----------------------------------------------------------------------
%package -n texlive-clxelatex.bin
Summary:	Binary files of clxelatex
Group:		System/Libraries

%description -n texlive-clxelatex.bin
texlive clxelatex.bin package.

%files -n texlive-clxelatex.bin
%{_bindir}/clxelatex

#-----------------------------------------------------------------------
%package -n texlive-ctanbib.bin
Summary:	Binary files of ctanbib
Group:		System/Libraries

%description -n texlive-ctanbib.bin
texlive ctanbib.bin package.

%files -n texlive-ctanbib.bin
%{_bindir}/ctanbib

#-----------------------------------------------------------------------
%package -n texlive-ctie.bin
Summary:	Binary files of ctie
Group:		System/Libraries

%description -n texlive-ctie.bin
texlive ctie.bin package.

%files -n texlive-ctie.bin
%{_bindir}/ctie

#-----------------------------------------------------------------------
%package -n texlive-ctwill.bin
Summary:	Binary files of ctwill
Group:		System/Libraries

%description -n texlive-ctwill.bin
texlive ctwill.bin package.

%files -n texlive-ctwill.bin
%{_bindir}/ctwill
%{_bindir}/ctwill-refsort
%{_bindir}/ctwill-twinx

#-----------------------------------------------------------------------
%package -n texlive-cweb.bin
Summary:	Binary files of cweb
Group:		System/Libraries

%description -n texlive-cweb.bin
texlive cweb.bin package.

%files -n texlive-cweb.bin
%{_bindir}/ctangle
%{_bindir}/cweave
%{_bindir}/twill

#-----------------------------------------------------------------------
%package -n texlive-detex.bin
Summary:	Binary files of detex
Group:		System/Libraries

%description -n texlive-detex.bin
texlive detex.bin package.

%files -n texlive-detex.bin
%{_bindir}/detex

#-----------------------------------------------------------------------
%package -n texlive-devnag.bin
Summary:	Binary files of devnag
Group:		System/Libraries

%description -n texlive-devnag.bin
texlive devnag.bin package.

%files -n texlive-devnag.bin
%{_bindir}/devnag

#-----------------------------------------------------------------------
%package -n texlive-dtl.bin
Summary:	Binary files of dtl
Group:		System/Libraries

%description -n texlive-dtl.bin
texlive dtl.bin package.

%files -n texlive-dtl.bin
%{_bindir}/dt2dv
%{_bindir}/dv2dt

#-----------------------------------------------------------------------
%package -n texlive-dvi2tty.bin
Summary:	Binary files of dvi2tty
Group:		System/Libraries

%description -n texlive-dvi2tty.bin
texlive dvi2tty.bin package.

%files -n texlive-dvi2tty.bin
%{_bindir}/disdvi
%{_bindir}/dvi2tty

#-----------------------------------------------------------------------
%package -n texlive-dvicopy.bin
Summary:	Binary files of dvicopy
Group:		System/Libraries

%description -n texlive-dvicopy.bin
texlive dvicopy.bin package.

%files -n texlive-dvicopy.bin
%{_bindir}/dvicopy

#-----------------------------------------------------------------------
%package -n texlive-dvidvi.bin
Summary:	Binary files of dvidvi
Group:		System/Libraries

%description -n texlive-dvidvi.bin
texlive dvidvi.bin package.

%files -n texlive-dvidvi.bin
%{_bindir}/dvidvi

#-----------------------------------------------------------------------
%package -n texlive-dviljk.bin
Summary:	Binary files of dviljk
Group:		System/Libraries

%description -n texlive-dviljk.bin
texlive dviljk.bin package.

%files -n texlive-dviljk.bin
%{_bindir}/dvihp
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6

#-----------------------------------------------------------------------
%package -n texlive-dvipdfmx.bin
Summary:	Binary files of dvipdfmx
Group:		System/Libraries
Provides:	texlive-dvipdfm.bin = %{EVRD}

%description -n texlive-dvipdfmx.bin
texlive dvipdfmx.bin package.

%files -n texlive-dvipdfmx.bin
%{_bindir}/dvipdfm
%{_bindir}/dvipdfmx
%{_bindir}/ebb
%{_bindir}/extractbb

#-----------------------------------------------------------------------
%package -n texlive-dvipng.bin
Summary:	Binary files of dvipng
Group:		System/Libraries

%description -n texlive-dvipng.bin
texlive dvipng.bin package.

%files -n texlive-dvipng.bin
%{_bindir}/dvigif
%{_bindir}/dvipng

#-----------------------------------------------------------------------
%package -n texlive-dvipos.bin
Summary:	Binary files of dvipos
Group:		System/Libraries

%description -n texlive-dvipos.bin
texlive dvipos.bin package.

%files -n texlive-dvipos.bin
%{_bindir}/dvipos

#-----------------------------------------------------------------------
%package -n texlive-dvips.bin
Summary:	Binary files of dvips
Group:		System/Libraries

%description -n texlive-dvips.bin
texlive dvips.bin package.

%files -n texlive-dvips.bin
%{_bindir}/afm2tfm
%{_bindir}/dvips

#-----------------------------------------------------------------------
%package -n texlive-dvispc.bin
Summary:	Binary files of dvispc
Group:		System/Libraries

%description -n texlive-dvispc.bin
texlive dvispc.bin package.

%files -n texlive-dvispc.bin
%{_bindir}/dvispc

#-----------------------------------------------------------------------
%package -n texlive-dvisvgm.bin
Summary:	Binary files of dvisvgm
Group:		System/Libraries

%description -n texlive-dvisvgm.bin
texlive dvisvgm.bin package.

%files -n texlive-dvisvgm.bin
%{_bindir}/dvisvgm

#-----------------------------------------------------------------------
%package -n texlive-fontware.bin
Summary:	Binary files of fontware
Group:		System/Libraries

%description -n texlive-fontware.bin
texlive fontware.bin package.

%files -n texlive-fontware.bin
%{_bindir}/pltotf
%{_bindir}/tftopl
%{_bindir}/vftovp
%{_bindir}/vptovf

#-----------------------------------------------------------------------
%package -n texlive-gsftopk.bin
Summary:	Binary files of gsftopk
Group:		System/Libraries

%description -n texlive-gsftopk.bin
texlive gsftopk.bin package.

%files -n texlive-gsftopk.bin
%{_bindir}/gsftopk

#-----------------------------------------------------------------------
%package -n texlive-kpathsea.bin
Summary:	Binary files of kpathsea
Group:		System/Libraries

%description -n texlive-kpathsea.bin
texlive kpathsea.bin package.

%files -n texlive-kpathsea.bin
%{_bindir}/kpseaccess
%{_bindir}/kpsepath
%{_bindir}/kpsereadlink
%{_bindir}/kpsestat
%{_bindir}/kpsetool
%{_bindir}/kpsewhich
%{_bindir}/kpsexpand
%{_bindir}/mkocp
%{_bindir}/mkofm
%{_bindir}/mktexfmt
%{_bindir}/mktexlsr
%{_bindir}/mktexmf
%{_bindir}/mktexpk
%{_bindir}/mktextfm
%{_bindir}/texhash

#-----------------------------------------------------------------------
%package -n texlive-lacheck.bin
Summary:	Binary files of lacheck
Group:		System/Libraries

%description -n texlive-lacheck.bin
texlive lacheck.bin package.

%files -n texlive-lacheck.bin
%{_bindir}/lacheck

#-----------------------------------------------------------------------
%package -n texlive-latex.bin
Summary:	Binary files of latex
Group:		System/Libraries
Provides:	texlive-latex-bin.bin = %{EVRD}

%description -n texlive-latex.bin
texlive latex.bin package.

%files -n texlive-latex.bin
%{_bindir}/dvilualatex
%{_bindir}/latex
%{_bindir}/lualatex
%{_bindir}/pdflatex
%{_bindir}/ltx2crossrefxml
%{_bindir}/git-latexdiff

#-----------------------------------------------------------------------
%package -n texlive-albatross.bin
Summary:	Binary files of albatross
Group:		System/Libraries

%description -n texlive-albatross.bin
texlive albatross.bin package.

%files -n texlive-albatross.bin
%{_bindir}/albatross

#-----------------------------------------------------------------------
%package -n texlive-hyperxmp-add-bytecount.bin
Summary:	Binary files of hyperxmp-add-bytecount
Group:		System/Libraries

%description -n texlive-hyperxmp-add-bytecount.bin
texlive hyperxmp-add-bytecount.bin package.

%files -n texlive-hyperxmp-add-bytecount.bin
%{_bindir}/hyperxmp-add-bytecount

#-----------------------------------------------------------------------
%package -n texlive-llmk.bin
Summary:	Binary files of llmk
Group:		System/Libraries

%description -n texlive-llmk.bin
texlive llmk.bin package.

%files -n texlive-llmk.bin
%{_bindir}/llmk

#-----------------------------------------------------------------------
%package -n texlive-spix.bin
Summary:	Binary files of spix
Group:		System/Libraries

%description -n texlive-spix.bin
texlive spix.bin package.

%files -n texlive-spix.bin
%{_bindir}/spix

#-----------------------------------------------------------------------
%package -n texlive-tikztosvg.bin
Summary:	Binary files of tikztosvg
Group:		System/Libraries

%description -n texlive-tikztosvg.bin
texlive tikztosvg.bin package.

%files -n texlive-tikztosvg.bin
%{_bindir}/tikztosvg

#-----------------------------------------------------------------------
%package -n texlive-xml2pmx.bin
Summary:	Binary files of xml2pmx
Group:		System/Libraries

%description -n texlive-xml2pmx.bin
texlive xml2pmx.bin package.

%files -n texlive-xml2pmx.bin
%{_bindir}/xml2pmx

#-----------------------------------------------------------------------
%package -n texlive-msxlint.bin
Summary:	Binary files of msxlint
Group:		System/Libraries

%description -n texlive-msxlint.bin
texlive msxlint.bin package.

%files -n texlive-msxlint.bin
%{_bindir}/msxlint

#-----------------------------------------------------------------------
%package -n texlive-lcdftypetools.bin
Summary:	Binary files of lcdftypetools
Group:		System/Libraries

%description -n texlive-lcdftypetools.bin
texlive lcdftypetools.bin package.

%files -n texlive-lcdftypetools.bin
%{_bindir}/cfftot1
%{_bindir}/mmafm
%{_bindir}/mmpfb
%{_bindir}/otfinfo-texlive
%{_bindir}/otftotfm
%{_bindir}/t1dotlessj
%{_bindir}/t1lint
%{_bindir}/t1rawafm
%{_bindir}/t1reencode
%{_bindir}/t1testpage
%{_bindir}/ttftotype42

#-----------------------------------------------------------------------
%package -n texlive-luatex.bin
Summary:	Binary files of luatex
Group:		System/Libraries

%description -n texlive-luatex.bin
texlive luatex.bin package.

%files -n texlive-luatex.bin
%{_bindir}/cllualatex
%{_bindir}/dviluatex
%{_bindir}/luatex
%{_bindir}/texlua
%{_bindir}/texluac
%{_bindir}/mflua
%{_bindir}/mflua-nowin
%{_bindir}/luahbtex
%{_bindir}/luajithbtex
%{_bindir}/luafindfont
%ifnarch %{riscv} %{mips} %{power64} s390 s390x
%{_bindir}/luajittex
%{_bindir}/mfluajit
%{_bindir}/mfluajit-nowin
%endif

%ifnarch %{riscv} %{mips} %{power64} s390 s390x
%libpackage texluajit 2
%endif
%libpackage texlua53 5

#-----------------------------------------------------------------------
%package -n texlive-m-tx.bin
Summary:	Binary files of m-tx
Group:		System/Libraries

%description -n texlive-m-tx.bin
texlive m-tx.bin package.

%files -n texlive-m-tx.bin
%{_bindir}/prepmx

#-----------------------------------------------------------------------
%package -n texlive-makeindex.bin
Summary:	Binary files of makeindex
Group:		System/Libraries

%description -n texlive-makeindex.bin
texlive makeindex.bin package.

%files -n texlive-makeindex.bin
%{_bindir}/makeindex
%{_bindir}/mkindex
%{_bindir}/xindex

#-----------------------------------------------------------------------
%package -n texlive-metafont.bin
Summary:	Binary files of metafont
Group:		System/Libraries

%description -n texlive-metafont.bin
texlive metafont.bin package.

%files -n texlive-metafont.bin
%{_bindir}/inimf
%{_bindir}/mf
%{_bindir}/mf-nowin

#-----------------------------------------------------------------------
%package -n texlive-metapost.bin
Summary:	Binary files of metapost
Group:		System/Libraries

%description -n texlive-metapost.bin
texlive metapost.bin package.

%files -n texlive-metapost.bin
%{_bindir}/dvitomp
%{_bindir}/mfplain
%{_bindir}/mpost
%{_bindir}/pdvitomp
%{_bindir}/pmpost
%{_bindir}/updvitomp
%{_bindir}/upmpost
%{_bindir}/r-mpost
%{_bindir}/r-pmpost
%{_bindir}/r-upmpost

#-----------------------------------------------------------------------
%package -n texlive-mfware.bin
Summary:	Binary files of mfware
Group:		System/Libraries

%description -n texlive-mfware.bin
texlive mfware.bin package.

%files -n texlive-mfware.bin
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/mft
%{_bindir}/pktogf
%{_bindir}/pktype

#-----------------------------------------------------------------------
%package -n texlive-omegaware.bin
Summary:	Binary files of omegaware
Group:		System/Libraries

%description -n texlive-omegaware.bin
texlive omegaware.bin package.

%files -n texlive-omegaware.bin
%{_bindir}/odvicopy
%{_bindir}/odvitype
%{_bindir}/ofm2opl
%{_bindir}/omfonts
%{_bindir}/opl2ofm
%{_bindir}/otangle
%{_bindir}/otp2ocp
%{_bindir}/outocp
%{_bindir}/ovf2ovp
%{_bindir}/ovp2ovf

#-----------------------------------------------------------------------
%package -n texlive-patgen.bin
Summary:	Binary files of patgen
Group:		System/Libraries

%description -n texlive-patgen.bin
texlive patgen.bin package.

%files -n texlive-patgen.bin
%{_bindir}/patgen

#-----------------------------------------------------------------------
%package -n texlive-pdftex.bin
Summary:	Binary files of pdftex
Group:		System/Libraries
Provides:	texlive-amstex.bin = %{EVRD}
Provides:	texlive-cslatex.bin = %{EVRD}
Provides:	texlive-csplain.bin = %{EVRD}
Provides:	texlive-eplain.bin = %{EVRD}
Provides:	texlive-jadetex.bin = %{EVRD}
Provides:	texlive-mex.bin = %{EVRD}
Provides:	texlive-mltex.bin = %{EVRD}
Provides:	texlive-texsis.bin = %{EVRD}
Provides:	texlive-xmltex.bin = %{EVRD}

%description -n texlive-pdftex.bin
texlive pdftex.bin package.

%files -n texlive-pdftex.bin
%{_bindir}/amstex
%{_bindir}/cslatex
%{_bindir}/csplain
%{_bindir}/pdfcsplain
%{_bindir}/eplain
%{_bindir}/etex
%{_bindir}/jadetex
%{_bindir}/mex
%{_bindir}/mllatex
%{_bindir}/mltex
%{_bindir}/pdfcslatex
%{_bindir}/pdfetex
%{_bindir}/pdfjadetex
%{_bindir}/pdfmex
%{_bindir}/pdftex
%{_bindir}/pdftex-quiet
%{_bindir}/pdfxmltex
%{_bindir}/texsis
%{_bindir}/utf8mex
%{_bindir}/xmltex

#-----------------------------------------------------------------------
%package -n texlive-pdftools.bin
Summary:	Binary files of pdftools
Group:		System/Libraries

%description -n texlive-pdftools.bin
texlive pdftools.bin package.

%files -n texlive-pdftools.bin
%{_bindir}/pdfclose
%{_bindir}/pdfopen
%{_bindir}/pdftosrc

#-----------------------------------------------------------------------
%package -n texlive-pmx.bin
Summary:	Binary files of pmx
Group:		System/Libraries

%description -n texlive-pmx.bin
texlive pmx.bin package.

%files -n texlive-pmx.bin
%{_bindir}/pmxab
%{_bindir}/scor2prt

#-----------------------------------------------------------------------
%package -n texlive-ps2pkm.bin
Summary:	Binary files of ps2pkm
Group:		System/Libraries

%description -n texlive-ps2pkm.bin
texlive ps2pkm.bin package.

%files -n texlive-ps2pkm.bin
%{_bindir}/mag
%{_bindir}/pfb2pfa
%{_bindir}/pk2bm
%{_bindir}/ps2pk

#-----------------------------------------------------------------------
%package -n texlive-pstools.bin
Summary:	Binary files of pstools
Group:		System/Libraries

%description -n texlive-pstools.bin
texlive pstools.bin package.

%files -n texlive-pstools.bin
%{_bindir}/bbox

#-----------------------------------------------------------------------
%package -n texlive-ptex.bin
Summary:	Binary files of ptex
Group:		System/Libraries

%description -n texlive-ptex.bin
texlive ptex.bin package.

%files -n texlive-ptex.bin
%{_bindir}/eptex
%{_bindir}/makejvf
%{_bindir}/mendex
%{_bindir}/pbibtex
%{_bindir}/pdvitype
%{_bindir}/platex
%{_bindir}/ppltotf
%{_bindir}/ptex
%{_bindir}/ptftopl

#-----------------------------------------------------------------------
%package -n texlive-seetexk.bin
Summary:	Binary files of seetexk
Group:		System/Libraries

%description -n texlive-seetexk.bin
texlive seetexk.bin package.

%files -n texlive-seetexk.bin
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dviselect
%{_bindir}/dvitodvi

#-----------------------------------------------------------------------
%package -n texlive-synctex.bin
Summary:	Binary files of synctex
Group:		System/Libraries

%description -n texlive-synctex.bin
texlive synctex.bin package.

%files -n texlive-synctex.bin
%{_bindir}/synctex

%libpackage synctex 2

%define synctex_devel %{mklibname -d synctex}
%package -n %{synctex_devel}
Summary:	SyncTeX development files
Group:		Development/C
Requires:	texlive-synctex.bin = %{version}-%{release}
Requires:	%{mklibname synctex 2} = %{version}-%{release}

%description -n %{synctex_devel}
This package includes the SyncTeX development files.

%files -n %{synctex_devel}
%{_includedir}/synctex
%{_libdir}/libsynctex.so
%{_libdir}/pkgconfig/synctex.pc
#-----------------------------------------------------------------------

%package -n texlive-tex.bin
Summary:	Binary files of tex
Group:		System/Libraries

%description -n texlive-tex.bin
texlive tex.bin package.

%files -n texlive-tex.bin
%{_bindir}/initex
%{_bindir}/tex

#-----------------------------------------------------------------------
%package -n texlive-tex4ht.bin
Summary:	Binary files of tex4ht
Group:		System/Libraries

%description -n texlive-tex4ht.bin
texlive tex4ht.bin package.

%files -n texlive-tex4ht.bin
%{_bindir}/t4ht
%{_bindir}/tex4ht

#-----------------------------------------------------------------------
%package -n texlive-texware.bin
Summary:	Binary files of texware
Group:		System/Libraries

%description -n texlive-texware.bin
texlive texware.bin package.

%files -n texlive-texware.bin
%{_bindir}/dvitype
%{_bindir}/pooltype

#-----------------------------------------------------------------------
%package -n texlive-tie.bin
Summary:	Binary files of tie
Group:		System/Libraries

%description -n texlive-tie.bin
texlive tie.bin package.

%files -n texlive-tie.bin
%{_bindir}/tie

#-----------------------------------------------------------------------
%package -n texlive-ttfutils.bin
Summary:	Binary files of ttfutils
Group:		System/Libraries

%description -n texlive-ttfutils.bin
texlive ttfutils.bin package.

%files -n texlive-ttfutils.bin
%{_bindir}/ttf2afm
%{_bindir}/ttf2pk
%{_bindir}/ttf2tfm
%{_bindir}/ttfdump

#-----------------------------------------------------------------------
%package -n texlive-uptex.bin
Summary:	Binary files of uptex
Group:		System/Libraries

%description -n texlive-uptex.bin
texlive uptex.bin package.

%files -n texlive-uptex.bin
%{_bindir}/euptex
%{_bindir}/upbibtex
%{_bindir}/updvitype
%{_bindir}/uplatex
%{_bindir}/upmendex
%{_bindir}/uppltotf
%{_bindir}/uptex
%{_bindir}/uptftopl
%{_bindir}/wovp2ovf

#-----------------------------------------------------------------------
%package -n texlive-vlna.bin
Summary:	Binary files of vlna
Group:		System/Libraries

%description -n texlive-vlna.bin
texlive vlna.bin package.

%files -n texlive-vlna.bin
%{_bindir}/vlna

#-----------------------------------------------------------------------
%package -n texlive-web.bin
Summary:	Binary files of web
Group:		System/Libraries

%description -n texlive-web.bin
texlive web.bin package.

%files -n texlive-web.bin
%{_bindir}/tangle
%{_bindir}/weave
%{_bindir}/webquiz

%if %{with dvik}
#-----------------------------------------------------------------------
%package -n texlive-xdvi.bin
Summary:	Binary files of xdvi
Group:		System/Libraries

%description -n texlive-xdvi.bin
texlive xdvi.bin package.

%files -n texlive-xdvi.bin
%{_bindir}/xdvi
%{_bindir}/xdvi-xaw
%{_datadir}/applications/xdvi.desktop
%endif

#-----------------------------------------------------------------------
%package -n texlive-xetex.bin
Summary:	Binary files of xetex
Group:		System/Libraries

%if ! %{_texmf_with_system_teckit}
Requires:	teckit
%endif

%description -n texlive-xetex.bin
texlive xetex.bin package.

%files -n texlive-xetex.bin
%if ! %{_texmf_with_system_teckit}
%{_bindir}/teckit_compile
%endif
%{_bindir}/xdvipdfmx
%{_bindir}/xelatex
%{_bindir}/xetex
%{_bindir}/xelatex-unsafe
%{_bindir}/xetex-unsafe

#-----------------------------------------------------------------------
%package -n texlive-texlog.bin
Summary:	texlog binaries, part of TeX Live
Group:		System/Libraries

%description -n texlive-texlog.bin
texlog binaries, part of TeX Live

%files -n texlive-texlog.bin
%{_bindir}/texlogfilter
%{_bindir}/texlogsieve

#-----------------------------------------------------------------------
%package -n texlive-optexcount.bin
Summary:	optexcount binary, part of TeX Live
Group:		System/Libraries

%description -n texlive-optexcount.bin
optexcount binary, part of TeX Live

%files -n texlive-optexcount.bin
%{_bindir}/optexcount

#-----------------------------------------------------------------------
%package -n texlive-hitex.bin
Summary:	hitex binaries, part of TeX Live
Group:		System/Libraries

%description -n texlive-hitex.bin
hitex binaries, part of TeX Live

%files -n texlive-hitex.bin
%{_bindir}/hishrink
%{_bindir}/histretch
%{_bindir}/hitex

#-----------------------------------------------------------------------
%package -n texlive-citeproc.bin
Summary:	citeproc binary, part of TeX Live
Group:		System/Libraries

%description -n texlive-citeproc.bin
citeproc binary, part of TeX Live

%files -n texlive-citeproc.bin
%{_bindir}/citeproc

#-----------------------------------------------------------------------
%package -n texlive-autosp.bin
Summary:	autosp binary, part of TeX Live
Group:		System/Libraries

%description -n texlive-autosp.bin
autosp binary, part of TeX Live.

%files -n texlive-autosp.bin
%{_bindir}/autosp

#-----------------------------------------------------------------------
%package -n texlive-gregorio.bin
Summary:	gregorio - tool for working with Gregorian Chants in TeX
Group:		System/Libraries

%description -n texlive-gregorio.bin
gregorio - tool for working with Gregorian Chants in TeX.

%files -n texlive-gregorio.bin
%{_bindir}/gregorio

#-----------------------------------------------------------------------
%package -n texlive-tex2aspc.bin
Summary:	Binary files of tex2aspc
Group:		System/Libraries

%description -n texlive-tex2aspc.bin
texlive tex2aspc.bin package.

%files -n texlive-tex2aspc.bin
%{_bindir}/tex2aspc

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -n %{name}-%{version}-source
# libtool suuuuuuuuuuuuucks!!!!!
find . -name libtool -o -name ltmain.sh -o -name configure |xargs sed -i -e "s,2\.4\.6,$(libtool --version |head -n1 |rev |cut -d' ' -f1 |rev),g"

# setup default builtin values, added to paths.h from texmf.cnf
perl -pi -e 's|^(TEXMFMAIN\s+= ).*|$1%{_texmfdistdir}|;'		  \
	 -e 's|^(TEXMFDIST\s+= ).*|$1%{_texmfdistdir}|;'		  \
	 -e 's|\@\@TEXMFCNF\@\@|%{_texmfdistdir}/web2c|;'		  \
	 -e 's|^(TEXMFLOCAL\s+= ).*|$1%{_texmflocaldir}|;'		  \
	 -e 's|^(TEXMFSYSVAR\s+= ).*|$1%{_texmfvardir}|;'		  \
	 -e 's|^(TEXMFSYSCONFIG\s+= ).*|$1%{_texmfconfdir}|;'		  \
	 -e 's|^(TEXMFHOME\s+= ).*|$1\$HOME/texmf|;'			  \
	 -e 's|^(TEXMFVAR\s+= ).*|$1\$HOME/.texlive2013/texmf-var|;'	  \
	 -e 's|^(TEXMFCONFIG\s+= ).*|$1\$HOME/.texlive2013/texmf-config|;'\
	 -e 's|^(OSFONTDIR\s+= ).*|$1%{_datadir}/fonts|;'		  \
	texk/kpathsea/texmf.cnf

# t4ht expects to be un /usr/share/texmf/bin/t4ht (FS#27251)
sed -i s/SELFAUTOPARENT/TEXMFROOT/ texk/tex4htk/t4ht.c

## prevent compiling Xdvi with libXp
sed -i~ 's|-lXp ||' texk/xdvik/configure
#find texk/web2c/{lua,pdf}texdir -type f | xargs sed -e 's|gTrue|true|g' -e 's|gFalse|false|g' -e 's|GBool|bool|g' -i

#-----------------------------------------------------------------------
%build
mkdir texlive
pushd texlive

# As of 2.9.1, freetype-config doesn't exist anymore -- but texlive
# uses it in so many places that patching its use away would be painful.
# Let's provide it instead...
cat >freetype-config <<'EOF'
#!/bin/sh
for i in "$@"; do
    if [ "$i" = "--ftversion" ]; then
	ARGS="$ARGS --modversion"
    else
	ARGS="$ARGS $i"
    fi
done
exec pkg-config $ARGS freetype2
EOF
chmod +x freetype-config
export PATH=$PATH:$(pwd)

CONFIGURE_TOP=.. \
CXXFLAGS="%{optflags} -std=gnu++17 $(pkg-config --cflags poppler)" \
%configure							\
	--with-banner-add="/OpenMandriva"			\
	--disable-native-texlive-build				\
	--enable-missing					\
%ifarch %{riscv} %{mips} %{power64} s390 s390x
	--disable-luajittex --disable-mfluajit			\
%endif
%if %{_texmf_enable_biber}
	--enable-biber						\
%else
	--disable-biber						\
%endif
%if %{enable_shared}
	--enable-shared						\
	--disable-static					\
%else
	--disable-shared					\
%endif
%if %{_texmf_enable_xindy}
	--enable-xindy						\
%else
	--disable-xindy						\
%endif
	--with-system-freetype2					\
	--with-freetype2-includes=%{_includedir}/freetype2	\
%if %{_texmf_with_system_dialog}
	--disable-dialog					\
%else
	--enable-dialog						\
%endif
%if %{_texmf_with_system_psutils}
	--disable-psutils					\
%else
	--enable-psutils					\
%endif
	--with-system-gd					\
	--with-system-mpfr					\
	--with-system-gmp					\
%if %{_texmf_with_system_lcdf}
	--disable-lcdf-typetools				\
%endif
%if %{_texmf_with_system_icu}
	--with-system-icu					\
%endif
	--with-system-png					\
%if %{_texmf_with_system_t1lib}
	--with-system-t1lib					\
	--disable-t1utils					\
%endif
%if %{_texmf_with_system_teckit}
	--with-system-teckit					\
	--with-teckit-includes=%{_includedir}/teckit		\
%endif
%if %{_texmf_with_system_tex4ht}
	--disable-tex4htk					\
%endif
%if %{_texmf_with_system_poppler}
	--with-system-xpdf					\
	--with-system-poppler					\
%else
	--without-system-xpdf					\
	--without-system-poppler				\
%endif
%if %{without dvik}
	--disable-xdvik						\
%else
	--enable-xdvik						\
%endif
	--disable-static					\
	--with-system-pixman					\
	--with-system-harfbuzz					\
	--with-system-cairo					\
	--with-system-libpaper					\
	--with-system-zziplib

%make_build LIBGS_LIBS="-lgs" XPDF_INCLUDES="$(pkg-config --cflags poppler) -DPOPPLER_VERSION=\\\"$(pkg-config --modversion poppler)\\\"" XPDF_LIBS="$(pkg-config --libs poppler)"
popd

%if %{_texmf_enable_asymptote}
mkdir asympote
pushd asympote
CONFIGURE_TOP=../utils/asymptote
%configure							\
	--enable-gc=system					\
	--enable-texlive-build					\
	--datadir=%{_texmfdir}
%make_build LIBGS_LIBS="-lgs"
popd
%endif

#-----------------------------------------------------------------------
%install
pushd texlive
%make_install LIBGS_LIBS="-lgs"
popd

%if %{_texmf_enable_asymptote}
pushd asymptote
%make_install LIBGS_LIBS="-lgs"
popd
%endif

mkdir -p %{buildroot}%{_datadir}
for dir in texmf texmf-dist; do
    if [ -d %{buildroot}%{_prefix}/$dir ]; then
	rm -fr %{buildroot}%{_datadir}/$dir
	mv %{buildroot}%{_prefix}/$dir %{buildroot}%{_datadir}
    fi
done

mkdir -p %{buildroot}%{_texmfvardir}
mkdir -p %{buildroot}%{_texmfconfdir}

%if %{_texmf_with_system_lcdf}
# stray directory left
rm -fr %{buildroot}%{_datadir}/lcdf-typetools-for-tex-live
%else
# openmpi has a program with the same name
if [ -f %{buildroot}%{_bindir}/otfinfo ]; then
    mv -f %{buildroot}%{_bindir}/otfinfo{,-texlive}
fi
%endif

# relocate binaries to %%{_bindir} and fix relative symlinks
pushd %{buildroot}%{_bindir}
for i in $(find . -type l); do
if [ "$(readlink $i | grep '..' | wc -l)" == "1" ]; then
l=$(readlink $i | sed s,.*/texmf,/usr/share/texmf,)
rm -f $i
if [[ -f %{buildroot}/$l && $i != "./ltx2crossrefxml" ]]; then
  cp %{buildroot}/$l $i
else
  ln -s $l $i
fi

fi
done
popd

pushd %{buildroot}%{_bindir}
    # missing symbolic links
    ln -sf aleph lamed
    ln -sf euptex uplatex
    ln -sf luatex dvilualatex
    ln -sf luatex lualatex
    ln -sf luatex dviluatex
    ln -sf pdftex amstex
    ln -sf pdftex cslatex
    ln -sf pdftex csplain
    ln -sf pdftex eplain
    ln -sf pdftex etex
    ln -sf pdftex jadetex
    ln -sf pdftex latex
    ln -sf pdftex mex
    ln -sf pdftex mltex
    ln -sf pdftex mllatex
    ln -sf pdftex pdfcslatex
    ln -sf pdftex pdfcsplain
    ln -sf pdftex pdfetex
    ln -sf pdftex pdfjadetex
    ln -sf pdftex pdflatex
    ln -sf pdftex pdfmex
    ln -sf pdftex pdfxmltex
    ln -sf pdftex utf8mex
    ln -sf pdftex texsis
    ln -sf pdftex xmltex
    ln -sf ptex platex
    ln -sf mpost mfplain
    ln -sf xetex xelatex
%if %{_texmf_enable_asymptote}
    ln -sf %{_texmfdir}/asymptote/GUI/xasy.py xasy
%endif

    # use scripts from noarch packages
    rm -f a5toa4 adhocfilelist allcm allneeded arara bib2gls biburl2doi	\
	  chkweb context convertgls2bib ctan-o-mat			\
	  ctxtools dtxgen dvi2fax dviinfox dvired fmtutil fmtutil-sys	\
	  fontinst jfmutil						\
	  kanji-config-updmap kanji-config-updmap-sys			\
	  kanji-fontmap-creator kpsewhere				\
	  l3build latexdef  latexpand ltxfileinfo			\
	  lua2dox_filter luaotfload-tool luatools mtxrun		\
	  multibibliography pfarrei ps2frag pslatex pstopdf ptex2pdf	\
	  rlxtools rubibtex rumakeindex texconfig texconfig-dialog	\
	  texconfig-sys texexec tlcockpit tlshell tpic2pdftex wordcount

    # use symlinks from noarch packages
    rm -f chklref ketcindy pamphletangler texplate			\
	  a2ping afm2afm allec arlatex authorindex autoinst bbl2bib	\
	  bibexport bibdoiadd bibmradd bibzbladd bundledoc cachepic	\
	  checkcites checklistings cjk-gs-integrate cmap2enc contextjit \
	  convbkmk diadia getmapdl pygmentex \
	  ctanify ctanupload de-macro depythontex deweb dviasm dvipdft	\
	  dosepsbin ebong e2pall epspdf epspdftk epstopdf exceltex	\
	  fig4latex findhyph font2afm fragmaster fmtutil-user		\
	  ht htcontext htlatex htmex httex httexi htxelatex htxetex	\
	  installfont-tl jamo-normalize					\
	  kanji-config-updmap-user komkindex latex2man latex-git-log	\
	  latexdiff latexdiff-vc latexfileversion latexindent latexmk	\
	  latex-papersize latexrevise latex2nemeth			\
	  lily-glyph-commands lily-image-commands lily-rebuild-pdfs	\
	  listbib listings-ext.sh ltximg lwarpmk			\
	  m-tx make4ht makedtx makeglossaries				\
	  makeglossaries-lite match_parens mathspic mf2pt1 mk4ht mkgrkindex mkjobtexmf \
	  mkluatexfontdb mkpic mkt1font mptopdf mtxrunjit musixflx 	\
	  musixtex ot2kpx pdf180 pdf270 pdf90 pdfannotextractor pdfatfi	\
	  pdfbook pdfbook2 pdfcrop pdfflip pdflatexpicscale pdfjam pdfjam-pocketmod	\
	  pdfjam-slides3up pdfjam-slides6up pdfjoin pdfnup pdfpun 	\
	  pdfthumb pdfxup pedigree perltex pfm2kpx pkfix pkfix-helper	\
	  pmxchords pn2pdf ppower4 ps2eps ps4pdf pst2pdf pmx2pdf purifyeps \
	  pythontex repstopdf rpdfcrop rubikrotation rungs srcredact showglyphs \
	  simpdftex splitindex sty2dtx svn-multi tex4ebook texcount texdef	\
	  texdiff texdirflatten texdoc texdoctk texfot texlinks		\
	  texliveonfly texloganalyser texluajit texluajitc texmfstart	\
	  texosquery texosquery-jre5 texosquery-jre8			\
	  thumbpdf tlmgr ttf2kotexfont typeoutfileinfo ulqda updmap	\
	  updmap-user							\
	  updmap-setup-kanji updmap-sys urlbst vpe vpl2ovp vpl2vpl	\
	  wofm2opl wopl2ofm wovf2ovp xhlatex yplan
popd

# use texmf data
rm -fr %{buildroot}%{_texmfdir} %{buildroot}%{_texmfdistdir}

# install manual pages and info files from noarch packages
rm -fr %{buildroot}%{_mandir} %{buildroot}%{_infodir}

# Stuff should really use upstream lua
rm -rf %{buildroot}%{_includedir}/texlua53 \
	%{buildroot}%{_includedir}/texlua52 \
	%{buildroot}%{_includedir}/texluajit \
	%{buildroot}%{_libdir}/libtexlua*.a \
	%{buildroot}%{_libdir}/libtexlua*.so \
	%{buildroot}%{_libdir}/pkgconfig/texlua*.pc

%if ! %{enable_shared}
    # do not generate dynamic libraries and do not install static ones
    rm -fr %{buildroot}%{_libdir}
    rm -fr %{buildroot}%{_includedir}
%endif
