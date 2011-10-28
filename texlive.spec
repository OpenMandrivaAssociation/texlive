
# warning: automatically generated file by texlive-texmf/SOURCES/texlive.pl

%define _binary_payload		w9.gzdio
%define _source_payload		w9.gzdio

%define _requires_exceptions	perl(Text::Unidecode)\\|perl(Tie::Watch)\\|perl(SelfLoader)\\|/usr/local/bin/fontforge

%define enable_asymptote	0
%define enable_xindy		0

%define with_system_dialog	1
%define with_system_lcdf	0
%define with_system_poppler	0
%define with_system_psutils	1
%define with_system_t1lib	1
%define with_system_tex4ht	0
%define with_system_teckit	0

%define enable_shared		1

%define texmfdir		%{_datadir}/texmf
%define texmfdistdir		%{_datadir}/texmf-dist
%define texmflocaldir		%{_datadir}/texmf-local
%define texmfextradir		%{_datadir}/texmf-extra
%define texmffontsdir		%{_datadir}/texmf-fonts
%define texmfprojectdir		%{_datadir}/texmf-project
%define texmfvardir		%{_localstatedir}/lib/texmf
%define texmfconfdir		%{_sysconfdir}/texmf


#-----------------------------------------------------------------------
Name:		texlive
Version:	20110705
Release:	6.3
Summary:	The TeX formatting system
Group:		Publishing
License:	http://www.tug.org/texlive/LICENSE.TL
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/2011/texlive-20110705-source.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/2011/texlive-20110705-source.tar.xz.sha256
Source2:	mktexlsr.post
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Obsoletes:	tetex-usrlocal <= 3.0

#-----------------------------------------------------------------------
%if %{with_system_dialog}
Requires:	cdialog
%endif
Requires:	ghostscript
%if %{enable_asymptote}
Requires:	gv
Requires:	tkinter
%endif
%if %{with_system_teckit}
Requires:	teckit
%endif

Conflicts:	texlive-fonts <= 2007, texlive-texmf-fonts <= 2007
Conflicts:	tetex-xdvi <= 3.0, texlive-xdvi <= 2007, xdvik <= 22.84.16
Conflicts:	ps2eps <= 1.64
Conflicts:	jadetex <= 3.12, texlive-jadetex <= 2007, texlive-texmf-jadetex <= 2007
Conflicts:	dvi2tty <= 5.3.1
Conflicts:	tex4ht <= 1:1.0.2008_02_28_2058
Conflicts:	tetex-latex <= 3.0, texlive-latex <= 2007, texlive-texmf-latex <= 2007
Conflicts:	tetex <= 3.0
Conflicts:	tetex-cmsuper <= 0.3.3, texlive-texmf-cmsuper <= 2007
Conflicts:	texlive-contex <= 2007, texlive-texmf-contex <= 2007
Conflicts:	tetex-afm <= 3.0, texlive-afm <= 2007, texlive-texmf-afm <= 2007
Conflicts:	kpathsea-devel <= 20100722, kpathsea-static-devel <= 20100722
Conflicts:	tetex-dvipdfm <= 3.0, texlive-dvipdfm <= 2007, texlive-texmf-dvipdfm <= 2007
Conflicts:	texlive-xmltex <= 2007, texlive-texmf-xmltex <= 2007, xmltex <= 1:3.0
Conflicts:	tetex-dvips <= 3.0, texlive-dvips <= 2007, texlive-texmf-dvips <= 2007
Conflicts:	tetex-dvilj <= 3.0, texlive-dvilj <= 2007
Conflicts:	vlna <= 1.4
Conflicts:	tetex-mfwin <= 3.0, texlive-mfwin <= 2007
Conflicts:	texlive-fontsextra < %{version}-3.3
Conflicts:	texlive-dviutils <= 2007
Conflicts:	pdfjam <= 1.21
Conflicts:	latexdiff <= 0.5

Conflicts:	texlive <= 20110705-6
Conflicts:	texlive-texmf < %{version}
Requires(post):	texlive-texmf = %{version}
Requires(post):	texlive-kpathsea.bin = %{version}-6.3

#-----------------------------------------------------------------------
BuildRequires:	bison
%if %{enable_xindy}
BuildRequires:	clisp
BuildRequires:	ffcall-devel
%endif
%if %{enable_asymptote}
BuildRequires:	fftw-devel
BuildRequires:	flex
%endif
BuildRequires:	freetype-devel
BuildRequires:	fontconfig-devel
%if %{enable_asymptote}
BuildRequires:	libgc-devel
BuildRequires:	libsigsegv-devel
BuildRequires:	ghostscript-dvipdf
BuildRequires:	gsl-devel
BuildRequires:	GL-devel
%endif
BuildRequires:	libgd-devel
%if %{with_system_poppler}
BuildRequires:	libpoppler-devel
%endif
BuildRequires:	libxaw-devel
%if !%{with_system_dialog}
BuildRequires:	ncurses-devel
%endif
BuildRequires:	png-devel
%if %{with_system_t1lib}
BuildRequires:	t1lib-devel
%endif
%if %{with_system_teckit}
BuildRequires:	teckit-devel
%endif
%if %{enable_xindy}
BuildRequires:	texlive
%endif
%if %{enable_asymptote}
BuildRequires:	texinfo
%endif
BuildRequires:	zziplib-devel

#-----------------------------------------------------------------------
Patch0:		texlive-20110312-underlink.patch
Patch1:		texlive-20110312-format.patch
Patch2:		texlive-20110312-asymptote.patch
Patch3:		texlive-20110312-xdvi.patch
# http://tug.org/svn/texlive?view=revision&revision=23644
Patch4:		texlive-20110705-synctex-coordinates.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files

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

%files		-n %{kpathsea}
%defattr(-,root,root,-)
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

%files		-n %{kpathsea_devel}
%defattr(-,root,root,-)
%{_includedir}/kpathsea
%{_libdir}/libkpathsea.la
%{_libdir}/libkpathsea.so

#-----------------------------------------------------------------------
%define	kpathsea_static_devel	%{mklibname -d -s kpathsea}

%package	-n %{kpathsea_static_devel}
Summary:	Kpathsea development files
Group:		Development/C
Requires:	kpathsea-devel = %{version}-%{release}
Provides:	kpathsea-devel-static = %{version}-%{release}

%description	-n %{kpathsea_static_devel}
Kpathsea implements generic path searching, configuration,
and TeX-specific file searching.
This package includes the static kpathsea library.

%files		-n %{kpathsea_static_devel}
%defattr(-,root,root,-)
%{_libdir}/libkpathsea.a

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

%files		-n %{ptexenc}
%defattr(-,root,root,-)
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

%files		-n %{ptexenc_devel}
%defattr(-,root,root,-)
%{_includedir}/ptexenc
%{_libdir}/libptexenc.la
%{_libdir}/libptexenc.so

#-----------------------------------------------------------------------
%define	ptexenc_static_devel	%{mklibname -d -s ptexenc}

%package	-n %{ptexenc_static_devel}
Summary:	Library for Japanese pTeX
Group:		Development/C
Requires:	ptexenc-devel = %{version}-%{release}
Provides:	ptexenc-devel-static = %{version}-%{release}

%description	-n %{ptexenc_static_devel}
ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.
This package includes the static ptexenc library.

%files		-n %{ptexenc_static_devel}
%defattr(-,root,root,-)
%{_libdir}/libptexenc.a

