%define	major 1
%define libname	%mklibname ykpers %{major}
%define develname %mklibname -d ykpers

Summary:	Yubikey Personalization
Name:		ykpers
Version:	1.7.0
Release:	1
Group:		System/Libraries
License:	BSD
URL:		http://code.google.com/p/yubikey-personalization/
Source0:	http://yubikey-personalization.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	http://yubikey-personalization.googlecode.com/files/%{name}-%{version}.tar.gz.sig
BuildRequires:	autoconf automake libtool
BuildRequires:	libyubikey-devel
BuildRequires:	libusb-devel

%description
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

%package -n	%{libname}
Summary:	The shared Yubikey Personalization library
Group:          System/Libraries

%description -n	%{libname}
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

%package -n	%{develname}
Summary:	Development files for the Yubikey Personalization library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} >= %{version}

%description -n	%{develname}
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

This package contains the development files for the ykpers library.

%package	tools
Summary:	Command line tools for ykpers
Group:          System/Libraries

%description	tools
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

This package contains various tools for ykpers.

%prep

%setup -q -n %{name}-%{version}

%build
#autoreconf -fis

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanups
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libykpers-*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/ykpers-1
%{_includedir}/ykpers-1/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files tools
%{_bindir}/ykchalresp
%{_bindir}/ykpersonalize
%{_mandir}/man1/*

