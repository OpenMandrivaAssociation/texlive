#%#define __spec_install_pre	export RPM_SOURCE_DIR="%{_sourcedir}";export RPM_BUILD_DIR="%{_builddir}";export RPM_OPT_FLAGS="%{optflags}";export RPM_ARCH="%{_arch}";export RPM_OS="%{_os}";export RPM_DOC_DIR="%%{_docdir}";export RPM_PACKAGE_NAME="%%{name}";export RPM_PACKAGE_VERSION="%%{version}";export RPM_PACKAGE_RELEASE="%%{release}";export RPM_BUILD_ROOT="%{buildroot}";export LC_ALL=C;export LANG=C;cd %_builddir

# need to bootstrap first
%define enable_asymptote	0
%define enable_xindy		0

%define with_system_poppler	0
%define with_system_dialog	1
%define with_system_lcdf	0
%define with_system_psutils	1
%define with_system_t1lib	1
%define with_system_tex4ht	0
%define with_system_teckit	0

#-----------------------------------------------------------------------
Name:		texlive
Version:	20100722
Release:	%mkrel 4
Summary:	The TeX formatting system
Group:		Publishing
License:	Apache2 and Artistic and BSD and FDL and Freeware and GFL and GFSL and GPL and GPLv2 and GPLv3 and LGPL and LGPLv2.1 and LPPL and LPPLv1 and LPPLv1.2 and LPPLv1.3 and OFL and Public Domain
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-source.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-source.tar.xz.sha256
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%if %mdkversion <= 201100
Provides:	jadetex = %{version}
Provides:	tetex = %{version}
Provides:	tetex-dvipdfm = %{version}
Provides:	tetex-dvips = %{version}
Provides:	tetex-latex = %{version}
Provides:	texlive-afm = %{version}
Provides:	texlive-context = %{version}
Provides:	texlive-dvilj = %{version}
Provides:	texlive-dvipdfm = %{version}
Provides:	texlive-dvips = %{version}
Provides:	texlive-dviutils = %{version}
Provides:	texlive-latex = %{version}
Provides:	texlive-mfwin = %{version}
Provides:	xmltex = %{version}
%endif

Obsoletes:	jadetex <= 3.12-153
Obsoletes:	tetex <= 3.0-55
Obsoletes:	tetex-dvipdfm <= 3.0-55
Obsoletes:	tetex-dvips <= 3.0-55
Obsoletes:	tetex-latex <= 3.0-55
Obsoletes:	texlive-afm <= 2007
Obsoletes:	texlive-context <= 2007
Obsoletes:	texlive-dvilj <= 2007
Obsoletes:	texlive-dvipdfm <= 2007
Obsoletes:	texlive-dvips <= 2007
Obsoletes:	texlive-dviutils <= 2007
Obsoletes:	texlive-latex <= 2007
Obsoletes:	texlive-mfwin <= 2007
Obsoletes:	xmltex <= 3.0-55

%if %{with_system_teckit}
Requires:	teckit
%else
Provides:	teckit
Obsoletes:	teckit <= 2.5.1
%endif

%if %{with_system_tex4ht}
Requires:	tex4ht
%else
Provides:	tex4ht
Obsoletes:	tex4ht <= 1.0.2008_02_28_2058
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
%if %{with_system_dialog}
Requires:	cdialog
%endif
Requires:	ghostscript
%if %{with_system_psutils}
Requires:	psutils
%endif
Requires:	texlive-texmf
Requires:	texlive-fonts

Requires(post):	texlive-texmf
Requires(post):	texlive-fonts

#-----------------------------------------------------------------------
Patch0:		texlive-20100722-underlink.patch
Patch1:		texlive-20100722-format.patch
Patch2:		texlive-20100722-asymptote.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files
%defattr(-,root,root,-)
%{_bindir}/*
%dir %{_datadir}/texmf
%dir %{_datadir}/texmf-dist
%dir %{_localstatedir}/lib/texmf
%dir %{_sysconfdir}/texmf

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}-source
%patch0	-p1
%patch1	-p1
%if %{enable_asymptote}
%patch2 -p1
%endif

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
	--datadir=%{_datadir}/texmf
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

mkdir -p %{buildroot}%{_localstatedir}/lib/texmf
mkdir -p %{buildroot}%{_sysconfdir}/texmf

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
    rm -f a2ping
    rm -f e2pall
    rm -f rungs
    rm -f simpdftex
    rm -f tlmgr
    rm -f texdoc
    rm -f texdoctk
popd

# use texmf data
rm -fr %{buildroot}%{_datadir}/texmf/*
rm -fr %{buildroot}%{_datadir}/texmf-dist/*

# install manual pages and info files from texlive-texmf tarball
rm -fr %{buildroot}%{_mandir} %{buildroot}%{_infodir}

# do not generate dynamic libraries and do not install static ones
rm -fr %{buildroot}%{_libdir}
rm -fr %{buildroot}%{_includedir}

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}

#-----------------------------------------------------------------------
%post
pushd %{_datadir}
    rm -f texmf/ls-R texmf-dist/ls-R
    mktexlsr %{_datadir}/texmf{,-dist}
popd
pushd %{_localstatedir}/lib/texmf
    texconfig-sys init
popd
