%define fuseversion 2.5.2

Summary:	FunionFS - An union filesystem for FUSE 
Name:		funionfs
Version:	0.4.2
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://funionfs.apiou.org
Source:		http://funionfs.apiou.org/file/%{name}-%{version}.tar.bz2
BuildRequires:	libfuse-devel >= %{fuseversion}
Requires:	fuse >= %{fuseversion}

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
make distclean

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


