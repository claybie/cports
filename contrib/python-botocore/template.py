pkgname = "python-botocore"
pkgver = "1.34.124"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-dateutil",
    "python-jmespath",
    "python-urllib3",
]
checkdepends = depends + ["python-pytest"]
pkgdesc = "Core module supporting boto3 and aws cli"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/boto/botocore"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "17687c4c63d6b7f0838e97cf9db112b90fd32b7277a3950a7654a9bdc415008f"
# takes forever
options = ["!check"]
