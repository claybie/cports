pkgname = "tokodon"
pkgver = "24.05.0"
pkgrel = 1
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "knotifications-devel",
    "mpvqt-devel",
    "purpose-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwebsockets-devel",
    "qt6-qtwebview-devel",
    "qtkeychain-devel",
]
depends = [
    "kirigami-addons",
    "kitemmodels",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Mastodon client"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "(GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.0-or-later"
url = "https://apps.kde.org/tokodon"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/tokodon-{pkgver}.tar.xz"
sha256 = "575cc7d3cfe6d28b69390b6cc20a4fa541d320cd8cfc84afc192fe094e1d9eea"
