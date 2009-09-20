Summary: Virtuozzo/OpenVZ disk quota control utility
Name: vzquota
Version: 3.0.12
Release: %mkrel 2
License: GPLv2
Group: System/Kernel and hardware
Source: http://download.openvz.org/utils/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://openvz.org/

%description
This utility allows system administator to control disk quotas
for Virtuozzo/OpenVZ containers.

%prep
%setup -q

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
