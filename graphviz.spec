%bcond_without static
%bcond_with libr

%define cdt_major 4
%define cgraph_major 4
%define graph_major 4
%define gvc_major 5
%define pathplan_major 4

%define lib_cdt %mklibname cdt %{cdt_major}
%define lib_cgraph %mklibname cgraph %{cgraph_major}
%define lib_graph %mklibname graph %{graph_major}
%define lib_gvc %mklibname gvc %{gvc_major}
%define lib_pathplan %mklibname pathplan %{pathplan_major}
%define develname %mklibname graphviz -d
%define staticname %mklibname graphviz -d -s

Name: graphviz
Version: 2.22.2 
Release: %mkrel 5 
Summary:	Graph visualization tools
Group:		Graphics
License:	Common Public License
URL:		http://www.graphviz.org
Source:		http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
Patch4:		graphviz-2.22.2-fix-format-errors.patch
Patch6:		graphviz-2.22.2-use-system-libtool.patch
BuildRequires:	bison >= 2.3
BuildRequires:	flex >= 2.5.4a
BuildRequires:	swig >= 1.3.29
BuildRequires:	freetype2-devel >= 2.1.10
BuildRequires:	pango-devel >= 1.12.4
BuildRequires:	gd-devel >= 2.0.34
BuildRequires:	gettext-devel >= 0.14.5
BuildRequires:	libcurl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel >= 1.2.10
BuildRequires:	librsvg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	X11-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglarea2-devel
BuildRequires:	gtkglext-devel
BuildRequires:	zlib-devel >= 1.2.3
BuildRequires:	libexpat-devel >= 2.0.0

