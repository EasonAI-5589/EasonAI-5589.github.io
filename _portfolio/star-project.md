---
title: "STAR: Stage-wise Attention-Guided Token Reduction"
excerpt: "A novel framework for efficient Large Vision-Language Models inference"
header:
  image: /images/star-project.jpg
  teaser: /images/star-teaser.jpg
---

# STAR: Stage-wise Attention-Guided Token Reduction

STAR is a groundbreaking framework designed to improve the inference efficiency of Large Vision-Language Models (LVLMs) through intelligent token reduction strategies.

## Key Features

- **Two-Stage Framework**: Early pruning via visual self-attention and late pruning via cross-modal attention
- **Training-Free**: No additional training required, works with pre-trained models
- **High Efficiency**: Up to 95% token reduction with 58% FLOPS reduction
- **Performance Preservation**: Maintains over 101.3% performance across 10 Vision-Language tasks
- **Model Compatibility**: Successfully integrated with LLaVA-1.5, LLaVA-NeXT, MPlugOwl-2, and Qwen-VL

## Technical Innovation

The framework addresses key challenges in LVLM inference:
- Redundant visual token processing
- Cross-modal attention optimization
- Inference speed vs. accuracy trade-offs

## Results

STAR outperforms existing baselines including FastV, FasterVLM, and SparseVLM in both accuracy and latency trade-offs, making it a state-of-the-art solution for efficient LVLM inference.

## Publication

Submitted to NeurIPS 2025 and currently under review.

## Links

- [GitHub Repository](https://github.com/EasonAI-5589/STAR)
- [Paper PDF](/files/star-neurips2025.pdf)
