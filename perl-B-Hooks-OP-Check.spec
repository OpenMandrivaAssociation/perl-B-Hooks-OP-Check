%define upstream_name    B-Hooks-OP-Check
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    Wrap OP check callbacks
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-parent
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:      perl-parent

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