BuildRequires:	libfontconfig-devel >= 2.3.95
Conflicts: %{mklibname graphviz 4} < 2.20.3-3
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A collection of tools for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%files
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%{_bindir}/*
%_mandir/man?/*
%{_datadir}/graphviz
%{_libdir}/graphviz/*.so.*

#-------------------------------------------------------------------------

%package doc
Group:		Books/Computer books
Summary:	%{name} documentation

%description doc
%{name} documentation

%files doc
%defattr(-,root,root)
%{_datadir}/doc/%{name}

#-------------------------------------------------------------------------

%package -n %{lib_cdt}
Group:		System/Libraries
Summary:	Shared library for %{name}
Obsoletes:  %mklibname graphviz 4

%description -n %{lib_cdt}
This package provides cdt shared library for %{name}.

%files -n %{lib_cdt}
%defattr(-,root,root)
%{_libdir}/libcdt.so.%{cdt_major}*

#-------------------------------------------------------------------------

%package -n %{lib_cgraph}
Group:		System/Libraries
Summary:	Shared library for %{name}
Obsoletes:  %mklibname graphviz 4

%description -n %{lib_cgraph}
This package provides cgraph shared library for %{name}.

%files -n %{lib_cgraph}
%defattr(-,root,root)
%{_libdir}/libcgraph.so.%{cgraph_major}*

#-------------------------------------------------------------------------

%package -n %{lib_graph}
Group:		System/Libraries
Summary:	Shared library for %{name}
Obsoletes:  %mklibname graphviz 4

%description -n %{lib_graph}
This package provides graph shared library for %{name}.

%files -n %{lib_graph}
%defattr(-,root,root)
%{_libdir}/libgraph.so.%{graph_major}*

#-------------------------------------------------------------------------

%package -n %{lib_gvc}
Group:		System/Libraries
Summary:	Shared library for %{name}

%description -n %{lib_gvc}
This package provides gvc shared library for %{name}.

%files -n %{lib_gvc}
%defattr(-,root,root)
%{_libdir}/libgvc.so.%{gvc_major}*

#-------------------------------------------------------------------------

%package -n %{lib_pathplan}
Group:		System/Libraries
Summary:	Shared library for %{name}
Obsoletes:  %mklibname graphviz 4

%description -n %{lib_pathplan}
This package provides pathplan shared library for %{name}.

%files -n %{lib_pathplan}
%defattr(-,root,root)
%{_libdir}/libpathplan.so.%{pathplan_major}*

#-------------------------------------------------------------------------

%define lua_version %(if [ -x /usr/bin/lua ]; then lua -v 2>&1| awk '{print $2}' | awk -F. '{print $1 "." $2}'; fi)

%package -n lua-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for lua
BuildRequires: lua-devel
Obsoletes: %{mklibname graphvizlua 0}

%description -n lua-graphviz
This package provides shared library for %{name}.

%files -n lua-graphviz
%defattr(-,root,root)
%{_libdir}/graphviz/lua
%{_libdir}/lua/%{lua_version}/gv.so

#-------------------------------------------------------------------------

%package  -n php-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for php
BuildRequires: php-devel
BuildRequires: php-cli
Obsoletes: %{mklibname graphvizphp 0}

%description -n php-graphviz
This package provides shared library for %{name}.

%files -n php-graphviz
%defattr(-,root,root)
%{_libdir}/graphviz/php
%{_libdir}/php/modules/gv.so
%{_datadir}/php/gv.php

#-------------------------------------------------------------------------

%package -n python-graphviz
Group: System/Libraries
Summary: Graphviz bindings for python
Obsoletes: %{mklibname graphvizpython 0}
%py_requires -d

%description -n python-graphviz
This package provides shared library for %{name}.

%files -n python-graphviz
%defattr(-,root,root)
%{_libdir}/graphviz/python
%py_platsitedir/*

#-------------------------------------------------------------------------

%package -n ruby-graphviz
Group: System/Libraries
Summary: Graphviz bindings for ruby
BuildRequires: ruby-devel
Obsoletes: %{mklibname graphvizruby 0}

%description -n ruby-graphviz
This package provides shared library for %{name}.

%files -n ruby-graphviz
%defattr(-,root,root)
%{_libdir}/graphviz/ruby
%{_prefix}/lib/ruby

#-------------------------------------------------------------------------

%package -n perl-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for perl
BuildRequires:	perl-devel
Obsoletes: %{mklibname graphvizperl 0}

%description -n perl-graphviz
This package provides shared library for %{name}.

%files -n perl-graphviz
%defattr(-,root,root)
%{_prefix}/lib/perl*
%{_libdir}/graphviz/perl

#-------------------------------------------------------------------------

%package -n tcl-graphviz
Group: System/Libraries
Summary: Graphviz bindings for tcl
BuildRequires:	tcl-devel >= 8.3.0
BuildRequires:	tk-devel >= 8.3.0
BuildRequires:	tk >= 8.3.0
Obsoletes: %{mklibname graphviztcl 7 -d}
Obsoletes: %{mklibname graphviztcl 0}

%description -n tcl-graphviz
This package provides shared library for %{name}.

%files -n tcl-graphviz
%defattr(-,root,root)
%{_libdir}/tcl*
%{_libdir}/graphviz/tcl

#-------------------------------------------------------------------------

%define jdk_path %{_prefix}/lib/jvm/java
%define java_includes %{_includedir}/libgcj

%package -n java-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for java
BuildRequires:	java-devel
Obsoletes: %{mklibname graphvizjava 0}

%description -n java-graphviz
This package provides shared library for %{name}.

%files -n java-graphviz
%defattr(-,root,root)
%{_libdir}/graphviz/java

#-------------------------------------------------------------------------
%if %with libr

%package -n r-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for R
BuildRequires:	libRmath-devel
Obsoletes: %{mklibname graphvizr 0}

%description -n r-graphviz
This package provides shared library for %{name}.

%files -n r-graphviz
%defattr(-,root,root)
%{_libdir}/graphviz/R

%endif
#-------------------------------------------------------------------------

%package -n ocaml-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for OCaml
BuildRequires:	ocaml
Obsoletes: %{mklibname graphvizocaml 0}

%description -n ocaml-graphviz
This package provides shared library for %{name}.

%files -n ocaml-graphviz
%defattr(-,root,root)
%{_libdir}/graphviz/ocaml

#-------------------------------------------------------------------------

%define oldmajor 3

%package -n %{develname}
Group:		Development/Other
Summary:	Development package for %{name}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname graphviz -d 7}
Obsoletes:	%{mklibname graphviztcl -d 7}
Obsoletes:	%{mklibname -d %name %oldmajor}
Requires:	%{lib_cdt} = %{version}-%{release}
Requires:	%{lib_cgraph} = %{version}-%{release}
Requires:	%{lib_graph} = %{version}-%{release}
Requires:	%{lib_gvc} = %{version}-%{release}
Requires:	%{lib_pathplan} = %{version}-%{release}

%description -n %{develname}
Development package for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/graphviz/*.so
%{_libdir}/graphviz/*.la
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/graphviz

#-------------------------------------------------------------------------

%if ! %without static
%package -n %{staticname}
Group:		Development/Other
Summary:	Static development package for %{name}
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	%mklibname -d -s %name %oldmajor

%description -n %{staticname}
Static development package for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/graphviz/*.a
%{_libdir}/*.a

%endif

#-------------------------------------------------------------------------

%prep
%setup -q
%patch4 -p1 -b .format
%patch6 -p1 -b .libtool

%build
autoreconf -fi
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
	--enable-ocaml \
	--enable-perl \
	--enable-php \
	--enable-python \
	--disable-guile \
	--disable-sharp \
	--with-pangocairo \
	--with-gtk \
	--with-libgd \
	--disable-io \
	--disable-dependency-tracking

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# fix documentation
install -d -m 755 %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/%{name}/doc %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/demo %{buildroot}%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%post
%{_bindir}/dot -c

%postun
if ! test -x %{_bindir}/dot; then rm -f %{_libdir}/%{name}/config; fi

