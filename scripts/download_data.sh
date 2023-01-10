#! /bin/bash
mkdir -p data
wget http://cseweb.ucsd.edu/~viscomp/projects/LF/papers/ECCV20/nerf/tiny_nerf_data.npz
wget http://cseweb.ucsd.edu/~viscomp/projects/LF/papers/ECCV20/nerf/nerf_example_data.zip
mv tiny_nerf_data ./data/
mv nerf_example_data.zip ./data/
unzip ./data/nerf_example_data.zip
unzip ./data/tiny_nerf_data.zip