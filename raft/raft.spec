Name:           raft
Version:        0.11.3
Release:        0.4%{?dist}
Summary:        C implementation of the Raft consensus protocol

License:        LGPLv3 with exceptions
URL:            https://github.com/canonical/raft
Source0:        %{URL}/archive/v%{version}.tar.gz
# https://github.com/canonical/raft/pull/259/
Patch0:         0.11.3-test_compress-Respect-32bit-architectures.patch
# https://github.com/canonical/raft/pull/261
Patch1:         0.11.3-test-integration-uv-skip-init-oom-test-on-tmpfs.patch
# https://github.com/canonical/raft/issues/263
Patch2:         0.11.3-Revert-test-runner-Define-order-of-constructors.patch

BuildRequires:  autoconf libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libuv)

%description
Fully asynchronous C implementation of the Raft consensus protocol. It consists
of a core part that implements the core Raft algorithm logic and a pluggable
interface defining the I/O implementation for networking and disk persistence.

%package benchmark
Summary:        Benchmark operating system disk write performance
BuildRequires:  pkgconfig(liburing)

%description benchmark
Benchmark operating system disk write performance.

%package devel
Summary:        Development libraries for raft
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and library for raft.

%package doc
Summary:        C-Raft documentation
BuildArch:      noarch
BuildRequires:  python-sphinx

%description doc
This package contains the C-Raft documentation in HTML format and some code
examples.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if 0%{?fedora} && 0%{?fedora} < 35
# Strict c11 mode results in build failure caused by included liburing headers
# See https://github.com/axboe/liburing/issues/181
sed -i '/std=c11/d' configure.ac
%endif

%build
autoreconf -i
%configure --disable-static --enable-benchmark
%make_build
sphinx-build -b html -d docs/_build/doctrees docs docs/_build/html

%install
%make_install
rm -f %{buildroot}%{_libdir}/libraft.la

%check
%make_build check

%ldconfig_scriptlets

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/libraft.so.*

%files benchmark
%license LICENSE
%{_bindir}/os-disk-write

%files devel
%{_libdir}/libraft.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/raft.h
%{_includedir}/raft/

%files doc
%license LICENSE
%doc docs/_build/html/
%doc example/

%changelog
* Sat Feb 05 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.11.3-0.3
- Replace tmpfs patch with upstream fix

* Sat Feb 05 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.11.3-0.2
- Re-add patch to fix build failures on COPR

* Sat Jan 22 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.11.3-0.1
- Update to 0.11.3.

* Wed Oct 27 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.11.2-0.2
- Add -doc and -benchmark subpackages
- Remove -static subpackage
- Various spec file cleanups related to packaging guidelines

* Mon Aug 23 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.11.2-0.1
- Update to 0.11.2.

* Sun Jun 20 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.11.1-0.1
- Update to 0.11.1.

* Tue May 11 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.10.1-0.1
- Update to 0.10.1

* Thu Apr 22 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.10.0-0.1.20210409gite318fd8
- Update to git snapshot e318fd8

* Sat Apr 03 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.10.0-0.1
- Update to 0.10.0

* Sat Mar 13 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.9.25-0.2.20210203git329e3d8
- Update to git snapshot 329e3d8

* Mon Jan 18 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.9.25-0.2.20201206gitf205aaf
- Update to git snapshot f205aaf5

* Sun Nov 22 2020 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.9.25-0.2.20201027gitc1539a7
- Update to git snapshot c1539a7.

* Thu Oct 22 2020 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.9.25-0.2.20201015git9761242
- Add patch to fix test for x86_64/aarch64

* Tue Oct 20 2020 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.9.25-0.1.20201015git9761242
- Initial package

