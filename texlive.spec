%define _binary_payload			w9.gzdio
%define _source_payload			w9.gzdio

%define _texmf_enable_asymptote		0
%define _texmf_enable_biber		0
%define _texmf_enable_xindy		0
%define _texmf_with_system_dialog	1
%define _texmf_with_system_icu		1
%define _texmf_with_system_lcdf		0
%define _texmf_with_system_poppler	1
%define _texmf_with_system_psutils	1
%define _texmf_with_system_t1lib	1
%define _texmf_with_system_tex4ht	0
%define _texmf_with_system_teckit	0

%define enable_shared			1

%define historic			0

#-----------------------------------------------------------------------
Name:		texlive
Version:	20121026
Release:	4
Summary:	The TeX formatting system
Group:		Publishing
License:	http://www.tug.org/texlive/LICENSE.TL
URL:		http://tug.org/texlive/
%if %{historic}
Source0:	ftp://tug.org/historic/systems/texlive/2012/texlive-20120701-source.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/2012/texlive-20120701-source.tar.xz.sha256
%else
# svn co svn://tug.org/texlive/branches/branch2012/Build/source texlive-source
# tar Jcf texlive-20121026-source.tar.xz  --exclude .svn --transform 's/^texlive-source/texlive-20121026-source/'  texlive-source/
Source0:      texlive-20121026-source.tar.xz
# sha256sum texlive-20121026-source.tar.xz > texlive-20121026-source.tar.xz.sha256
Source1:      texlive-20121026-source.tar.xz.sha256
%endif
Source100:	%name.rpmlintrc
Obsoletes:	tetex-usrlocal < 3.0-1

#-----------------------------------------------------------------------
Requires:	ghostscript
%if %{_texmf_enable_asymptote}
Requires:	gv
Requires:	tkinter
%endif
%if %{_texmf_with_system_teckit}
Requires:	teckit
%endif

Requires:	texlive-scheme-medium texlive-scheme-xml
Requires:	texlive-collection-latexextra
Requires(post):	texlive-tlpkg
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
BuildRequires:	libpoppler-devel
%endif
BuildRequires:	xaw-devel
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

#-----------------------------------------------------------------------
Patch0:		texlive-20120810-underlink.patch
Patch1:		texlive-20120810-format.patch
Patch2:		texlive-20120810-asymptote.patch
Patch3:		texlive-20120810-xdvi.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files

%posttrans
    %{_sbindir}/texlive.post -

#-----------------------------------------------------------------------
%if %{enable_shared}
########################################################################
%define	kpathsea		%{mklibname kpathsea 6}

%package	-n %{kpathsea}
Summary:	Path searching library for TeX-related files
Group:		System/Libraries
Provides:	kpathsea = %{version}-%{release}

%description	-n %{kpathsea}
Kpathsea implements generic path searching, configuration,
and TeX-specific file searching.

%files -n %{kpathsea}
%{_libdir}/libkpathsea.so.*

#-----------------------------------------------------------------------
%define	kpathsea_devel		%{mklibname -d kpathsea}

%package	-n %{kpathsea_devel}
Summary:	Kpathsea development files
Group:		Development/C
Requires:	kpathsea = %{version}-%{release}
Provides:	kpathsea-devel = %{version}-%{release}

%description	-n %{kpathsea_devel}
Kpathsea implements generic path searching, configuration,
and TeX-specific file searching.
This package includes the kpathsea development files.

%files -n %{kpathsea_devel}
%{_includedir}/kpathsea
%{_libdir}/libkpathsea.so

#-----------------------------------------------------------------------
%define	ptexenc			%{mklibname ptexenc 1}

%package	-n %{ptexenc}
Summary:	Library for Japanese pTeX
Group:		System/Libraries
Provides:	ptexenc = %{version}-%{release}

%description	-n %{ptexenc}
ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.

%files -n %{ptexenc}
%{_libdir}/libptexenc.so.*

#-----------------------------------------------------------------------
%define	ptexenc_devel		%{mklibname -d ptexenc}

%package	-n %{ptexenc_devel}
Summary:	Library for Japanese pTeX
Group:		Development/C
Requires:	ptexenc = %{version}-%{release}
Provides:	ptexenc-devel = %{version}-%{release}

%description	-n %{ptexenc_devel}
ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.
This package includes the ptexenc development files.

%files -n %{ptexenc_devel}
%{_includedir}/ptexenc/
%{_libdir}/libptexenc.so
########################################################################
# enable_shared
%endif

#-----------------------------------------------------------------------
%package -n texlive-afm2pl.bin
Summary:	binary files of afm2pl
Conflicts:	texlive < 20110705-7

%description	-n texlive-afm2pl.bin
texlive afm2pl.bin package.

%files -n texlive-afm2pl.bin
%{_bindir}/afm2pl

#-----------------------------------------------------------------------
%package	-n texlive-aleph.bin
Summary:	binary files of aleph
Conflicts:	texlive < 20110705-7

%description	-n texlive-aleph.bin
texlive aleph.bin package.

%files -n texlive-aleph.bin
%{_bindir}/aleph
%{_bindir}/lamed

