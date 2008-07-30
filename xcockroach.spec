Name:		xcockroach
Version:        0.4
Release:        %mkrel 6
Summary:	Displays cockroaches on your desktop
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}.libdir.patch.bz2
License:	GPL
Group:		Toys
Url:		http://xcockroach.free.fr/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*

