%define upstream_name    B-Hooks-OP-Check
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.19
Release:	3

Summary:	Wrap OP check callbacks
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/B/B-Hooks-OP-Check-0.19.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(parent)
Requires:	perl(parent)

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorarch}/B
%{perl_vendorarch}/auto/B

%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.180.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.180.0-3
+ Revision: 680527
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-2mdv2011.0
+ Revision: 555685
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 402085
- rebuild using %%perl_convert_version

* Tue Jul 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2010.0
+ Revision: 393192
- update to new version 0.18

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2010.0
+ Revision: 370009
- update to new version 0.17

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-2mdv2009.1
+ Revision: 307129
- fix missing dependency on perl-parent

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2009.1
+ Revision: 307063
- import perl-B-Hooks-OP-Check


* Wed Nov 26 2008 cpan2dist 0.15-1mdv
- initial mdv release, generated with cpan2dist


