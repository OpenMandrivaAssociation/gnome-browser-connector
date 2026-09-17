%global debug_package %{nil}

Name:           gnome-browser-connector
Version:        42.1
Release:        1
Summary:        GNOME Shell browser connector
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-browser-connector
Source0:        https://download.gnome.org/sources/gnome-browser-connector/42/gnome-browser-connector-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(pygobject-3.0)

Requires:       dbus
Requires:       gnome-shell
Requires:       hicolor-icon-theme
Recommends:     mozilla-filesystem
Requires:       python-gi

Obsoletes:      chrome-gnome-shell

%description
Native host messaging connector that provides integration with GNOME Shell and
the corresponding extensions repository https://extensions.gnome.org.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc NEWS README.md
%{_sysconfdir}/chromium/
%{_sysconfdir}/opt/chrome/
%{_bindir}/gnome-browser-connector
%{_bindir}/gnome-browser-connector-host
%{python3_sitelib}/gnome_browser_connector/
%{_libdir}/mozilla/native-messaging-hosts/
%{_datadir}/applications/org.gnome.BrowserConnector.desktop
%{_datadir}/dbus-1/services/org.gnome.BrowserConnector.service
%{_datadir}/icons/hicolor/*/apps/org.gnome.BrowserConnector.png
