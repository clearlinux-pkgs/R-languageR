#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-languageR
Version  : 1.5.0
Release  : 13
URL      : https://cran.r-project.org/src/contrib/languageR_1.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/languageR_1.5.0.tar.gz
Summary  : Analyzing Linguistic Data: A Practical Introduction to
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
facilitatory utility functions used in ``Analyzing Linguistic

%prep
%setup -q -c -n languageR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552926164

%install
export SOURCE_DATE_EPOCH=1552926164
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library languageR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library languageR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library languageR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  languageR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/languageR/DESCRIPTION
/usr/lib64/R/library/languageR/INDEX
/usr/lib64/R/library/languageR/Meta/Rd.rds
/usr/lib64/R/library/languageR/Meta/data.rds
/usr/lib64/R/library/languageR/Meta/features.rds
/usr/lib64/R/library/languageR/Meta/hsearch.rds
/usr/lib64/R/library/languageR/Meta/links.rds
/usr/lib64/R/library/languageR/Meta/nsInfo.rds
/usr/lib64/R/library/languageR/Meta/package.rds
/usr/lib64/R/library/languageR/NAMESPACE
/usr/lib64/R/library/languageR/R/languageR
/usr/lib64/R/library/languageR/R/languageR.rdb
/usr/lib64/R/library/languageR/R/languageR.rdx
/usr/lib64/R/library/languageR/data/Rdata.rdb
/usr/lib64/R/library/languageR/data/Rdata.rds
/usr/lib64/R/library/languageR/data/Rdata.rdx
/usr/lib64/R/library/languageR/data/datalist
/usr/lib64/R/library/languageR/help/AnIndex
/usr/lib64/R/library/languageR/help/aliases.rds
/usr/lib64/R/library/languageR/help/languageR.rdb
/usr/lib64/R/library/languageR/help/languageR.rdx
/usr/lib64/R/library/languageR/help/paths.rds
/usr/lib64/R/library/languageR/html/00Index.html
/usr/lib64/R/library/languageR/html/R.css
/usr/lib64/R/library/languageR/scripts/examples.txt
/usr/lib64/R/library/languageR/scripts/figure7.10.R
/usr/lib64/R/library/languageR/scripts/figure7.5.R
/usr/lib64/R/library/languageR/scripts/figure7.7.R
