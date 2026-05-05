Name:           python-hidapi
Version:        0.15.0
Release:        %autorelease
Summary:        Python bindings for the HIDAPI C library
# cython-hidapi is triple-licensed; the Python binding may be used under any:
License:        (GPL-3.0-only OR BSD-3-Clause)
URL:            https://pypi.org/project/hidapi/
Source:         %{pypi_source hidapi}

BuildRequires:  python3-devel
BuildRequires:  hidapi-devel
BuildRequires:  gcc
BuildRequires:  libusb1-devel libusb1

%global _description %{expand:
Python bindings for the HIDAPI C library, providing access to USB and
Bluetooth HID devices on Linux, macOS, and Windows.  Two importable
modules are installed: hid (libusb backend) and hidraw (hidraw backend,
Linux only).}

%description %_description

%package -n     python3-hidapi
Summary:        %{summary}

%description -n python3-hidapi %_description

%prep
%autosetup -p1 -n hidapi-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hid hidraw

%check
%pyproject_check_import

%files -n python3-hidapi -f %{pyproject_files}

%changelog
%autochangelog
