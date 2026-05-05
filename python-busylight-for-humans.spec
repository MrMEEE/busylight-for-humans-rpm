Name:           python-busylight-for-humans
Version:        1.0.0
Release:        %autorelease
Summary:        Control USB connected LED lights, like a human.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://pypi.org/project/busylight-for-humans/
Source:         %{pypi_source busylight_for_humans}
Patch0:		uvbuild2setuptools.patch

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Control USB connected LED lights from multiple vendors with a unified
Python interface. Supports Agile Innovative, CompuLab, EPOS, Embrava,
Kuando, Luxafor, MuteMe, Plantronics, and ThingM devices.}

%description %_description

%package -n     python3-busylight-for-humans
Summary:        %{summary}

%description -n python3-busylight-for-humans %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
# Uncomment and adjust if you want to ship the web/webapi extras:
#%pyproject_extras_subpkg -n python3-busylight-for-humans web,webapi


%prep
%autosetup -p1 -n busylight_for_humans-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files busylight


%check
%pyproject_check_import


%files -n python3-busylight-for-humans -f %{pyproject_files}


%changelog
%autochangelog
