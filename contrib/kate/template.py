pkgname = "kate"
pkgver = "24.05.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "ktexteditor-devel",
    "ktextwidgets-devel",
    "kuserfeedback-devel",
    "kwallet-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Advanced Text Editor"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/kate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kate-{pkgver}.tar.xz"
sha256 = "d2dc5fdf099068d315be9562d334c980c80ef6df7cd7400013abc38d4a4ed626"
# FIXME: cfi breaks at least location_history_test & kate_view_mgmt_tests
hardening = ["vis", "!cfi"]


# for kwrite to not pull in kate
@subpackage("kate-libs")
def _libs(self):
    return self.default_libs()


@subpackage("kwrite")
def _kwrite(self):
    self.pkgdesc = f"{pkgdesc} (KWrite)"
    return [
        "usr/bin/kwrite",
        "usr/share/icons/hicolor/*/apps/kwrite.*",
        "usr/share/applications/org.kde.kwrite.desktop",
        "usr/share/metainfo/org.kde.kwrite.appdata.xml",
    ]
