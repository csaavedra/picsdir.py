#!/usr/bin/env python

# Copyright (C) 2008  Claudio Saavedra <csaavedra@igalia.com>
#
# Licensed under the GNU General Public License Version 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import pyexiv2
import os
import os.path
import shutil
import mimetypes

def move_smartly(file, dir_out, suffix):
    metadata = pyexiv2.ImageMetadata(file)
    metadata.read()
    if ('Exif.Photo.DateTimeOriginal' in metadata):
        date_creation = metadata['Exif.Photo.DateTimeOriginal'].value
        print(date_creation)
        str_date = date_creation.strftime('%Y-%m-%d-')
        target_dir = os.path.join (dir_out, str_date + suffix)

        if (not os.path.exists(target_dir)):
            os.mkdir(target_dir)

        try:
            shutil.move (file, target_dir)
        except shutil.Error:
            print file + " already exists in destination, not moving."
    else:
        print file + " has no date metadata, not moving."


def Main(args):
    if (len (args) < 2):
        sys.exit("picsdir.py input_dir [output_dir [suffix]]")
    dir_in = args[1]
    if (len (args) < 3):
        dir_out = dir_in
    else:
        dir_out = args[2]
    if (len (args) < 4):
        suffix = ''
    else:
        suffix = args[3]
    mimetypes.knownfiles.append('/home/claudio/.mime.types')
    mimetypes.init()
    for root, dirs, files in os.walk (dir_in):
        for f in files:
            filename = os.path.join (root, f)
            if mimetypes.guess_type(filename)[0] in ['image/jpeg', 'image/x-canon-cr2']:
		print filename
                move_smartly (filename, dir_out, suffix)
    print sum(os.path.getsize(join(root, name)) for name in files)

start=Main(sys.argv)

