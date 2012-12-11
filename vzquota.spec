Summary: Virtuozzo/OpenVZ disk quota control utility
Name: vzquota
Version: 3.0.12
Release: %mkrel 3
License: GPLv2
Group: System/Kernel and hardware
Source: http://download.openvz.org/utils/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
Patch0: vzquota-3.0.12-fixbuild.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://openvz.org/

%description
This utility allows system administator to control disk quotas
for Virtuozzo/OpenVZ containers.

%prep
%setup -q
%patch0 -p1

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) %{_sbindir}/vzquota
%attr(755,root,root) %{_sbindir}/vzdqcheck
%attr(755,root,root) %{_sbindir}/vzdqdump
%attr(755,root,root) %{_sbindir}/vzdqload
%attr(755,root,root) %{_var}/vzquota
%attr(644,root,root) %{_mandir}/man8/vzquota.8*
%attr(644,root,root) %{_mandir}/man8/vzdqcheck.8*
%attr(644,root,root) %{_mandir}/man8/vzdqdump.8*
%attr(644,root,root) %{_mandir}/man8/vzdqload.8*


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0.12-3mdv2011.0
+ Revision: 615422
- the mass rebuild of 2010.1 packages

* Sat May 01 2010 Funda Wang <fwang@mandriva.org> 3.0.12-2mdv2010.1
+ Revision: 541416
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Feb 04 2009 Jérôme Soyer <saispo@mandriva.org> 3.0.12-1mdv2009.1
+ Revision: 337525
- import vzquota


