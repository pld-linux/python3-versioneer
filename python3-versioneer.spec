#
# Conditional build:
%bcond_with	tests	# unit tests (FIXME)

Summary:	Easy VCS-based management of project version strings
Summary(pl.UTF-8):	Łatwe, oparte o VCS zarządzanie łańcuchami wersji projektu
Name:		python3-versioneer
Version:	0.29
Release:	1
License:	Public Domain
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/versioneer/
Source0:	https://files.pythonhosted.org/packages/source/v/versioneer/versioneer-%{version}.tar.gz
# Source0-md5:	1703d6ced3656553066fa71e42c5eee6
URL:		https://pypi.org/project/versioneer/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
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

%prep
%setup -q -n versioneer-%{version}

%build
%py3_build

%if %{with tests}
# FIXME: how to unpack versioneer.py for tests?
%{__python3} -m unittest discover -s test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/versioneer{,-3}
ln -sf versioneer-3 $RPM_BUILD_ROOT%{_bindir}/versioneer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md details.md developers.md
%attr(755,root,root) %{_bindir}/versioneer
%attr(755,root,root) %{_bindir}/versioneer-3
%{py3_sitescriptdir}/versioneer.py
%{py3_sitescriptdir}/__pycache__/versioneer.cpython-*.py[co]
%{py3_sitescriptdir}/versioneer-%{version}-py*.egg-info
