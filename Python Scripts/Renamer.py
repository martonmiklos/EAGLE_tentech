# Ce script passe � travers tous les fichiers du r�pertoire courant et fait une substitution
# de nom en cherchant la regexp IN_PATTERN et en rempla�ant le match par OUT_PATTERN.
# Si le fichier n'a pas chang� de nom dans cette op�ration, aucun rename n'est effectu�.
# Un message est affich� si le fichier de destination existe d�j� et il n'est pas �cras�.
#
# Auteur: Tennessee Carmel-Veilleux <tcv - at - ro.boto.ca>
# $Id: Renamer.py 493 2007-01-25 13:44:21Z veilleux $

import os
import re
import glob

IN_PATTERN = r"DS[0-9]+_(.*)"
OUT_PATTERN = r"\1"

def rename(name, inPattern, outPattern):
    if name.lower() <> "renamer.py":
        out = re.sub(inPattern, outPattern, name)
        try:
            if out != name:
                os.rename(name,out)
            print "%s => %s" % (name, out)
        except OSError:
            print "Cannot rename %s to %s" % (name, out)
            

for filename in glob.glob("*.*"):
    rename(filename, IN_PATTERN, OUT_PATTERN)
    
    