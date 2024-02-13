Name:		texlive-hvqrurl
Version:	69723
Release:	1
Summary:	Insert a QR code in the margin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hvqrurl
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvqrurl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvqrurl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to draw an URL as a QR code into the margin
of a one- or twosided document. The following packages are
loaded by default: qrcode, marginnote, url, xcolor and xkeyval.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hvqrurl
%doc %{_texmfdistdir}/doc/latex/hvqrurl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
