---
title: "STAR: Stage-Wise Attention-Guided Token Reduction for Efficient Large Vision-Language Models Inference"
authors: "Yichen Guo, H. Li, Z. Zhang, J. You, K. Tang, X. Huang"
venue: "NeurIPS 2025"
year: 2025
type: "conference"
status: "under_review"
pdf: "/files/star-neurips2025.pdf"
code: "https://github.com/EasonAI-5589/STAR"
---

We propose STAR, a stage-wise image token reduction strategy for Large Vision-Language Models (LVLMs). STAR is a novel two-stage, training-free framework for pruning redundant visual tokens in LVLMs, improving inference efficiency without performance degradation. The framework employs a dual-phase token reduction strategy: early pruning via visual self-attention and late pruning via cross-modal attention. We achieved up to 95% token reduction, significantly reducing FLOPS (58%) and achieving over 101.3% performance across 10 Vision-Language tasks. STAR has been integrated into models like LLaVA-1.5, LLaVA-NeXT, MPlugOwl-2, and Qwen-VL, demonstrating generality and cross-model compatibility, outperforming prior token pruning baselines (FastV, FasterVLM, SparseVLM) in accuracy and latency trade-offs.
