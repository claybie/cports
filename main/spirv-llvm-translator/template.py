pkgname = "spirv-llvm-translator"
pkgver = "18.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    "-DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=/usr/include/spirv",
    "-DLLVM_LINK_LLVM_DYLIB=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DCMAKE_SKIP_RPATH=ON",
    "-DLLVM_SPIRV_INCLUDE_TESTS=OFF",
]
make_build_target = "llvm-spirv"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "clang-tools-extra",
    "spirv-headers",
    "spirv-tools-devel",
]
makedepends = ["llvm-devel"]
pkgdesc = "API and commands for processing SPIR-V modules"
maintainer = "q66 <q66@chimera-linux.org>"
license = "NCSA"
url = "https://github.com/KhronosGroup/SPIRV-LLVM-Translator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c1c7aee4ea23a6a1089bb7f7bad198c28ada65c5b7671434562fe0241d8674d6"
# FIXME int: crashes libclc build
hardening = ["!int"]
# tests disabled
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.TXT")


@subpackage("spirv-llvm-translator-devel")
def _devel(self):
    return self.default_devel()
