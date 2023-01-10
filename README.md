# nerf: a reimplementation
A Customized NeRF pipeline by Qi

## Install
To install the environment, you just need to type
```
make setup_env_conda
```

## Download dataset
To get a minimal dataset for traning demo, you just need to type
```
make download_data
```

## Trainning
To train a lego for yourself after the environment had been set up, you just need to type
```
make train_lego
```
This will make a `log` directory for check points, visualizations, etc.
See `makefile` for other commands. 

## Extra your mesh
To extra a mesh yourself, you just need to type
```
make extra_mesh_demo
```

Please see [makefile](./makefile) for more information.

## Custom data
Please refer to [preprocess_data](./preprocess_data/) for more information to a customized dataset.

## Reference
- [NeRF](https://www.matthewtancik.com/nerf) : original project page

## Helpful resources
- [D-NeRF](https://github.com/albertpumarola/D-NeRF): D-NeRF is based on the same project as this one.
