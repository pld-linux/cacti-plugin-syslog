%define		namesrc	haloe
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Syslog
Summary(pl):	Wtyczka do Cacti - Syslog
Name:		cacti-plugin-syslog
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	9105635bc1e03565d0e72427eba38127
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - h.aloe is a cacti integrated interface to a MySQL
database that can be used to log events from scripts, cacti or
whatever.

It is the console component for a light weight monitoring addon for
cacti. Because the database schema is based on syslog,
it can be configured to use a syslog-ng or kiwi's syslogd for Windows
database so events can be correlated.

%description -l pl
Wtyczka do Cacti - h.aloe to zintegrowany interfejs cacti do bazy
danych MySQL, którego mo¿na u¿ywaæ do logowania zdarzeñ ze skryptów,
cacti czy czegokolwiek.

Jest to sk³adnik konsolowy bêd±cy lekkim dodatkiem do monitorowania
dla cacti. Poniewa¿ schemat bazy danych jest oparty na syslogu, mo¿e
byæ skonfigurowany do u¿ywania sysloga-ng lub syslogd z kiwi dla
Windows, przez co zdarzenia mog± byæ skorelowane.

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc haloe.txt README 
%{webcactipluginroot}