########################################################################
# enable_shared
%endif

#-----------------------------------------------------------------------
%package	-n texlive-a2ping.bin
Summary:	binary files of a2ping
Conflicts:	texlive <= 20110705-6

%description	-n texlive-a2ping.bin
texlive a2ping.bin package.

%files		-n texlive-a2ping.bin
%{_bindir}/a2ping

#-----------------------------------------------------------------------
%package	-n texlive-accfonts.bin
Summary:	binary files of accfonts
Conflicts:	texlive <= 20110705-6

%description	-n texlive-accfonts.bin
texlive accfonts.bin package.

%files		-n texlive-accfonts.bin
%{_bindir}/mkt1font
%{_bindir}/vpl2ovp
%{_bindir}/vpl2vpl

#-----------------------------------------------------------------------
%package	-n texlive-afm2pl.bin
Summary:	binary files of afm2pl
Conflicts:	texlive <= 20110705-6

%description	-n texlive-afm2pl.bin
texlive afm2pl.bin package.

%files		-n texlive-afm2pl.bin
%{_bindir}/afm2pl

#-----------------------------------------------------------------------
%package	-n texlive-aleph.bin
Summary:	binary files of aleph
Conflicts:	texlive <= 20110705-6

%description	-n texlive-aleph.bin
texlive aleph.bin package.

%files		-n texlive-aleph.bin
%{_bindir}/aleph
%{_bindir}/lamed

#-----------------------------------------------------------------------
%package	-n texlive-amstex.bin
Summary:	binary files of amstex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-amstex.bin
texlive amstex.bin package.

%files		-n texlive-amstex.bin
%{_bindir}/amstex

#-----------------------------------------------------------------------
%package	-n texlive-authorindex.bin
Summary:	binary files of authorindex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-authorindex.bin
texlive authorindex.bin package.

%files		-n texlive-authorindex.bin
%{_bindir}/authorindex

#-----------------------------------------------------------------------
%package	-n texlive-biber.bin
Summary:	binary files of biber
Conflicts:	texlive <= 20110705-6

%description	-n texlive-biber.bin
texlive biber.bin package.

%files		-n texlive-biber.bin
%{_bindir}/biber

#-----------------------------------------------------------------------
%package	-n texlive-bibexport.bin
Summary:	binary files of bibexport
Conflicts:	texlive <= 20110705-6

%description	-n texlive-bibexport.bin
texlive bibexport.bin package.

%files		-n texlive-bibexport.bin
%{_bindir}/bibexport

#-----------------------------------------------------------------------
%package	-n texlive-bibtex.bin
Summary:	binary files of bibtex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-bibtex.bin
texlive bibtex.bin package.

%files		-n texlive-bibtex.bin
%{_bindir}/bibtex

#-----------------------------------------------------------------------
%package	-n texlive-bibtex8.bin
Summary:	binary files of bibtex8
Conflicts:	texlive <= 20110705-6

%description	-n texlive-bibtex8.bin
texlive bibtex8.bin package.

%files		-n texlive-bibtex8.bin
%{_bindir}/bibtex8

#-----------------------------------------------------------------------
%package	-n texlive-bibtexu.bin
Summary:	binary files of bibtexu
Conflicts:	texlive <= 20110705-6

%description	-n texlive-bibtexu.bin
texlive bibtexu.bin package.

%files		-n texlive-bibtexu.bin
%{_bindir}/bibtexu

#-----------------------------------------------------------------------
%package	-n texlive-bundledoc.bin
Summary:	binary files of bundledoc
Conflicts:	texlive <= 20110705-6

%description	-n texlive-bundledoc.bin
texlive bundledoc.bin package.

%files		-n texlive-bundledoc.bin
%{_bindir}/arlatex
%{_bindir}/bundledoc

#-----------------------------------------------------------------------
%package	-n texlive-cachepic.bin
Summary:	binary files of cachepic
Conflicts:	texlive <= 20110705-6

%description	-n texlive-cachepic.bin
texlive cachepic.bin package.

%files		-n texlive-cachepic.bin
%{_bindir}/cachepic

#-----------------------------------------------------------------------
%package	-n texlive-chktex.bin
Summary:	binary files of chktex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-chktex.bin
texlive chktex.bin package.

%files		-n texlive-chktex.bin
%{_bindir}/chktex
%{_bindir}/chkweb
%{_bindir}/deweb

#-----------------------------------------------------------------------
%package	-n texlive-cjkutils.bin
Summary:	binary files of cjkutils
Conflicts:	texlive <= 20110705-6

%description	-n texlive-cjkutils.bin
texlive cjkutils.bin package.

%files		-n texlive-cjkutils.bin
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
%package	-n texlive-context.bin
Summary:	binary files of context
Conflicts:	texlive <= 20110705-6

%description	-n texlive-context.bin
texlive context.bin package.

%files		-n texlive-context.bin
%{_bindir}/context
%{_bindir}/ctxtools
%{_bindir}/luatools
%{_bindir}/mtxrun
%{_bindir}/pstopdf
%{_bindir}/rlxtools
%{_bindir}/texexec
%{_bindir}/texmfstart

#-----------------------------------------------------------------------
%package	-n texlive-cslatex.bin
Summary:	binary files of cslatex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-cslatex.bin
texlive cslatex.bin package.

%files		-n texlive-cslatex.bin
%{_bindir}/cslatex
%{_bindir}/pdfcslatex

#-----------------------------------------------------------------------
%package	-n texlive-csplain.bin
Summary:	binary files of csplain
Conflicts:	texlive <= 20110705-6

%description	-n texlive-csplain.bin
texlive csplain.bin package.

%files		-n texlive-csplain.bin
%{_bindir}/csplain
%{_bindir}/pdfcsplain

#-----------------------------------------------------------------------
%package	-n texlive-ctie.bin
Summary:	binary files of ctie
Conflicts:	texlive <= 20110705-6

%description	-n texlive-ctie.bin
texlive ctie.bin package.

%files		-n texlive-ctie.bin
%{_bindir}/ctie

#-----------------------------------------------------------------------
%package	-n texlive-cweb.bin
Summary:	binary files of cweb
Conflicts:	texlive <= 20110705-6

%description	-n texlive-cweb.bin
texlive cweb.bin package.

%files		-n texlive-cweb.bin
%{_bindir}/ctangle
%{_bindir}/cweave

#-----------------------------------------------------------------------
%package	-n texlive-cyrillic-bin.bin
Summary:	binary files of cyrillic-bin
Conflicts:	texlive <= 20110705-6

%description	-n texlive-cyrillic-bin.bin
texlive cyrillic-bin.bin package.

%files		-n texlive-cyrillic-bin.bin
%{_bindir}/rubibtex
%{_bindir}/rumakeindex

#-----------------------------------------------------------------------
%package	-n texlive-de-macro.bin
Summary:	binary files of de-macro
Conflicts:	texlive <= 20110705-6

%description	-n texlive-de-macro.bin
texlive de-macro.bin package.

%files		-n texlive-de-macro.bin
%{_bindir}/de-macro

#-----------------------------------------------------------------------
%package	-n texlive-detex.bin
Summary:	binary files of detex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-detex.bin
texlive detex.bin package.

%files		-n texlive-detex.bin
%{_bindir}/detex

