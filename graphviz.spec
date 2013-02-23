# disable madness
%define _unpackaged_subdirs_terminate_build 0

%define _disable_ld_no_undefined 1
%bcond_without static
%bcond_with libr

%define cdt_major 5
%define cgraph_major 6
%define graph_major 5
%define gvc_major 6
%define gvpr_major 2
%define pathplan_major 4
%define xdot_major 4

%define lib_cdt %mklibname cdt %{cdt_major}
%define lib_cgraph %mklibname cgraph %{cgraph_major}
%define lib_graph %mklibname graph %{graph_major}
%define lib_gvc %mklibname gvc %{gvc_major}
%define lib_gvpr %mklibname gvpr %{gvpr_major}
%define lib_pathplan %mklibname pathplan %{pathplan_major}
%define lib_xdot %mklibname xdot %{xdot_major}
%define develname %mklibname graphviz -d
%define staticname %mklibname graphviz -d -s

%if %{_use_internal_dependency_generator}
%define __noautoreq '/usr/bin/lua'
%endif

Summary:	Graph visualization tools
Name:		graphviz
Version:	2.30.1
Release:	1
Group:		Graphics
License:	Common Public License
URL:		http://www.graphviz.org
Source0:	http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
Patch0:		graphviz-2.30.1-linkage.patch
Patch5:		graphviz-2.30.1-ruby1.9.patch
BuildRequires:	bison >= 2.3
BuildRequires:	flex >= 2.5.4a
BuildRequires:	libtool
BuildRequires:	swig >= 1.3.29
BuildRequires:	expat-devel
BuildRequires:	gd-devel >= 2.0.34
BuildRequires:	gettext-devel >= 0.14.5
# jpeg:          No (only required by internal libgd)
#BuildRequires:	jpeg-devel
BuildRequires:	libltdl-devel
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

Conflicts: %{mklibname graphviz 4} < 2.20.3-3

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
Group:		Books/Computer books
Summary:	%{name} documentation

%description doc
The %{name} documentation.

%files doc
%{_datadir}/doc/%{name}

#-------------------------------------------------------------------------

%package -n %{lib_cdt}
Group:		System/Libraries
Summary:	Shared library for %{name}
Conflicts:	%{_lib}graphviz4 < 2.26

%description -n %{lib_cdt}
This package provides the cdt shared library for %{name}.

%files -n %{lib_cdt}
%{_libdir}/libcdt.so.%{cdt_major}*

#-------------------------------------------------------------------------

%package -n %{lib_cgraph}
Group:		System/Libraries
Summary:	Shared library for %{name}
Conflicts:	%{_lib}graphviz4 < 2.26

%description -n %{lib_cgraph}
This package provides the cgraph shared library for %{name}.

%files -n %{lib_cgraph}
%{_libdir}/libcgraph.so.%{cgraph_major}*

#-------------------------------------------------------------------------

%package -n %{lib_graph}
Group:		System/Libraries
Summary:	Shared library for %{name}
Conflicts:	%{_lib}graphviz4 < 2.26
Obsoletes:	%{_lib}graphviz4 < 2.26

%description -n %{lib_graph}
This package provides the graph shared library for %{name}.

%files -n %{lib_graph}
%defattr(-,root,root)
%{_libdir}/libgraph.so.%{graph_major}*

#-------------------------------------------------------------------------

%package -n %{lib_gvc}
Group:		System/Libraries
Summary:	Shared library for %{name}
Conflicts:	%{_lib}graphviz4 < 2.26

%description -n %{lib_gvc}
This package provides the gvc shared library for %{name}.

%files -n %{lib_gvc}
%{_libdir}/libgvc.so.%{gvc_major}*

#-------------------------------------------------------------------------

%package -n %{lib_gvpr}
Group:		System/Libraries
Summary:	Shared library for %{name}

%description -n %{lib_gvpr}
This package provides the gvpr shared library for %{name}.

%files -n %{lib_gvpr}
%{_libdir}/libgvpr.so.%{gvpr_major}*

#-------------------------------------------------------------------------

%package -n %{lib_pathplan}
Group:		System/Libraries
Summary:	Shared library for %{name}
Conflicts:	%{_lib}graphviz4 < 2.26

