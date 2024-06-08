pkgname = "perl-moo"
pkgver = "2.005005"
pkgrel = 0
build_style = "perl_module"
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "perl",
]
makedepends = ["perl"]
depends = [
    "perl-class-method-modifiers",
    "perl-sub-quote",
    "perl-role-tiny",
]
checkdepends = list(depends)
pkgdesc = "Moose-compatible object oriented library for perl"
maintainer = "psykose <alice@ayaya.dev>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/dist/Moo"
source = f"https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-{pkgver}.tar.gz"
sha256 = "fb5a2952649faed07373f220b78004a9c6aba387739133740c1770e9b1f4b108"