#-----------------------------------------------------------------------
%package	-n texlive-devnag.bin
Summary:	binary files of devnag
Conflicts:	texlive <= 20110705-6

%description	-n texlive-devnag.bin
texlive devnag.bin package.

%files		-n texlive-devnag.bin
%{_bindir}/devnag

#-----------------------------------------------------------------------
%package	-n texlive-dtl.bin
Summary:	binary files of dtl
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dtl.bin
texlive dtl.bin package.

%files		-n texlive-dtl.bin
%{_bindir}/dt2dv
%{_bindir}/dv2dt

#-----------------------------------------------------------------------
%package	-n texlive-dvi2tty.bin
Summary:	binary files of dvi2tty
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dvi2tty.bin
texlive dvi2tty.bin package.

%files		-n texlive-dvi2tty.bin
%{_bindir}/disdvi
%{_bindir}/dvi2tty

#-----------------------------------------------------------------------
%package	-n texlive-dviasm.bin
Summary:	binary files of dviasm
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dviasm.bin
texlive dviasm.bin package.

%files		-n texlive-dviasm.bin
%{_bindir}/dviasm

#-----------------------------------------------------------------------
%package	-n texlive-dvicopy.bin
Summary:	binary files of dvicopy
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dvicopy.bin
texlive dvicopy.bin package.

%files		-n texlive-dvicopy.bin
%{_bindir}/dvicopy

#-----------------------------------------------------------------------
%package	-n texlive-dvidvi.bin
Summary:	binary files of dvidvi
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dvidvi.bin
texlive dvidvi.bin package.

%files		-n texlive-dvidvi.bin
%{_bindir}/dvidvi

#-----------------------------------------------------------------------
%package	-n texlive-dviljk.bin
Summary:	binary files of dviljk
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dviljk.bin
texlive dviljk.bin package.

%files		-n texlive-dviljk.bin
%{_bindir}/dvihp
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6

#-----------------------------------------------------------------------
%package	-n texlive-dvipdfm.bin
Summary:	binary files of dvipdfm
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dvipdfm.bin
texlive dvipdfm.bin package.

%files		-n texlive-dvipdfm.bin
%{_bindir}/dvipdfm
%{_bindir}/dvipdft

#-----------------------------------------------------------------------
%package	-n texlive-dvipdfmx.bin
Summary:	binary files of dvipdfmx
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dvipdfmx.bin
texlive dvipdfmx.bin package.

%files		-n texlive-dvipdfmx.bin
%{_bindir}/dvipdfmx
%{_bindir}/ebb
%{_bindir}/extractbb

#-----------------------------------------------------------------------
%package	-n texlive-dvipng.bin
Summary:	binary files of dvipng
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dvipng.bin
texlive dvipng.bin package.

%files		-n texlive-dvipng.bin
%{_bindir}/dvigif
%{_bindir}/dvipng

#-----------------------------------------------------------------------
%package	-n texlive-dvipos.bin
Summary:	binary files of dvipos
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dvipos.bin
texlive dvipos.bin package.

%files		-n texlive-dvipos.bin
%{_bindir}/dvipos

#-----------------------------------------------------------------------
%package	-n texlive-dvips.bin
Summary:	binary files of dvips
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dvips.bin
texlive dvips.bin package.

%files		-n texlive-dvips.bin
%{_bindir}/afm2tfm
%{_bindir}/dvips

#-----------------------------------------------------------------------
%package	-n texlive-dvisvgm.bin
Summary:	binary files of dvisvgm
Conflicts:	texlive <= 20110705-6

%description	-n texlive-dvisvgm.bin
texlive dvisvgm.bin package.

%files		-n texlive-dvisvgm.bin
%{_bindir}/dvisvgm

#-----------------------------------------------------------------------
%package	-n texlive-ebong.bin
Summary:	binary files of ebong
Conflicts:	texlive <= 20110705-6

%description	-n texlive-ebong.bin
texlive ebong.bin package.

%files		-n texlive-ebong.bin
%{_bindir}/ebong

#-----------------------------------------------------------------------
%package	-n texlive-eplain.bin
Summary:	binary files of eplain
Conflicts:	texlive <= 20110705-6

%description	-n texlive-eplain.bin
texlive eplain.bin package.

%files		-n texlive-eplain.bin
%{_bindir}/eplain

#-----------------------------------------------------------------------
%package	-n texlive-epspdf.bin
Summary:	binary files of epspdf
Conflicts:	texlive <= 20110705-6

%description	-n texlive-epspdf.bin
texlive epspdf.bin package.

%files		-n texlive-epspdf.bin
%{_bindir}/epspdf
%{_bindir}/epspdftk

#-----------------------------------------------------------------------
%package	-n texlive-epstopdf.bin
Summary:	binary files of epstopdf
Conflicts:	texlive <= 20110705-6

%description	-n texlive-epstopdf.bin
texlive epstopdf.bin package.

%files		-n texlive-epstopdf.bin
%{_bindir}/epstopdf
%{_bindir}/repstopdf

#-----------------------------------------------------------------------
%package	-n texlive-fig4latex.bin
Summary:	binary files of fig4latex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-fig4latex.bin
texlive fig4latex.bin package.

%files		-n texlive-fig4latex.bin
%{_bindir}/fig4latex

#-----------------------------------------------------------------------
%package	-n texlive-findhyph.bin
Summary:	binary files of findhyph
Conflicts:	texlive <= 20110705-6

%description	-n texlive-findhyph.bin
texlive findhyph.bin package.

%files		-n texlive-findhyph.bin
%{_bindir}/findhyph

#-----------------------------------------------------------------------
%package	-n texlive-fontinst.bin
Summary:	binary files of fontinst
Conflicts:	texlive <= 20110705-6

%description	-n texlive-fontinst.bin
texlive fontinst.bin package.

%files		-n texlive-fontinst.bin
%{_bindir}/fontinst

#-----------------------------------------------------------------------
%package	-n texlive-fontools.bin
Summary:	binary files of fontools
Conflicts:	texlive <= 20110705-6

%description	-n texlive-fontools.bin
texlive fontools.bin package.

%files		-n texlive-fontools.bin
%{_bindir}/afm2afm
%{_bindir}/autoinst
%{_bindir}/cmap2enc
%{_bindir}/font2afm
%{_bindir}/ot2kpx
%{_bindir}/pfm2kpx
%{_bindir}/showglyphs

#-----------------------------------------------------------------------
%package	-n texlive-fontware.bin
Summary:	binary files of fontware
Conflicts:	texlive <= 20110705-6

%description	-n texlive-fontware.bin
texlive fontware.bin package.

%files		-n texlive-fontware.bin
%{_bindir}/pltotf
%{_bindir}/tftopl
%{_bindir}/vftovp
%{_bindir}/vptovf

#-----------------------------------------------------------------------
%package	-n texlive-fragmaster.bin
Summary:	binary files of fragmaster
Conflicts:	texlive <= 20110705-6

%description	-n texlive-fragmaster.bin
texlive fragmaster.bin package.

%files		-n texlive-fragmaster.bin
%{_bindir}/fragmaster

#-----------------------------------------------------------------------
%package	-n texlive-glossaries.bin
Summary:	binary files of glossaries
Conflicts:	texlive <= 20110705-6

%description	-n texlive-glossaries.bin
texlive glossaries.bin package.

%files		-n texlive-glossaries.bin
%{_bindir}/makeglossaries

