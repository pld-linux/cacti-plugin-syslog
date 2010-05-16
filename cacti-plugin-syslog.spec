%define		plugin	syslog
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Syslog
Summary(pl.UTF-8):	Wtyczka do Cacti - Syslog
Name:		cacti-plugin-syslog
Version:	0.5.2
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{plugin}-%{version}.zip
# Source0-md5:	1e2b1fc5b560452f937ccd0bca1af0a2
Patch0:		%{name}-config.patch
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
BuildRequires:	unzip
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Plugin for Cacti - Syslog is a cacti integrated interface to a MySQL
database that can be used to log events from scripts, cacti or
whatever.

It is the console component for a light weight monitoring addon for
cacti. Because the database schema is based on syslog, it can be
configured to use a syslog-ng or kiwi's syslogd for Windows database
so events can be correlated.

%description -l pl.UTF-8
Wtyczka do Cacti - Syslog to zintegrowany interfejs cacti do bazy
danych MySQL, którego można używać do logowania zdarzeń ze skryptów,
cacti czy czegokolwiek.

Jest to składnik konsolowy będący lekkim dodatkiem do monitorowania
dla cacti. Ponieważ schemat bazy danych jest oparty na syslogu, może
być skonfigurowany do używania sysloga-ng lub syslogd z kiwi dla
Windows, przez co zdarzenia mogą być skorelowane.

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%{plugindir}
