#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-highr
Version  : 0.9
Release  : 83
URL      : https://cran.r-project.org/src/contrib/highr_0.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/highr_0.9.tar.gz
Summary  : Syntax Highlighting for R Source Code
Group    : Development/Tools
License  : GPL-2.0
Requires: R-xfun
BuildRequires : R-xfun
BuildRequires : buildreq-R

%description
supports LaTeX and HTML output. Source code of other languages is supported

%prep
%setup -q -c -n highr
cd %{_builddir}/highr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641032576

%install
export SOURCE_DATE_EPOCH=1641032576
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library highr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library highr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library highr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc highr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/highr/DESCRIPTION
/usr/lib64/R/library/highr/INDEX
/usr/lib64/R/library/highr/Meta/Rd.rds
/usr/lib64/R/library/highr/Meta/features.rds
/usr/lib64/R/library/highr/Meta/hsearch.rds
/usr/lib64/R/library/highr/Meta/links.rds
/usr/lib64/R/library/highr/Meta/nsInfo.rds
/usr/lib64/R/library/highr/Meta/package.rds
/usr/lib64/R/library/highr/Meta/vignette.rds
/usr/lib64/R/library/highr/NAMESPACE
/usr/lib64/R/library/highr/NEWS.Rd
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
/usr/lib64/R/library/highr/tests/test-all.R
/usr/lib64/R/library/highr/tests/testit/test-hilight.R
/usr/lib64/R/library/highr/tests/testit/test-utils.R