#-----------------------------------------------------------------------
%package	-n texlive-gsftopk.bin
Summary:	binary files of gsftopk
Conflicts:	texlive <= 20110705-6

%description	-n texlive-gsftopk.bin
texlive gsftopk.bin package.

%files		-n texlive-gsftopk.bin
%{_bindir}/gsftopk

#-----------------------------------------------------------------------
%package	-n texlive-installfont.bin
Summary:	binary files of installfont
Conflicts:	texlive <= 20110705-6

%description	-n texlive-installfont.bin
texlive installfont.bin package.

%files		-n texlive-installfont.bin
%{_bindir}/installfont-tl

#-----------------------------------------------------------------------
%package	-n texlive-jadetex.bin
Summary:	binary files of jadetex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-jadetex.bin
texlive jadetex.bin package.

%files		-n texlive-jadetex.bin
%{_bindir}/jadetex
%{_bindir}/pdfjadetex

#-----------------------------------------------------------------------
%package	-n texlive-kpathsea.bin
Summary:	binary files of kpathsea
Conflicts:	texlive <= 20110705-6

%description	-n texlive-kpathsea.bin
texlive kpathsea.bin package.

%files		-n texlive-kpathsea.bin
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
%{_sbindir}/mktexlsr.post

#-----------------------------------------------------------------------
%package	-n texlive-lacheck.bin
Summary:	binary files of lacheck
Conflicts:	texlive <= 20110705-6

%description	-n texlive-lacheck.bin
texlive lacheck.bin package.

%files		-n texlive-lacheck.bin
%{_bindir}/lacheck

#-----------------------------------------------------------------------
%package	-n texlive-latex-bin.bin
Summary:	binary files of latex-bin
Conflicts:	texlive <= 20110705-6

%description	-n texlive-latex-bin.bin
texlive latex-bin.bin package.

%files		-n texlive-latex-bin.bin
%{_bindir}/dvilualatex
%{_bindir}/latex
%{_bindir}/lualatex
%{_bindir}/pdflatex

#-----------------------------------------------------------------------
%package	-n texlive-latex2man.bin
Summary:	binary files of latex2man
Conflicts:	texlive <= 20110705-6

%description	-n texlive-latex2man.bin
texlive latex2man.bin package.

%files		-n texlive-latex2man.bin
%{_bindir}/latex2man

#-----------------------------------------------------------------------
%package	-n texlive-latexdiff.bin
Summary:	binary files of latexdiff
Conflicts:	texlive <= 20110705-6

%description	-n texlive-latexdiff.bin
texlive latexdiff.bin package.

%files		-n texlive-latexdiff.bin
%{_bindir}/latexdiff
%{_bindir}/latexdiff-vc
%{_bindir}/latexrevise

#-----------------------------------------------------------------------
%package	-n texlive-latexmk.bin
Summary:	binary files of latexmk
Conflicts:	texlive <= 20110705-6

%description	-n texlive-latexmk.bin
texlive latexmk.bin package.

%files		-n texlive-latexmk.bin
%{_bindir}/latexmk

#-----------------------------------------------------------------------
%package	-n texlive-lcdftypetools.bin
Summary:	binary files of lcdftypetools
Conflicts:	texlive <= 20110705-6

%description	-n texlive-lcdftypetools.bin
texlive lcdftypetools.bin package.

%files		-n texlive-lcdftypetools.bin
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
%package	-n texlive-listings-ext.bin
Summary:	binary files of listings-ext
Conflicts:	texlive <= 20110705-6

%description	-n texlive-listings-ext.bin
texlive listings-ext.bin package.

%files		-n texlive-listings-ext.bin
%{_bindir}/listings-ext.sh

#-----------------------------------------------------------------------
%package	-n texlive-luaotfload.bin
Summary:	binary files of luaotfload
Conflicts:	texlive <= 20110705-6

%description	-n texlive-luaotfload.bin
texlive luaotfload.bin package.

%files		-n texlive-luaotfload.bin
%{_bindir}/mkluatexfontdb

#-----------------------------------------------------------------------
%package	-n texlive-luatex.bin
Summary:	binary files of luatex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-luatex.bin
texlive luatex.bin package.

%files		-n texlive-luatex.bin
%{_bindir}/dviluatex
%{_bindir}/luatex
%{_bindir}/texlua
%{_bindir}/texluac

#-----------------------------------------------------------------------
%package	-n texlive-makeindex.bin
Summary:	binary files of makeindex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-makeindex.bin
texlive makeindex.bin package.

%files		-n texlive-makeindex.bin
%{_bindir}/makeindex
%{_bindir}/mkindex

#-----------------------------------------------------------------------
%package	-n texlive-mathspic.bin
Summary:	binary files of mathspic
Conflicts:	texlive <= 20110705-6

%description	-n texlive-mathspic.bin
texlive mathspic.bin package.

%files		-n texlive-mathspic.bin
%{_bindir}/mathspic

#-----------------------------------------------------------------------
%package	-n texlive-metafont.bin
Summary:	binary files of metafont
Conflicts:	texlive <= 20110705-6

%description	-n texlive-metafont.bin
texlive metafont.bin package.

%files		-n texlive-metafont.bin
%{_bindir}/inimf
%{_bindir}/mf
%{_bindir}/mf-nowin

#-----------------------------------------------------------------------
%package	-n texlive-metapost.bin
Summary:	binary files of metapost
Conflicts:	texlive <= 20110705-6

%description	-n texlive-metapost.bin
texlive metapost.bin package.

%files		-n texlive-metapost.bin
%{_bindir}/dvitomp
%{_bindir}/mfplain
%{_bindir}/mpost

#-----------------------------------------------------------------------
%package	-n texlive-mex.bin
Summary:	binary files of mex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-mex.bin
texlive mex.bin package.

%files		-n texlive-mex.bin
%{_bindir}/mex
%{_bindir}/pdfmex
%{_bindir}/utf8mex

#-----------------------------------------------------------------------
%package	-n texlive-mfware.bin
Summary:	binary files of mfware
Conflicts:	texlive <= 20110705-6

%description	-n texlive-mfware.bin
texlive mfware.bin package.

%files		-n texlive-mfware.bin
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/mft
%{_bindir}/pktogf
%{_bindir}/pktype

#-----------------------------------------------------------------------
%package	-n texlive-mkgrkindex.bin
Summary:	binary files of mkgrkindex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-mkgrkindex.bin
texlive mkgrkindex.bin package.

%files		-n texlive-mkgrkindex.bin
%{_bindir}/mkgrkindex

#-----------------------------------------------------------------------
%package	-n texlive-mkjobtexmf.bin
Summary:	binary files of mkjobtexmf
Conflicts:	texlive <= 20110705-6

%description	-n texlive-mkjobtexmf.bin
texlive mkjobtexmf.bin package.

%files		-n texlive-mkjobtexmf.bin
%{_bindir}/mkjobtexmf

#-----------------------------------------------------------------------
%package	-n texlive-mltex.bin
Summary:	binary files of mltex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-mltex.bin
texlive mltex.bin package.

%files		-n texlive-mltex.bin
%{_bindir}/mllatex
%{_bindir}/mltex

#-----------------------------------------------------------------------
%package	-n texlive-mptopdf.bin
Summary:	binary files of mptopdf
Conflicts:	texlive <= 20110705-6

%description	-n texlive-mptopdf.bin
texlive mptopdf.bin package.

