Summary:	Mono ASP.NET Standalone Web Server
Summary(pl):	Serwer HTTP obs³uguj±cy ASP.NET
Name:		xsp
Version:	1.0
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Daemons
Source0:	http://mono2.ximian.com/archive/1.0/%{name}-%{version}.tar.gz
# Source0-md5:	cd681f02d0f93774ba126d77fd377f4b
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono-csharp >= 1.0
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Requires:	mono-csharp >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_httpdir	/home/services/httpd

%description
XSP provides a minimalistic web server which hosts the ASP.NET runtime
and can be used to test and debug web applications that use the
System.Web facilities in Mono.

%description -l pl
XSP to minimalistyczny serwer HTTP utrzymuj±cy aplikacje i strony
ASP.NET, który mo¿e byæ te¿ u¿ywany do testów i ¶ledzenia b³êdów
aplikacji u¿ywaj±cych klasy System.Web dostarczanej z pakietem Mono.

%prep
%setup -q -n %{name}-%{version}

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

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/httpd/httpd.conf,%{_examplesdir}/%{name}-%{version}} \
	$RPM_BUILD_ROOT%{_httpdir}/{.wapi,asp_net}

mv -f $RPM_BUILD_ROOT%{_docdir}/%{name}/test $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid http`" ]; then
	if [ "`getgid http`" != "51" ]; then
		echo "Error: group http doesn't have gid=51. Correct this before installing XSP." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 51 -r -f http
fi
if [ -n "`id -u http 2>/dev/null`" ]; then
	if [ "`id -u http`" != "51" ]; then
		echo "Error: user http doesn't have uid=51. Correct this before installing XSP." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 51 -r -d %{_httpdir} -s /bin/false -c "HTTP User" -g http http 1>&2
fi

%postun
/sbin/ldconfig
if [ "$1" = "0" ]; then
	/usr/sbin/userdel http
	/usr/sbin/groupdel http
fi


%files
%defattr(644,root,root,755)
%doc INSTALL NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/NUnitAsp.dll
%attr(750,http,http) %{_httpdir}/.wapi
%attr(750,http,http) %{_httpdir}/asp_net
%{_mandir}/man1/*
%{_examplesdir}/%{name}-%{version}
