---
title: "MAP: Map-Level Attention Processing for Hallucination Mitigation"
excerpt: "A training-free framework to reduce hallucinations in Large Vision-Language Models"
header:
  image: /images/map-project.jpg
  teaser: /images/map-teaser.jpg
---

# MAP: Map-Level Attention Processing

MAP is an innovative training-free decoding framework designed to mitigate hallucinations in Large Vision-Language Models (LVLMs) by treating hidden states as 2D semantic maps.

## Key Innovation

- **Map-Level Perspective**: Interprets hidden states across layers as 2D semantic maps
- **Layer-Wise Criss-Cross Attention**: Novel attention mechanism for token aggregation
- **Global-Local Logit Fusion**: Ensures factual consistency and multimodal reasoning
- **Training-Free**: Works with existing pre-trained models without additional training

## Technical Approach

The framework addresses hallucination issues in LVLMs through:
- Semantic map construction from hidden representations
- Cross-layer consistency enforcement
- Multi-scale attention processing
- Factual consistency validation

## Performance

MAP achieved state-of-the-art hallucination mitigation across multiple benchmarks:
- **POPE**: Improved hallucination detection
- **MME**: Enhanced multimodal evaluation
- **MMHal-Bench**: Superior hallucination mitigation

The method outperforms existing approaches including VCD, DAMO, DCLA, and SPIN.

## Publication

Submitted to AAAI 2026 and currently under review.

## Links

- [GitHub Repository](https://github.com/EasonAI-5589/MAP)
- [Paper PDF](/files/map-aaai2026.pdf)
