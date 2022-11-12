Name:		texlive-context-notes-zh-cn
Version:	23171
Release:	1
Summary:	Notes on using ConTeXt MkIV
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/context-notes-zh-cn
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-notes-zh-cn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-notes-zh-cn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-context

%description
An introductory tutorial on ConTeXt, in Chinese. The document
covers ConTeXt installation, fonts, layout design, cross-
reference, project structure, metafun and presentation design.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/README
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/ctxnotes.pdf
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/Makefile
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/basis.tex
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/bibl-lyr.tex
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/bibliography.bib
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/ctxnotes.tex
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/doc-env.tex
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/figures/bookmark.png
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/figures/cow.pdf
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/figures/gardeninglion.jpg
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/figures/header.png
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/fonts.tex
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/layout.tex
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/metafun.tex
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/project.tex
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/references.tex
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/t-layout.tex
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/t-zhfonts.lua
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/t-zhfonts.mkiv
%doc %{_texmfdistdir}/doc/context/third/context-notes-zh-cn/src/t-zhspuncs.lua

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
