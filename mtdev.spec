Summary:	Multitouch library
Name:		mtdev
Version:	1.1.5
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://bitmath.org/code/mtdev/%{name}-%{version}.tar.bz2
# Source0-md5:	52c9610b6002f71d1642dc1a1cca5ec1
URL:		http://bitmath.org/code/mtdev/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mtdev is a stand-alone library which transforms all variants of
kernel MT events to the slotted type B protocol. The events put into
mtdev may be from any MT device, specifically type A without contact
tracking, type A with contact tracking, or type B with contact
tracking. See the kernel documentation for further details.

%package devel
Summary:	Header files for mtdev library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for use with mtdev library.

%package tools
Summary:	Tools for mtdev library
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description tools
mtdev test tool.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libmtdev.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmtdev.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmtdev.so
%{_includedir}/mtdev*.h
%{_pkgconfigdir}/mtdev.pc

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mtdev-test

