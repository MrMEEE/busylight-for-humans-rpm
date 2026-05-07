Name:           python-typer
Version:        0.25.1
Release:        %autorelease
Summary:        Build great CLIs. Easy to code. Based on Python type hints.
License:        MIT
URL:            https://pypi.org/project/typer/
Source:         %{pypi_source typer}
Patch0:         pdm2setuptools-typer.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-annotated-doc
BuildRequires:  python3-click python3-shellingham python3-rich

# Runtime dependencies not yet available in RHEL 10 that may need separate specs:
#   python3dist(annotated-doc) >= 0.0.2  (new dep, check availability)
#   python3dist(shellingham) >= 1.3.0    (check availability in AppStream/EPEL)

%global _description %{expand:
Typer is a library for building CLI applications based on Python type
hints. Inspired by FastAPI, it enables you to create powerful and
user-friendly command-line interfaces with minimal code.}

%description %_description

%package -n     python3-typer
Summary:        %{summary}

%description -n python3-typer %_description

%prep
%autosetup -p1 -n typer-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files typer

%check
%pyproject_check_import

%files -n python3-typer -f %{pyproject_files}
/usr/bin/typer

%changelog
%autochangelog
