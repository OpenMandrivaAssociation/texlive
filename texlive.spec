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
%define historic 1

# From texlive-tlpkg macros; fallback if macros not loaded yet in parse
%{!?_tlpkgdir:%global _tlpkgdir %{_datadir}/tlpkg}

#-----------------------------------------------------------------------
Name:		texlive
Version:	20260301
Release:	7
Summary:	The TeX formatting system
Group:		Publishing
License:	http://www.tug.org/texlive/LICENSE.TL
URL:		https://tug.org/texlive/
%if %{historic}
Source0:	ftp://tug.org/historic/systems/texlive/%(echo %{version}|cut -b1-4)/texlive-%{version}-source.tar.xz
%else
# svn co svn://tug.org/texlive/branches/branch2019/Build/source texlive-source
# cd texlive-source
# svn export . /tmp/texlive-$(date +%Y%m%d)-source
# cd /tmp
# tar cJf texlive-$(date +%Y%m%d)-source.tar.xz texlive-$(date +%Y%m%d)-source/
Source0:	https://ctan.org/tex-archive/systems/texlive/Source/texlive-%{version}-source.tar.xz
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
BuildRequires:	slibtool
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
BuildRequires:	pkgconfig(poppler) >= 26.06.0
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
BuildRequires:	slibtool
BuildRequires:	make

#-----------------------------------------------------------------------
Patch1:		texlive-asymptote.patch
Patch2:		texlive-xdvi.patch
# New definition only misses default location...
Patch3:		texlive-texmfcnf.patch
Patch4:		texlive-20150521-clang-3.8.patch
Patch5:		texlive-c++20.patch
Patch7:		texlive-20210324-restore-poppler-support.patch
Patch8:		texlive-poppler-21.09.patch
Patch9:		texlive-20210324-poppler-22.03.patch
Patch10:	texlive-20210324-poppler-22.04.patch
Patch11:	texlive-20220321-poppler-22.09.patch
Patch12:	texlive-20250506-poppler-25.05.patch
Patch13:	texlive-20220321-fix-m4-syntax-errors.patch
Patch14:	texlive-20220321-ghostscript-10.patch
patch16:	texlive-2025-poppler-25.11.patch
Patch17:	texlive-2025-poppler-26.02.patch
Patch18:	texlive-poppler-26.03.patch
Patch19:	texlive-poppler-26.05.patch
Patch20:	texlive-poppler-26.07.patch
# LFS sometimes (not yet for 2023) has useful patches at
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
# texlive-*.bin subpackages + texlive-extras are generated at the end of
# %install by tools from texlive-tlpkg (BuildRequires) into %%{specpartsdir}.
#-----------------------------------------------------------------------
%libpackage synctex 2

%define synctex_devel %{mklibname -d synctex}
%package -n %{synctex_devel}
Summary:	SyncTeX development files
Group:		Development/C
Requires:	texlive-synctex.bin = %{version}-%{release}
Requires:	%{mklibname synctex} = %{version}-%{release}

%description -n %{synctex_devel}
This package includes the SyncTeX development files.

%files -n %{synctex_devel}
%{_includedir}/synctex
%{_libdir}/libsynctex.so
%{_libdir}/pkgconfig/synctex.pc
%ifnarch %{riscv} %{mips} %{power64} s390 s390x
%libpackage texluajit 2
%endif
%libpackage texlua53 5

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
CXXFLAGS="%{optflags} -std=gnu++20 $(pkg-config --cflags poppler)" \
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

%make_build LIBGS_LIBS="-lgs" XPDF_INCLUDES="$(pkg-config --cflags poppler) -DPOPPLER_VERSION=\\\"$(pkg-config --modversion poppler)\\\"" XPDF_LIBS="$(pkg-config --libs poppler)" LIBTOOL=slibtool-shared
popd

%if %{_texmf_enable_asymptote}
mkdir asympote
pushd asympote
CONFIGURE_TOP=../utils/asymptote
%configure							\
	--enable-gc=system					\
	--enable-texlive-build					\
	--datadir=%{_texmfdir}
%make_build LIBGS_LIBS="-lgs" LIBTOOL=slibtool-shared
popd
%endif

#-----------------------------------------------------------------------
%install
pushd texlive
%make_install LIBGS_LIBS="-lgs" LIBTOOL=slibtool-shared
popd

%if %{_texmf_enable_asymptote}
pushd asymptote
%make_install LIBGS_LIBS="-lgs" LIBTOOL=slibtool-shared
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

# Drop noarch-owned script wrappers; create engine/format sibling links.
# Tools + maps come from texlive-tlpkg (BuildRequires).
%{_rpmconfigdir}/texlive-fixup-bindir %{buildroot} \
	--remove-map %{_rpmconfigdir}/texlive-bindir-remove.map \
	--links-map %{_rpmconfigdir}/texlive-engine-links.map

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

# Auto-generate texlive-*.bin / texlive-extras from tlpdb + bindir (texlive-tlpkg).
%{_rpmconfigdir}/texlive-generate-bin-specparts \
	%{buildroot} %{specpartsdir} %{_tlpkgdir}/texlive.tlpdb.xz %{version}
