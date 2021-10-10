pkgname = "run-parts"
pkgver = "4.11.2"
pkgrel = 0
build_style = "gnu_configure"
make_build_target = "run-parts"
pkgdesc = "Run scripts or programs in a directory"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://tracker.debian.org/pkg/debianutils"
source = f"$(DEBIAN_SITE)/main/d/debianutils/debianutils_{pkgver}.tar.xz"
sha256 = "3b680e81709b740387335fac8f8806d71611dcf60874e1a792e862e48a1650de"
options = ["bootstrap", "!check", "!lint"]

def do_install(self):
    self.install_bin("build/run-parts")
    self.install_man("run-parts.8")
