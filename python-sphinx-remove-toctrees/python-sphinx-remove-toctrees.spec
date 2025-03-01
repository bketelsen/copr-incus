Name:           python-sphinx-remove-toctrees
Version:        0.0.3
Release:        0.1%{?dist}
Summary:        Speed up Sphinx builds by selectively removing toctrees from some pages

License:        MIT
URL:            https://github.com/executablebooks/sphinx-remove-toctrees
Source0:        %{pypi_source sphinx-remove-toctrees}
 
BuildArch:      noarch
BuildRequires:  python3-devel
 
%global _description %{expand:
Improve your Sphinx build time by selectively removing TocTree objects
from pages. This is useful if your documentation uses auto-generated
API documentation, which generates a lot of stub pages.}
 
%description %_description
%package     -n python3-sphinx-remove-toctrees
Summary:        %{summary}
 
%description -n python3-sphinx-remove-toctrees %_description

%prep
%autosetup -n sphinx-remove-toctrees-%{version}
 
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_remove_toctrees

%check
%pyproject_check_import

%files -n python3-sphinx-remove-toctrees -f %{pyproject_files}
%doc README.md

%changelog
* Wed Oct 11 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.0.3-0.1
- Initial release

