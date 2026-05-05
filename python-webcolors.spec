Name:           python-webcolors
Version:        25.10.0
Release:        %autorelease
Summary:        A library for working with the color formats defined by HTML and CSS
License:        BSD-3-Clause
URL:            https://pypi.org/project/webcolors/
Source:         %{pypi_source webcolors}
Patch0:         pdm2setuptools-webcolors.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A library for working with the color formats defined by HTML and CSS.
Provides utilities for converting between different representations of
HTML/CSS colors, including hex codes, named colors, and RGB tuples.}

%description %_description

%package -n     python3-webcolors
Summary:        %{summary}

%description -n python3-webcolors %_description

%prep
%autosetup -p1 -n webcolors-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files webcolors

%check
%pyproject_check_import

%files -n python3-webcolors -f %{pyproject_files}

%changelog
%autochangelog
