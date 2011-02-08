# need to bootstrap first
%define enable_asymptote	0

# need to bootstrap first
%define enable_xindy		0

# does not build with poppler-0.16
%define with_system_poppler	0
%define with_system_dialog	1
%define with_system_psutils	1
%define with_system_t1lib	1

#-----------------------------------------------------------------------
Name:		texlive
Version:	20100722
Release:	%mkrel 1
Summary:	The TeX formatting system
Group:		Publishing
License:	GPLv2 and BSD and Public Domain and LGPLv2+ and GPLv2+ and LPPL
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-source.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-source.tar.xz.sha256
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Obsoletes:	tetex <= 3.0-55
%if %mdkversion <= 201100
Provides:	tetex = %{version}
%endif

Provides:	texlive-afm = %{version}
Obsoletes:	texlive-afm <= 2007
Provides:	texlive-context = %{version}
Obsoletes:	texlive-context <= 2007
Provides:	texlive-dvilj = %{version}
Obsoletes:	texlive-dvilj <= 2007

Provides:	tex4ht
Obsoletes:	tex4ht <= 1.0.2008_02_28_2058

Provides:	texlive-dvipdfm = %{version}
Provides:	texlive-dvipdfm <= 2007

Obsoletes:	tetex-dvipdfm <= 3.0-55
%if %mdkversion <= 201100
Provides:	tetex-dvipdfm = %{version}
%endif

Provides:	texlive-dvips = %{version}
Obsoletes:	texlive-dvips <= 2007
Provides:	texlive-dviutils = %{version}
Obsoletes:	texlive-dviutils <= 2007
Provides:	texlive-fonts = %{version}
Obsoletes:	texlive-fonts <= 2007

Obsoletes:	jadetex <= 3.12-153
%if %mdkversion <= 201100
Provides:	jadetex = %{version}
%endif

Provides:	texlive-latex = %{version}
Obsoletes:	texlive-latex <= 2007

Obsoletes:	tetex-latex <= 3.0-55
%if %mdkversion <= 201100
Provides:	tetex-latex = %{version}
%endif

Provides:	texlive-latex = %{version}
Obsoletes:	texlive-latex <= 2007

Provides:	texlive-mfwin = %{version}
Obsoletes:	texlive-mfwin <= 2007

Obsoletes:	xmltex <= 3.0-55
%if %mdkversion <= 201100
Provides:	xmltex = %{version}
%endif
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
BuildRequires:	gc-devel
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
%if %{enable_xindy}
BuildRequires:	texlive-latex
%endif
BuildRequires:	zziplib-devel

#-----------------------------------------------------------------------
%if %{with_system_dialog}
Requires:	cdialog
%endif
%if %{with_system_psutils}
Requires:	psutils
%endif

#-----------------------------------------------------------------------
Patch0:		texlive-20100722-underlink.patch
Patch1:		texlive-20100722-format.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system with
binaries for most flavors of Unix, including GNU/Linux, and also
Windows. It includes all the major TeX-related programs, macro
packages, and fonts that are free software, including support for
many languages around the world.

%files
%defattr(-,root,root,-)
%{_bindir}/*
%exclude %{_bindir}/k*
%exclude %{_bindir}/xdvi*
%{_mandir}/man1/*
%exclude %{_mandir}/man1/k*
%exclude %{_mandir}/man1/xdvi.1*
%{_mandir}/man5/*
%{_infodir}/*
%exclude %{_infodir}/kpathsea.info*
%{_datadir}/texmf-dist
%{_datadir}/texmf
%exclude %{_datadir}/texmf/doc
%exclude %{_datadir}/texmf/xdvi

#-----------------------------------------------------------------------
%package	doc
Summary:	TeX Live documentation
Group:		Publishing
Requires:	texlive = %{version}-%{release}
Requires:	texlive-texmf-doc = %{version}

%description	doc
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system with
binaries for most flavors of Unix, including GNU/Linux, and also
Windows. It includes all the major TeX-related programs, macro
packages, and fonts that are free software, including support for
many languages around the world.

%files		doc
%defattr(-,root,root,-)
%{_datadir}/texmf/doc

#-----------------------------------------------------------------------
%package	xdvi
Summary:	X viewer for DVI files
Group:		Publishing
Requires:	xdg-utils

%description	xdvi
Xdvi allows you to preview the TeX text formatting system's output
.dvi files on an X Window System.

%files		xdvi
%defattr(-,root,root,-)
%{_bindir}/xdvi*
%{_mandir}/man1/xdvi.1*
%{_datadir}/texmf/xdvi
%{_datadir}/X11/app-defaults/XDvi

#-----------------------------------------------------------------------
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
%{_bindir}/k*
%{_libdir}/libkpathsea.so.*
%{_infodir}/kpathsea.info*
%{_mandir}/man1/k*

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

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}-source

perl -pi -e 's%^(TEXMFMAIN = ).*%$1%{_datadir}/texmf%;'					\
	 -e 's%^(TEXMFDIST = ).*%$1%{_datadir}/texmf-dist%;'				\
	 -e 's%^(TEXMFLOCAL = ).*%$1\{%{_datadir}/texmf-local,%{_datadir}/texmf\}%;'	\
	 -e 's%^(TEXMFSYSVAR = ).*%$1%{_localstatedir}/lib/texmf-var%;'			\
	 -e 's%^(TEXMFSYSCONFIG = ).*%$1%{_datadir}/texmf-config%;'			\
	 -e 's%^(TEXMFHOME = ).*%$1\{\$HOME/texmf,%{_datadir}/texmf\}%;'		\
	 -e 's%^(TEXMFVAR = ).*%$1\$HOME/.texlive2010/texmf-var%;'			\
	 -e 's%^(TEXMFCONFIG = ).*%$1\$HOME/.texlive2010/texmf-config%;'		\
	 -e 's%^(OSFONTDIR = ).*%$1%{_datadir}/fonts%;'					\
	texk/kpathsea/texmf.cnf

%patch0	-p1
%patch1	-p1

#-----------------------------------------------------------------------
%build
%configure2_5x							\
	--with-banner-add="/Mandriva"				\
	--disable-native-texlive-build				\
	--enable-missing					\
	--enable-shared						\
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
	--with-system-png					\
%if %{with_system_t1lib}
	--with-system-t1lib					\
	--disable-t1utils					\
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
	--enable-texlive-build
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
mv -f %{buildroot}%{_prefix}/texmf %{buildroot}%{_datadir}
mv -f %{buildroot}%{_prefix}/texmf-dist %{buildroot}%{_datadir}

mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
mv -f %{buildroot}%{_datadir}/texmf/xdvi/XDvi %{buildroot}%{_datadir}/X11/app-defaults

# fixme openmpi has a program with the same name
mv -f %{buildroot}%{_bindir}/otfinfo{,-texlive}

# Correct symlinks
pushd %{_buildroot}%{_bindir}
    for file in *; do
	link=`readlink $file`
	if [ "x$link" != "x" ]; then
	    ln -sf `echo $link | sed -e 's%../%../share/%'` $file
	fi
    done
popd

#-----------------------------------------------------------------------
%clean
# FIXME temporary hack for test builds
%if 0
rm -rf %{buildroot}
%endif
