pkgname = "grantleetheme"
pkgver = "24.05.0"
pkgrel = 0
build_style = "cmake"
# can't find itself
make_check_args = ["-E", "grantleethemetest"]
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
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "knewstuff-devel",
    "ktexttemplate-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Grantlee template theme library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/pim/grantleetheme"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/grantleetheme-{pkgver}.tar.xz"
)
sha256 = "ba8e79b0fd460074dfb9f24cedfb606c3c8bde5901e28334967960776f292798"


@subpackage("grantleetheme-devel")
def _devel(self):
    self.depends += ["ktexttemplate-devel"]
    return self.default_devel()
