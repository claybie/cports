pkgname = "perl-sub-quote"
pkgver = "2.006008"
pkgrel = 0
build_style = "perl_module"
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "perl",
]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for eval-based subroutine generation"
maintainer = "psykose <alice@ayaya.dev>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/Sub::Quote"
source = f"$(CPAN_SITE)/Sub/Sub-Quote-{pkgver}.tar.gz"
sha256 = "94bebd500af55762e83ea2f2bc594d87af828072370c7110c60c238a800d15b2"
