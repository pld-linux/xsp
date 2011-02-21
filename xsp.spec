%include /usr/lib/rpm/macros.mono
Summary:	Mono ASP.NET Standalone Web Server
Summary(pl.UTF-8):	Serwer HTTP obsługujący ASP.NET
Name:		xsp
Version:	2.10
Release:	1
Epoch:		1
License:	MIT X11
Group:		Networking/Daemons/HTTP
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	ftp://ftp.novell.com/pub/mono/sources/xsp/%{name}-%{version}.tar.bz2
# Source0-md5:	aec9369a00a9728801ea2587a1a8fd9c
URL:		http://www.mono-project.com/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	mono-csharp >= 2.10
BuildRequires:	pkgconfig
Requires:	mono-csharp >= 2.10
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
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/httpd/httpd.conf,%{_examplesdir}/%{name}-%{version}}

mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/test $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README 
%attr(755,root,root) %{_bindir}/asp-state
%attr(755,root,root) %{_bindir}/asp-state2
%attr(755,root,root) %{_bindir}/asp-state4
%attr(755,root,root) %{_bindir}/dbsessmgr
%attr(755,root,root) %{_bindir}/dbsessmgr2
%attr(755,root,root) %{_bindir}/dbsessmgr4
%attr(755,root,root) %{_bindir}/fastcgi-mono-server
%attr(755,root,root) %{_bindir}/fastcgi-mono-server2
%attr(755,root,root) %{_bindir}/fastcgi-mono-server4
%attr(755,root,root) %{_bindir}/mod-mono-server
%attr(755,root,root) %{_bindir}/mod-mono-server2
%attr(755,root,root) %{_bindir}/mod-mono-server4
%attr(755,root,root) %{_bindir}/xsp
%attr(755,root,root) %{_bindir}/xsp2
%attr(755,root,root) %{_bindir}/xsp4
%{_libdir}/%{name}
%{_prefix}/lib/mono/2.0/fastcgi-mono-server2.exe
%{_prefix}/lib/mono/2.0/mod-mono-server2.exe
%{_prefix}/lib/mono/2.0/xsp2.exe
%{_prefix}/lib/mono/4.0/fastcgi-mono-server4.exe
%{_prefix}/lib/mono/4.0/mod-mono-server4.exe
%{_prefix}/lib/mono/4.0/xsp4.exe
%{_prefix}/lib/mono/gac/Mono.WebServer2
%{_prefix}/lib/mono/gac/fastcgi-mono-server2
%{_prefix}/lib/mono/gac/fastcgi-mono-server4
%{_prefix}/lib/mono/gac/mod-mono-server2
%{_prefix}/lib/mono/gac/mod-mono-server4
%{_prefix}/lib/mono/gac/xsp2
%{_prefix}/lib/mono/gac/xsp4
%exclude %{_prefix}/lib/mono/gac/*/*/*.mdb
%{_mandir}/man1/asp-state.1*
%{_mandir}/man1/dbsessmgr.1*
%{_mandir}/man1/fastcgi-mono-server.1*
%{_mandir}/man1/mod-mono-server.1*
%{_mandir}/man1/xsp.1*

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/2.0/Mono.WebServer2.dll
%{_prefix}/lib/mono/4.0/Mono.WebServer2.dll
%{_prefix}/lib/monodoc/sources/Mono.FastCGI.*
%{_prefix}/lib/monodoc/sources/Mono.WebServer.*
%{_pkgconfigdir}/xsp-2.pc
%{_pkgconfigdir}/xsp-4.pc
%{_examplesdir}/%{name}-%{version}

%files debug
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/*/*/*.mdb
