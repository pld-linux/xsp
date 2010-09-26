%include /usr/lib/rpm/macros.mono
Summary:	Mono ASP.NET Standalone Web Server
Summary(pl.UTF-8):	Serwer HTTP obsługujący ASP.NET
Name:		xsp
Version:	2.6.5
Release:	1
Epoch:		1
License:	MIT X11
Group:		Networking/Daemons/HTTP
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	ftp://ftp.novell.com/pub/mono/sources/xsp/%{name}-%{version}.tar.bz2
# Source0-md5:	46a4d05b10bd942245c7ba426a36841a
URL:		http://www.mono-project.com/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	mono-csharp >= 2.4.2
BuildRequires:	mono-jscript >= 2.4.2
BuildRequires:	pkgconfig
Requires:	mono-csharp >= 2.4.2
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
%{__make} -j1 \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_bindir}/asp-state*
%attr(755,root,root) %{_bindir}/dbsessmgr*
%attr(755,root,root) %{_bindir}/fastcgi-mono-server*
%attr(755,root,root) %{_bindir}/mod-mono-server*
%attr(755,root,root) %{_bindir}/xsp*
%{_libdir}/%{name}
%exclude %{_prefix}/lib/mono/gac/*/*/*.mdb
%{_prefix}/lib/mono/1.0/Mono.WebServer.dll
%{_prefix}/lib/mono/1.0/fastcgi-mono-server.exe
%{_prefix}/lib/mono/1.0/mod-mono-server.exe
%{_prefix}/lib/mono/1.0/xsp.exe
%{_prefix}/lib/mono/2.0/Mono.WebServer2.dll
%{_prefix}/lib/mono/2.0/fastcgi-mono-server2.exe
%{_prefix}/lib/mono/2.0/mod-mono-server2.exe
%{_prefix}/lib/mono/2.0/xsp2.exe
%{_prefix}/lib/mono/gac/Mono.WebServer
%{_prefix}/lib/mono/gac/Mono.WebServer2
%{_prefix}/lib/mono/gac/fastcgi-mono-server
%{_prefix}/lib/mono/gac/fastcgi-mono-server2
%{_prefix}/lib/mono/gac/mod-mono-server
%{_prefix}/lib/mono/gac/mod-mono-server2
%{_prefix}/lib/mono/gac/xsp
%{_prefix}/lib/mono/gac/xsp2
%{_pkgconfigdir}/xsp.pc
%{_pkgconfigdir}/xsp-2.pc
%{_mandir}/man1/asp-state.1*
%{_mandir}/man1/dbsessmgr.1*
%{_mandir}/man1/fastcgi-mono-server.1*
%{_mandir}/man1/mod-mono-server.1*
%{_mandir}/man1/xsp.1*
%{_examplesdir}/%{name}-%{version}

%files debug
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/*/*/*.mdb
