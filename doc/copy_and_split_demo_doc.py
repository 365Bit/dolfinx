#!/usr/bin/env python
#
# Copyright (C) 2011 Marie E. Rognes
#
# This file is part of DOLFIN.
#
# DOLFIN is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DOLFIN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with DOLFIN.  If not, see <http://www.gnu.org/licenses/>.
#
# Utility script for splitting the cpp and python demos into separate
# directory trees. Ignores cmake files for python.

import sys, shutil

def copy_split_demo_doc(input_dir, cpp_output_dir, python_output_dir):

    def ignore_cpp(directory, contents):
        if directory[-3:] == "cpp":
            return contents
        else:
            return [c for c in contents if "cmake" in c.lower()]

    def ignore_python(directory, contents):
        if directory[-6:] == "python":
            return contents
        else:
            return ()

    # Copy demo tree to cpp_output_dir ignoring python demos
    try:
        shutil.rmtree(cpp_output_dir)
    except:
        pass
    shutil.copytree(input_dir, cpp_output_dir, ignore=ignore_python)

    # Copy demo tree to python_output_dir ignoring cpp demos
    try:
        shutil.rmtree(python_output_dir)
    except:
        pass
    shutil.copytree(input_dir, python_output_dir, ignore=ignore_cpp)

if __name__ == "__main__":

    args = sys.argv[1:]

    if len(args) != 3:
        usage= "Usage: python copy_and_split_demo_doc.py input_dir cpp_output_dir python_output_dir"
        print usage
        sys.exit(2)

    copy_split_demo_doc(args[0], args[1], args[2])
