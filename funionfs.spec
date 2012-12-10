%define fuseversion 2.5.2

Summary:	An union filesystem for FUSE 
Name:		funionfs
Version:	0.4.3
Release:	%mkrel 2
License:	GPLv2
Group:		System/Servers
URL:		http://funionfs.apiou.org
Source:		http://funionfs.apiou.org/file/%{name}-%{version}.tar.bz2
BuildRequires:	fuse-devel >= %{fuseversion}
Requires:	fuse >= %{fuseversion}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Funionfs is a filesystem which concatenate two or more directories. These
directories are hierarchised by Funionfs. Typically, you could use a mounted
filesystem wich is in read-only where you only read files and an upper
filesystem (empty at the start of the system) where you write modifications.
Funionfs is very useful for embedded linux (the system must resist powerfail)
and for live-cd Linux.

%prep
%setup -q -n %{name}-%{version}

%build 
rm -rf autom4te.cache
%configure2_5x
%make

%install
rm -fr %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README NEWS TODO BUGS
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-2mdv2011.0
+ Revision: 610778
- rebuild

* Sun Feb 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 505872
- update to 0.4.3
- Fix build (remove make distclean)
- Fix summary

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.4.2-4mdv2010.0
+ Revision: 428970
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.2-3mdv2009.0
+ Revision: 222292
- fix buildrequires on x86_64
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Feb 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-1mdv2007.0
+ Revision: 116595
- Import funionfs

* Tue Feb 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-1mdv2007.1
- use the correct tar ball

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-1mdk
- initial Mandriva package (mille-xterm import)

