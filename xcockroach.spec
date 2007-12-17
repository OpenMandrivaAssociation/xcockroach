Name:		xcockroach
Version:        0.4
Release:        %mkrel 4
Summary:	Displays cockroaches on your desktop
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}.libdir.patch.bz2
License:	GPL
Group:		Toys
Url:		http://xcockroach.free.fr/
BuildRequires:  X11-devel

%description
xcockroach displays cockroaches on your root  window,
they will look for windows and hide themselves under them.
It is a GPL clone of xroach, with many enhancements.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make CFLAGS+=-fPIC

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING TODO
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/behaviors/
%{_libdir}/%{name}/behaviors/*
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/themes/
%{_datadir}/%{name}/themes/*
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*

