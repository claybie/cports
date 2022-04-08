pkgname = "vulkan-tools"
pkgver = "1.3.211"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    "-DGLSLANG_INSTALL_DIR=/usr", "-DVULKAN_HEADERS_INSTALL_DIR=/usr",
    "-DBUILD_CUBE=ON",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf", "glslang-progs"]
makedepends = [
    "vulkan-headers", "vulkan-loader", "libxkbcommon-devel", "libxcb-devel",
    "libxrandr-devel", "wayland-devel", "wayland-protocols", "linux-headers",
]
pkgdesc = "Official Vulkan tools and utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Tools/archive/v{pkgver}.tar.gz"
sha256 = "57b203eb722d9b43b47450739396d7ac1e7d881df31d39d50da39107f0182c3e"
# no test suite
options = ["!cross", "!check"]