%files		-n texlive-mptopdf.bin
%{_bindir}/mptopdf

#-----------------------------------------------------------------------
%package	-n texlive-musixtex.bin
Summary:	binary files of musixtex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-musixtex.bin
texlive musixtex.bin package.

%files		-n texlive-musixtex.bin
%{_bindir}/musixflx
%{_bindir}/musixtex

#-----------------------------------------------------------------------
%package	-n texlive-omegaware.bin
Summary:	binary files of omegaware
Conflicts:	texlive <= 20110705-6

%description	-n texlive-omegaware.bin
texlive omegaware.bin package.

%files		-n texlive-omegaware.bin
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
Conflicts:	texlive <= 20110705-6

%description	-n texlive-patgen.bin
texlive patgen.bin package.

%files		-n texlive-patgen.bin
%{_bindir}/patgen

#-----------------------------------------------------------------------
%package	-n texlive-pax.bin
Summary:	binary files of pax
Conflicts:	texlive <= 20110705-6

%description	-n texlive-pax.bin
texlive pax.bin package.

%files		-n texlive-pax.bin
%{_bindir}/pdfannotextractor

#-----------------------------------------------------------------------
%package	-n texlive-pdfcrop.bin
Summary:	binary files of pdfcrop
Conflicts:	texlive <= 20110705-6

%description	-n texlive-pdfcrop.bin
texlive pdfcrop.bin package.

%files		-n texlive-pdfcrop.bin
%{_bindir}/pdfcrop
%{_bindir}/rpdfcrop

#-----------------------------------------------------------------------
%package	-n texlive-pdfjam.bin
Summary:	binary files of pdfjam
Conflicts:	texlive <= 20110705-6

%description	-n texlive-pdfjam.bin
texlive pdfjam.bin package.

%files		-n texlive-pdfjam.bin
%{_bindir}/pdf180
%{_bindir}/pdf270
%{_bindir}/pdf90
%{_bindir}/pdfbook
%{_bindir}/pdfflip
%{_bindir}/pdfjam
%{_bindir}/pdfjam-pocketmod
%{_bindir}/pdfjam-slides3up
%{_bindir}/pdfjam-slides6up
%{_bindir}/pdfjoin
%{_bindir}/pdfnup
%{_bindir}/pdfpun

#-----------------------------------------------------------------------
%package	-n texlive-pdftex.bin
Summary:	binary files of pdftex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-pdftex.bin
texlive pdftex.bin package.

%files		-n texlive-pdftex.bin
%{_bindir}/etex
%{_bindir}/pdfetex
%{_bindir}/pdftex
%{_bindir}/simpdftex

#-----------------------------------------------------------------------
%package	-n texlive-pdftools.bin
Summary:	binary files of pdftools
Conflicts:	texlive <= 20110705-6

%description	-n texlive-pdftools.bin
texlive pdftools.bin package.

%files		-n texlive-pdftools.bin
%{_bindir}/e2pall
%{_bindir}/pdfatfi
%{_bindir}/pdfclose
%{_bindir}/pdfopen
%{_bindir}/pdftosrc
%{_bindir}/ps4pdf

#-----------------------------------------------------------------------
%package	-n texlive-perltex.bin
Summary:	binary files of perltex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-perltex.bin
texlive perltex.bin package.

%files		-n texlive-perltex.bin
%{_bindir}/perltex

#-----------------------------------------------------------------------
%package	-n texlive-pkfix-helper.bin
Summary:	binary files of pkfix-helper
Conflicts:	texlive <= 20110705-6

%description	-n texlive-pkfix-helper.bin
texlive pkfix-helper.bin package.

%files		-n texlive-pkfix-helper.bin
%{_bindir}/pkfix-helper

#-----------------------------------------------------------------------
%package	-n texlive-pkfix.bin
Summary:	binary files of pkfix
Conflicts:	texlive <= 20110705-6

%description	-n texlive-pkfix.bin
texlive pkfix.bin package.

%files		-n texlive-pkfix.bin
%{_bindir}/pkfix

#-----------------------------------------------------------------------
%package	-n texlive-ppower4.bin
Summary:	binary files of ppower4
Conflicts:	texlive <= 20110705-6

%description	-n texlive-ppower4.bin
texlive ppower4.bin package.

%files		-n texlive-ppower4.bin
%{_bindir}/pdfthumb
%{_bindir}/ppower4

#-----------------------------------------------------------------------
%package	-n texlive-ps2pkm.bin
Summary:	binary files of ps2pkm
Conflicts:	texlive <= 20110705-6

%description	-n texlive-ps2pkm.bin
texlive ps2pkm.bin package.

%files		-n texlive-ps2pkm.bin
%{_bindir}/mag
%{_bindir}/pfb2pfa
%{_bindir}/pk2bm
%{_bindir}/ps2pk

#-----------------------------------------------------------------------
%package	-n texlive-pst2pdf.bin
Summary:	binary files of pst2pdf
Conflicts:	texlive <= 20110705-6

%description	-n texlive-pst2pdf.bin
texlive pst2pdf.bin package.

%files		-n texlive-pst2pdf.bin
%{_bindir}/pst2pdf

#-----------------------------------------------------------------------
%package	-n texlive-pstools.bin
Summary:	binary files of pstools
Conflicts:	texlive <= 20110705-6

%description	-n texlive-pstools.bin
texlive pstools.bin package.

%files		-n texlive-pstools.bin
%{_bindir}/bbox
%{_bindir}/ps2eps
%{_bindir}/ps2frag
%{_bindir}/pslatex

#-----------------------------------------------------------------------
%package	-n texlive-ptex.bin
Summary:	binary files of ptex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-ptex.bin
texlive ptex.bin package.

%files		-n texlive-ptex.bin
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
%package	-n texlive-purifyeps.bin
Summary:	binary files of purifyeps
Conflicts:	texlive <= 20110705-6

%description	-n texlive-purifyeps.bin
texlive purifyeps.bin package.

%files		-n texlive-purifyeps.bin
%{_bindir}/purifyeps

#-----------------------------------------------------------------------
%package	-n texlive-seetexk.bin
Summary:	binary files of seetexk
Conflicts:	texlive <= 20110705-6

%description	-n texlive-seetexk.bin
texlive seetexk.bin package.

%files		-n texlive-seetexk.bin
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dviselect
%{_bindir}/dvitodvi

#-----------------------------------------------------------------------
%package	-n texlive-splitindex.bin
Summary:	binary files of splitindex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-splitindex.bin
texlive splitindex.bin package.

%files		-n texlive-splitindex.bin
%{_bindir}/splitindex

#-----------------------------------------------------------------------
%package	-n texlive-sty2dtx.bin
Summary:	binary files of sty2dtx
Conflicts:	texlive <= 20110705-6

%description	-n texlive-sty2dtx.bin
texlive sty2dtx.bin package.

%files		-n texlive-sty2dtx.bin
%{_bindir}/sty2dtx

#-----------------------------------------------------------------------
%package	-n texlive-svn-multi.bin
Summary:	binary files of svn-multi
Conflicts:	texlive <= 20110705-6

%description	-n texlive-svn-multi.bin
texlive svn-multi.bin package.

%files		-n texlive-svn-multi.bin
%{_bindir}/svn-multi

#-----------------------------------------------------------------------
%package	-n texlive-synctex.bin
Summary:	binary files of synctex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-synctex.bin
texlive synctex.bin package.

