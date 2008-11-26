%define module   B-Hooks-OP-Check
%define version    0.15
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Wrap OP check callbacks
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/B/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-parent
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module provides a c api for XS modules to hook into the callbacks of
'PL_check'.

the ExtUtils::Depends manpage is used to export all functions for other XS
modules to use. Include the following in your Makefile.PL:

    my $pkg = ExtUtils::Depends->new('Your::XSModule', 'B::Hooks::OP::Check');
    WriteMakefile(
        ... # your normal makefile flags
        $pkg->get_makefile_vars,
    );

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorarch/B
%perl_vendorarch/auto/B

