pkgname=maketxt
pkgver=1.0.0
pkgrel=1
pkgdesc="maketxt is a simple cli tool that creates .txt files."
arch=('any')
url="https://github.com/skirexwastaken/maketxt"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')

# we keep the url as is to ensure the download works
source=("git+https://github.com/skirexwastaken/maketxt.git")
sha256sums=('SKIP')

build() {
    # git usually clones into a folder matching the repo name (makeTXT)
    # so we cd into that folder to run the lowercase setup
    cd "$srcdir/makeTXT"
    python setup.py build
}

package() {
    cd "$srcdir/makeTXT"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
