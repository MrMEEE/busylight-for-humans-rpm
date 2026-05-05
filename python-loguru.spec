Name:           python-loguru
Version:        0.7.3
Release:        %autorelease
Summary:        Python logging made (stupidly) simple
License:        MIT
URL:            https://pypi.org/project/loguru/
Source:         %{pypi_source loguru}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Loguru is a library which aims to bring enjoyable logging to Python.
It provides a simple, powerful and feature-rich logging interface with
zero boilerplate configuration.}

%description %_description

%package -n     python3-loguru
Summary:        %{summary}

%description -n python3-loguru %_description

%prep
%autosetup -p1 -n loguru-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files loguru

%check
%pyproject_check_import

%files -n python3-loguru -f %{pyproject_files}

%changelog
%autochangelog