#-----------------------------------------------------------------------
%if %{_texmf_enable_biber}
%package	-n texlive-biber.bin
Summary:	binary files of biber
Conflicts:	texlive < 20110705-7

%description	-n texlive-biber.bin
texlive biber.bin package.

%files -n texlive-biber.bin
%{_bindir}/biber
%endif

#-----------------------------------------------------------------------
%package	-n texlive-bibtex.bin
Summary:	binary files of bibtex
Conflicts:	texlive < 20110705-7

%description	-n texlive-bibtex.bin
texlive bibtex.bin package.

%files -n texlive-bibtex.bin
%{_bindir}/bibtex

#-----------------------------------------------------------------------
%package	-n texlive-bibtex8.bin
Summary:	binary files of bibtex8
Conflicts:	texlive < 20110705-7

%description	-n texlive-bibtex8.bin
texlive bibtex8.bin package.

%files -n texlive-bibtex8.bin
%{_bindir}/bibtex8

#-----------------------------------------------------------------------
%package	-n texlive-bibtexu.bin
Summary:	binary files of bibtexu
Conflicts:	texlive < 20110705-7

%description	-n texlive-bibtexu.bin
texlive bibtexu.bin package.

%files -n texlive-bibtexu.bin
%{_bindir}/bibtexu

#-----------------------------------------------------------------------
%package	-n texlive-chktex.bin
Summary:	binary files of chktex
Conflicts:	texlive < 20110705-7

%description	-n texlive-chktex.bin
texlive chktex.bin package.

%files -n texlive-chktex.bin
%{_bindir}/chktex

#-----------------------------------------------------------------------
%package	-n texlive-cjkutils.bin
Summary:	binary files of cjkutils
Conflicts:	texlive < 20110705-7

%description	-n texlive-cjkutils.bin
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
%package	-n texlive-ctie.bin
Summary:	binary files of ctie
Conflicts:	texlive < 20110705-7

%description	-n texlive-ctie.bin
texlive ctie.bin package.

%files -n texlive-ctie.bin
%{_bindir}/ctie

#-----------------------------------------------------------------------
%package	-n texlive-cweb.bin
Summary:	binary files of cweb
Conflicts:	texlive < 20110705-7

%description	-n texlive-cweb.bin
texlive cweb.bin package.

%files -n texlive-cweb.bin
%{_bindir}/ctangle
%{_bindir}/cweave

#-----------------------------------------------------------------------
%package	-n texlive-detex.bin
Summary:	binary files of detex
Conflicts:	texlive < 20110705-7

%description	-n texlive-detex.bin
texlive detex.bin package.

%files -n texlive-detex.bin
%{_bindir}/detex

#-----------------------------------------------------------------------
%package	-n texlive-devnag.bin
Summary:	binary files of devnag
Conflicts:	texlive < 20110705-7

%description	-n texlive-devnag.bin
texlive devnag.bin package.

%files -n texlive-devnag.bin
%{_bindir}/devnag

#-----------------------------------------------------------------------
%package	-n texlive-dtl.bin
Summary:	binary files of dtl
Conflicts:	texlive < 20110705-7

%description	-n texlive-dtl.bin
texlive dtl.bin package.

%files -n texlive-dtl.bin
%{_bindir}/dt2dv
%{_bindir}/dv2dt

#-----------------------------------------------------------------------
%package	-n texlive-dvi2tty.bin
Summary:	binary files of dvi2tty
Conflicts:	texlive < 20110705-7

%description	-n texlive-dvi2tty.bin
texlive dvi2tty.bin package.

%files -n texlive-dvi2tty.bin
%{_bindir}/disdvi
%{_bindir}/dvi2tty

#-----------------------------------------------------------------------
%package	-n texlive-dvicopy.bin
Summary:	binary files of dvicopy
Conflicts:	texlive < 20110705-7

%description	-n texlive-dvicopy.bin
texlive dvicopy.bin package.

%files -n texlive-dvicopy.bin
%{_bindir}/dvicopy

#-----------------------------------------------------------------------
%package	-n texlive-dvidvi.bin
Summary:	binary files of dvidvi
Conflicts:	texlive < 20110705-7

%description	-n texlive-dvidvi.bin
texlive dvidvi.bin package.

%files -n texlive-dvidvi.bin
%{_bindir}/dvidvi

#-----------------------------------------------------------------------
%package	-n texlive-dviljk.bin
Summary:	binary files of dviljk
Conflicts:	texlive < 20110705-7

%description	-n texlive-dviljk.bin
texlive dviljk.bin package.

%files -n texlive-dviljk.bin
%{_bindir}/dvihp
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6

#-----------------------------------------------------------------------
%package	-n texlive-dvipdfmx.bin
Summary:	binary files of dvipdfmx
Provides:	texlive-dvipdfm.bin = %{EVRD}
Conflicts:	texlive < 20110705-7

%description	-n texlive-dvipdfmx.bin
texlive dvipdfmx.bin package.

%files -n texlive-dvipdfmx.bin
%{_bindir}/dvipdfm
%{_bindir}/dvipdfmx
%{_bindir}/ebb
%{_bindir}/extractbb

#-----------------------------------------------------------------------
%package	-n texlive-dvipng.bin
Summary:	binary files of dvipng
Conflicts:	texlive < 20110705-7

