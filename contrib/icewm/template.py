pkgname = "icewm"
pkgver = "3.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCONFIG_GDK_PIXBUF_XLIB=ON",
    "-DCONFIG_LIBRSVG=ON",
    "-DCONFIG_XPM=ON",
    "-DCFGDIR=/etc/icewm",
    "-DICESOUND=alsa",
    "-DXTERMCMD=urxvt",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext", "asciidoc", "perl"]
makedepends = [
    "alsa-lib-devel",
    "fontconfig-devel",
    "gdk-pixbuf-devel",
    "librsvg-devel",
    "libsm-devel",
    "libsndfile-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxft-devel",
    "libxinerama-devel",
    "libxpm-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "fribidi-devel",
    "imlib2-devel",
]
depends = ["shared-mime-info"]
pkgdesc = "Window manager for X11"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://ice-wm.org"
source = f"https://github.com/ice-wm/icewm/archive/{pkgver}.tar.gz"
sha256 = "fba9b72ab13061511dc09ad6d536f1b9cd12631cb191f15a29828a6c8f802be6"
