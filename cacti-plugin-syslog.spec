%define		namesrc	syslog
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Syslog
Summary(pl.UTF-8):	Wtyczka do Cacti - Syslog
Name:		cacti-plugin-syslog
Version:	0.5.1
Release:	2
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{namesrc}-%{version}.zip
# Source0-md5:	85f438603c0dcab50b55322374ec26c4
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - Syslog is a cacti integrated interface to a MySQL
database that can be used to log events from scripts, cacti or
whatever.

It is the console component for a light weight monitoring addon for
cacti. Because the database schema is based on syslog,
it can be configured to use a syslog-ng or kiwi's syslogd for Windows
database so events can be correlated.

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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE 
%{webcactipluginroot}
