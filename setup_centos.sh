#!/bin/bash

REPO=https://github.com/ben-liang/heroku_engvtweb.git

# Install epel repo
sudo rpm -Uvh http://mirror.metrocast.net/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm
sudo yum -y install foo

# Install system dependencies
sudo yum install -y zlib-devel xz-libs wget
sudo yum -y install libxml2-devel libxslt-devel libpng libpng-devel ntp unzip postfix postgresql-devel s3cmd git git-gui gitk screen bash-completion gmp gmp-devel gcc-gfortran libgfortran gcc gcc-c++ libgcc freetype freetype-devel ruby ruby-devel mysql mysql-devel blas blas-devel lapack lapack-devel atlas atlas-devel

# These are required for python and maybe other fun things
sudo yum -y groupinstall "development tools"
sudo yum -y install readline-devel openssl-devel gmp-devel ncurses-devel gdbm-devel zlib-devel expat-devel libGL-devel tk tix gcc-c++ libX11-devel glibc-devel bzip2 tar tcl-devel tk-devel pkgconfig tix-devel bzip2-devel sqlite-devel autoconf db4-devel libffi-devel valgrind-devel openldap openldap-devel

yum install centos-release-SCL
yum install python27
scl enable python27 bash

#install pip
curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | python2.7 -

mkdir ~/repositories
cd ~/repositories
git clone $REPO heroku_engvtweb
cd heroku_engvtweb
virtualenv venv
source activate
pip install -r requirements.txt
