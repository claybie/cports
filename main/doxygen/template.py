pkgname = "doxygen"
pkgver = "1.9.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "perl", "python", "flex", "bison"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Source code documentation generator tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://doxygen.nl"
source = f"{url}/files/{pkgname}-{pkgver}.src.tar.gz"
sha256 = "a15e9cd8c0d02b7888bc8356eac200222ecff1defd32f3fe05257d81227b1f37"

def post_extract(self):
    # needs texlive stuff
    self.rm("testing/012_cite.dox")

def post_install(self):
    self.install_man("doc/doxygen.1")