%files		-n texlive-synctex.bin
%{_bindir}/synctex

#-----------------------------------------------------------------------
%package	-n texlive-tcdialog.bin
Summary:	binary files of tcdialog
Conflicts:	texlive <= 20110705-6

%description	-n texlive-tcdialog.bin
texlive tcdialog.bin package.

%files		-n texlive-tcdialog.bin
%{_bindir}/tcdialog

#-----------------------------------------------------------------------
%package	-n texlive-tetex.bin
Summary:	binary files of tetex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-tetex.bin
texlive tetex.bin package.

%files		-n texlive-tetex.bin
%{_bindir}/allcm
%{_bindir}/allec
%{_bindir}/allneeded
%{_bindir}/dvi2fax
%{_bindir}/dvired
%{_bindir}/fmtutil
%{_bindir}/fmtutil-sys
%{_bindir}/kpsewhere
%{_bindir}/texconfig-dialog
%{_bindir}/texconfig-sys
%{_bindir}/texlinks
%{_bindir}/updmap
%{_bindir}/updmap-sys

#-----------------------------------------------------------------------
%package	-n texlive-tex.bin
Summary:	binary files of tex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-tex.bin
texlive tex.bin package.

%files		-n texlive-tex.bin
%{_bindir}/initex
%{_bindir}/tex

#-----------------------------------------------------------------------
%package	-n texlive-tex4ht.bin
Summary:	binary files of tex4ht
Conflicts:	texlive <= 20110705-6

%description	-n texlive-tex4ht.bin
texlive tex4ht.bin package.

%files		-n texlive-tex4ht.bin
%{_bindir}/ht
%{_bindir}/htcontext
%{_bindir}/htlatex
%{_bindir}/htmex
%{_bindir}/httex
%{_bindir}/httexi
%{_bindir}/htxelatex
%{_bindir}/htxetex
%{_bindir}/mk4ht
%{_bindir}/t4ht
%{_bindir}/tex4ht

#-----------------------------------------------------------------------
%package	-n texlive-texconfig.bin
Summary:	binary files of texconfig
Conflicts:	texlive <= 20110705-6

%description	-n texlive-texconfig.bin
texlive texconfig.bin package.

%files		-n texlive-texconfig.bin
%{_bindir}/texconfig

#-----------------------------------------------------------------------
%package	-n texlive-texcount.bin
Summary:	binary files of texcount
Conflicts:	texlive <= 20110705-6

%description	-n texlive-texcount.bin
texlive texcount.bin package.

%files		-n texlive-texcount.bin
%{_bindir}/texcount

#-----------------------------------------------------------------------
%package	-n texlive-texdef.bin
Summary:	binary files of texdef
Conflicts:	texlive <= 20110705-6

%description	-n texlive-texdef.bin
texlive texdef.bin package.

%files		-n texlive-texdef.bin
%{_bindir}/texdef

#-----------------------------------------------------------------------
%package	-n texlive-texdiff.bin
Summary:	binary files of texdiff
Conflicts:	texlive <= 20110705-6

%description	-n texlive-texdiff.bin
texlive texdiff.bin package.

%files		-n texlive-texdiff.bin
%{_bindir}/texdiff

#-----------------------------------------------------------------------
%package	-n texlive-texdirflatten.bin
Summary:	binary files of texdirflatten
Conflicts:	texlive <= 20110705-6

%description	-n texlive-texdirflatten.bin
texlive texdirflatten.bin package.

%files		-n texlive-texdirflatten.bin
%{_bindir}/texdirflatten

#-----------------------------------------------------------------------
%package	-n texlive-texdoc.bin
Summary:	binary files of texdoc
Conflicts:	texlive <= 20110705-6

%description	-n texlive-texdoc.bin
texlive texdoc.bin package.

%files		-n texlive-texdoc.bin
%{_bindir}/texdoc
%{_bindir}/texdoctk

#-----------------------------------------------------------------------
%package	-n texlive-texlive-scripts.bin
Summary:	binary files of texlive-scripts
Conflicts:	texlive <= 20110705-6

%description	-n texlive-texlive-scripts.bin
texlive texlive-scripts.bin package.

%files		-n texlive-texlive-scripts.bin
%{_bindir}/rungs

#-----------------------------------------------------------------------
%package	-n texlive-texloganalyser.bin
Summary:	binary files of texloganalyser
Conflicts:	texlive <= 20110705-6

%description	-n texlive-texloganalyser.bin
texlive texloganalyser.bin package.

%files		-n texlive-texloganalyser.bin
%{_bindir}/texloganalyser

#-----------------------------------------------------------------------
%package	-n texlive-texsis.bin
Summary:	binary files of texsis
Conflicts:	texlive <= 20110705-6

%description	-n texlive-texsis.bin
texlive texsis.bin package.

%files		-n texlive-texsis.bin
%{_bindir}/texsis

#-----------------------------------------------------------------------
%package	-n texlive-texware.bin
Summary:	binary files of texware
Conflicts:	texlive <= 20110705-6

%description	-n texlive-texware.bin
texlive texware.bin package.

%files		-n texlive-texware.bin
%{_bindir}/dvitype
%{_bindir}/pooltype

#-----------------------------------------------------------------------
%package	-n texlive-thumbpdf.bin
Summary:	binary files of thumbpdf
Conflicts:	texlive <= 20110705-6

%description	-n texlive-thumbpdf.bin
texlive thumbpdf.bin package.

%files		-n texlive-thumbpdf.bin
%{_bindir}/thumbpdf

#-----------------------------------------------------------------------
%package	-n texlive-tie.bin
Summary:	binary files of tie
Conflicts:	texlive <= 20110705-6

%description	-n texlive-tie.bin
texlive tie.bin package.

%files		-n texlive-tie.bin
%{_bindir}/tie

#-----------------------------------------------------------------------
%package	-n texlive-tpic2pdftex.bin
Summary:	binary files of tpic2pdftex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-tpic2pdftex.bin
texlive tpic2pdftex.bin package.

%files		-n texlive-tpic2pdftex.bin
%{_bindir}/tpic2pdftex

#-----------------------------------------------------------------------
%package	-n texlive-ttfutils.bin
Summary:	binary files of ttfutils
Conflicts:	texlive <= 20110705-6

%description	-n texlive-ttfutils.bin
texlive ttfutils.bin package.

%files		-n texlive-ttfutils.bin
%{_bindir}/ttf2afm
%{_bindir}/ttf2pk
%{_bindir}/ttf2tfm
%{_bindir}/ttfdump

#-----------------------------------------------------------------------
%package	-n texlive-ulqda.bin
Summary:	binary files of ulqda
Conflicts:	texlive <= 20110705-6

%description	-n texlive-ulqda.bin
texlive ulqda.bin package.

%files		-n texlive-ulqda.bin
%{_bindir}/ulqda

#-----------------------------------------------------------------------
%package	-n texlive-vlna.bin
Summary:	binary files of vlna
Conflicts:	texlive <= 20110705-6

%description	-n texlive-vlna.bin
texlive vlna.bin package.

%files		-n texlive-vlna.bin
%{_bindir}/vlna

#-----------------------------------------------------------------------
%package	-n texlive-vpe.bin
Summary:	binary files of vpe
Conflicts:	texlive <= 20110705-6

%description	-n texlive-vpe.bin
texlive vpe.bin package.

