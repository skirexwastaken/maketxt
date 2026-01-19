pkgname=maketxt
pkgver=1.0.0
pkgrel=1
pkgdesc="makeTXT is a simple CLI tool that creates .txt files."
arch=('any')
url="https://github.com/skirexwastaken/makeTXT"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')

source=("git+https://github.com/skirexwastaken/makeTXT.git")
sha256sums=('SKIP')

build() {
    cd "$srcdir/$pkgname"
    python setup.py build
}

package() {
    cd "$srcdir/$pkgname"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
