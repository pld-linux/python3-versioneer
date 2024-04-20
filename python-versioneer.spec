#
# Conditional build:
%bcond_with	tests	# unit tests (FIXME)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Easy VCS-based management of project version strings
Summary(pl.UTF-8):	Łatwe, oparte o VCS zarządzanie łańcuchami wersji projektu
Name:		python-versioneer
# keep 0.18 here for python2 support
Version:	0.18
Release:	1
License:	Public Domain
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/versioneer/
Source0:	https://files.pythonhosted.org/packages/source/v/versioneer/versioneer-%{version}.tar.gz
# Source0-md5:	c8000ed8adf127cc95fa2584e9810115
URL:		https://pypi.org/project/versioneer/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Versioneer is a tool to automatically update version strings (in
setup.py and the conventional "from PROJECT import _version" pattern)
by asking your version-control system about the current tree.

%description -l pl.UTF-8
Versioneer to narzędzie do automatycznego uaktualniania łańcuchów
wersji (w setup.py oraz konwencjonalnym wzorcu "from PROJECT import
_version), odpytując system kontroli wersji o bieżące drzewo.

%package -n python3-versioneer
Summary:	Easy VCS-based management of project version strings
Summary(pl.UTF-8):	Łatwe, oparte o VCS zarządzanie łańcuchami wersji projektu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-versioneer
Versioneer is a tool to automatically update version strings (in
setup.py and the conventional "from PROJECT import _version" pattern)
by asking your version-control system about the current tree.

%description -n python3-versioneer -l pl.UTF-8
Versioneer to narzędzie do automatycznego uaktualniania łańcuchów
wersji (w setup.py oraz konwencjonalnym wzorcu "from PROJECT import
_version), odpytując system kontroli wersji o bieżące drzewo.

%prep
%setup -q -n versioneer-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
# FIXME: how to unpack versioneer.py for tests?
%{__python} -m unittest discover -s test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
# FIXME: how to unpack versioneer.py for tests?
%{__python3} -m unittest discover -s test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/versioneer{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/versioneer{,-3}
ln -sf versioneer-3 $RPM_BUILD_ROOT%{_bindir}/versioneer
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md details.md developers.md
%attr(755,root,root) %{_bindir}/versioneer-2
%{py_sitescriptdir}/versioneer.py[co]
%{py_sitescriptdir}/versioneer-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-versioneer
%defattr(644,root,root,755)
%doc README.md details.md developers.md
%attr(755,root,root) %{_bindir}/versioneer
%attr(755,root,root) %{_bindir}/versioneer-3
%{py3_sitescriptdir}/versioneer.py
%{py3_sitescriptdir}/__pycache__/versioneer.cpython-*.py[co]
%{py3_sitescriptdir}/versioneer-%{version}-py*.egg-info
%endif
