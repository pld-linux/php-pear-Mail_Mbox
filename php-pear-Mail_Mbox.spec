%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	Mbox
%define		_status		alpha

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Mbox PHP class to Unix MBOX parsing and using
Summary(pl):	%{_pearname} - klasa PHP Mbox do analizy i korzystania z unisowych skrzynek
Name:		php-pear-%{_pearname}
Version:	0.1.5
Release:	0.1
License:	LGPL
Group:		Development/Languages/PHP
# Source0-md5:	bb73829b44dbcc663b29c7e4726cc0fd
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It can split messages inside a Mbox, return the number of messages,
return, update or remove an specific message or add a message on the
Mbox.

This class has in PEAR status: %{_status}.

%description -l pl
Ta klasa mo¿e dzieliæ wiadomo¶ci wewn±trz skrzynek w formacie mbox,
zwracaæ liczbê wiadomo¶ci, zwracaæ, uaktualniaæ lub usuwaæ dan±
wiadomo¶æ lub dodaæ wiadomo¶æ do skrzynki.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
