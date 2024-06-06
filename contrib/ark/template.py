pkgname = "ark"
pkgver = "24.05.0"
pkgrel = 0
build_style = "cmake"
# kerfuffle-extracttest: needs arj/unar etc
# kerfuffle-loadtest: fails to open some archives
make_check_args = ["-E", "(kerfuffle-extracttest|)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "breeze-icons-devel",
    "kconfig-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kfilemetadata-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kparts-devel",
    "kpty-devel",
    "kservice-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libarchive-devel",
    "libzip-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["7zip", "xwayland-run", "zstd"]
pkgdesc = "KDE archive manager"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ark"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ark-{pkgver}.tar.xz"
sha256 = "70b149f0226eb404c9d957971e86a94bc4c071c1aa1a4d233c491e5fdb63f9d7"


@subpackage("ark-computils")
def _computils(self):
    self.pkgdesc = f"{pkgdesc} (default de/compression utilities)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        "7zip",
        # TODO: missing deps
        # there's also arj/lzop but seems pointless
        # "lrzip",
        # "unar",
        # "unzip",  # pointless with 7z (in code), also it uses libzip anyway?
        "zstd",
    ]
    self.options = ["empty"]
    return []
