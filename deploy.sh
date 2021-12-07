#!/bin/sh
USERNAME=hledoux

jekyll build
rsync --delete -pthrvz ./_site/ ${USERNAME}@3d.bk.tudelft.nl:/var/www/people/hledoux/site/
