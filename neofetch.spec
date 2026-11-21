Name:           neofetch
Version:        7.1.0
Release:        6%{?dist}
Summary:        CLI system information tool written in Bash

License:        MIT
URL:            https://github.com/dylanaraps/%{name}
ExclusiveArch:  x86_64 aarch64
%global debug_package %{nil}
Source0:        https://github.com/dylanaraps/%{name}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  make
Requires:       bash >= 3.0
%if 0%{?rhel} >= 8 || 0%{?fedora} || 0%{?suse_version}
Recommends:     bind-utils, coreutils, curl, gawk, grep, ImageMagick
Recommends:     pciutils, xdotool
%endif

%description
Neofetch displays information about your system next to an image,
your OS logo, or any ASCII file of your choice. The main purpose of Neofetch
is to be used in screenshots to show other users what OS/distribution you're
running, what theme/icons you're using and more.

%prep
%autosetup
sed 's,/usr/bin/env bash,%{_bindir}/bash,g' -i neofetch

%build

%check
bash -n neofetch

%install
%make_install

%files
%{_bindir}/%{name}
%license LICENSE.md
%doc README.md
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Oct 01 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 7.1.0-6
- Validate the installed Bash program syntax during package checks

* Thu Oct 01 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 7.1.0-5
- Declare make as a build dependency

* Thu Oct 01 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 7.1.0-4
- Disable empty debug source package generation for this Bash-only program

* Thu Oct 01 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 7.1.0-3
- List only files installed by the upstream make install target

* Thu Oct 01 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 7.1.0-2
- Guard weak runtime dependencies on distributions that support them
- Correct changelog weekdays

* Sun Jul 05 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 7.1.0-1
- Source0: use refs/tags/ GitHub archive URL (verified 302→200)
- Remove commented-out BuildArch line; drop EL8 Recommends guard (EL8+ always)

* Fri Jul 03 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 7.1.0-1
- Add ExclusiveArch: x86_64 aarch64

* Fri May 22 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 7.1.0-1
- Wrap Recommends lines in EL8+/Fedora guard

* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 7.1.0-1
- Update to 7.1.0 (final release - project archived)
- Remove Fedora version conditionals

* Fri Apr 06 2018 Kees de Jong <keesdejong@fedoraproject.org> - 3.4.0-1
- New upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 13 2017 Kees de Jong <keesdejong@fedoraproject.org> - 3.3.0-1
- Initial package.
