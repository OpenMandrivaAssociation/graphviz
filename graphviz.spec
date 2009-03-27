%define name	graphviz
%define version	2.22.2
%define release	%mkrel 3

%define build_java 0
%{?_with_java: %{expand: %%global build_java 1}}

%define jdk_path %{_prefix}/lib/jvm/java
%define java_includes %{_includedir}/libgcj

%if %mdkversion >= 200900
    %define build_lua 1
%else
    %define build_lua 0
%endif
%{?_without_lua: %{expand: %%global build_lua 0}}

%define enable_static 1
%{?_without_static: %{expand: %%global enable_static 0}}

%define oldmajor 3
%define ruby_major 0
%define php_major 0
%define lua_major 0
%define python_major 0
%define perl_major 0
%define java_major 0
%define tcl_major 0
%define r_major 0
%define ocaml_major 0

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

%define lib_ruby %mklibname graphvizruby %{ruby_major}
%define lib_php %mklibname graphvizphp %{php_major}
%define lib_lua %mklibname graphvizlua %{lua_major}
%define lib_python %mklibname graphvizpython %{python_major}
%define lib_perl %mklibname graphvizperl %{perl_major}
%define lib_java %mklibname graphvizjava %{java_major}
%define lib_tcl %mklibname graphviztcl %{tcl_major}
%define lib_r %mklibname graphvizr %{r_major}
%define lib_ocaml %mklibname graphvizocaml %{ocaml_major}
%define lua_version %(if [ -x /usr/bin/lua ]; then lua -v 2>&1| awk '{print $2}' | awk -F. '{print $1 "." $2}'; fi)

Name:		%{name}
Version:	%{version}
Release:	%{release}
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
BuildRequires:	python-devel
BuildRequires:	php-devel
BuildRequires:	php-cli
BuildRequires:	perl-devel
BuildRequires:	ruby-devel
BuildRequires:	libRmath-devel
BuildRequires:	ocaml
BuildRequires:	tcl-devel >= 8.3.0
BuildRequires:	tk-devel >= 8.3.0
BuildRequires:	tk >= 8.3.0
BuildRequires:	libfontconfig-devel >= 2.3.95
%if %build_lua
BuildRequires:	lua-devel
%endif
%if %build_java
BuildRequires:	java-1.4.2-gcj-compat-devel
%endif
Conflicts:	%{_lib}graphviz4 < 2.20.3-3
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A collection of tools for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%package doc
Group:		Books/Computer books
Summary:	%{name} documentation

%description doc
%{name} documentation

%package -n %{lib_cdt}
Group:		System/Libraries
Summary:	Shared library for %{name}
Obsoletes:  %mklibname graphviz 4

%description -n %{lib_cdt}
This package provides cdt shared library for %{name}.

%package -n %{lib_cgraph}
Group:		System/Libraries
Summary:	Shared library for %{name}
Obsoletes:  %mklibname graphviz 4

%description -n %{lib_cgraph}
This package provides cgraph shared library for %{name}.

%package -n %{lib_graph}
Group:		System/Libraries
Summary:	Shared library for %{name}
Obsoletes:  %mklibname graphviz 4

%description -n %{lib_graph}
This package provides graph shared library for %{name}.

%package -n %{lib_gvc}
Group:		System/Libraries
Summary:	Shared library for %{name}

%description -n %{lib_gvc}
This package provides gvc shared library for %{name}.

%package -n %{lib_pathplan}
Group:		System/Libraries
Summary:	Shared library for %{name}
Obsoletes:  %mklibname graphviz 4

%description -n %{lib_pathplan}
This package provides pathplan shared library for %{name}.

%if %build_lua
%package -n %lib_lua
Group:		System/Libraries
Summary:	Graphviz bindings for lua
Provides:	lua-%{name} = %{version}-%{release}

%description -n %lib_lua
This package provides shared library for %{name}.
%endif

%package -n %lib_php
Group:		System/Libraries
Summary:	Graphviz bindings for php
Provides:	php-%{name} = %{version}-%{release}

%description -n %lib_php
This package provides shared library for %{name}.

%package -n %lib_python
Group:		System/Libraries
Summary:	Graphviz bindings for python
Provides:	python-%{name} = %{version}-%{release}
%py_requires -d

%description -n %lib_python
This package provides shared library for %{name}.

%package -n %lib_ruby
Group:		System/Libraries
Summary:	Graphviz bindings for ruby
Provides:	ruby-%{name} = %{version}-%{release}

%description -n %lib_ruby
This package provides shared library for %{name}.

%package -n %lib_perl
Group:		System/Libraries
Summary:	Graphviz bindings for perl
Provides:	perl-%{name} = %{version}-%{release}

%description -n %lib_perl
This package provides shared library for %{name}.

