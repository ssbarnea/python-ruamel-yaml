%global pypi_name ruamel.yaml
%global pname ruamel-yaml

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pname}
Version:        0.12.14
Release:        1%{?dist}
Summary:        YAML 1.2 loader/dumper package for Python 

License:        MIT
URL:            https://bitbucket.org/ruamel/yaml
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

BuildRequires:  libyaml-devel

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
ruamel.yaml is a YAML 1.2 loader/dumper package for Python.
It is a derivative of Kirill Simonov’s PyYAML 3.11

%package -n     python2-%{pname}
Summary:        YAML 1.2 loader/dumper package for Python 
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-ruamel-ordereddict
Requires:       python2-typing
Requires:       python-setuptools

%description -n python2-%{pname}
ruamel.yaml is a YAML 1.2 loader/dumper package for Python.
It is a derivative of Kirill Simonov’s PyYAML 3.11

%if 0%{?with_python3}
%package -n     python3-%{pname}
Summary:        YAML 1.2 loader/dumper package for Python 
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-ruamel-ordereddict
Requires:       python3-setuptools

%description -n python3-%{pname}
ruamel.yaml is a YAML 1.2 loader/dumper package for Python.
It is a derivative of Kirill Simonov’s PyYAML 3.11
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
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

%files -n python2-%{pname}
%license LICENSE
%doc README.rst
%{python2_sitearch}/ruamel
%{python2_sitearch}/_ruamel_yaml.so
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?-*.pth
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/ruamel
%{python3_sitearch}/_ruamel_yaml.cpython-35m-*
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?-*.pth
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Fri Oct 14 2016 Chandan Kumar <chkumar@redhat.com> - 0.12.14-1
- Initial package.
