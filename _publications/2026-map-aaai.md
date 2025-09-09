---
title: "MAP: Mitigating Hallucinations in Large Vision-Language Models with Map-Level Attention Processing"
authors: "C. Li*, Yichen Guo*, B. Qian, J. You, K. Tang, Y. Du, Z. Zhang, X. Huang"
venue: "AAAI 2026"
year: 2026
type: "conference"
status: "under_review"
pdf: "/files/map-aaai2026.pdf"
code: "https://github.com/EasonAI-5589/MAP"
note: "*Equal contribution"
---

We propose MAP, a training-free decoding framework to reduce hallucinations in Large Vision-Language Models (LVLMs) by treating hidden states as 2D semantic maps. MAP introduces a novel map-level perspective interpreting hidden states across layers as 2D semantic maps, designed with Layer-Wise Criss-Cross Attention for token aggregation and hallucination mitigation. The framework incorporates a Global-Local Logit Fusion mechanism for factual consistency and multimodal reasoning. MAP achieved state-of-the-art hallucination mitigation across benchmarks (POPE, MME, MMHal-Bench), outperforming VCD, DAMO, DCLA, and SPIN methods.
