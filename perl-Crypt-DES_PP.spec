%define		pdir	Crypt
%define		pnam	DES_PP
Summary:	Crypt::DES_PP Perl module - DES implementation in pure Perl
Summary(pl.UTF-8):	Moduł Perla Crypt::DES_PP - czysto perlowa implementacja DES
Name:		perl-Crypt-DES_PP
Version:	1.00
Release:	5
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2fdfee7afd3ffabdc85297b15e60d270
URL:		http://search.cpan.org/dist/Crypt-DES_PP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The module is 100% compatible to Crypt::DES but is implemented
entirely in Perl. The module implements the Crypt::CBC interface.

%description -l pl.UTF-8
Ten moduł jest w 100% kompatybilny z Crypt::DES, ale jest
zaimplementowany całkowicie w Perlu. Ma zaimplementowany interfejs
Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Crypt/DES_PP.pm
%{_mandir}/man3/*
