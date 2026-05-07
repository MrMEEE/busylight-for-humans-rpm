Name:           python-click
Version:        8.3.3
Release:        %autorelease
Summary:        Composable command line interface toolkit
License:        BSD-3-Clause
URL:            https://pypi.org/project/click/
Source:         %{pypi_source click}
Patch0:         flit2setuptools-click.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary.  It is the
"Command Line Interface Creation Kit".}

%description %_description

%package -n     python3-click
Summary:        %{summary}

%description -n python3-click %_description

%prep
%autosetup -p1 -n click-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files click

%check
%pyproject_check_import

%files -n python3-click -f %{pyproject_files}

%changelog
%autochangelog
