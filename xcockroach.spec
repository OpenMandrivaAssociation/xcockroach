Name: xcockroach
Version: 0.4
Release: %mkrel 10
Summary: Displays cockroaches on your desktop
License: GPL
Group: Toys
Url: http://xcockroach.free.fr/
Source0: %{name}-%{version}.tar.bz2
Patch0: xcockroach-0.4-flags.patch
BuildRequires: libx11-devel
BuildRequires: libxpm-devel
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
xcockroach displays cockroaches on your root  window,
they will look for windows and hide themselves under them.
It is a GPL clone of xroach, with many enhancements.

%prep
%setup -q
%patch0 -p0 -b .flags

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING TODO
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
