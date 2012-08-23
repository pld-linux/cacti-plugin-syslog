%define		plugin	syslog
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Syslog Viewer for Cacti
Summary(pl.UTF-8):	Wtyczka do Cacti - Syslog
Name:		cacti-plugin-%{plugin}
Version:	1.22
Release:	7
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:syslog-v%{version}-1.tgz
# Source0-md5:	bed7d51a915e6dd0813766a09c31f2fe
URL:		http://docs.cacti.net/plugin:syslog
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	cacti
Requires:	cacti(pia) >= 2.8
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php-date
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

# bad depsolver
%define		_noautopear	pear

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
A comprehensive Syslog Alerting tool that support very large
partitioned databases.

Features:
- Message filter
- Message search
- Output to screen or file
- Date time picker
- Event Alerter
- Event Removal (for Events you don't want to see)

%description -l pl.UTF-8
Wtyczka do Cacti - Syslog to zintegrowany interfejs cacti do bazy
danych MySQL, którego można używać do logowania zdarzeń ze skryptów,
cacti czy czegokolwiek.

Jest to składnik konsolowy będący lekkim dodatkiem do monitorowania
dla cacti. Ponieważ schemat bazy danych jest oparty na syslogu, może
być skonfigurowany do używania sysloga-ng lub syslogd z kiwi dla
Windows, przez co zdarzenia mogą być skorelowane.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
