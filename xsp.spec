Summary:	Mono ASP.NET Standalone Web Server
Summary(pl.UTF-8):	Serwer HTTP obsługujący ASP.NET
Name:		xsp
Version:	4.7.1
Release:	1
Epoch:		1
License:	MIT
Group:		Networking/Daemons/HTTP
Source0:	https://download.mono-project.com/sources/xsp/%{name}-%{version}.tar.gz
# Source0-md5:	cdcead997e96d86b24a2766f5f04e5d4
URL:		https://www.mono-project.com/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 4.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.015
Requires:	mono-csharp >= 4.0
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSP provides a minimalistic web server which hosts the ASP.NET runtime
and can be used to test and debug web applications that use the
System.Web facilities in Mono.

%description -l pl.UTF-8
XSP to minimalistyczny serwer HTTP utrzymujący aplikacje i strony
ASP.NET, który może być też używany do testów i śledzenia błędów
aplikacji używających klasy System.Web dostarczanej z pakietem Mono.

%package devel
Summary:	Development files for XSP
Summary(pl.UTF-8):	Pliki programistyczne XSP
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	monodoc

%description devel
Development files for XSP.

%description devel -l pl.UTF-8
Pliki programistyczne XSP.

%package debug
Summary:	xsp libraries debugging resources
Summary(pl.UTF-8):	Pliki umożliwiające debugowanie bibliotek xsp
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description debug
xsp libraries debugging resources.

%description debug -l pl.UTF-8
Pliki umożliwiające debugowanie bibliotek xsp.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I build/m4/shamrock -I build/m4/shave
%{__autoconf}
%{__automake}

%configure \
	--disable-static
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfpm_helper.la
# 2.0 profile is no longer supported
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{asp-state2,dbsessmgr2,fastcgi-mono-server2,mod-mono-server2,xsp2} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/xsp-2.pc
# switch default scripts to 4.0 profile
for f in asp-state dbsessmgr fastcgi-mono-server mod-mono-server xsp ; do
	ln -sf ${f}4 $RPM_BUILD_ROOT%{_bindir}/$f
done

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/httpd/httpd.conf,%{_examplesdir}/%{name}-%{version}}

%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/test $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README 
%attr(755,root,root) %{_bindir}/asp-state
%attr(755,root,root) %{_bindir}/asp-state4
%attr(755,root,root) %{_bindir}/dbsessmgr
%attr(755,root,root) %{_bindir}/dbsessmgr4
%attr(755,root,root) %{_bindir}/fastcgi-mono-server
%attr(755,root,root) %{_bindir}/fastcgi-mono-server4
%attr(755,root,root) %{_bindir}/mod-mono-server
%attr(755,root,root) %{_bindir}/mod-mono-server4
%attr(755,root,root) %{_bindir}/mono-fpm
%attr(755,root,root) %{_bindir}/shim
%attr(755,root,root) %{_bindir}/xsp
%attr(755,root,root) %{_bindir}/xsp4
%attr(755,root,root) %{_libdir}/libfpm_helper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfpm_helper.so.0
%{_libdir}/%{name}
%{_prefix}/lib/mono/4.5/fastcgi-mono-server4.exe
%{_prefix}/lib/mono/4.5/mod-mono-server4.exe
%{_prefix}/lib/mono/4.5/mono-fpm.exe
%{_prefix}/lib/mono/4.5/xsp4.exe
%{_prefix}/lib/mono/gac/Mono.WebServer2
%{_prefix}/lib/mono/gac/fastcgi-mono-server4
%{_prefix}/lib/mono/gac/mod-mono-server4
%{_prefix}/lib/mono/gac/mono-fpm
%{_prefix}/lib/mono/gac/xsp4
%exclude %{_prefix}/lib/mono/gac/*/*/*.mdb
%{_mandir}/man1/asp-state.1*
%{_mandir}/man1/dbsessmgr.1*
%{_mandir}/man1/fastcgi-mono-server.1*
%{_mandir}/man1/mod-mono-server.1*
%{_mandir}/man1/xsp.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfpm_helper.so
%{_prefix}/lib/mono/4.5/Mono.WebServer2.dll
%{_prefix}/lib/monodoc/sources/Mono.FastCGI.*
%{_prefix}/lib/monodoc/sources/Mono.WebServer.*
%{_pkgconfigdir}/xsp-4.pc
%{_examplesdir}/%{name}-%{version}

%files debug
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/*/*/*.mdb
