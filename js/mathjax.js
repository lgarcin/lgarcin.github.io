window.MathJax = {
  tex: {
    inlineMath: [
      [
        '$', '$'
      ],
      ["\\(", "\\)"]
    ],
    processEscapes: true,
    macros: {
      cC: "\\mathcal{C}",
      cD: "\\mathcal{D}",
      cP: "\\mathcal{P}",
      la: "\\lambda",
      va: "\\varphi",
      dF: "\\mathbb{F}",
      dK: "\\mathbb{K}",
      dN: "\\mathbb{N}",
      dP: "\\mathbb{P}",
      dQ: "\\mathbb{Q}",
      dR: "\\mathbb{R}",
      dU: "\\mathbb{U}",
      dZ: "\\mathbb{Z}",
      lb: "\\left[\\!\\left[",
      rb: "\\right]\\!\\right]",
      card: "\\operatorname{card}",
      vect: "\\operatorname{vect}",
      dim: "\\operatorname{dim}",
      deg: "\\operatorname{deg}",
      ident: "\\operatorname{Id}",
      stab: "\\operatorname{Stab}",
      Im: "\\operatorname{Im}",
      Ker: "\\operatorname{Ker}",
      conj: "\\overline",
      te: "\\theta",
      eps: "\\epsilon",
      si: "\\sigma",
      un: "\\boldsymbol{1}"
    },
    autoload: {
      color: [],
      colorv2: ['color']
    },
    packages: { '[+]': ['noerrors'] }
  },
  options: {
    ignoreHtmlClass: 'tex2jax_ignore',
    processHtmlClass: 'tex2jax_process'
  },
  loader: {
    load: ['[tex]/noerrors']
  }
};
