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
BuildSystem:	texlive
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

