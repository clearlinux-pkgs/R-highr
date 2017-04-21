#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-highr
Version  : 0.6
Release  : 25
URL      : http://cran.r-project.org/src/contrib/highr_0.6.tar.gz
Source0  : http://cran.r-project.org/src/contrib/highr_0.6.tar.gz
Summary  : Syntax Highlighting for R Source Code
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : R-knitr
BuildRequires : clr-R-helpers

%description
# highr
[![Build Status](https://travis-ci.org/yihui/highr.svg)](https://travis-ci.org/yihui/highr)

%prep
%setup -q -c -n highr

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484539837

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1484539837
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library highr
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library highr


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/highr/DESCRIPTION
/usr/lib64/R/library/highr/INDEX
/usr/lib64/R/library/highr/Meta/Rd.rds
/usr/lib64/R/library/highr/Meta/hsearch.rds
/usr/lib64/R/library/highr/Meta/links.rds
/usr/lib64/R/library/highr/Meta/nsInfo.rds
/usr/lib64/R/library/highr/Meta/package.rds
/usr/lib64/R/library/highr/Meta/vignette.rds
/usr/lib64/R/library/highr/NAMESPACE
/usr/lib64/R/library/highr/NEWS
/usr/lib64/R/library/highr/R/highr
/usr/lib64/R/library/highr/R/highr.rdb
/usr/lib64/R/library/highr/R/highr.rdx
/usr/lib64/R/library/highr/doc/highr-custom.R
/usr/lib64/R/library/highr/doc/highr-custom.Rmd
/usr/lib64/R/library/highr/doc/highr-custom.html
/usr/lib64/R/library/highr/doc/highr-internals.R
/usr/lib64/R/library/highr/doc/highr-internals.Rmd
/usr/lib64/R/library/highr/doc/highr-internals.html
/usr/lib64/R/library/highr/doc/index.html
/usr/lib64/R/library/highr/help/AnIndex
/usr/lib64/R/library/highr/help/aliases.rds
/usr/lib64/R/library/highr/help/highr.rdb
/usr/lib64/R/library/highr/help/highr.rdx
/usr/lib64/R/library/highr/help/paths.rds
/usr/lib64/R/library/highr/html/00Index.html
/usr/lib64/R/library/highr/html/R.css
