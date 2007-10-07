%define name	graphviz
%define version	2.14.1
%define release	%mkrel 1

%define build_java 0
%{?_with_java: %{expand: %%global build_java 1}}

%define jdk_path %{_prefix}/lib/jvm/java
%define java_includes %{_includedir}/libgcj

%define build_lua 1
%{?_without_lua: %{expand: %%global build_lua 0}}

%define enable_static 1
%{?_without_static: %{expand: %%global enable_static 0}}

%define major 4
%define oldmajor 3
%define ruby_major 0
%define php_major 0
%define lua_major 0
%define python_major 0
%define perl_major 0
%define java_major 0
%define tcl_major 0

%define libname %mklibname graphviz %{major}
%define develname %mklibname graphviz -d
%define staticname %mklibname graphviz -d -s

%define lib_ruby %mklibname graphvizruby %{ruby_major}
%define lib_php %mklibname graphvizphp %{php_major}
%define lib_lua %mklibname graphvizlua %{lua_major}
%define lib_python %mklibname graphvizpython %{python_major}
%define lib_perl %mklibname graphvizperl %{perl_major}
%define lib_java %mklibname graphvizjava %{java_major}
%define lib_tcl %mklibname graphviztcl %{tcl_major}


Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Graph visualization tools
Group:		Graphics
License:	Common Public License
URL:		http://www.graphviz.org
Source:		http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.bz2
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	freetype2-devel
BuildRequires:	pango-devel >= 1.10
BuildRequires:	gd-devel >= 2.0.34
BuildRequires:	gettext-devel
BuildRequires:	libcurl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	X11-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gnomeui2-devel
BuildRequires:	zlib-devel
BuildRequires:	chrpath
BuildRequires:	libexpat-devel
BuildRequires:	python-devel
BuildRequires:	php-devel
BuildRequires:	perl-devel
BuildRequires:	ruby-devel
BuildRequires:	swig-devel
BuildRequires:	tcl-devel >= 8.3.0
BuildRequires:	tk-devel >= 8.3.0
BuildRequires:	tk >= 8.3.0
BuildRequires:	libfontconfig-devel
%if %build_lua
BuildRequires:	lua-devel
%endif
%if %build_java
BuildRequires:	java-1.4.2-gcj-compat-devel
%endif
%py_requires -d
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A collection of tools for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%package doc
Group:		Books/Computer books
Summary:	%{name} documentation

%description doc
%{name} documentation

%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library for %{name}

%description -n %{libname}
This package provides shared library for %{name}.

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

%package -n %{develname}
Group:		Development/Other
Summary:	Development package for %{name}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	lib64graphviz7-devel
Obsoletes:	lib64graphviztcl7-devel
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{libname}-devel
Obsoletes:	%mklibname -d %name %oldmajor

%description -n %{develname}
Development package for %{name}

%if %enable_static
%package -n %{staticname}
Group:		Development/Other
Summary:	Static development package for %{name}
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	%{libname}-static-devel
Obsoletes:	%mklibname -d -s %name %oldmajor

%description -n %{staticname}
Static development package for %{name}
%endif

%prep
%setup -q

%build
sh autogen.sh

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
	--disable-guile \
	--disable-sharp \
	--disable-ocaml \
	--enable-ltdl \
	--with-pangocairo \
	--with-gtk \
	--with-libgd \
	--with-mng \
	--disable-io \
	--disable-dependency-tracking

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# fix documentation
install -d -m 755 %{buildroot}%{_datadir}/doc
mv %{buildroot}%{_datadir}/%{name}/doc %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}
mv %{buildroot}%{_datadir}/%{name}/demo %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}

mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}" >  %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}.conf

%clean
rm -rf %{buildroot}

%post
%{_bindir}/dot -c

%postun
if ! test -x %{_bindir}/dot; then rm -f %{_libdir}/%{name}/config; fi

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%{_bindir}/*
%_mandir/man?/*
%{_datadir}/graphviz

%files doc
%defattr(-,root,root)
%{_datadir}/doc/%{name}-doc-%{version}

%files -n %{libname}
%defattr(-,root,root)
%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%{_libdir}/graphviz/*.so.*
%{_libdir}/*.so.%{major}*

%if %build_lua
%files -n %lib_lua
%defattr(-,root,root)
%{_libdir}/graphviz/lua
%endif

%files -n %lib_php
%defattr(-,root,root)
%{_libdir}/graphviz/php

%files -n %lib_python
%defattr(-,root,root)
%{_libdir}/graphviz/python

%files -n %lib_ruby
%defattr(-,root,root)
%{_libdir}/graphviz/ruby

%files -n %lib_perl
%defattr(-,root,root)
%{_libdir}/graphviz/perl

%files -n %lib_tcl
%defattr(-,root,root)
%{_libdir}/graphviz/tcl
%{_libdir}/graphviz/pkgIndex.tcl

%if %build_java
%files -n %lib_java
%defattr(-,root,root)
%{_libdir}/graphviz/java
%endif

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
