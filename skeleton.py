import os

repo_structure = {
    "configs": ["base.yaml", "vae_mnist.yaml", "vae_cifar10.yaml", "bvae_dsprites.yaml", "vqvae_cifar10.yaml"],
    "data": [],
    "models": ["__init__.py", "vae.py", "bvae.py", "vqvae.py", "hier_vae.py", "vaegan.py", "gan.py", "diffusion.py"],
    "training": ["__init__.py", "trainer.py", "losses.py", "utils.py", "metrics.py", "logger.py"],
    "experiments": ["run_experiment.py", "eval.py"],
    "reports/figures": [],
    "reports/tables": [],
    "reports/logs": [],
    "samples": [],
    "scripts": ["train_cifar10.sh", "sweep_latent.sh"],
    "notebooks": ["latent_interpolations.ipynb", "plot_metrics.ipynb"],
    "tests": ["test_vae.py", "test_losses.py"]
}

base_files = {
    ".gitignore": "reports/\nsamples/\n__pycache__/\n*.pt\n*.pth\n*.log\n",
    "requirements.txt": "torch\n torchvision\n numpy\n matplotlib\n pyyaml\n",
    "README.md": "# VAE Benchmark Project\n\nThis repo benchmarks VAEs and their variants across datasets.\n",
    "LICENSE": "MIT License\n",
    "plan.md": ""  # will fill below
}

def create_repo(base_path="."):
    os.makedirs(base_path, exist_ok=True)
    
    for folder, files in repo_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            open(os.path.join(folder_path, file), "w").close()
    
    for file, content in base_files.items():
        with open(os.path.join(base_path, file), "w") as f:
            f.write(content)

if __name__ == "__main__":
    create_repo()
    print("✅ Repo skeleton created in ./vae-benchmark")