%description	-n texlive-dvipng.bin
texlive dvipng.bin package.

%files -n texlive-dvipng.bin
%{_bindir}/dvigif
%{_bindir}/dvipng

#-----------------------------------------------------------------------
%package	-n texlive-dvipos.bin
Summary:	binary files of dvipos
Conflicts:	texlive < 20110705-7

%description	-n texlive-dvipos.bin
texlive dvipos.bin package.

%files -n texlive-dvipos.bin
%{_bindir}/dvipos

#-----------------------------------------------------------------------
%package	-n texlive-dvips.bin
Summary:	binary files of dvips
Conflicts:	texlive < 20110705-7

%description	-n texlive-dvips.bin
texlive dvips.bin package.

%files -n texlive-dvips.bin
%{_bindir}/afm2tfm
%{_bindir}/dvips

#-----------------------------------------------------------------------
%package	-n texlive-dvisvgm.bin
Summary:	binary files of dvisvgm
Conflicts:	texlive < 20110705-7

%description	-n texlive-dvisvgm.bin
texlive dvisvgm.bin package.

%files -n texlive-dvisvgm.bin
%{_bindir}/dvisvgm

#-----------------------------------------------------------------------
%package	-n texlive-fontware.bin
Summary:	binary files of fontware
Conflicts:	texlive < 20110705-7

%description	-n texlive-fontware.bin
texlive fontware.bin package.

%files -n texlive-fontware.bin
%{_bindir}/pltotf
%{_bindir}/tftopl
%{_bindir}/vftovp
%{_bindir}/vptovf

#-----------------------------------------------------------------------
%package	-n texlive-gsftopk.bin
Summary:	binary files of gsftopk
Conflicts:	texlive < 20110705-7

%description	-n texlive-gsftopk.bin
texlive gsftopk.bin package.

%files -n texlive-gsftopk.bin
%{_bindir}/gsftopk

#-----------------------------------------------------------------------
%package	-n texlive-kpathsea.bin
Summary:	binary files of kpathsea
Conflicts:	texlive < 20110705-7

%description	-n texlive-kpathsea.bin
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
%package	-n texlive-lacheck.bin
Summary:	binary files of lacheck
Conflicts:	texlive < 20110705-7

%description	-n texlive-lacheck.bin
texlive lacheck.bin package.

%files -n texlive-lacheck.bin
%{_bindir}/lacheck

#-----------------------------------------------------------------------
%package	-n texlive-latex.bin
Summary:	binary files of latex
Conflicts:	texlive < 20110705-7

%description	-n texlive-latex.bin
texlive latex.bin package.

%files -n texlive-latex.bin
%{_bindir}/dvilualatex
%{_bindir}/latex
%{_bindir}/lualatex
%{_bindir}/pdflatex

#-----------------------------------------------------------------------
%package	-n texlive-lcdftypetools.bin
Summary:	binary files of lcdftypetools
Conflicts:	texlive < 20110705-7

%description	-n texlive-lcdftypetools.bin
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
%package	-n texlive-luatex.bin
Summary:	binary files of luatex
Conflicts:	texlive < 20110705-7

%description	-n texlive-luatex.bin
texlive luatex.bin package.

%files -n texlive-luatex.bin
%{_bindir}/dviluatex
%{_bindir}/luatex
%{_bindir}/texlua
%{_bindir}/texluac

#-----------------------------------------------------------------------
%package	-n texlive-m-tx.bin
Summary:	binary files of m-tx
Conflicts:	texlive < 20110705-7

%description	-n texlive-m-tx.bin
texlive m-tx.bin package.

%files -n texlive-m-tx.bin
%{_bindir}/prepmx

#-----------------------------------------------------------------------
%package	-n texlive-makeindex.bin
Summary:	binary files of makeindex
Conflicts:	texlive < 20110705-7

%description	-n texlive-makeindex.bin
texlive makeindex.bin package.

%files -n texlive-makeindex.bin
%{_bindir}/makeindex
%{_bindir}/mkindex

#-----------------------------------------------------------------------
%package	-n texlive-metafont.bin
Summary:	binary files of metafont
Conflicts:	texlive < 20110705-7

%description	-n texlive-metafont.bin
texlive metafont.bin package.

%files -n texlive-metafont.bin
%{_bindir}/inimf
%{_bindir}/mf
%{_bindir}/mf-nowin

#-----------------------------------------------------------------------
%package	-n texlive-metapost.bin
Summary:	binary files of metapost
Conflicts:	texlive < 20110705-7

%description	-n texlive-metapost.bin
texlive metapost.bin package.

%files -n texlive-metapost.bin
%{_bindir}/dvitomp
%{_bindir}/mfplain
%{_bindir}/mpost

#-----------------------------------------------------------------------
%package	-n texlive-mfware.bin
Summary:	binary files of mfware
Conflicts:	texlive < 20110705-7

%description	-n texlive-mfware.bin
texlive mfware.bin package.

%files -n texlive-mfware.bin
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/mft
%{_bindir}/pktogf
%{_bindir}/pktype

