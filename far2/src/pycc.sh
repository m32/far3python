#!/bin/bash
gcc -E -P -xc consts.gen | sh > consts.h
vpython3 pythongen.py /devel/00mirror-cvs/00-m32/far2l .
