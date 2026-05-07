Name:           python-uvicorn
Version:        0.46.0
Release:        %autorelease
Summary:        The lightning-fast ASGI server
License:        BSD-3-Clause
URL:            https://pypi.org/project/uvicorn/
Source:         %{pypi_source uvicorn}
Patch0:         hatch2setuptools-uvicorn.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Uvicorn is an ASGI web server implementation for Python.
It supports HTTP/1.1 and WebSockets, and is built on top of
uvloop and httptools for high performance.}

%description %_description

%package -n     python3-uvicorn
Summary:        %{summary}

%description -n python3-uvicorn %_description

%prep
%autosetup -p1 -n uvicorn-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files uvicorn

%check
%pyproject_check_import

%files -n python3-uvicorn -f %{pyproject_files}

%changelog
%autochangelog
