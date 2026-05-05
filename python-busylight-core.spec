Name:           python-busylight-core
Version:        2.4.0
Release:        %autorelease
Summary:        Busylight Core Implementation for Humans, presumably like you!

License:        Apache-2.0
URL:            https://pypi.org/project/busylight-core/
Source:         %{pypi_source busylight_core}
Patch0:         uvbuild2setuptools-core.patch

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
A unified Python library for controlling USB status lights from multiple
vendors. Provides a consistent interface to control USB LED status lights
from Agile Innovative, CompuLab, EPOS, Embrava, Kuando, Luxafor, MuteMe,
Plantronics, and ThingM.}

%description %_description

%package -n     python3-busylight-core
Summary:        %{summary}

%description -n python3-busylight-core %_description


%prep
%autosetup -p1 -n busylight_core-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files busylight_core


%check
%pyproject_check_import


%files -n python3-busylight-core -f %{pyproject_files}


%changelog
%autochangelog
