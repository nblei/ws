---
ENTRYTYPE: inproceedings
ID: 8Bleier_2022
abstract: "Earables such as earphones, hearing aids, and smart glasses are poised to be a prominent programmable computing platform in the future. In this paper, we ask the question: what kind of programmable hardware would be needed to support earable computing in future? To understand hardware requirements, we propose EarBench, a suite of representative emerging earable applications with diverse sensor-based inputs and computation requirements. Our analysis of EarBench applications shows that, on average, there is a 13.54×-3.97× performance gap between the computational needs of EarBench applications and the performance of the microprocessors that several of today's programmable earable SoCs are based on; more complex microprocessors have unacceptable energy efficiency for Earable applications. Our analysis also shows that EarBench applications are dominated by a small number of digital signal processing (DSP) and machine learning (ML)-based kernels that have significant computational similarity. We propose SpEaC --- a coarse-grained reconfigurable spatial architecture - as an energy-efficient programmable processor for earable applications. SpEaC targets earable applications efficiently using a) a reconfigurable fixed-point multiply-and-add augmented reduction tree-based substrate with support for vectorized complex operations that is optimized for the earable ML and DSP kernel code and b) a tightly coupled control core for executing other code (including non-matrix computation, or non-multiply or add operations in the earable DSP kernel code). Unlike other CGRAs that typically target general-purpose computations, SpEaC substrate is optimized for energy-efficient execution of the earable kernels at the expense of generality. Across all our kernels, SpEaC outperforms programmable cores modeled after M4, M7, A53, and HiFi4 DSP by 99.3×, 32.5×, 14.8×, and 9.8× respectively. At 63 mW in 28 nm, the energy efficiency benefits are 1.55 ×, 9.04×, 68.3 ×, and 32.7 × respectively; energy efficiency benefits are 15.7 × -- 1087 × over a low power Mali T628 MP6 GPU."
doi: 10.1145/3470496.3527396
url: https://doi.org/10.1145%2F3470496.3527396
year: 2022
month: jun
publisher: "ACM"
author: ['Nathaniel Bleier', 'Muhammad Husnain Mubarik', 'Srijan Chakraborty', 'Shreyas Kishore', 'Rakesh Kumar']
title: "Rethinking programmable earable processors"
conference: ISCA
---
