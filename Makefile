NAME=diosteama
VERSION=0.1
PACKAGE=${NAME}_${VERSION}_amd64.deb
INSTALL_PATH=/usr/share/python

deb:
	make-deb --install-path=${INSTALL_PATH}
	DH_VIRTUALENV_INSTALL_ROOT=${INSTALL_PATH} dpkg-buildpackage -us -uc
