%define _binary_payload		w9.gzdio
%define _source_payload		w9.gzdio

# need to bootstrap first
%define enable_asymptote	1
%define enable_xindy		1

%define with_system_poppler	0
%define with_system_dialog	1
%define with_system_lcdf	0
%define with_system_psutils	1
%define with_system_t1lib	1
%define with_system_tex4ht	0
%define with_system_teckit	0

%if %mdkversion >= 201100
  %define texmfbindir		%{_bindir}
  %define texmfdir		%{_datadir}/texmf
  %define texmfdistdir		%{_datadir}/texmf-dist
  %define texmfextradir		%{_datadir}/texmf-extra
  %define texmfprojectdir	%{_datadir}/texmf-project
  %define texmfvardir		%{_localstatedir}/lib/texmf
  %define texmfconfdir		%{_sysconfdir}/texmf
%else
  %define texmfbindir		/opt/texlive2010/bin
  %define texmfdir		/opt/texlive2010/texmf
  %define texmfdistdir		/opt/texlive2010/texmf-dist
  %define texmfextradir		/opt/texlive2010/texmf-extra
  %define texmfprojectdir	/opt/texlive2010/texmf-project
  %define texmfvardir		/opt/texlive2010/lib/texmf
  %define texmfconfdir		/opt/texlive2010/texmf
%endif

#-----------------------------------------------------------------------
Name:		texlive
Version:	20100722
Release:	%mkrel 10
Summary:	The TeX formatting system
Group:		Publishing
License:	http://www.tug.org/texlive/LICENSE.TL
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-source.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-source.tar.xz.sha256
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%if %mdkversion <= 201100
Provides:	jadetex = %{version}
Provides:	kpathsea = %{version}
Provides:	pdfjam = %{version}
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
Provides:	texlive-jadetex = %{version}
Provides:	texlive-latex = %{version}
Provides:	texlive-mfwin = %{version}
Provides:	texlive-xdvi = %{version}
Provides:	texlive-xmltex = %{version}
Provides:	xmltex = 1:%{version}
%endif
%if %mdkversion >= 201100
Obsoletes:	jadetex <= 3.12
Obsoletes:	kpathsea <= 20100722
Conflicts:	kpathsea-devel <= 20100722
Obsoletes:	kpathsea-devel <= 20100722
Conflicts:	kpathsea-static-devel <= 20100722
Obsoletes:	kpathsea-static-devel <= 20100722
Obsoletes:	pdfjam <= 1.21
Obsoletes:	tetex <= 3.0
Obsoletes:	tetex-dvipdfm <= 3.0
Obsoletes:	tetex-dvips <= 3.0
Obsoletes:	tetex-latex <= 3.0
Obsoletes:	texlive-afm <= 2007
Obsoletes:	texlive-context <= 2007
Obsoletes:	texlive-dvilj <= 2007
Obsoletes:	texlive-dvipdfm <= 2007
Obsoletes:	texlive-dvips <= 2007
Obsoletes:	texlive-dviutils <= 2007
Obsoletes:	texlive-jadetex <= 2007
Obsoletes:	texlive-latex <= 2007
Obsoletes:	texlive-mfwin <= 2007
Obsoletes:	texlive-xdvi <= 2007
Obsoletes:	texlive-xmltex <= 2007
Obsoletes:	xmltex <= 1:3.0
%endif

#-----------------------------------------------------------------------
%if %{with_system_dialog}
Requires:	cdialog
%endif
Requires:	ghostscript
%if %{enable_asymptote}
Requires:	gv
%endif
%if %{with_system_lcdf}
Requires:	lcdf-typetoools
%else
Provides:	lcdf-typetools = %{version}
Obsoletes:	lcdf-typetools <= 2.59-5
%endif
%if %{with_system_psutils}
Requires:	psutils
%endif
%if %{with_system_teckit}
Requires:	teckit
%endif
%if %{with_system_tex4ht}
Requires:	tex4ht
%else
Provides:	tex4ht = %{version}
Obsoletes:	tex4ht <= 1:1.0.2008_02_28_2058
%endif
Requires(post):	texlive-texmf

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
Patch0:		texlive-20100722-underlink.patch
Patch1:		texlive-20100722-format.patch
Patch2:		texlive-20100722-asymptote.patch
Patch3:		texlive-20100722-xdvi.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files
%defattr(-,root,root,-)
%{texmfbindir}/*
%dir %{texmfvardir}
%dir %{texmfconfdir}

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}-source
%patch0	-p1
%patch1	-p1
%if %{enable_asymptote}
%patch2 -p1
%endif
%patch3 -p1

# setup default builtin values, added to paths.h from texmf.cnf
perl -pi -e 's%^(TEXMFMAIN\s+= ).*%$1%{texmfdir}%;'			  \
	 -e 's%^(TEXMFDIST\s+= ).*%$1%{texmfdistdir}%;'			  \
	 -e 's%^(TEXMFLOCAL\s+= ).*%$1%{texmfdir}%;'			  \
	 -e 's%^(TEXMFSYSVAR\s+= ).*%$1%{texmfvardir}%;'		  \
	 -e 's%^(TEXMFSYSCONFIG\s+= ).*%$1%{texmfconfdir}%;'		  \
	 -e 's%^(TEXMFHOME\s+= ).*%$1\{\$HOME/texmf,%{texmfdir}\}%;'	  \
	 -e 's%^(TEXMFVAR\s+= ).*%$1\$HOME/.texlive2010/texmf-var%;'	  \
	 -e 's%^(TEXMFCONFIG\s+= ).*%$1\$HOME/.texlive2010/texmf-config%;'\
	 -e 's%^(OSFONTDIR\s+= ).*%$1%{_datadir}/fonts%;'		  \
	texk/kpathsea/texmf.cnf

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
if [ -f %{buildroot}%{texmfbindir}/otfinfo ]; then
    mv -f %{buildroot}%{texmfbindir}/otfinfo{,-texlive}
fi
%endif

pushd %{buildroot}%{texmfbindir}
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
	    ln -sf `echo %link |					\
		sed	-e 's|\.\./.*texmf-dist/|%{texmfdistdir}/|'	\
			-e 's|\.\./.*texmf/|%{texmfdir}|'`		\
		$file
	fi
    done
%if %{with_system_dialog}
    ln -sf %{_bindir}/dialog tcdialog
%endif
%if %{enable_asymptote}
    ln -sf %{texmfdir}/asymptote/GUI/xasy.py xasy
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
rm -fr %{buildroot}%{texmfdir} %{buildroot}%{texmfdistdir}

# install manual pages and info files from texlive-texmf tarball
rm -fr %{buildroot}%{_mandir} %{buildroot}%{_infodir}

# do not generate dynamic libraries and do not install static ones
rm -fr %{buildroot}%{_libdir}
rm -fr %{buildroot}%{_includedir}

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}

#-----------------------------------------------------------------------
%posttrans
rm -f %{texmfdir}/ls-R %{texmfdistdir}/ls-R
mktexlsr %{texmfdir} %{texmfdistdir}
texconfig-sys init
