#!/bin/sh
USERNAME=hledoux

chmod a+r ./_pdfs/*.pdf
rsync --delete -pthrvz ./_pdfs/ ${USERNAME}@3d:/var/www/people/hledoux/pdfs/
