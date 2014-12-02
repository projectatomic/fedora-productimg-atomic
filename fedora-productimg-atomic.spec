%global loraxtarget %{_datadir}/lorax/product
%global loraxanacondadir %{loraxtarget}/usr/share/anaconda
%global pixmapsource %{_datadir}/anaconda/pixmaps/cloud

Name:           fedora-productimg-atomic
Version:        22
Release:        4%{?dist}
Summary:        Installer branding and configuration for Fedora Atomic

# Copyright and related rights waived via CC0
# http://creativecommons.org/publicdomain/zero/1.0/
License:        CC0

Source0:        anaconda-gtk.css
Source1:        installclass_atomic.py

BuildArch:      noarch

BuildRequires:  cpio, findutils, xz

Provides:       lorax-product-atomic

%description
This package contains differentiated branding and configuration for Fedora
Atomic for use in a product.img file for Anaconda, the Fedora installer. It
is not useful on an installed system.

%prep

%build

%install
install -m 755 -d %{buildroot}%{loraxtarget}/run/install/product/pyanaconda/installclasses
install -m 644 %{SOURCE1} %{buildroot}%{loraxtarget}/run/install/product/pyanaconda/installclasses
install -m 755 -d %{buildroot}%{loraxanacondadir}/pixmaps
install -m 644 %{SOURCE0} %{buildroot}%{loraxanacondadir}

ln -sf %{pixmapsource}/sidebar-bg.png %{buildroot}%{loraxanacondadir}/pixmaps
ln -sf %{pixmapsource}/topbar-bg.png %{buildroot}%{loraxanacondadir}/pixmaps

# note filename change with this one
ln -sf %{pixmapsource}/sidebar-logo.png %{buildroot}%{loraxanacondadir}/pixmaps/sidebar-logo_flavor.png


%files
%dir %{loraxtarget}/run/install/product/pyanaconda/installclasses
%{loraxtarget}/run/install/product/pyanaconda/installclasses/*.py*
%dir %{_datadir}/lorax/product/usr/share/anaconda
%{_datadir}/lorax/product/usr/share/anaconda/anaconda-gtk.css
%dir %{_datadir}/lorax/product/usr/share
%dir %{_datadir}/lorax/product/usr
%dir %{loraxanacondadir}/pixmaps
%{loraxanacondadir}/pixmaps/*.png

%changelog
* Tue Nov 25 2014 Colin Walters <walters@redhat.com> - 22-1
- Forked for atomic

* Thu Nov 20 2014 Matthew Miller <mattdm@fedoraproject.org> 22-4
- provides lorax-product-cloud

* Thu Nov 20 2014 Matthew Miller <mattdm@fedoraproject.org> 22-3
- merge changes in from f21

* Fri Nov  7 2014 Matthew Miller <mattdm@fedoraproject.org> 22-1
- bump to 22 for rawhide

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-2
- conflict with the other fedora-productimg packages

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-1
- change license to CC0

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-0
- Initial creation for Fedora 21
