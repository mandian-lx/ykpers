%define	major 1
%define libname	%mklibname ykpers %{major}
%define develname %mklibname -d ykpers

Summary:	Yubikey Personalization
Name:		ykpers
Version:	1.17.3
Release:	1
Group:		System/Libraries
License:	BSD
URL:		https://developers.yubico.com/yubikey-personalization/
Source0:	https://developers.yubico.com/yubikey-personalization/Releases/%{name}-%{version}.tar.gz
Source1:	https://developers.yubico.com/yubikey-personalization/Releases/%{name}-%{version}.tar.gz.sig

BuildRequires:	autoconf automake libtool
BuildRequires:	libyubikey-devel
BuildRequires:	pkgconfig(libusb-1.0)

%description
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	The shared Yubikey Personalization library
Group:		System/Libraries

%description -n	%{libname}
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libykpers-*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for the Yubikey Personalization library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} >= %{version}

%description -n	%{develname}
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

This package contains the development files for the ykpers library.

%files -n %{develname}
%dir %{_includedir}/ykpers-1
%{_includedir}/ykpers-1/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%package tools
Summary:	Command line tools for ykpers
Group:		System/Libraries

%description tools
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

This package contains various tools for ykpers.

%files tools
%{_bindir}/ykchalresp
%{_bindir}/ykinfo
%{_bindir}/ykpersonalize
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
#autoreconf -fis
%configure
%make

%install
%makeinstall_std

