pkgname = "libxt"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libsm-devel", "libx11-devel"]
pkgdesc = "X Toolkit Intrinsics library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXt-{pkgver}.tar.bz2"
sha256 = "679cc08f1646dbd27f5e48ffe8dd49406102937109130caab02ca32c083a3d60"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxt-static")
def _static(self):
    return self.default_static()

@subpackage("libxt-devel")
def _devel(self):
    return self.default_devel(man = True)
