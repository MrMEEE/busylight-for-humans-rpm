Name:           python-annotated-doc
Version:        0.0.4
Release:        %autorelease
Summary:        Document parameters inline with Annotated
License:        MIT
URL:            https://pypi.org/project/annotated-doc/
Source:         %{pypi_source annotated_doc}
Patch0:         pdm2setuptools-annotated-doc.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A library for documenting parameters, class attributes, return types,
and variables inline using Python's Annotated type hint.  Used by
FastAPI, Typer, SQLModel, and related projects.}

%description %_description

%package -n     python3-annotated-doc
Summary:        %{summary}

%description -n python3-annotated-doc %_description

%prep
%autosetup -p1 -n annotated_doc-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files annotated_doc

%check
%pyproject_check_import

%files -n python3-annotated-doc -f %{pyproject_files}

%changelog
%autochangelog
