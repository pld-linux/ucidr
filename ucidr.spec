Summary:	A small static library for IPv4 CIDR operations
Name:		ucidr
Version:	1.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://unixservice.com/source/libs/%{name}-%{version}.tar.gz
# Source0-md5:	7f19628e97ec2d212bc66cbd7b3f4fdc
Patch0:		%{name}-include.patch
URL:		http://openisp.net/ucidr

%description
The ucidr program provides functions for determining if a given IPv4
is in a given IPv4 CIDR specified block among other basic CIDR
operations.

Current version provides these functions:

unsigned ExpandCIDR4(const char *cCIDR4, char *cIPs[]); unsigned
uIpv4InCIDR4(const char *cIPv4, const char *cCIDR4); unsigned
uInCIDR4Format(const char *cCIDR4,unsigned *uIPv4,unsigned
- *uCIDR4Mask); unsigned uInIpv4Format(const char *cIPv4,unsigned
- *uIPv4); unsigned uGetNumIPs(char *cCIDR4); unsigned
  uGetNumNets(char
- *cCIDR4);

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install

rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir} \
	includedir=%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%{_libdir}/openisp/libucidr.a
%{_includedir}/openisp/ucidr.h
