Name: perl-Time-modules
Version: 2006.0814
Release: 5%{?dist}
Summary: Perl modules for parsing dates and times       
Group: Development/Libraries
License: Copyright only and Public Domain
URL: http://search.cpan.org/dist/Time-modules/
Source0: http://www.cpan.org/authors/id/M/MU/MUIR/modules/Time-modules-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Time-modules provides several Perl modules, including Time::CTime,
Time::DaysInMonth, Time::JulianDay, Time::ParseDate, and Time::Timezone.
These modules can be useful for parsing and manipulating dates and times.

%prep
%setup -q -n Time-modules-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGELOG README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.0814-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.0814-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May  31 2008 Xavier Bachelot <xavier@bachelot.org> 2006.0814-3
- Remove '|| :' from %%check

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2006.0814-2
- rebuild for new perl (again)

* Sat Feb 16 2008 Chris Ricker <kaboom@oobleck.net> 2006.0814-1
- New upstream release

* Thu Feb 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2003.1126-5
- rebuild for new perl

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2003.1126-4.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 2003.1126-4
- Bump and rebuild

* Wed Feb 15 2006 Chris Ricker <kaboom@oobleck.net> 2003.1126-3
- Bump and rebuild

* Fri Jul 01 2005 Chris Ricker <kaboom@oobleck.net> 2003.1126-2
- Remove overly high perl version BuildRequires (Ralf Corsepius)

* Fri Jul 01 2005 Chris Ricker <kaboom@oobleck.net> 2003.1126-1
- Version is 2003.1126, not 0.2003.1126 (Ville Skyttä)

* Fri Jul 01 2005 Chris Ricker <kaboom@oobleck.net> 0.2003.1126-2
- license change, include README, simplify build (Ville Skyttä)
- Add dist tag

* Fri May 27 2005 Chris Ricker <kaboom@oobleck.net> 0.2003.1126-1
- Initial package
