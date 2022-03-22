#!/bin/sh
USERNAME=hledoux

chmod a+r ./_pdfs/*.pdf
rsync --delete -pthrvz ./_pdfs/ ${USERNAME}@3d.bk.tudelft.nl:/var/www/people/hledoux/pdfs/
