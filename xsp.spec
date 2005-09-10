Summary:	Mono ASP.NET Standalone Web Server
Summary(pl):	Serwer HTTP obs�uguj�cy ASP.NET
Name:		xsp
Version:	1.1.9
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.go-mono.com/sources/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9ded4f1dd882112abfc1b5bb0df367cf
#Patch0:		%{name}-Makefile.am.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono-csharp >= 1.0.6
Requires:	mono-csharp >= 1.0.6
ExcludeArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSP provides a minimalistic web server which hosts the ASP.NET runtime
and can be used to test and debug web applications that use the
System.Web facilities in Mono.

%description -l pl
XSP to minimalistyczny serwer HTTP utrzymuj�cy aplikacje i strony
ASP.NET, kt�ry mo�e by� te� u�ywany do test�w i �ledzenia b��d�w
aplikacji u�ywaj�cych klasy System.Web dostarczanej z pakietem Mono.

%prep
%setup -q -n %{name}-%{version}
#%patch0 -p1

%build
rm -rf $RPM_BUILD_ROOT
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
%doc INSTALL NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_libdir}/mono/1.0/*
%{_libdir}/mono/2.0/*
%{_libdir}/%{name}/1.0/*
%{_libdir}/%{name}/2.0/*
%{_mandir}/man1/*
%{_examplesdir}/%{name}-%{version}
