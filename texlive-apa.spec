%global tl_name apa
%global tl_revision 54080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.4
Release:	%{tl_revision}.1
Summary:	American Psychological Association format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/apa
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apa.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX class to format text according to the American Psychological
Association Publication Manual (5th ed.) specifications for manuscripts
or to the APA journal look found in journals like the Journal of
Experimental Psychology etc. In addition, it provides regular LaTeX-like
output with a few enhancements and APA-motivated changes. Note that the
apa7 class (covering the 7th edition of the manual) and apa6 (covering
the 6th edition of the manual) are now commonly in use. Apacite, which
used to work with this class, has been updated for use with apa6.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/apa
%dir %{_datadir}/texmf-dist/tex/latex/apa
%doc %{_datadir}/texmf-dist/doc/latex/apa/APAendfloat.cfg
%doc %{_datadir}/texmf-dist/doc/latex/apa/CHANGELOG.txt
%doc %{_datadir}/texmf-dist/doc/latex/apa/LICENCE
%doc %{_datadir}/texmf-dist/doc/latex/apa/README
%doc %{_datadir}/texmf-dist/doc/latex/apa/apacls.html
%doc %{_datadir}/texmf-dist/doc/latex/apa/apacls.txt
%doc %{_datadir}/texmf-dist/doc/latex/apa/apaenum.txt
%doc %{_datadir}/texmf-dist/doc/latex/apa/apaexample.tex
%doc %{_datadir}/texmf-dist/doc/latex/apa/examplebib.bib
%doc %{_datadir}/texmf-dist/doc/latex/apa/examples.txt
%{_datadir}/texmf-dist/tex/latex/apa/apa.cls
%{_datadir}/texmf-dist/tex/latex/apa/dutch.apa
%{_datadir}/texmf-dist/tex/latex/apa/english.apa
%{_datadir}/texmf-dist/tex/latex/apa/greek.apa
