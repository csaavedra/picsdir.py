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

def move_smartly(file, dir_in, dir_out, suffix):
    image_file = os.path.join (dir_in, file)
    image = pyexiv2.Image(image_file)
    image.readMetadata()
    date_creation = image['Exif.Image.DateTime']
    str_date = date_creation.strftime('%Y-%m-%d-')

    target_dir = os.path.join (dir_out, str_date + suffix)

    if (not os.path.exists(target_dir)):
        print "creating dir " + target_dir
        os.mkdir(target_dir)

    shutil.move (image_file, target_dir)


def Main(args):
    if (len (args) < 2):
        sys.exit("not enough parameters")
    dir_in = args[1]
    if (len (args) < 3):
        dir_out = dir_in
    else:
        dir_out = args[2]
    if (len (args) < 4):
        suffix = ''
    else:
        suffix = args[3]

    for root, dirs, files in os.walk (dir_in):
        for f in files:
            filename = os.path.join (root, f)
            if mimetypes.guess_type(filename)[0] == 'image/jpeg':
                move_smartly (filename, dir_in, dir_out, suffix)

start=Main(sys.argv)

print sum(getsize(join(root, name)) for name in files)