#-----------------------------------------------------------------------
%package	-n texlive-omegaware.bin
Summary:	binary files of omegaware
Conflicts:	texlive < 20110705-7

%description	-n texlive-omegaware.bin
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
%package	-n texlive-patgen.bin
Summary:	binary files of patgen
Conflicts:	texlive < 20110705-7

%description	-n texlive-patgen.bin
texlive patgen.bin package.

%files -n texlive-patgen.bin
%{_bindir}/patgen

#-----------------------------------------------------------------------
%package	-n texlive-pdftex.bin
Summary:	binary files of pdftex
Provides:	texlive-amstex.bin = %{EVRD}
Provides:	texlive-cslatex.bin = %{EVRD}
Provides:	texlive-csplain.bin = %{EVRD}
Provides:	texlive-eplain.bin = %{EVRD}
Provides:	texlive-jadetex.bin = %{EVRD}
Provides:	texlive-mex.bin = %{EVRD}
Provides:	texlive-mltex.bin = %{EVRD}
Provides:	texlive-texsis.bin = %{EVRD}
Provides:	texlive-xmltex.bin = %{EVRD}
Conflicts:	texlive < 20110705-7

%description	-n texlive-pdftex.bin
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
%{_bindir}/pdfxmltex
%{_bindir}/texsis
%{_bindir}/utf8mex
%{_bindir}/xmltex

#-----------------------------------------------------------------------
%package	-n texlive-pdftools.bin
Summary:	binary files of pdftools
Conflicts:	texlive < 20110705-7

%description	-n texlive-pdftools.bin
texlive pdftools.bin package.

%files -n texlive-pdftools.bin
%{_bindir}/pdfclose
%{_bindir}/pdfopen
%{_bindir}/pdftosrc

#-----------------------------------------------------------------------
%package	-n texlive-pmx.bin
Summary:	binary files of pmx
Conflicts:	texlive < 20110705-7

%description	-n texlive-pmx.bin
texlive m-tx.bin package.

%files -n texlive-pmx.bin
%{_bindir}/pmxab
%{_bindir}/scor2prt

#-----------------------------------------------------------------------
%package	-n texlive-ps2pkm.bin
Summary:	binary files of ps2pkm
Conflicts:	texlive < 20110705-7

%description	-n texlive-ps2pkm.bin
texlive ps2pkm.bin package.

%files -n texlive-ps2pkm.bin
%{_bindir}/mag
%{_bindir}/pfb2pfa
%{_bindir}/pk2bm
%{_bindir}/ps2pk

#-----------------------------------------------------------------------
%package	-n texlive-pstools.bin
Summary:	binary files of pstools
Conflicts:	texlive < 20110705-7

%description	-n texlive-pstools.bin
texlive pstools.bin package.

%files -n texlive-pstools.bin
%{_bindir}/bbox

#-----------------------------------------------------------------------
%package	-n texlive-ptex.bin
Summary:	binary files of ptex
Conflicts:	texlive < 20110705-7

%description	-n texlive-ptex.bin
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
%package	-n texlive-seetexk.bin
Summary:	binary files of seetexk
Conflicts:	texlive < 20110705-7

%description	-n texlive-seetexk.bin
texlive seetexk.bin package.

%files -n texlive-seetexk.bin
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dviselect
%{_bindir}/dvitodvi

#-----------------------------------------------------------------------
%package	-n texlive-synctex.bin
Summary:	binary files of synctex
Conflicts:	texlive < 20110705-7

%description	-n texlive-synctex.bin
texlive synctex.bin package.

%files -n texlive-synctex.bin
%{_bindir}/synctex

#-----------------------------------------------------------------------
%package	-n texlive-tex.bin
Summary:	binary files of tex
Conflicts:	texlive < 20110705-7

%description	-n texlive-tex.bin
texlive tex.bin package.

%files -n texlive-tex.bin
%{_bindir}/initex
%{_bindir}/tex

#-----------------------------------------------------------------------
%package	-n texlive-tex4ht.bin
Summary:	binary files of tex4ht
Conflicts:	texlive < 20110705-7

%description	-n texlive-tex4ht.bin
texlive tex4ht.bin package.

%files -n texlive-tex4ht.bin
%{_bindir}/t4ht
%{_bindir}/tex4ht

#-----------------------------------------------------------------------
%package	-n texlive-texware.bin
Summary:	binary files of texware
Conflicts:	texlive < 20110705-7

%description	-n texlive-texware.bin
texlive texware.bin package.

%files -n texlive-texware.bin
%{_bindir}/dvitype
%{_bindir}/pooltype

#-----------------------------------------------------------------------
%package	-n texlive-tie.bin
Summary:	binary files of tie
Conflicts:	texlive < 20110705-7

%description	-n texlive-tie.bin
texlive tie.bin package.

%files -n texlive-tie.bin
%{_bindir}/tie

#-----------------------------------------------------------------------
%package	-n texlive-ttfutils.bin
Summary:	binary files of ttfutils
Conflicts:	texlive < 20110705-7

%description	-n texlive-ttfutils.bin
texlive ttfutils.bin package.

%files -n texlive-ttfutils.bin
%{_bindir}/ttf2afm
%{_bindir}/ttf2pk
%{_bindir}/ttf2tfm
%{_bindir}/ttfdump

