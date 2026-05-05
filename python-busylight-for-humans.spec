Name:           python-busylight-for-humans
Version:        1.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Control USB connected LED lights, like a human.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            ...
Source:         %{pypi_source busylight_for_humans}
Patch0:		uvbuild2setuptools.patch

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'busylight-for-humans' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-busylight-for-humans
Summary:        %{summary}

%description -n python3-busylight-for-humans %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
#%pyproject_extras_subpkg -n python3-busylight-for-humans # docs,web,webapi


%prep
%autosetup -p1 -n busylight_for_humans-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files ...


%check
%pyproject_check_import


%files -n python3-busylight-for-humans -f %{pyproject_files}


%changelog
%autochangelog
