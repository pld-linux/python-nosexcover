#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	nose.plugins.cover extension to add Cobertura-style XML reports
Summary(pl.UTF-8):	Rozszerzenie nose.plugins.cover dodające raporty XML w stylu Cobertury
Name:		python-nosexcover
Version:	1.0.11
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nosexcover/
Source0:	https://files.pythonhosted.org/packages/source/n/nosexcover/nosexcover-%{version}.tar.gz
# Source0-md5:	f32ef4824b4484343e9766b2c376365d
URL:		https://github.com/cmheisel/nose-xcover
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-coverage >= 3.4
BuildRequires:	python-nose
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-coverage >= 3.4
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A companion to the built-in nose.plugins.cover, this plugin will write
out an XML coverage report to a file named coverage.xml.

%description -l pl.UTF-8
Dodatek do wbudowanego nose.plugins.cover - wtyczka zapisująca raport
pokrycia XML do pliku o nazwie coverage.xml.

%package -n python3-nosexcover
Summary:	nose.plugins.cover extension to add Cobertura-style XML reports
Summary(pl.UTF-8):	Rozszerzenie nose.plugins.cover dodające raporty XML w stylu Cobertury
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-nosexcover
A companion to the built-in nose.plugins.cover, this plugin will write
out an XML coverage report to a file named coverage.xml.

%description -n python3-nosexcover -l pl.UTF-8
Dodatek do wbudowanego nose.plugins.cover - wtyczka zapisująca raport
pokrycia XML do pliku o nazwie coverage.xml.

%prep
%setup -q -n nosexcover-%{version}

%build
%if %{with python2}
%py_build

%{?with_tests:nosetests-%{py_ver} nosexcover}
%endif

%if %{with python3}
%py3_build

%{?with_tests:nosetests-%{py3_ver} nosexcover}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/nosexcover
%{py_sitescriptdir}/nosexcover-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-nosexcover
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/nosexcover
%{py3_sitescriptdir}/nosexcover-%{version}-py*.egg-info
%endif