#-----------------------------------------------------------------------
%package	-n texlive-uptex.bin
Summary:	binary files of uptex
Conflicts:	texlive < 20110705-7

%description	-n texlive-uptex.bin
texlive uptex.bin package.

%files -n texlive-uptex.bin
%{_bindir}/euptex
%{_bindir}/upbibtex
%{_bindir}/updvitype
%{_bindir}/uplatex
%{_bindir}/uppltotf
%{_bindir}/uptex
%{_bindir}/uptftopl
%{_bindir}/wovp2ovf

#-----------------------------------------------------------------------
%package	-n texlive-vlna.bin
Summary:	binary files of vlna
Conflicts:	texlive < 20110705-7

%description	-n texlive-vlna.bin
texlive vlna.bin package.

%files -n texlive-vlna.bin
%{_bindir}/vlna

#-----------------------------------------------------------------------
%package	-n texlive-web.bin
Summary:	binary files of web
Conflicts:	texlive < 20110705-7

%description	-n texlive-web.bin
texlive web.bin package.

%files -n texlive-web.bin
%{_bindir}/tangle
%{_bindir}/weave

#-----------------------------------------------------------------------
%package	-n texlive-xdvi.bin
Summary:	binary files of xdvi
Conflicts:	texlive < 20110705-7

%description	-n texlive-xdvi.bin
texlive xdvi.bin package.

%files -n texlive-xdvi.bin
%{_bindir}/xdvi
%{_bindir}/xdvi-xaw

#-----------------------------------------------------------------------
%package	-n texlive-xetex.bin
Summary:	binary files of xetex
Conflicts:	texlive < 20110705-7

%description	-n texlive-xetex.bin
texlive xetex.bin package.

%files -n texlive-xetex.bin
%{_bindir}/teckit_compile
%{_bindir}/xdvipdfmx
%{_bindir}/xelatex
%{_bindir}/xetex

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
%patch1 -p1
%if %{_texmf_enable_asymptote}
%patch2 -p1
%endif
%patch3 -p1

# setup default builtin values, added to paths.h from texmf.cnf
perl -pi -e 's|^(TEXMFMAIN\s+= ).*|$1%{_texmfdir}|;'			  \
	 -e 's|^(TEXMFDIST\s+= ).*|$1%{_texmfdistdir}|;'		  \
	 -e 's|^(TEXMFLOCAL\s+= ).*|$1%{_texmflocaldir}|;'		  \
	 -e 's|^(TEXMFSYSVAR\s+= ).*|$1%{_texmfvardir}|;'		  \
	 -e 's|^(TEXMFSYSCONFIG\s+= ).*|$1%{_texmfconfdir}|;'		  \
	 -e 's|^(TEXMFHOME\s+= ).*|$1\$HOME/texmf|;'			  \
	 -e 's|^(TEXMFVAR\s+= ).*|$1\$HOME/.texlive2012/texmf-var|;'	  \
	 -e 's|^(TEXMFCONFIG\s+= ).*|$1\$HOME/.texlive2012/texmf-config|;'\
	 -e 's|^(OSFONTDIR\s+= ).*|$1%{_datadir}/fonts|;'		  \
	texk/kpathsea/texmf.cnf

#-----------------------------------------------------------------------
%build
mkdir texlive
pushd texlive
CONFIGURE_TOP=.. \
%configure2_5x							\
	--with-banner-add="/Mandriva"				\
	--disable-native-texlive-build				\
	--enable-missing					\
%if %{_texmf_enable_biber}
	--enable-biber						\
%else
	--disable-biber						\
%endif
%if %{enable_shared}
	--enable-shared						\
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
	--disable-teckit					\
	--with-teckit-includes=%{_includedir}/teckit		\
%endif
%if %{_texmf_with_system_tex4ht}
	--disable-tex4htk					\
%endif
%if %{_texmf_with_system_poppler}
	--with-system-xpdf					\
%else
	--without-system-xpdf					\
%endif
	--disable-static					\
	--with-system-zziplib
%make
popd

%if %{_texmf_enable_asymptote}
mkdir asympote
pushd asympote
CONFIGURE_TOP=../utils/asymptote
%configure2_5x							\
	--enable-gc=system					\
	--enable-texlive-build					\
	--datadir=%{_texmfdir}
%make
popd
%endif

#-----------------------------------------------------------------------
%install
pushd texlive
%makeinstall_std
popd

