#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pytest_tap
Version  : 3.3
Release  : 24
URL      : https://files.pythonhosted.org/packages/fc/65/df1488188d6a43525460e829ff887cf0330e2c0de6a806765925bdf37d30/pytest-tap-3.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/65/df1488188d6a43525460e829ff887cf0330e2c0de6a806765925bdf37d30/pytest-tap-3.3.tar.gz
Summary  : Test Anything Protocol (TAP) reporting plugin for pytest
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-pytest_tap-license = %{version}-%{release}
Requires: pypi-pytest_tap-python = %{version}-%{release}
Requires: pypi-pytest_tap-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pytest)
BuildRequires : pypi(tap.py)

%description
pytest-tap
==========
|version| |license| |travis| |travismac| |appveyor| |coverage|

%package license
Summary: license components for the pypi-pytest_tap package.
Group: Default

%description license
license components for the pypi-pytest_tap package.


%package python
Summary: python components for the pypi-pytest_tap package.
Group: Default
Requires: pypi-pytest_tap-python3 = %{version}-%{release}

%description python
python components for the pypi-pytest_tap package.


%package python3
Summary: python3 components for the pypi-pytest_tap package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_tap)
Requires: pypi(pytest)
Requires: pypi(tap.py)

%description python3
python3 components for the pypi-pytest_tap package.


%prep
%setup -q -n pytest-tap-3.3
cd %{_builddir}/pytest-tap-3.3
pushd ..
cp -a pytest-tap-3.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656401355
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_tap
cp %{_builddir}/pytest-tap-3.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_tap/8521b76892024fdde6e0ab4b291b133d05d0d074
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pytest_tap/8521b76892024fdde6e0ab4b291b133d05d0d074

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
