#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Business-SMA
Summary:	Math::Business::SMA - Perl extension for calculating SMAs
Summary(pl):	Math::Business::SMA - rozszerzenie Perla do obliczania SMA
Name:		perl-Math-Business-SMA
Version:	0.99
Release:	2
License:	unknown
Vendor:		Jettero Heller <jettero@cpan.org>
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Business::SMA - Perl extension for calculating simple moving averages.

%description -l pl
Math::Business::SMA - rozszerzenie Perla do obliczania SMA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Math/Business/SMA.pm
%{_mandir}/man3/*
