%define		namesrc	haloe
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Syslog
Summary(pl):	Wtyczka do Cacti - Syslog
Name:		cacti-plugin-syslog
Version:	0.1b
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	39eac8ae4b65b752d2991cbabbb3e58a
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - h.aloe is a cacti integrated interface to a mysql 
database that can be used to log events from scripts, cacti or 
whatever.
It is the console component for a light weight monitoring addon for
cacti. Because the database schema is based on syslog,
it can be configured to use a syslog-ng or kiwi's syslogd for windows
database so events can be correlated.

%description -l pl
Wtyczka do Cacti - 

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}
#look this
rm -r $RPM_BUILD_ROOT%{webcactipluginroot}/temp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme-haloe.txt
%{webcactipluginroot}