%files		-n texlive-vpe.bin
%{_bindir}/vpe

#-----------------------------------------------------------------------
%package	-n texlive-web.bin
Summary:	binary files of web
Conflicts:	texlive <= 20110705-6

%description	-n texlive-web.bin
texlive web.bin package.

%files		-n texlive-web.bin
%{_bindir}/tangle
%{_bindir}/weave

#-----------------------------------------------------------------------
%package	-n texlive-xdvi.bin
Summary:	binary files of xdvi
Conflicts:	texlive <= 20110705-6

%description	-n texlive-xdvi.bin
texlive xdvi.bin package.

%files		-n texlive-xdvi.bin
%{_bindir}/xdvi
%{_bindir}/xdvi-xaw

#-----------------------------------------------------------------------
%package	-n texlive-xetex.bin
Summary:	binary files of xetex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-xetex.bin
texlive xetex.bin package.

%files		-n texlive-xetex.bin
%{_bindir}/teckit_compile
%{_bindir}/xdvipdfmx
%{_bindir}/xelatex
%{_bindir}/xetex

#-----------------------------------------------------------------------
%package	-n texlive-xmltex.bin
Summary:	binary files of xmltex
Conflicts:	texlive <= 20110705-6

%description	-n texlive-xmltex.bin
texlive xmltex.bin package.

%files		-n texlive-xmltex.bin
%{_bindir}/pdfxmltex
%{_bindir}/xmltex

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
%patch1 -p1
%if %{enable_asymptote}
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1

# setup default builtin values, added to paths.h from texmf.cnf
perl -pi -e 's%^(TEXMFMAIN\s+= ).*%$1%{texmfdir}%;'			  \
	 -e 's%^(TEXMFDIST\s+= ).*%$1%{texmfdistdir}%;'			  \
	 -e 's%^(TEXMFLOCAL\s+= ).*%$1%{texmflocaldir}%;'			  \
	 -e 's%^(TEXMFSYSVAR\s+= ).*%$1%{texmfvardir}%;'		  \
	 -e 's%^(TEXMFSYSCONFIG\s+= ).*%$1%{texmfconfdir}%;'		  \
	 -e 's%^(TEXMFHOME\s+= ).*%$1\$HOME/texmf%;'			  \
	 -e 's%^(TEXMFVAR\s+= ).*%$1\$HOME/.texlive2011/texmf-var%;'	  \
	 -e 's%^(TEXMFCONFIG\s+= ).*%$1\$HOME/.texlive2011/texmf-config%;'\
	 -e 's%^(OSFONTDIR\s+= ).*%$1%{_datadir}/fonts%;'		  \
	texk/kpathsea/texmf.cnf

#-----------------------------------------------------------------------
%build
%configure2_5x							\
	--with-banner-add="/Mandriva"				\
	--disable-native-texlive-build				\
	--enable-missing					\
%if %{enable_shared}
	--enable-shared						\
%else
	--disable-shared					\
%endif
%if %{enable_xindy}
	--enable-xindy						\
%else
	--disable-xindy						\
%endif
	--with-system-freetype					\
	--with-freetype-includes=%{_includedir}/freetype	\
	--with-system-freetype2					\
	--with-freetype2-includes=%{_includedir}/freetype2	\
%if %{with_system_dialog}
	--disable-dialog					\
%else
	--enable-dialog						\
%endif
%if %{with_system_psutils}
	--disable-psutils					\
%else
	--enable-psutils					\
%endif
	--with-system-gd					\
%if %{with_system_lcdf}
	--disable-lcdf-typetools				\
%endif
	--with-system-png					\
%if %{with_system_t1lib}
	--with-system-t1lib					\
	--disable-t1utils					\
%endif
%if %{with_system_teckit}
	--disable-teckit					\
	--with-teckit-includes=%{_includedir}/teckit		\
%endif
%if %{with_system_tex4ht}
	--disable-tex4htk					\
%endif
%if %{with_system_poppler}
	--with-system-xpdf					\
%else
	--without-system-xpdf					\
%endif
	--with-system-zziplib
%make

%if %{enable_asymptote}
pushd utils/asymptote
%configure2_5x							\
	--enable-gc=system					\
	--enable-texlive-build					\
	--datadir=%{texmfdir}
%make
popd
%endif

#-----------------------------------------------------------------------
%install
%makeinstall_std

%if %{enable_asymptote}
pushd utils/asymptote
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

mkdir -p %{buildroot}%{texmfvardir}
mkdir -p %{buildroot}%{texmfconfdir}

%if %{with_system_lcdf}
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
    # correct symlinks
    for file in *; do
	link=`readlink $file` || :
	if [ "x$link" != "x" ]; then
	    ln -sf `echo $link |					\
		sed	-e 's|\.\./.*texmf-dist/|%{texmfdistdir}/|'	\
			-e 's|\.\./.*texmf/|%{texmfdir}/|'`		\
		$file
	fi
    done
%if %{with_system_dialog}
    ln -sf %{_bindir}/dialog tcdialog
%endif
%if %{enable_asymptote}
    ln -sf %{texmfdir}/asymptote/GUI/xasy.py xasy
%endif
    rm -f a2ping afm2afm arlatex authorindex autoinst bibexport		\
	  bundledoc cachepic cmap2enc de-macro dviasm ebong e2pall	\
	  epspdf epspdftk epstopdf fig4latex findhyph font2afm		\
	  fragmaster ht htcontext htlatex htmex httex httexi htxelatex	\
	  htxetex latex2man latexdiff latexdiff-vc latexmk latexrevise	\
	  listings-ext.sh makeglossaries mathspic mk4ht mkgrkindex	\
	  mkjobtexmf mkluatexfontdb mkt1font mptopdf ot2kpx pdf180	\
	  pdf270 pdf90 pdfannotextractor pdfatfi pdfbook pdfcrop	\
	  pdfflip pdfjam pdfjam-pocketmod pdfjam-slides3up		\
	  pdfjam-slides6up pdfjoin pdfnup pdfpun pdfthumb perltex	\
	  pfm2kpx pkfix  pkfix-helper ppower4 ps4pdf pst2pdf purifyeps	\
	  repstopdf rpdfcrop rungs showglyphs simpdftex splitindex	\
	  svn-multi texcount texdiff texdirflatten texdoc texdoctk	\
	  texloganalyser thumbpdf tlmgr ulqda updmap vpe vpl2ovp	\
	  vpl2vpl

    ln -sf %{texmfdir}/scripts/a2ping/a2ping.pl a2ping
    ln -sf %{texmfdistdir}/scripts/fontools/afm2afm afm2afm
    ln -sf %{texmfdistdir}/scripts/bundledoc/arlatex arlatex
    ln -sf %{texmfdistdir}/scripts/authorindex/authorindex authorindex
    ln -sf %{texmfdistdir}/scripts/fontools/autoinst autoinst
    ln -sf %{texmfdistdir}/scripts/bibexport/bibexport.sh bibexport
    ln -sf %{texmfdistdir}/scripts/bundledoc/bundledoc bundledoc
    ln -sf %{texmfdistdir}/scripts/cachepic/cachepic.tlu cachepic
    ln -sf %{texmfdistdir}/scripts/fontools/cmap2enc cmap2enc
    ln -sf %{texmfdistdir}/scripts/de-macro/de-macro de-macro
    ln -sf %{texmfdistdir}/scripts/dviasm/dviasm.py dviasm
    ln -sf %{texmfdir}/scripts/tetex/e2pall.pl e2pall
    ln -sf %{texmfdistdir}/scripts/ebong/ebong.py ebong
    ln -sf %{texmfdistdir}/scripts/epspdf/epspdf.rb epspdf
    ln -sf %{texmfdistdir}/scripts/epspdf/epspdftk.tcl epspdftk
    ln -sf %{texmfdistdir}/scripts/epstopdf/epstopdf.pl epstopdf
    ln -sf %{texmfdistdir}/scripts/fig4latex/fig4latex fig4latex
    ln -sf %{texmfdistdir}/scripts/findhyph/findhyph findhyph
    ln -sf %{texmfdistdir}/scripts/fontools/font2afm font2afm
    ln -sf %{texmfdistdir}/scripts/fragmaster/fragmaster.pl fragmaster