%description -n %{lib_pathplan}
This package provides the pathplan shared library for %{name}.

%files -n %{lib_pathplan}
%{_libdir}/libpathplan.so.%{pathplan_major}*

#-------------------------------------------------------------------------

%package -n %{lib_xdot}
Group:		System/Libraries
Summary:	Shared library for %{name}

%description -n %{lib_xdot}
This package provides the xdot shared library for %{name}.

%files -n %{lib_xdot}
%{_libdir}/libxdot.so.%{xdot_major}*

#-------------------------------------------------------------------------

%define lua_version %(if [ -x /usr/bin/lua ]; then lua -v 2>&1| awk '{print $2}' | awk -F. '{print $1 "." $2}'; fi)

%package -n lua-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for lua
BuildRequires: lua-devel
Obsoletes: %{mklibname graphvizlua 0}

%description -n lua-graphviz
This package provides the Lua extension for %{name}.

%files -n lua-graphviz
%{_libdir}/graphviz/lua
%{_libdir}/lua/%{lua_version}/gv.so

#-------------------------------------------------------------------------

%package  -n php-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for php
BuildRequires:	php-devel
BuildRequires:	php-cli
Obsoletes:	%{mklibname graphvizphp 0} < 2.28.0-4

%description -n php-graphviz
This package provides the PHP extension for %{name}.

%files -n php-graphviz
%{_libdir}/graphviz/php
%{_libdir}/php/modules/gv.so
%{_datadir}/php/gv.php

#-------------------------------------------------------------------------

%package -n python-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for python
Obsoletes:	%{mklibname graphvizpython 0} < 2.28.0-4
%py_requires -d

%description -n python-graphviz
This package provides the Python extension for %{name}.

