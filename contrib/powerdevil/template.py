pkgname = "powerdevil"
pkgver = "6.0.5"
pkgrel = 0
build_style = "cmake"
# FIXME: all tests broken like on alpine, migrateconfig_test*
make_check_args = [
    "-E",
    "(default_configs_can_suspend_to_ram"
    "|activities$"
    "|activities_no_double_migration"
    "|profiles$"
    "|profiles_more)",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "libcap-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ddcutil-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kidletime-devel",
    "kio-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "knotifications-devel",
    "kxmlgui-devel",
    "layer-shell-qt-devel",
    "libcap-devel",
    "libkscreen-devel",
    "plasma-activities-devel",
    "plasma-workspace-devel",
    "qt6-qtbase-devel",
]
checkdepends = [
    "bash",
]
depends = [
    "upower",
]
pkgdesc = "KDE Plasma shell power consumption settings manager"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/powerdevil"
source = f"$(KDE_SITE)/plasma/{pkgver}/powerdevil-{pkgver}.tar.xz"
sha256 = "27f995bce6f27e35b78e0c232f8dee8fba50fb91d7b3afd117583bdb79a12fd4"
# FIXME: having CAP_WAKE_ALARM set breaks kdbusaddons connecting to DBus session bus?!
# "Needed for scheduled wakeup which can wake from suspend"
# file_modes = {
#     "usr/lib/libexec/org_kde_powerdevil": ("root", "root", 0o755),
# }
# file_xattrs = {
#     "usr/lib/libexec/org_kde_powerdevil": {
#         "security.capability": "cap_wake_alarm+ep",
#     },
# }
hardening = ["vis", "cfi"]


def post_install(self):
    # TODO: dinit user services with graphical
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)
