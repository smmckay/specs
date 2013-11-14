Name: glfw
Version: 3.0.3
Release: 1%{?dist}
Summary: glfw
License: BSD
Source0: glfw-%{version}.zip

BuildRequires: cmake28
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libXrandr-devel
BuildRequires: libXi-devel

%description


%package devel
Summary: glfw headers and cmake files
Requires: glfw
Requires: cmake28
Requires: mesa-libGL-devel
Requires: mesa-libGLU-devel
Requires: libXrandr-devel
Requires: libXi-devel


%description devel


%prep
%setup -q


%build
%cmake28 -G 'Unix Makefiles'
%__make %{?_smp_mflags}


%install
%make_install
rm -rf %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_libdir}/cmake %{buildroot}%{_libdir}/cmake28


%files
%defattr(-,root,root,-)
%{_libdir}/libglfw.so
%{_libdir}/libglfw.so.3
%{_libdir}/libglfw.so.3.0


%files devel
%defattr(-,root,root,-)
%{_libdir}/cmake28/glfw
%{_includedir}/GLFW