%if !%{with_system_tex4ht}
    ln -sf %{texmfdistdir}/scripts/tex4ht/ht.sh ht
    ln -sf %{texmfdistdir}/scripts/tex4ht/htcontext.sh htcontext
    ln -sf %{texmfdistdir}/scripts/tex4ht/htlatex.sh htlatex
    ln -sf %{texmfdistdir}/scripts/tex4ht/htmex.sh htmex
    ln -sf %{texmfdistdir}/scripts/tex4ht/httex.sh httex
    ln -sf %{texmfdistdir}/scripts/tex4ht/httexi.sh httexi
    ln -sf %{texmfdistdir}/scripts/tex4ht/htxelatex.sh htxelatex
    ln -sf %{texmfdistdir}/scripts/tex4ht/htxetex.sh htxetex
%endif
    ln -sf %{texmfdistdir}/scripts/latex2man/latex2man latex2man
    ln -sf %{texmfdistdir}/scripts/latexdiff/latexdiff.pl latexdiff
    ln -sf %{texmfdistdir}/scripts/latexdiff/latexdiff-vc.pl latexdiff-vc
    ln -sf %{texmfdistdir}/scripts/latexmk/latexmk.pl latexmk
    ln -sf %{texmfdistdir}/scripts/latexdiff/latexrevise.pl latexrevise
    ln -sf %{texmfdistdir}/scripts/listings-ext/listings-ext.sh listings-ext.sh
    ln -sf %{texmfdistdir}/scripts/glossaries/makeglossaries makeglossaries
    ln -sf %{texmfdistdir}/scripts/mathspic/mathspic.pl mathspic
%if !%{with_system_tex4ht}
    ln -sf %{texmfdistdir}/scripts/tex4ht/mk4ht.pl mk4ht
%endif
    ln -sf %{texmfdistdir}/scripts/mkgrkindex/mkgrkindex mkgrkindex
    ln -sf %{texmfdistdir}/scripts/mkjobtexmf/mkjobtexmf.pl mkjobtexmf
    ln -sf %{texmfdistdir}/scripts/luaotfload/mkluatexfontdb.lua mkluatexfontdb
    ln -sf %{texmfdistdir}/scripts/accfonts/mkt1font mkt1font
    ln -sf %{texmfdistdir}/scripts/context/perl/mptopdf.pl mptopdf
    ln -sf %{texmfdistdir}/scripts/fontools/ot2kpx ot2kpx
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdf180 pdf180
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdf270 pdf270
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdf90 pdf90
    ln -sf %{texmfdistdir}/scripts/pax/pdfannotextractor.pl pdfannotextractor
    ln -sf %{texmfdistdir}/scripts/oberdiek/pdfatfi.pl pdfatfi
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfbook pdfbook
    ln -sf %{texmfdistdir}/scripts/pdfcrop/pdfcrop.pl pdfcrop
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfflip pdfflip
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam pdfjam
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-pocketmod pdfjam-pocketmod
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-slides3up pdfjam-slides3up
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-slides6up pdfjam-slides6up
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjoin pdfjoin
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfnup pdfnup
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfpun pdfpun
    ln -sf %{texmfdistdir}/scripts/ppower4/pdfthumb.tlu pdfthumb
    ln -sf %{texmfdistdir}/scripts/perltex/perltex.pl perltex
    ln -sf %{texmfdistdir}/scripts/fontools/pfm2kpx pfm2kpx
    ln -sf %{texmfdistdir}/scripts/pkfix/pkfix.pl pkfix
    ln -sf %{texmfdistdir}/scripts/pkfix-helper/pkfix-helper pkfix-helper
    ln -sf %{texmfdistdir}/scripts/ppower4/ppower4.tlu ppower4
    ln -sf %{texmfdistdir}/scripts/pst-pdf/ps4pdf ps4pdf
    ln -sf %{texmfdistdir}/scripts/pst2pdf/pst2pdf pst2pdf
    ln -sf %{texmfdistdir}/scripts/purifyeps/purifyeps purifyeps
    ln -sf epstopdf repstopdf
    ln -sf pdfcrop rpdfcrop
    ln -sf %{texmfdir}/scripts/texlive/rungs.tlu rungs
    ln -sf %{texmfdistdir}/scripts/fontools/showglyphs showglyphs
    ln -sf %{texmfdistdir}/scripts/splitindex/perl/splitindex.pl splitindex
    ln -sf %{texmfdir}/scripts/simpdftex/simpdftex simpdftex
    ln -sf %{texmfdistdir}/scripts/svn-multi/svn-multi.pl svn-multi
    ln -sf %{texmfdistdir}/scripts/texcount/texcount.pl texcount
    ln -sf %{texmfdistdir}/scripts/texdiff/texdiff texdiff
    ln -sf %{texmfdistdir}/scripts/texdirflatten/texdirflatten texdirflatten
    ln -sf %{texmfdir}/scripts/texdoc/texdoc.tlu texdoc
    ln -sf %{texmfdir}/scripts/tetex/texdoctk.pl texdoctk
    ln -sf %{texmfdistdir}/scripts/texloganalyser/texloganalyser texloganalyser
    ln -sf %{texmfdistdir}/scripts/thumbpdf/thumbpdf.pl thumbpdf
    ln -sf %{texmfdistdir}/scripts/ulqda/ulqda.pl ulqda
    ln -sf %{texmfdistdir}/scripts/vpe/vpe.pl vpe
    ln -sf %{texmfdistdir}/scripts/accfonts/vpl2ovp vpl2ovp
    ln -sf %{texmfdistdir}/scripts/accfonts/vpl2vpl vpl2vpl
    ln -sf %{texmfdir}/scripts/tetex/updmap.pl updmap
popd

# use texmf data
rm -fr %{buildroot}%{texmfdir} %{buildroot}%{texmfdistdir}

# install manual pages and info files from texlive-texmf tarball
rm -fr %{buildroot}%{_mandir} %{buildroot}%{_infodir}

%if !%{enable_shared}
# do not generate dynamic libraries and do not install static ones
rm -fr %{buildroot}%{_libdir}
rm -fr %{buildroot}%{_includedir}
%endif

install -D -m 755 %{SOURCE2} %{buildroot}%{_sbindir}/mktexlsr.post

#-----------------------------------------------------------------------
%posttrans
%{_sbindir}/mktexlsr.post
%{_bindir}/updmap-sys --syncwithtrees > /dev/null
%{_bindir}/texconfig-sys init > /dev/null
%{_bindir}/mtxrun --generate > /dev/null
