pkgname = "milou"
pkgver = "6.0.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "ki18n-devel",
    "krunner-devel",
    "ksvg-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Dedicated search application"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://api.kde.org/plasma/milou/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/milou-{pkgver}.tar.xz"
sha256 = "708e18b5b424985a167507e9b5934de93c65acaf2f524466312d09515eb842cf"
# FIXME: cfi kills krunner (plasma-workspace) on launch (Alt+Space) in libmilouqmlplugin.so
hardening = ["vis", "!cfi"]
