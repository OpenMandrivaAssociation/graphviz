# disable madness
%define _unpackaged_subdirs_terminate_build 0
%define _disable_ld_no_undefined 1
%bcond_without static
%bcond_with libr
%bcond_with bootstrap
%if %{with bootstrap}
%bcond_with java
%endif

%define cdt_major 5
%define cgraph_major 6
%define graph_major 5
%define gvc_major 6
%define gvpr_major 2
%define pathplan_major 4
%define xdot_major 4

%define libcdt %mklibname cdt %{cdt_major}
%define libcgraph %mklibname cgraph %{cgraph_major}
%define libgvc %mklibname gvc %{gvc_major}
%define libgvpr %mklibname gvpr %{gvpr_major}
%define libpathplan %mklibname pathplan %{pathplan_major}
%define libxdot %mklibname xdot %{xdot_major}
%define devname %mklibname graphviz -d
%define staticname %mklibname graphviz -d -s

%if %{_use_internal_dependency_generator}
%define __noautoreq '(/usr/bin/lua|/usr/bin/php|/usr/bin/tclsh)'
%endif

Summary:	Graph visualization tools
Name:		graphviz
Version:	2.36.0
Release:	11
Group:		Graphics
License:	Common Public License
Url:		http://www.graphviz.org
Source0:	http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
Patch0:		graphviz-2.30.1-linkage.patch
Patch5:		graphviz-2.36.0-ruby1.9.patch

BuildRequires:	bison >= 2.3
BuildRequires:	flex >= 2.5.4a
BuildRequires:	swig >= 1.3.29
BuildRequires:	gd-devel >= 2.0.34
BuildRequires:	gettext-devel >= 0.14.5
# jpeg:          No (only required by internal libgd)
#BuildRequires:	jpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	pkgconfig(gtkgl-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(zlib)