%if %{_texmf_enable_asymptote}
pushd asymptote
%makeinstall_std
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
    rm -f allcm allneeded chkweb context ctxtools dvi2fax dvired	\
	  fmtutil fmtutil-sys fontinst kpsewhere luatools mtxrun	\
	  ps2frag pslatex pstopdf rlxtools rubibtex rumakeindex		\
	  texconfig texconfig-dialog texconfig-sys texexec tpic2pdftex

    # use symlinks from noarch packages
    rm -f a2ping afm2afm allec arlatex authorindex autoinst bibexport	\
	  bundledoc cachepic checkcites cmap2enc convbkmk ctanify	\
	  ctanupload de-macro deweb dviasm dvipdft dosepsbin ebong	\
	  e2pall epspdf epspdftk epstopdf exceltex fig4latex findhyph	\
	  font2afm fragmaster ht htcontext htlatex htmex httex httexi	\
	  htxelatex htxetex installfont-tl latex2man latexdiff		\
	  latexdiff-vc latexfileversion latexmk latexrevise listbib	\
	  listings-ext.sh m-tx makeglossaries match_parens mathspic	\
	  mf2pt1 mk4ht mkgrkindex mkjobtexmf mkluatexfontdb mkt1font	\
	  mptopdf musixflx musixtex ot2kpx pdf180 pdf270 pdf90		\
	  pdfannotextractor pdfatfi pdfbook pdfcrop pdfflip pdfjam	\
	  pdfjam-pocketmod pdfjam-slides3up pdfjam-slides6up pdfjoin	\
	  pdfnup pdfpun pdfthumb pedigree perltex pfm2kpx pkfix		\
	  pkfix-helper ppower4 ps2eps ps4pdf pst2pdf pmx2pdf purifyeps	\
	  repstopdf rpdfcrop rungs showglyphs simpdftex splitindex	\
	  sty2dtx svn-multi texcount texdef texdiff texdirflatten	\
	  texdoc texdoctk texlinks texliveonfly texloganalyser		\
	  texmfstart thumbpdf tlmgr typeoutfileinfo ulqda updmap	\
	  updmap-setup-kanji updmap-sys urlbst vpe vpl2ovp vpl2vpl
popd

# use texmf data
rm -fr %{buildroot}%{_texmfdir} %{buildroot}%{_texmfdistdir}

# install manual pages and info files from noarch packages
rm -fr %{buildroot}%{_mandir} %{buildroot}%{_infodir}

%if !%{enable_shared}
    # do not generate dynamic libraries and do not install static ones
    rm -fr %{buildroot}%{_libdir}
    rm -fr %{buildroot}%{_includedir}
%endif


%changelog
* Fri Aug 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120810-2
+ Revision: 815205
- Bump release and rebuild as some packages were uploaded only to i586.

* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120810-1
+ Revision: 813897
- Update to TeX Live 2012
- Disable build of texlive-biber.bin by default.

  + Bernhard Rosenkraenzer <bero@bero.eu>
    - Re-enable building with system poppler
    - Rebuild for icu 49.1

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - removed {libkpathsea,libptexenc}.la

* Tue Feb 14 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120214-1
+ Revision: 773911
- Update to more recent checkout of bug fixes texlive branch2011.
- Add patch to correct xetex problem with zlib 1.2.6.

* Mon Jan 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120113-1
+ Revision: 761749
- Update to bug fixes texlive branch2011.
- Use system libicu.
- Drop patch already in branch2011 and rediff others.

* Mon Dec 05 2011 Zé <ze@mandriva.org> 20110705-11
+ Revision: 737796
- clean defattr and BR
- rpm isnt able to handle = in conflicts

* Fri Dec 02 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-10
+ Revision: 737277
- Add posttrans logic to block waiting for texlive.post to finish.

* Thu Nov 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-9
+ Revision: 731256
- Add implicit requires of texlive-collection-latexextra

* Mon Nov 14 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-8
+ Revision: 730630
- Merge latex-bin and latex packages.

* Tue Nov 08 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-7
+ Revision: 729180
- Remove unused and duplicated files and patches.
- Redefine some rpm macros to be able to detect texlive-tlpkg build requires.
- Correct pstools.bin to not include scripts provided by pstools
- Update for new texlive texmf packages.
- Temporarily revert to monolithic texlive packages

* Fri Oct 28 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-6.3
+ Revision: 707731
- Update micro release to match texlive-texmf.

* Thu Oct 27 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-6.2
+ Revision: 707592
- Add mktexlsr.post helper script to keep instalation always consistent.

* Thu Oct 27 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-6.1
+ Revision: 707496
- Experimental rework to map TeX Live packages as rpm packages

* Sun Oct 02 2011 Oden Eriksson <oeriksson@mandriva.com> 20110705-6
+ Revision: 702455
- attempt to relink against libpng15.so.15

* Wed Aug 24 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-5
+ Revision: 696528
- Change default user dir to .texlive2011 to match texlive version
- Run "mtxrun --generate" to correct context (thanks to Mojca Miklavec)

* Tue Aug 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-4
+ Revision: 693789
- Correct wrong texlive-texmf conflicts.

* Sat Aug 06 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-3
+ Revision: 693390
- Add extra conflicts with older texlive-texmf for easier upgrade

* Sun Jul 24 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-2
+ Revision: 691468
- Require texlive-texmf version matching texlive one
- Run "updmap-sys --syncwithtrees" to ensure cfg files math installed files

* Fri Jul 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110705-1
+ Revision: 690910
- Update to texlive 2011

* Wed Jun 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110312-5
+ Revision: 686606
- Avoid conflict with the vlna package
  CCBUG: 63171

