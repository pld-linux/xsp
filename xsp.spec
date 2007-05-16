
%include /usr/lib/rpm/macros.mono

Summary:	Mono ASP.NET Standalone Web Server
Summary(pl.UTF-8):	Serwer HTTP obsługujący ASP.NET
Name:		xsp
Version:	1.2.4
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.go-mono.com/sources/xsp/%{name}-%{version}.tar.bz2
# Source0-md5:	b1b9641d2ffeaca465a29ff62c5584e2
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono-csharp >= 1.1.10
Requires:	mono-csharp >= 1.1.10
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
%{__make} \
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
%doc AUTHORS ChangeLog NEWS README 
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man1/*
%{_pkgconfigdir}/*.pc
%exclude %{_prefix}/lib/mono/gac/*/*/*.mdb
%{_prefix}/lib/mono/1.0/*
%{_prefix}/lib/mono/2.0/*
%{_prefix}/lib/mono/gac/Mono.WebServer
%{_prefix}/lib/mono/gac/Mono.WebServer2
%{_prefix}/lib/mono/gac/mod-mono-server
%{_prefix}/lib/mono/gac/mod-mono-server2
%{_prefix}/lib/mono/gac/xsp
%{_prefix}/lib/mono/gac/xsp2
%{_examplesdir}/%{name}-%{version}

%files debug
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/*/*/*.mdb
