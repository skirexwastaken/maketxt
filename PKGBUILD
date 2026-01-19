pkgname=maketxt
_pkgname=makeTXT
pkgver=1.0.0
pkgrel=1
pkgdesc="A simple CLI tool that creates .txt files."
arch=('any')
url="https://github.com/skirexwastaken/makeTXT"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')

# Use the actual repo name for the source
source=("git+https://github.com/skirexwastaken/makeTXT.git")
sha256sums=('SKIP')

build() {
    # GitHub clones into the repo name (makeTXT), not the lowercase pkgname
    cd "$srcdir/$_pkgname"
    python setup.py build
}

package() {
    cd "$srcdir/$_pkgname"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
    
    # Optional: Install the license file specifically for Arch standards
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