%package -n %lib_tcl
Group: System/Libraries
Summary:	Graphviz bindings for tcl
Obsoletes:	lib64graphviztcl7-devel
Provides:	tcl-%{name} = %{version}-%{release}

%description -n %lib_tcl
This package provides shared library for %{name}.

%if %build_java
%package -n %lib_java
Group:		System/Libraries
Summary:	Graphviz bindings for java
Provides:	java-%{name} = %{version}-%{release}

%description -n %lib_java
This package provides shared library for %{name}.
%endif

%package -n %lib_r
Group:		System/Libraries
Summary:	Graphviz bindings for R
Provides:	r-%{name} = %{version}-%{release}

%description -n %lib_r
This package provides shared library for %{name}.

%package -n %lib_ocaml
Group:		System/Libraries
Summary:	Graphviz bindings for OCaml
Provides:	ocaml-%{name} = %{version}-%{release}

%description -n %lib_ocaml
This package provides shared library for %{name}.

%package -n %{develname}
Group:		Development/Other
Summary:	Development package for %{name}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	lib64graphviz7-devel
Obsoletes:	lib64graphviztcl7-devel
Requires:	%{lib_cdt} = %{version}-%{release}
Requires:	%{lib_cgraph} = %{version}-%{release}
Requires:	%{lib_graph} = %{version}-%{release}
Requires:	%{lib_gvc} = %{version}-%{release}
Requires:	%{lib_pathplan} = %{version}-%{release}
Obsoletes:	%mklibname -d %name %oldmajor

%description -n %{develname}
Development package for %{name}

%if %enable_static
%package -n %{staticname}
Group:		Development/Other
Summary:	Static development package for %{name}
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	%mklibname -d -s %name %oldmajor

%description -n %{staticname}
Static development package for %{name}
%endif

%prep
%setup -q
%patch4 -p1 -b .format
%patch6 -p1 -b .libtool

%build
autoreconf -fi
%configure2_5x \
	--with-x \
%if ! %build_java
	--disable-java \
%endif
%if ! %build_lua
	--disable-lua \
%endif
%if ! %enable_static
	 --disable-static \
%else
	--enable-static \
%endif
	--enable-r \
	--enable-ocaml \
	--enable-perl \
	--enable-php \
	--enable-python \
	--disable-python23 \
	--disable-python24 \
	--disable-python25 \
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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%{_bindir}/*
%_mandir/man?/*
%{_datadir}/graphviz
%{_libdir}/graphviz/*.so.*

%files doc
%defattr(-,root,root)
%{_datadir}/doc/%{name}

%files -n %{lib_cdt}
%defattr(-,root,root)
%{_libdir}/libcdt.so.%{cdt_major}*

%files -n %{lib_cgraph}
%defattr(-,root,root)
%{_libdir}/libcgraph.so.%{cgraph_major}*

%files -n %{lib_graph}
%defattr(-,root,root)
%{_libdir}/libgraph.so.%{graph_major}*

%files -n %{lib_pathplan}
%defattr(-,root,root)
%{_libdir}/libpathplan.so.%{pathplan_major}*

%files -n %{lib_gvc}
%defattr(-,root,root)
%{_libdir}/libgvc.so.%{gvc_major}*

%if %build_lua
%files -n %lib_lua
%defattr(-,root,root)
%{_libdir}/graphviz/lua
%{_libdir}/lua/%{lua_version}/gv.so
%endif

%files -n %lib_php
%defattr(-,root,root)
%{_libdir}/graphviz/php
%{_libdir}/php/modules/gv.so
%{_datadir}/php/gv.php

%files -n %lib_python
%defattr(-,root,root)
%{_libdir}/python*
%{_libdir}/graphviz/python
%{_libdir}/graphviz/python23
%{_libdir}/graphviz/python24
%{_libdir}/graphviz/python25

%files -n %lib_ruby
%defattr(-,root,root)
%{_usr}/lib/ruby
%{_libdir}/graphviz/ruby

%files -n %lib_perl
%defattr(-,root,root)
%{_usr}/lib/perl*
%{_libdir}/graphviz/perl

%files -n %lib_tcl
%defattr(-,root,root)
%{_libdir}/tcl*
%{_libdir}/graphviz/tcl

%if %build_java
%files -n %lib_java
%defattr(-,root,root)
%{_libdir}/graphviz/java
%endif

%files -n %lib_r
%defattr(-,root,root)
%{_libdir}/graphviz/R

%files -n %lib_ocaml
%defattr(-,root,root)
%{_libdir}/graphviz/ocaml

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/graphviz/*.so
%{_libdir}/graphviz/*.la
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/graphviz

%if %enable_static
%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/graphviz/*.a
%{_libdir}/*.a
%endif
