Summary:	Mono ASP.NET Standalone Web Server
Summary(pl):	Serwer HTTP obs³uguj±cy ASP.NET
Name:		xsp
Version:	1.1.13
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.go-mono.com/sources/xsp/%{name}-%{version}.tar.gz
# Source0-md5:	58facfdb9d13d48f9e8ad5069500081d
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono-csharp >= 1.1.10
Requires:	mono-csharp >= 1.1.10
ExclusiveArch:	%{ix86} %{x8664} arm hppa ppc s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSP provides a minimalistic web server which hosts the ASP.NET runtime
and can be used to test and debug web applications that use the
System.Web facilities in Mono.

%description -l pl
XSP to minimalistyczny serwer HTTP utrzymuj±cy aplikacje i strony
ASP.NET, który mo¿e byæ te¿ u¿ywany do testów i ¶ledzenia b³êdów
aplikacji u¿ywaj±cych klasy System.Web dostarczanej z pakietem Mono.

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
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/1.0
%{_libdir}/%{name}/2.0
%{_mandir}/man1/*
%{_examplesdir}/%{name}-%{version}
