MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [
            [
                '$', '$'
            ],
            ["\\(", "\\)"]
        ],
        processEscapes: true
    },
    TeX: {
        Macros: {
            dK: "\\mathbb{K}",
            dN: "\\mathbb{N}",
            dQ: "\\mathbb{K}",
            dR: "\\mathbb{R}",
            dZ: "\\mathbb{Z}",
            lb: "\\left[\\!\\left[",
            rb: "\\right]\\!\\right]",
            vect: "\\mathop{\\mathrm{vect}}",
            dim: "\\mathop{\\mathrm{dim}}",
            deg: "\\mathop{\\mathrm{deg}}",
            ident: "\\mathop{\\mathrm{Id}}"
        }
    }
});
MathJax.Hub.Configured();
