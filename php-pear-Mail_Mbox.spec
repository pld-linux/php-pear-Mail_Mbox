%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	Mbox
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Mbox PHP class to Unix MBOX parsing and using
Summary(pl.UTF-8):	%{_pearname} - klasa PHP Mbox do analizy i korzystania z uniksowych skrzynek
Name:		php-pear-%{_pearname}
Version:	0.6.3
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e65b8828d2c49b14fe17de33b30589b1
URL:		http://pear.php.net/package/Mail_Mbox/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Mail_Mbox-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It can split messages inside a Mbox, return the number of messages,
return, update or remove an specific message or add a message on the
Mbox.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa może dzielić wiadomości wewnątrz skrzynek w formacie mbox,
zwracać liczbę wiadomości, zwracać, uaktualniać lub usuwać daną
wiadomość lub dodać wiadomość do skrzynki.

Ta klasa ma w PEAR status: %{_status}.

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
