%global pypi_name ruamel.yaml
%global pname ruamel-yaml
%global commit 171c3653fc01

%global with_python3 1

Name:           python-%{pname}
Version:        0.12.14
Release:        4%{?dist}
Summary:        YAML 1.2 loader/dumper package for Python 

License:        MIT
URL:            https://bitbucket.org/ruamel/yaml
#Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Use bitbucket sources so we can run the tests
Source0:        https://bitbucket.org/ruamel/yaml/get/%{version}.tar.gz#/%{pname}-%{version}.tar.gz
 
BuildRequires:  libyaml-devel

%description
ruamel.yaml is a YAML 1.2 loader/dumper package for Python.
It is a derivative of Kirill Simonov’s PyYAML 3.11

%package -n     python2-%{pname}
Summary:        YAML 1.2 loader/dumper package for Python 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# For tests
BuildRequires:  pytest
BuildRequires:  python2-ruamel-ordereddict
BuildRequires:  python2-typing
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2-ruamel-ordereddict
Requires:       python2-typing
Requires:       python-setuptools

%description -n python2-%{pname}
ruamel.yaml is a YAML 1.2 loader/dumper package for Python.
It is a derivative of Kirill Simonov’s PyYAML 3.11

%if 0%{?with_python3}
%package -n     python%{python3_pkgversion}-%{pname}
Summary:        YAML 1.2 loader/dumper package for Python 
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pname}
ruamel.yaml is a YAML 1.2 loader/dumper package for Python.
It is a derivative of Kirill Simonov’s PyYAML 3.11
%endif

%prep
%autosetup -n %{pname}-%{commit}
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python3}
%{__python3} setup.py install --single-version-externally-managed --skip-build --root $RPM_BUILD_ROOT
%endif

%{__python2} setup.py install --single-version-externally-managed --skip-build --root $RPM_BUILD_ROOT

%check
PYTHONPATH=$(echo build/lib.*%{python2_version}) py.test-%{python2_version} _test/test_*.py
%if 0%{?with_python3}
PYTHONPATH=$(echo build/lib.*%{python3_version}) py.test-%{python3_version} _test/test_*.py
%endif

%files -n python2-%{pname}
%license LICENSE
%doc README.rst
%{python2_sitearch}/ruamel
%{python2_sitearch}/_ruamel_yaml.so
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?-*.pth
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{pname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/ruamel
%{python3_sitearch}/_ruamel_yaml.cpython-35m-*
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?-*.pth
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Wed Oct 26 2016 Orion Poplawski <orion@cora.nwra.com> - 0.12.14-4
- Build python3 package
- Run tests

* Tue Oct 25 2016 Chandan Kumar <chkumar@redhat.com> - 0.12.14-3
- Disabling python3 as python3-ruamel-ordereddict not available

* Mon Oct 24 2016 Chandan Kumar <chkumar@redhat.com> - 0.12.14-2
- Fixed python2-typing runtime dependency issue

* Fri Oct 14 2016 Chandan Kumar <chkumar@redhat.com> - 0.12.14-1
- Initial package.
