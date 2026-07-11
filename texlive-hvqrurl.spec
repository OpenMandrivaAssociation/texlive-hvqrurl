%global tl_name hvqrurl
%global tl_revision 71361

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.09
Release:	%{tl_revision}.1
Summary:	Insert a QR code in the margin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hvqrurl
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hvqrurl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hvqrurl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows to draw an URL as a QR code into the margin of a
one- or twosided document. The following packages are loaded by default:
qrcode, marginnote, url, xcolor and xkeyval.

