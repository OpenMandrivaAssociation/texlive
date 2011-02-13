%define	__spec_install_pre	export RPM_SOURCE_DIR="%{_sourcedir}";export RPM_BUILD_DIR="%{_builddir}";export RPM_OPT_FLAGS="%{optflags}";export RPM_ARCH="%{_arch}";export RPM_OS="%{_os}";export RPM_DOC_DIR="%%{_docdir}";export RPM_PACKAGE_NAME="%%{name}";export RPM_PACKAGE_VERSION="%%{version}";export RPM_PACKAGE_RELEASE="%%{release}";export RPM_BUILD_ROOT="%{buildroot}";export LC_ALL=C;export LANG=C;cd %_builddir

# need to bootstrap first
%define enable_asymptote	0

# need to bootstrap first
%define enable_xindy		0

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
License:	Apache2 and Artistic and BSD and FDL and Freeware and GFL and GFSL and GPL and GPLv2 and GPLv3 and LGPL and LGPLv2.1 and LPPL and LPPLv1 and LPPLv1.2 and LPPLv1.3 and OFL and Public Domain
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-source.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-source.tar.xz.sha256
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/texmf-dist
%dir %{_datadir}/texmf
%{_datadir}/texmf/chktex
%doc %{_datadir}/texmf/doc
%{_datadir}/texmf/dvipdfmx
%{_datadir}/texmf/dvips
%{_datadir}/texmf/fonts
%{_datadir}/texmf/scripts
%{_datadir}/texmf/texconfig
%{_datadir}/texmf/web2c
%{_datadir}/texmf/xdvi
%{_datadir}/X11/app-defaults/XDvi
%{_localstatedir}/lib/texmf

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}-source

perl -pi -e 's%^(TEXMFMAIN = ).*%$1%{_datadir}/texmf%;'					\
	 -e 's%^(TEXMFDIST = ).*%$1%{_datadir}/texmf-dist%;'				\
	 -e 's%^(TEXMFLOCAL = ).*%$1\{%{_datadir}/texmf-local,%{_datadir}/texmf\}%;'	\
	 -e 's%^(TEXMFSYSVAR = ).*%$1%{_localstatedir}/lib/texmf%;'			\
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
for dir in texmf texmf-dist; do
    if [ -d %{buildroot}%{_prefix}/$dir ]; then
	rm -fr %{buildroot}%{_datadir}/$dir
	mv %{buildroot}%{_prefix}/$dir %{buildroot}%{_datadir}
    fi
done

if [ -f %{buildroot}%{_datadir}/texmf/xdvi/XDvi ]; then
    mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
    mv -f %{buildroot}%{_datadir}/texmf/xdvi/XDvi		\
	%{buildroot}%{_datadir}/X11/app-defaults
fi

mkdir -p %{buildroot}%{_localstatedir}/lib/texmf

# fixme openmpi has a program with the same name
[ -f %{buildroot}%{_bindir}/otfinfo ] &&
    mv -f %{buildroot}%{_bindir}/otfinfo{,-texlive}

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
    ln -sf pdftex physe
    ln -sf pdftex phyzzx
    ln -sf pdftex utf8mex
    ln -sf pdftex texsis
    ln -sf pdftex xmltex
    ln -sf ptex platex
    ln -sf mpost metafun
    ln -sf mpost mfplain
    ln -sf xetex xelatex
    # correct symlinks
    for file in *; do
	link=`readlink $file` || :
	if [ "x$link" != "x" ]; then
	    ln -sf `echo $link | sed -e 's%../%../share/%'` $file
	fi
    done
%if %{with_system_dialog}
    ln -sf dialog tcdialog
%endif

    rm -f tlmgr
    rm -f texdoctk
popd

pushd %{buildroot}%{_datadir}/texmf
    rm -f scripts/texlive/tlmgr.pl
    rm -f scripts/tetex/texdoctk.pl
popd

# install manual pages and info files from texlive-texmf tarball
rm -fr %{buildroot}%{_mandir} %{buildroot}%{_infodir}

# do not generate dynamic libraries and do not install static ones
rm -fr %{buildroot}%{_libdir}
rm -fr %{buildroot}%{_includedir}

# stray directory left
rm -fr %{buildroot}%{_datadir}/lcdf-typetools-for-tex-live

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}