%files -n python-graphviz
%{_libdir}/graphviz/python
%py_platsitedir/*

#-------------------------------------------------------------------------

%package -n ruby-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for ruby
BuildRequires:	ruby-devel
Obsoletes:	%{mklibname graphvizruby 0} < 2.28.0-4

%description -n ruby-graphviz
This package provides the Ruby extension for %{name}.

%files -n ruby-graphviz
%{_libdir}/graphviz/ruby
%{_prefix}/lib/ruby

#-------------------------------------------------------------------------

%package -n perl-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for perl
BuildRequires:	perl-devel
Obsoletes:	%{mklibname graphvizperl 0} < 2.28.0-4

%description -n perl-graphviz
This package provides the Perl extension for %{name}.

%files -n perl-graphviz
%{perl_vendorarch}/*
%{_libdir}/graphviz/perl

#-------------------------------------------------------------------------

%package -n tcl-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for tcl
BuildRequires:	tcl-devel >= 8.3.0
BuildRequires:	tk-devel >= 8.3.0
BuildRequires:	tk >= 8.3.0
Obsoletes:	%{mklibname graphviztcl 7 -d} < 2.28.0-4
Obsoletes:	%{mklibname graphviztcl 0} < 2.28.0-4

%description -n tcl-graphviz
This package provides the Tcl extension for %{name}.

%files -n tcl-graphviz
%{_libdir}/tcl*
%{_libdir}/graphviz/tcl

#-------------------------------------------------------------------------

%define jdk_path %{_prefix}/lib/jvm/java
%define java_includes %{_includedir}/libgcj

%package -n java-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for java
BuildRequires:	java-devel
Obsoletes:	%{mklibname graphvizjava 0} < 2.28.0-4

%description -n java-graphviz
This package provides the Java extension for %{name}.

%files -n java-graphviz
%{_libdir}/graphviz/java

#-------------------------------------------------------------------------
%if %with libr

%package -n r-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for R
BuildRequires:	libRmath-devel
Obsoletes:	%{mklibname graphvizr 0} < 2.28.0-4

%description -n r-graphviz
This package provides the R extension for %{name}.

%files -n r-graphviz
%{_libdir}/graphviz/R

%endif
#-------------------------------------------------------------------------

%package -n ocaml-graphviz
Group:		System/Libraries
Summary:	Graphviz bindings for OCaml
BuildRequires:	ocaml
Obsoletes:	%{mklibname graphvizocaml 0} < 2.28.0-4

%description -n ocaml-graphviz
This package provides the OCaml extension for %{name}.

%files -n ocaml-graphviz
%{_libdir}/graphviz/ocaml

#-------------------------------------------------------------------------

%package -n %{develname}
Group:		Development/Other
Summary:	Development package for %{name}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname graphviz -d 7} < 2.28.0-4
Obsoletes:	%{mklibname tcl -d 7} < 2.28.0-4
Obsoletes:	%{mklibname -d graphviz 3} < 2.28.0-4
Requires:	%{lib_cdt} = %{version}
Requires:	%{lib_cgraph} = %{version}
Requires:	%{lib_graph} = %{version}
Requires:	%{lib_gvc} = %{version}
Requires:	%{lib_gvpr} = %{version}
Requires:	%{lib_pathplan} = %{version}
Requires:	%{lib_xdot} = %{version}

%description -n %{develname}
Development package for %{name}.

%files -n %{develname}
%{_libdir}/pkgconfig/*
%{_libdir}/graphviz/*.so
%{_libdir}/*.so
%{_includedir}/graphviz

#-------------------------------------------------------------------------

%if ! %without static
%package -n %{staticname}
Group:		Development/Other
Summary:	Static development package for %{name}
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d -s graphviz 3} < 2.28.0-4

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
%patch5 -p0 -b .ruby19~
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

%make TK_LIB_SPEC="-ltcl -ltk" LIBS="-lX11"

%install
rm -rf %{buildroot}
%makeinstall_std

# fix documentation
install -d -m 755 %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/%{name}/doc %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/demo %{buildroot}%{_docdir}/%{name}

%post
%{_bindir}/dot -c

%postun
if ! test -x %{_bindir}/dot; then rm -f %{_libdir}/%{name}/config; fi

%changelog
* Thu Feb 16 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 2.28.0-4
+ Revision: 774845
- fix breakage with newer automake (P6)
- fix build with ruby 1.9 (P5)
- mass rebuild of ruby packages against ruby 1.9.1

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-3
+ Revision: 765932
- rebuilt for perl-5.14.2

* Wed Dec 14 2011 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-2
+ Revision: 741372
- revert the last commit as it didn't work and we need to move forward...
- fix linkage (funda wang)

  + Per Ãyvind Karlsen <peroyvind@mandriva.org>
    - don't manually remove .la files in %%install, it's handled by spec-helper now

  + Matthew Dawkins <mattydaw@mandriva.org>
    - added fixes for linking
    - fixed BRs
    - rebuild
    - cleaned up spec
    - converted BRs to pkgconfig provides
    - removed .la files
    - removed mkrel, buildroot, defattr, clean section
    - req for devel pkg to main

* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 2.28.0-1
+ Revision: 673577
- New version 2.28.0

* Wed Apr 27 2011 Funda Wang <fwang@mandriva.org> 2.26.3-7
+ Revision: 659617
- fix broken link

* Fri Feb 04 2011 Funda Wang <fwang@mandriva.org> 2.26.3-6
+ Revision: 635865
- rebuild
- tighten BR

* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 2.26.3-5mdv2011.0
+ Revision: 593059
- rebuild for py2.7

* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 2.26.3-4mdv2011.0
+ Revision: 583389
- rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.26.3-3mdv2011.0
+ Revision: 564281
- rebuild for perl 5.12.1

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 2.26.3-2mdv2011.0
+ Revision: 557038
- rebuild for perl 5.12

* Mon Feb 01 2010 Frederik Himpe <fhimpe@mandriva.org> 2.26.3-1mdv2010.1
+ Revision: 499306
- Update to new version 2.26.3
- Rediff format errors patch

* Fri Jan 29 2010 Funda Wang <fwang@mandriva.org> 2.26.0-3mdv2010.1
+ Revision: 498072
- rebuild for new ocaml

  + Shlomi Fish <shlomif@mandriva.org>
    - Correct many typos in the descriptions.

* Thu Dec 31 2009 Frederik Himpe <fhimpe@mandriva.org> 2.26.0-2mdv2010.1
+ Revision: 484287
- Add conflicts to library packages, to fix upgrade
- Move obsoletes to one library package instead of graphviz itself,
  because the latter pulls in additional X libraries, which might be
  unwanted

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 2.26.0-1mdv2010.1
+ Revision: 484088
- Update to new version 2.26.0

  + Christophe Fergeau <cfergeau@mandriva.com>
    - move Obsoletes from subpackages up to the main one
      urpmi can't deal with multiple packages obsoleting the same package, so it
      just doesn't do anything instead of upgrading the package to the newer version.
      We need anyway all the subpackages to be installed, so we can put the Obsoletes
      on the main package which drags all the subpackages.

* Wed Nov 18 2009 Oden Eriksson <oeriksson@mandriva.com> 2.24.0-2mdv2010.1
+ Revision: 467303
- force linkage against system libltdl.so.7

* Thu Sep 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.24.0-1mdv2010.0
+ Revision: 437324
- new version

* Thu Sep 10 2009 Helio Chissini de Castro <helio@mandriva.com> 2.22.2-5mdv2010.0
+ Revision: 436955
- Sanitize graphviz package to put proper name in subpackages and keep consistent with the rest of the distro
- Enable java package by default as we have a proper legal java sdk
- Disable R bindings as not working well
- Cleanup spec

* Mon Jun 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.22.2-4mdv2010.0
+ Revision: 390541
- rebuild for latest ocaml

* Fri Mar 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.22.2-3mdv2009.1
+ Revision: 361642
- fix wrong package names in obsoletes tags

* Mon Mar 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.22.2-2mdv2009.1
+ Revision: 360626
- split all libraries in individual subpackages (fix #49025)

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.22.2-1mdv2009.1
+ Revision: 358009
- new version
- drop xdg, linkage, gnomeui, bindings, tcl86 patches, not needed anymore
- update format-strings and system-libtool patches

* Wed Jan 28 2009 Funda Wang <fwang@mandriva.org> 2.20.3-10mdv2009.1
+ Revision: 334877
- use sys ltdl
- add lilnk to bindings
- build our own libtool
- rebuild for new libtool

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - don't build bundled libltdl

* Fri Jan 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.20.3-9mdv2009.1
+ Revision: 330329
- don't build lua bindings before 2009.0

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 2.20.3-8mdv2009.1
+ Revision: 319256
- rebuild for new ocaml

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 2.20.3-7mdv2009.1
+ Revision: 318548
- fix linkage
- more patches
- fix str fmt
- move python requirement into python subpackage
- fix patch
- rediff gnomeui patch

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 2.20.3-6mdv2009.1
+ Revision: 311074
- fix the patch
- add tcl86.patch (fix build for tcl 8.6)
- rebuild for new tcl

* Sun Nov 30 2008 Anssi Hannula <anssi@mandriva.org> 2.20.3-5mdv2009.1
+ Revision: 308312
- add a conflict on old libpackage due to the file move

* Wed Nov 26 2008 Adam Williamson <awilliamson@mandriva.org> 2.20.3-4mdv2009.1
+ Revision: 307169
- add xdg.patch (use xdg-open rather than firefox for opening urls)
- add gnomeui.patch (drops all gnomeui-related crap, it's useless)

* Wed Nov 26 2008 Adam Williamson <awilliamson@mandriva.org> 2.20.3-3mdv2009.1
+ Revision: 306894
- move the plugin 'libs' to the main package not the lib package (save more
  needless deps for apps that just use the libs)
- drop the libgnomeui br (apparently useless, just adds needless deps)

* Fri Nov 07 2008 Oden Eriksson <oeriksson@mandriva.com> 2.20.3-2mdv2009.1
+ Revision: 300719
- rebuilt against new libxcb

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 2.20.3-1mdv2009.1
+ Revision: 292265
- new version 2.20.3

* Mon Sep 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.20.2-3mdv2009.0
+ Revision: 286648
- drop non-working dependency exception, rpm-mandriva-setup has been fixed
- oops, don't keep duplicated doc files outside of /usr/share/doc

* Thu Sep 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.20.2-2mdv2009.0
+ Revision: 285738
- install doc files under %%_datadir/doc/%%name
- fix lua subpackage file list
- fix doc package dependencies

  + Pixel <pixel@mandriva.com>
    - fix build of dot_static when building with libgts

* Mon Jul 07 2008 Lev Givon <lev@mandriva.org> 2.20.2-1mdv2009.0
+ Revision: 232521
- Update to 2.20.2.
  Remove imageloading patch (no longer needed).

* Thu Jul 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.18-3mdv2009.0
+ Revision: 230926
- no need to workaround gs-config output anymore
- fix build dependencies
- fix build by allowing underlinking
- do not change dynamic loader configuration, everything under %%{_libdir}/graphviz/ is dlopened (fix #40881)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.18-2mdv2009.0
+ Revision: 202936
- add patch to fix image rendering in ps output (should fix #40568)

* Mon May 05 2008 Lev Givon <lev@mandriva.org> 2.18-1mdv2009.0
+ Revision: 201440
- Update to 2.18.

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.16.1-2mdv2008.1
+ Revision: 178360
- rebuild

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.16.1-1mdv2008.1
+ Revision: 156330
- new version
  enable ocaml and R bindings

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Lev Givon <lev@mandriva.org>
    - Update to 2.14.1.

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 2.12-6mdv2008.0
+ Revision: 82075
- rebuild for new soname of tk

* Sun Jul 15 2007 Funda Wang <fwang@mandriva.org> 2.12-5mdv2008.0
+ Revision: 52315
- Obsoletes old major

* Wed Jun 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.12-4mdv2008.0
+ Revision: 41846
- new devel library policy
- rebuild for expat


* Mon Mar 05 2007 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2.12-3mdv2007.1
+ Revision: 133388
- Fix group
- Fix group

* Wed Feb 28 2007 Nicholas Brown <nickbrown@mandriva.org> 2.12-2mdv2007.1
+ Revision: 127060
- Fix lib major version and BuildRequires

* Tue Feb 27 2007 Nicholas Brown <nickbrown@mandriva.org> 2.12-1mdv2007.1
+ Revision: 126358
- Version 2.12

* Wed Nov 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.8-7mdv2007.1
+ Revision: 88684
- Import graphviz

* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 2.8-7mdv2007.1
- fix build

* Mon Aug 14 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.8-6
- rebuild for fixed libxaw soname

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 2.8-4mdk
- Rebuild against latest libXaw.

* Sat May 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.8-4mdk
- spec cleanup
- fix duplicated directories
- move documentation in dedicated place

* Mon Mar 27 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.8-3mdk
- fix buildrequires: php4-devel => php-devel, add libltdl-devel

* Fri Mar 24 2006 Sebastien Savarin <plouf@mandriva.org> 2.8-2mdk
- Fix %%changelog

* Mon Mar 13 2006 Helio Chissini de Castro <helio@mandriva.com.br> 2.8-1mdv2007.1
- Update for 2.8
- Recreate bindings packages
- Devel package is now only one

* Thu Aug 18 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.2.1-3mdk
- lib64 & buildrequires fixes

* Mon Aug 01 2005 Couriousous <couriousous@mandriva.org> 2.2.1-2mdk
- Add linker file, thanks Abel Cheung for the sugestion

* Wed May 18 2005 Eskild Hustvedt <eskild@mandriva.org> 2.2.1-1mdk
- %%mkrel
- From Tigrux <tigrux@ximian.com>

* Wed Mar 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2-3mdk
- don't nuke rpath, it is required when building ImageMagick

* Thu Feb 10 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.2-2mdk
- multiarch, also fix typo in script that fooled check-multiarch-files

* Tue Feb 01 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2-1mdk
- 2.2
- use the %%configure2_5x macro
- fix pkgconfig location
- fix deps
- fix build on < 10.2 (autogen.sh)
- misc spec file fixes

* Tue Jan 25 2005 Pascal Terjan <pterjan@mandrake.org> 2.0-2mdk
- BuildRequires gd-devel

* Thu Jan 13 2005 Guillaume Rousse <guillomovitch@mandrake.org> 2.0-1mdk 
- new version
- back in official contribs

* Sun Sep 26 2004 Michael Scherer <misc@zarb.org> 1.12-3plf 
- rebuild, fix rpmlint warning

* Wed May 12 2004 Michael Scherer <misc@zarb.org> 1.12-2plf 
- fix plf reason
- fix email contact ( damned bug in rpmbuildupdate )
- fix prefix

* Tue May 11 2004 Michael Scherer <misc@mandrakesoft.com> 1.12-1mdk
- New release 1.12
- rpmbuildupdate aware
- plf reason

