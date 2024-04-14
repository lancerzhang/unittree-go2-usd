# unittree-go2-scene

The `unittree-go2-scene` repository is designed for working with the NVIDIA Isaac Sim environment, focusing on the `BigRoom.usdc` scene file. This README provides detailed instructions on setting up your environment to use the files in this repository, including the installation of Git LFS for handling large files.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- **Git**
- **Git Large File Storage (LFS)**
- **NVIDIA Isaac Sim**

### Installing Git LFS

Git LFS is used to handle large files such as `.usd`, `.usdc`, and `.usda` formats. Install Git LFS by running the following command in your terminal:

```bash
sudo apt-get install git-lfs
```

After installing Git LFS, set it up for use with your Git repository:

```bash
git lfs install
```

## Clone the Repository

To work with the `BigRoom.usdc` file, you first need to clone this repository. Use the following command to clone the repository:

```bash
git clone https://github.com/lancerzhang/unittree-go2-scene
```

## Track Large Files

Once you have cloned the repository and have Git LFS installed, set up tracking for the large files used in this project:

```bash
git lfs track "*.usd"
git lfs track "*.usdc"
git lfs track "*.usda"
```

Ensure you commit the `.gitattributes` file that Git LFS generates, as this file configures what files are tracked:

```bash
git add .gitattributes
git commit -m "Configure LFS tracking"
```

## Opening the Scene in NVIDIA Isaac Sim

To open the `BigRoom.usdc` file in NVIDIA Isaac Sim:

1. Launch NVIDIA Isaac Sim.
2. Navigate through the menu to open an existing project.
3. Browse to the location where you have cloned this repository and select `BigRoom.usdc`.

## Additional Information

This setup assumes you have administrative rights to install packages and the necessary hardware to run NVIDIA Isaac Sim. For more detailed instructions on using Isaac Sim, please refer to the [official NVIDIA Isaac Sim documentation](https://developer.nvidia.com/isaac-sim).

For any issues or contributions, please open an issue or pull request in the repository.