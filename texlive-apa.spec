Name:		texlive-apa
Version:	54080
Release:	2
Summary:	American Psychological Association format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/apa
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX class to format text according to the American
Psychological Association Publication Manual (5th ed.)
specifications for manuscripts or to the APA journal look found
in journals like the Journal of Experimental Psychology etc. In
addition, it provides regular LaTeX-like output with a few
enhancements and APA-motivated changes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/apa/apa.cls
%{_texmfdistdir}/tex/latex/apa/dutch.apa
%{_texmfdistdir}/tex/latex/apa/english.apa
%{_texmfdistdir}/tex/latex/apa/greek.apa
%doc %{_texmfdistdir}/doc/latex/apa/APAendfloat.cfg
%doc %{_texmfdistdir}/doc/latex/apa/CHANGELOG.txt
%doc %{_texmfdistdir}/doc/latex/apa/LICENCE
%doc %{_texmfdistdir}/doc/latex/apa/README
%doc %{_texmfdistdir}/doc/latex/apa/apacls.html
%doc %{_texmfdistdir}/doc/latex/apa/apacls.txt
%doc %{_texmfdistdir}/doc/latex/apa/apaenum.txt
%doc %{_texmfdistdir}/doc/latex/apa/apaexample.tex
%doc %{_texmfdistdir}/doc/latex/apa/examplebib.bib
%doc %{_texmfdistdir}/doc/latex/apa/examples.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
