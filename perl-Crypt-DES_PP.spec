%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	DES_PP
Summary:	Crypt::DES_PP Perl module - DES implementation in pure Perl
Summary(pl):	Modu³ Perla Crypt::DES_PP - czysto perlowa implementacja DES
Name:		perl-Crypt-DES_PP
Version:	1.00
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The module is 100% compatible to Crypt::DES but is implemented
entirely in Perl. The module implements the Crypt::CBC interface.

%description -l pl
Ten modu³ jest w 100% kompatybilny z Crypt::DES, ale jest
zaimplementowany ca³kowicie w Perlu. Ma zaimplementowany interfejs
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