* Thu May 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110312-4
+ Revision: 668841
- Provides kpathsea libs for evince (qa.mandriva.com #63192)

* Tue May 03 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110312-3
+ Revision: 664189
- Rebuild with new poppler
- Disable xindy and asymptote build by default
- Rebuild with gcc 4.6.0 and redirect scriptlets to /dev/null
- Redirect posttrans output to /dev/null - only print messages sent to stderr

* Sun Mar 13 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110312-1
+ Revision: 644407
- Update to use texlive svn checkout dated 20110312

* Sat Mar 12 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-15
+ Revision: 643994
- Rebuild again now that it can build requires itself, after rebuild for poppler

* Sat Mar 12 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-14
+ Revision: 643974
- Rebuild with new poppler

* Thu Mar 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-13
+ Revision: 643248
- Add provides/obsoletes to ps2eps
  CCBUG: 62747

* Mon Mar 07 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-12
+ Revision: 642404
- Correct remaining broken symbolic links
- Add tkinter to requires when enabling asymptote
- Build with system poppler
- Enable back build of asymptote and xindy
- Correct broken symbolic links

* Fri Mar 04 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-10
+ Revision: 641869
- Change license tag to point to license file
- Add basic infrastructure to allow test installs with tetex
  on older distro releases
- Add gv as requires (default ps viewer for asymptote)

* Sat Feb 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-9
+ Revision: 640010
- Correct tex4ht provides/obsoletes
- Correct xasy symlink

* Thu Feb 24 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-8
+ Revision: 639733
- Enable asymptote and xindy build

* Sat Feb 19 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-7
+ Revision: 638745
- Setup proper default values for kpathsea
- Enable asymptote and xindy build
- Move scriptlet from post to postrans

* Thu Feb 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-5
+ Revision: 638288
- Remove dependency loop of texlive and texlive-texmf

* Thu Feb 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-4
+ Revision: 638246
- Rebuild with proper post and updated Provides/Requires

* Tue Feb 15 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-3
+ Revision: 637825
- Correct build for asymptote and xindy, but still disabled
- Correct post that was passing incorrect arguments to mktexlsr

* Mon Feb 14 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-2
+ Revision: 637731
+ rebuild (emptylog)

* Mon Feb 14 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100722-1
+ Revision: 637669
- Update to texlive 20100722

* Tue Feb 01 2011 Paulo Andrade <pcpa@mandriva.com.br> 2007-22
+ Revision: 634608
- Update to match the fedora texlive package

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages
    - sync security patches with fedora

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild for new poppler

* Wed Feb 17 2010 Lev Givon <lev@mandriva.org> 0:2007-21.r6295.8mdv2010.1
+ Revision: 507127
- Fix compilation issue reported in Ubuntu bug #438031.
- Cron job in texlive-fonts requires tmpwatch (#48739).

* Thu Jul 16 2009 Eugeni Dodonov <eugeni@mandriva.com> 0:2007-21.r6295.7mdv2010.0
+ Revision: 396656
- Added patch to fix conflict with glibc getline().
  Rebuild for new poppler.

* Wed May 20 2009 Götz Waschk <waschk@mandriva.org> 0:2007-20.r6295.7mdv2010.0
+ Revision: 378035
- really fix bug #51077

* Wed May 20 2009 Götz Waschk <waschk@mandriva.org> 0:2007-20.r6295.6mdv2010.0
+ Revision: 377976
- fix wrong deps of xdvi (bug #51077)

* Tue May 19 2009 Götz Waschk <waschk@mandriva.org> 0:2007-20.r6295.5mdv2010.0
+ Revision: 377705
- fix build with gcc 4.4
- fix build with new poppler

  + Paulo Andrade <pcpa@mandriva.com.br>
    - o Correct a typo xdvv -> xdvi
      o Make texlive-xdvi provide xdvi
      o Make texlive-xdvi require missing font packages
      o This should correct #48029 (texlive-xdvi should Provides: xdvi), and
      to some extent, help in #38016 (texlive misses some fonts for xdvi)

* Thu Feb 12 2009 Rafael da Veiga Cabral <cabral@mandriva.com> 0:2007-20.r6295.3mdv2009.1
+ Revision: 339794
- added build fix patches:
     texlive-2007-buildfix2009.1.patch
     texlive-2007-buildfix2009.1-2.patch
     texlive-2007-buildfix2009.1-3.patch
  some of hunks are in disabled patches for further rediff
- disabled patches:
    texlive-fix_epstopdf_invocation.patch
    texlive-builtin-searchpath-fix.patch
    texlive-pdftex.patch
    texlive-source-t1lib.patch
- rediff texlive-libpoppler_new.patch
- including libpng as build require

  + Colin Guthrie <cguthrie@mandriva.org>
    - Fix the release
    - Rebuild against new libxcb

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 01 2008 Funda Wang <fwang@mandriva.org> 0:2007-20.r6295.3mdv2009.0
+ Revision: 199843
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long

* Sat Jan 19 2008 David Walluck <walluck@mandriva.org> 0:2007-20.r6295.2mdv2008.1
+ Revision: 155147
- Provides should not depend on status of obsolete_tetex option
- SVN r6295 (fixes build)
- keep source directory when creating tarball

  + Anssi Hannula <anssi@mandriva.org>
    - do not provide jadetex+xmltex when not obsoleting them

* Thu Jan 17 2008 Thierry Vignaud <tv@mandriva.org> 0:2007-20.r6225mdv2008.1
+ Revision: 154135
- stop providing/obsoleting tetex (too much issues)

  + Anssi Hannula <anssi@mandriva.org>
    - fix conflicts when built with obsolete_tetex=0 (not default)

* Mon Jan 14 2008 David Walluck <walluck@mandriva.org> 0:2007-19.r6225mdv2008.1
+ Revision: 151174
- fix  E: description-line-too-long
- comment out %%{_texmf_main}/web2c/xetex.pool, %%{_bindir}/platex, and %%{_bindir}/pdfplatex from file list
- use standard menu category for xdvi
- SVN r6225
- rediff and modify texlive-libpoppler_new.patch
- rediff texlive-Build_script.patch
- remove texlive-source-CVE-2007-0650.patch (applied upstream)
- remove texlive-2007-copyright-utf8-man.patch (no longer needed)
- modify texlive-build.patch
- add texlive-no-lzma.patch (avoid building lzma which is already in the distro)
- modify texlive-warns.patch
- this release adds mkjobtexmf, texcount, and tpic2pdftex

* Fri Jan 11 2008 Anssi Hannula <anssi@mandriva.org> 0:2007-19mdv2008.1
+ Revision: 147946
- restore lots of requires (it seems that someone had wrongly assumed
  that "requires" is a subset of "requires(post)" and replaced a lot of
  requires with requires(post); I restored them, but did not remove
  the added requires(post), even while some of them seem like they are
  superfluous)
- texlive-mfwin conflicts with old tetex
- versionize obsoletes and provides to avoid conflicts with other
  texlive packages

* Thu Jan 10 2008 Thierry Vignaud <tv@mandriva.org> 0:2007-18mdv2008.1
+ Revision: 147646
- make texlive-fonts conflict with tetex

* Thu Jan 10 2008 David Walluck <walluck@mandriva.org> 0:2007-17mdv2008.1
+ Revision: 147471
- change Requires to Requires(post) for scriptlets

* Wed Jan 09 2008 Thierry Vignaud <tv@mandriva.org> 0:2007-16mdv2008.1
+ Revision: 147226
- conflict with old tetex-doc (#36582)
- fix xdvi not working (#35288)
- fix descriptions (texlive-doc doesn't exists)
- texlive-xdvi conflicts with xdvi (#35288)

* Tue Jan 08 2008 Thierry Vignaud <tv@mandriva.org> 0:2007-15mdv2008.1
+ Revision: 146441
- really enable obsoloting/provides tetex

* Fri Jan 04 2008 Thierry Vignaud <tv@mandriva.org> 0:2007-14mdv2008.1
+ Revision: 145501
- enable obsoloting/provides tetex
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Sep 04 2007 David Walluck <walluck@mandriva.org> 0:2007-13mdv2008.0
+ Revision: 79575
- rebuild
- fix Icon entry in xdvi.desktop

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sat Aug 25 2007 David Walluck <walluck@mandriva.org> 0:2007-12mdv2008.0
+ Revision: 71099
- add some Requires

* Sat Aug 25 2007 David Walluck <walluck@mandriva.org> 0:2007-11mdv2008.0
+ Revision: 71098
- split out jadetex and xmltex packages

* Thu Aug 16 2007 David Walluck <walluck@mandriva.org> 0:2007-10mdv2008.0
+ Revision: 64085
- rebuild

* Wed Aug 15 2007 David Walluck <walluck@mandriva.org> 0:2007-9mdv2008.0
+ Revision: 63853
- fix conflict with context subpackage

  + Thierry Vignaud <tv@mandriva.org>
    - move out of descriptions stuff that do not actually describe these packages

* Sun Aug 12 2007 David Walluck <walluck@mandriva.org> 0:2007-8mdv2008.0
+ Revision: 62221
- remove file Requires

* Sat Aug 11 2007 David Walluck <walluck@mandriva.org> 0:2007-7mdv2008.0
+ Revision: 61921
- version tetex provide

* Sat Aug 11 2007 David Walluck <walluck@mandriva.org> 0:2007-6mdv2008.0
+ Revision: 61915
- safer calls in scriptlets

* Sat Aug 11 2007 David Walluck <walluck@mandriva.org> 0:2007-5mdv2008.0
+ Revision: 61864
- Xaw3d-devel is incorrectly named
- BuildRequires: xaw3d-devel
- BuildRequires: xaw-devel, not Xaw3d-devel
- fix %%bcond_with option
- fix %%with syntax
- update svn instructions
- don't obsolete tetex by default
- stricter version requirements on subpackages
- remove some library provides
- don't exclude .pool files
- exclude .pool files already shipped in texlive-texmf
- update to latest SVN for pdftex 1.40.5 support
- remove Fedora tkdep patch (we hopefully require perl-Tk from main automatically)
- remove Fedora kpse extensions patch (capital letters are bugs in themselves)
- remove dvips_fontbug_fix_upstream and fix_makempx_installation patches (merged upstream)
- rediff some Debian patches
- libpoppler_new patch disables pdftosrc
- fix pdftex patch
- add libpoppler_new patch
- installation fixes
- Import texlive

