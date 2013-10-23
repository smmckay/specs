Name: clang
Version: 3.3
Release: 1%{?dist}
Summary: LLVM and clang
License: BSD
Source0: http://llvm.org/releases/%{version}/llvm-%{version}.src.tar.gz
Source1: http://llvm.org/releases/%{version}/cfe-%{version}.src.tar.gz
Patch0: clang-3.3-libdir.patch
Patch1: clang-3.3-builtin-include-dir.patch

BuildRequires: chrpath autoconf gcc-c++

%description


%prep
%setup -q -n llvm-%{version}.src
cd tools
mkdir clang && cd clang
tar -xzf %SOURCE1 --strip-components=1
cd ../..
%patch0 -p1
%patch1 -p1


%build
%configure \
	--enable-optimized \
	--enable-bindings=no
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -rf %{buildroot}/usr/{src,docs} %{buildroot}%{_libdir}/debug
find %{buildroot}%{_libdir} -name '*.a' -exec rm -f {} \;
chrpath -d %{buildroot}%{_bindir}/*


%check
make check


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/man1/clang.1.gz

