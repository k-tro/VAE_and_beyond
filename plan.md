# Research Plan: Benchmarking Variational Autoencoders and Beyond

## Goals
- Implement and benchmark different VAE variants.
- Systematically evaluate reconstruction, generation, and latent representation quality.
- Compare VAEs against GANs and Diffusion models.
- Produce research-style writeup with experiments, plots, and conclusions.

---

## Phase A - Baseline VAEs
1. Implement vanilla VAE.
2. Experiments:
   - Latent size sweep (z=16,32,64,128).
   - KL annealing vs. no-anneal.
   - Reconstruction loss type (MSE vs. BCE vs. SmoothL1).
   - Dataset size effect (10%, 50%, 100%).

---

## Phase B - VAE Variants
1. β-VAE:
   - Vary β={0.5,1,2,4,8}.
   - Test disentanglement metrics on dSprites, 3D-Shapes.
2. VQ-VAE:
   - Codebook size {128,256,512}.
   - Check code usage, recon, FID.
3. Hierarchical VAE:
   - Compare single-level vs two-level latents.
4. Alternative Priors:
   - Standard Normal vs VampPrior.

---

## Phase C - Beyond VAE
1. VAE-GAN (compare sharpness vs ELBO).
2. GAN baselines (DCGAN, WGAN-GP).
3. Diffusion baseline (DDPM-lite).

---

## Phase D - Evaluation & Analysis
- Metrics:
  - Reconstruction: PSNR, SSIM, MSE
  - Generation: FID, IS
  - Latent quality: Disentanglement scores
  - Training: ELBO, KL, Recon curves
- Visualizations:
  - Recon vs input
  - Random generations
  - Latent interpolations
  - Traversals (β-VAE)
  - Codebook usage histograms
- Report results with mean ± std across 3 seeds.

---

## Deliverables
- **Codebase** with modular models and config-driven training.
- **Reports** (tables, plots, metrics).
- **Blog-style writeup / PDF** summarizing experiments.
- **(Optional)** Demo app for enc/dec + latent interpolation.
