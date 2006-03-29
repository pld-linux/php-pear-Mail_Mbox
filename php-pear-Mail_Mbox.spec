%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	Mbox
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Mbox PHP class to Unix MBOX parsing and using
Summary(pl):	%{_pearname} - klasa PHP Mbox do analizy i korzystania z uniksowych skrzynek
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	4
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	faa11b33d1ac28ca0f6fa96356a03751
URL:		http://pear.php.net/package/Mail_Mbox/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It can split messages inside a Mbox, return the number of messages,
return, update or remove an specific message or add a message on the
Mbox.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa mo¿e dzieliæ wiadomo¶ci wewn±trz skrzynek w formacie mbox,
zwracaæ liczbê wiadomo¶ci, zwracaæ, uaktualniaæ lub usuwaæ dan±
wiadomo¶æ lub dodaæ wiadomo¶æ do skrzynki.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
