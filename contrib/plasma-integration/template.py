pkgname = "plasma-integration"
pkgver = "6.0.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_QT5=OFF"]
make_check_args = [
    "-E",
    "(kdeplatformtheme|"  # 5/9 failing subtests due to differing values, kdeplatformtheme_unittest.cpp:(127,167,221,230,295)
    "kfontsettingsdata|"  # testFontsChanged() 'm_appChangedFont' returned FALSE, kfontsettingsdata_unittest.cpp:93
    "kfiledialog_unittest6|"  # SEGFAULT after 9s in testGetSaveFileUrl(), kfiledialog_unittest.cpp:144
    "kfiledialogqml)",  # testShowDialog* can't find KIO KFileWidget, kfiledialogqml_unittest.cpp:38
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "kxmlgui-devel",
    "plasma-wayland-protocols",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
]
checkdepends = [
    "breeze",
    "dbus",
]
pkgdesc = "Qt Platform Theme integration plugins for the Plasma workspaces"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-integration"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-integration-{pkgver}.tar.xz"
sha256 = "7f81683ff8f8a6e23d5c98e9b3f3bc3d638abd4dcad4e40d27446c0029004ff0"
# FIXME: cfi crashes e.g. kwrite upon "Save" in save file dialog in KDEPlasmaPlatformTheme6.so
hardening = ["vis", "!cfi"]
