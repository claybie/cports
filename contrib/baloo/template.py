pkgname = "baloo"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
# FIXME: "not connected to dbus server"
make_check_args = ["-E", "(fileindexerconfigtest|filewatchtest)"]
make_check_wrapper = ["dbus-run-session", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kfilemetadata-devel",
    "ki18n-devel",
    "kidletime-devel",
    "kio-devel",
    "lmdb-devel",
    "qt6-qtdeclarative-devel",
    "solid-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE Framework for searching and metadata"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://api.kde.org/frameworks/baloo/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/baloo-{pkgver}.tar.xz"
)
sha256 = "1ea413b9dbada7d0646a1f8dc3f0688928c266e6388528cfd05d4c079a7e22a8"
# CFI: test
hardening = ["vis", "!cfi"]


def post_install(self):
    # TODO: dinit user service with graphical
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)


@subpackage("baloo-devel")
def _devel(self):
    self.depends += [
        "qt6-qtbase-devel",
        "kcoreaddons-devel",
        "kfilemetadata-devel",
        "lmdb-devel",
    ]
    return self.default_devel()