%description
A collection of tools for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%files
%dir %{_libdir}/%{name}
%{_bindir}/*
%_mandir/man?/*
%{_datadir}/graphviz
%{_libdir}/graphviz/*.so.*

#-------------------------------------------------------------------------

%package doc
Summary:	%{name} documentation
Group:		Books/Computer books

%description doc
The %{name} documentation.

%files doc
%{_datadir}/doc/%{name}

#-------------------------------------------------------------------------

%package -n %{libcdt}
Group:		System/Libraries
Summary:	Shared library for %{name}

%description -n %{libcdt}
This package provides the cdt shared library for %{name}.

%files -n %{libcdt}
%{_libdir}/libcdt.so.%{cdt_major}*

#-------------------------------------------------------------------------

%package -n %{libcgraph}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libcgraph}
This package provides the cgraph shared library for %{name}.

%files -n %{libcgraph}
%{_libdir}/libcgraph.so.%{cgraph_major}*

#-------------------------------------------------------------------------

%package -n %{libgvc}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libgvc}
This package provides the gvc shared library for %{name}.

%files -n %{libgvc}
%{_libdir}/libgvc.so.%{gvc_major}*

#-------------------------------------------------------------------------

%package -n %{libgvpr}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libgvpr}
This package provides the gvpr shared library for %{name}.

%files -n %{libgvpr}
%{_libdir}/libgvpr.so.%{gvpr_major}*

#-------------------------------------------------------------------------

%package -n %{libpathplan}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libpathplan}
This package provides the pathplan shared library for %{name}.

%files -n %{libpathplan}
%{_libdir}/libpathplan.so.%{pathplan_major}*

#-------------------------------------------------------------------------

%package -n %{libxdot}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libxdot}
This package provides the xdot shared library for %{name}.

%files -n %{libxdot}
%{_libdir}/libxdot.so.%{xdot_major}*

#-------------------------------------------------------------------------

%define lua_version %(if [ -x /usr/bin/lua ]; then lua -v 2>&1| awk '{print $2}' | awk -F. '{print $1 "." $2}'; fi)

%package -n lua-graphviz
Summary:	Graphviz bindings for lua
Group:		System/Libraries
BuildRequires:	pkgconfig(lua)

%description -n lua-graphviz
This package provides the Lua extension for %{name}.

%files -n lua-graphviz
%{_libdir}/graphviz/lua
%{_libdir}/lua/%{lua_version}/gv.so

#-------------------------------------------------------------------------

%package  -n php-graphviz
Summary:	Graphviz bindings for php
Group:		System/Libraries
BuildRequires:	php-devel
BuildRequires:	php-cli

%description -n php-graphviz
This package provides the PHP extension for %{name}.

%files -n php-graphviz
%{_libdir}/graphviz/php
%{_libdir}/php/modules/gv.so
%{_datadir}/php/gv.php

#-------------------------------------------------------------------------

%package -n python-graphviz
Summary:	Graphviz bindings for python
Group:		System/Libraries
BuildRequires: python-devel

%description -n python-graphviz
This package provides the Python extension for %{name}.

%files -n python-graphviz
%{_libdir}/graphviz/python
%py_platsitedir/*

#-------------------------------------------------------------------------

%package -n ruby-graphviz
Summary:	Graphviz bindings for ruby
Group:		System/Libraries
BuildRequires:	pkgconfig(ruby)
BuildRequires:	jruby-devel

%description -n ruby-graphviz
This package provides the Ruby extension for %{name}.

%files -n ruby-graphviz
%{_libdir}/graphviz/ruby
%{ruby_vendorarchdir}/*

#-------------------------------------------------------------------------

%package -n perl-graphviz
Summary:	Graphviz bindings for perl
Group:		System/Libraries
BuildRequires:	perl-devel

%description -n perl-graphviz
This package provides the Perl extension for %{name}.

%files -n perl-graphviz
%{perl_vendorarch}/*
%{_libdir}/graphviz/perl

#-------------------------------------------------------------------------

%package -n tcl-graphviz
Summary:	Graphviz bindings for tcl
Group:		System/Libraries
BuildRequires:	pkgconfig(tcl)
BuildRequires:	pkgconfig(tk)

%description -n tcl-graphviz
This package provides the Tcl extension for %{name}.

%files -n tcl-graphviz
%{_libdir}/tcl*
%{_libdir}/graphviz/tcl

#-------------------------------------------------------------------------
# start of bcond_java
%if !%with java
%define jdk_path %{_prefix}/lib/jvm/java
%define java_includes %{_includedir}/libgcj

%package -n java-graphviz
Summary:	Graphviz bindings for java
Group:		System/Libraries
BuildRequires:	java-devel

%description -n java-graphviz
This package provides the Java extension for %{name}.

%files -n java-graphviz
%{_libdir}/graphviz/java
# end of bcond_java
%endif

#-------------------------------------------------------------------------
%if %with libr

%package -n r-graphviz
Summary:	Graphviz bindings for R
Group:		System/Libraries
BuildRequires:	pkgconfig(libRmath)

%description -n r-graphviz
This package provides the R extension for %{name}.

%files -n r-graphviz
%{_libdir}/graphviz/R

%endif
#-------------------------------------------------------------------------

%package -n ocaml-graphviz
Summary:	Graphviz bindings for OCaml
Group:		System/Libraries
BuildRequires:	ocaml

%description -n ocaml-graphviz
This package provides the OCaml extension for %{name}.

%files -n ocaml-graphviz
%{_libdir}/graphviz/ocaml
#-------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libcdt} = %{version}
Requires:	%{libcgraph} = %{version}
Requires:	%{libgvc} = %{version}
Requires:	%{libgvpr} = %{version}
Requires:	%{libpathplan} = %{version}
Requires:	%{libxdot} = %{version}

%description -n %{devname}
Development package for %{name}.

%files -n %{devname}
%{_libdir}/pkgconfig/*
%{_libdir}/graphviz/*.so
%{_libdir}/*.so
%{_includedir}/graphviz

#-------------------------------------------------------------------------

%if ! %without static
%package -n %{staticname}
Group:		Development/Other
Summary:	Static development package for %{name}
Requires:	%{devname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n %{staticname}
Static development package for %{name}.

%files -n %{staticname}
%{_libdir}/graphviz/*.a
%{_libdir}/*.a

%endif

#-------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .link
%patch5 -p1 -b .ruby19~
autoreconf -f

%build
%configure2_5x \
	--with-x \
%if %without static
	--disable-static \
%else
	--enable-static \
%endif
%if %with libr
	--enable-r \
%else
	--disable-r \
%endif
%if %with bootstrap
	--enable-ocaml \
	--enable-perl \
	--enable-php \
	--enable-python \
%endif
	--disable-guile \
	--disable-sharp \
	--with-pangocairo \
	--with-gtk \
	--with-libgd \
	--disable-io \
	--disable-dependency-tracking

%make TK_LIB_SPEC="-ltcl -ltk" LIBS="-lX11"

%install
%makeinstall_std

# fix documentation
install -d -m 755 %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/%{name}/doc %{buildroot}%{_docdir}/%{name}
%if !%without bootstrap
mv %{buildroot}%{_datadir}/%{name}/demo %{buildroot}%{_docdir}/%{name}
%endif

%post
%{_bindir}/dot -c

%postun
if ! test -x %{_bindir}/dot; then rm -f %{_libdir}/%{name}/config; fi

