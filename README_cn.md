# 中文 | [English](README.md)

# tron1-rl-isaacgym

基于 Isaac Gym 的 LimX TRON1 双足机器人强化学习训练栈，使用 PPO 训练 locomotion 策略。

### 安装
1. 创建 Python 虚拟环境（推荐 Python 3.8）：`conda create -n your_virtual_env python=3.8`
2. 安装 PyTorch（CUDA 12.1）：`pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121`
3. 安装 Isaac Gym Preview 3：从 https://developer.nvidia.com/isaac-gym 下载，`cd isaacgym/python && pip install -e .`
4. 安装本仓库：`cd tron1-rl-isaacgym && pip install -e .`

### 使用方法
**训练：** `export ROBOT_TYPE=PF_TRON1A && python legged_gym/scripts/train.py --task=pointfoot_flat --headless`
- `--headless` 关闭渲染
- `--resume` 从 checkpoint 恢复训练
- `--max_iterations N` 覆盖最大迭代次数
- 模型保存路径：`logs/<experiment_name>/<ROBOT_TYPE>/<date>_<run>/model_<iter>.pt`

**运行策略：** `python legged_gym/scripts/play.py --task=pointfoot_flat --load_run your_run --checkpoint your_ckpt`

## 致谢
基于 [legged_gym](https://github.com/leggedrobotics/legged_gym) 和 [rsl_rl](https://github.com/leggedrobotics/rsl_rl)，由 Robotic Systems Lab 创建。

## 相关仓库
| 仓库 | 描述 |
|---|---|
| [tron1-robot-description](https://github.com/limxdynamics/tron1-robot-description) | TRON1 机器人模型文件 |
| [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab) | TRON1 Isaac Lab RL 训练 |
| [tron1-rl-deploy-ros](https://github.com/limxdynamics/tron1-rl-deploy-ros) | TRON1 RL 部署（ROS） |
| [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python) | TRON1 RL 部署（Python） |

## 有问题？
如有疑问请在本仓库提交 Issue。
