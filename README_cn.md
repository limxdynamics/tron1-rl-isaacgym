[English](README.md) | 中文

# TRON1 RL (Isaac Gym)

**基于 NVIDIA Isaac Gym 大规模并行强化学习，为 LimX TRON1 的三种形态——点足、足板、轮足——训练运动控制策略。** 训练好的策略可导出为 ONNX，无需修改即可在 [MuJoCo](https://github.com/limxdynamics/tron1-mujoco-sim) 和真机上运行。

[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.8-blue.svg)
![Isaac Gym](https://img.shields.io/badge/Isaac%20Gym-Preview%204-76b900.svg)
[![Stars](https://img.shields.io/github/stars/limxdynamics/tron1-rl-isaacgym?style=social)](https://github.com/limxdynamics/tron1-rl-isaacgym/stargazers)

<p align="center">
  <img src="doc/tron1-isaacgym-demo.gif" width="900" alt="TRON1 点足、足板、轮足策略行走与转向">
  <br>
  <sub>由本仓库训练的策略，在 MuJoCo 中回放（sim-to-sim）。</sub>
</p>

## 亮点

- **一套代码，三种机器人。** 点足、足板（带踝关节）、轮足 TRON1，通过一个环境变量切换。
- **训练 → sim-to-sim → 真机。** 导出 ONNX，在 MuJoCo 中验证，再用官方 ROS / ROS 2 / Python 控制器部署。
- **单卡数千个并行环境**（默认 8192），基于 [legged_gym](https://github.com/leggedrobotics/legged_gym) 和 [rsl_rl](https://github.com/leggedrobotics/rsl_rl)。
- **想先看效果？** [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python/tree/main/controllers/model) 自带所有形态的 Isaac Gym 预训练策略，不用训练就能在 MuJoCo 里跑起来。

## 支持的机器人

所有形态都使用同一条命令和 `--task=pointfoot_flat`，由 `ROBOT_TYPE` 决定机器人、环境和奖励函数。

| 形态 | `ROBOT_TYPE` | 环境 | 默认迭代次数 |
|---|---|---|---|
| 点足 | `PF_TRON1A`（另有 `PF_P441A`、`PF_P441B`、`PF_P441C`、`PF_P441C2`） | `envs/pointfoot_flat` | 15000 |
| 足板 | `SF_TRON1A` | `envs/solefoot_flat` | 10000 |
| 轮足 | `WF_TRON1A` | `envs/wheelfoot_flat` | 8000 |

## TRON1 开源生态

TRON1 有一整套开源仓库，覆盖从机器人模型到真机运行的全流程。这里是总导航，其他 TRON1 仓库都会链接到这里。

```
tron1-robot-description ──► tron1-rl-isaaclab / tron1-rl-isaacgym ──► ONNX 策略 ──► tron1-mujoco-sim ──► tron1-rl-deploy-{ros, ros2, python} ──► TRON1
       （机器人模型）                    （训练）                                     （sim-to-sim 验证）          （真机运行）
```

**从哪里开始**

- **还没有机器人？** 在 [tron1-mujoco-sim](https://github.com/limxdynamics/tron1-mujoco-sim) 里运行 [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python) 自带的预训练策略，不用训练就能看到效果。
- **训练自己的策略：** 新项目建议用 [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab)（NVIDIA 已停止维护 Isaac Gym、改推 Isaac Lab）；已经在用 Isaac Gym 的话，用本仓库即可。
- **在真机上运行：** 用 [tron1-rl-deploy-ros](https://github.com/limxdynamics/tron1-rl-deploy-ros)、[tron1-rl-deploy-ros2](https://github.com/limxdynamics/tron1-rl-deploy-ros2) 或 [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python) 部署导出的 ONNX 策略。

| 环节 | 仓库 | 作用 |
|---|---|---|
| 机器人模型 | [tron1-robot-description](https://github.com/limxdynamics/tron1-robot-description) | URDF / Xacro / MJCF 模型，支持 ROS 1/2、MuJoCo、Gazebo |
| 仿真 | [tron1-mujoco-sim](https://github.com/limxdynamics/tron1-mujoco-sim) | MuJoCo 仿真器，接口和真机一致（`limxsdk`） |
| 仿真 | [tron1-gazebo-ros](https://github.com/limxdynamics/tron1-gazebo-ros) · [tron1-gazebo-ros2](https://github.com/limxdynamics/tron1-gazebo-ros2) | Gazebo 仿真，ROS Noetic · ROS 2 Iron |
| 训练 | [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab) | 基于 Isaac Lab 的 RL 训练，新项目推荐 |
| 训练 | **tron1-rl-isaacgym**（本仓库） | 基于 Isaac Gym 的 RL 训练 |
| 部署 | [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python) | Python 部署，含预训练策略 |
| 部署 | [tron1-rl-deploy-ros](https://github.com/limxdynamics/tron1-rl-deploy-ros) · [tron1-rl-deploy-ros2](https://github.com/limxdynamics/tron1-rl-deploy-ros2) | ROS Noetic · ROS 2 Iron 部署 |
| 部署 | [tron1-rl-deploy-arm](https://github.com/limxdynamics/tron1-rl-deploy-arm) | 带机械臂的 TRON1 RL 部署 |
| 应用 | [tron1-ss](https://github.com/limxdynamics/tron1-ss) | 激光 SLAM 与导航：建图、定位、路径规划 |
| 应用 | [tron1-agent](https://github.com/limxdynamics/tron1-agent) | 语音交互 AI Agent：语音指令、大模型对话、机器人动作 |
| SDK | [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) | 底层运动控制 SDK（C++ / Python），仿真和部署代码都依赖它 |

## 安装

环境要求：Linux，NVIDIA 显卡及支持 CUDA 12.1 的驱动。

1. 创建 Python 3.8 环境（Isaac Gym 支持 Python 3.6–3.8）：
   ```bash
   conda create -n tron1_rl python=3.8 -y
   conda activate tron1_rl
   ```
2. 安装 PyTorch（CUDA 12.1）：
   ```bash
   pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121
   ```
3. 安装 Isaac Gym Preview 4（Preview 2 不可用）。从 [NVIDIA 官网](https://developer.nvidia.com/isaac-gym) 下载后：
   ```bash
   cd isaacgym/python && pip install -e .
   pip install "numpy<1.24"   # Isaac Gym 用到了 np.float，NumPy 1.24 起已移除
   cd examples && python 1080_balls_of_solitude.py   # 验证安装
   ```
   遇到问题请查看 `isaacgym/docs/index.html`。
4. 安装本仓库，以及日志和导出所需的依赖：
   ```bash
   git clone https://github.com/limxdynamics/tron1-rl-isaacgym.git
   cd tron1-rl-isaacgym && pip install -e .
   pip install onnx tensorboard==2.12.0
   ```

在全新的 Ubuntu 机器上，可以用 [`install.sh`](install.sh) 一键完成上述步骤（包括 NVIDIA 驱动和 Anaconda），所有内容会装在 `~/limx_rl` 下，conda 环境名为 `pointfoot_legged_gym`。

## 使用方法

### 训练

```bash
export ROBOT_TYPE=PF_TRON1A        # 或 SF_TRON1A / WF_TRON1A
python legged_gym/scripts/train.py --task=pointfoot_flat --headless
```

- `--headless` 关闭渲染。如果打开了可视化窗口，按 `v` 暂停渲染可以加快训练。
- 显存较小时，用 `--num_envs 4096` 减少并行环境数。
- 在 CPU 上运行：`--sim_device=cpu --rl_device=cpu`（也可以仿真在 CPU、学习在 GPU）。
- 模型保存在 `logs/pointfoot_flat/<experiment_name>/<date_time>_<run_name>/model_<iteration>.pt`，`experiment_name` 默认等于 `ROBOT_TYPE`。

常用参数（会覆盖配置文件中的值）：

| 参数 | 含义 |
|---|---|
| `--resume` | 从 checkpoint 继续训练 |
| `--load_run RUN` | 要加载的运行目录，默认最新一次 |
| `--checkpoint N` | 要加载的迭代次数，默认最新一个 |
| `--experiment_name NAME` / `--run_name NAME` | 实验名 / 运行名 |
| `--num_envs N` | 并行环境数 |
| `--max_iterations N` | 最大训练迭代次数 |
| `--seed SEED` | 随机种子 |

### 运行与导出

```bash
python legged_gym/scripts/play.py --task=pointfoot_flat                       # 最新一次运行、最新模型
python legged_gym/scripts/play.py --task=pointfoot_flat --load_run Apr18_15-48-46_ --checkpoint 10000
```

- `load_run` 是训练结果所在的目录名；`checkpoint` 是迭代次数，例如 `model_10000.pt` 对应 `10000`。
- "最新一次运行"指按字母顺序排在最后的目录。目录名以英文月份开头（`Apr…`、`Oct…`），跨月训练时请显式指定 `--load_run`。
- `play.py` 同时会把策略导出到 `logs/pointfoot_flat/<experiment_name>/exported/policies/`，生成 `policy.onnx` 和 `encoder.onnx`。

### 部署

把 `policy.onnx` 和 `encoder.onnx` 复制到 [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python) 的 `controllers/model/<ROBOT_TYPE>/policy/isaacgym/` 目录，运行时设置 `export RL_TYPE=isaacgym`。先在 [tron1-mujoco-sim](https://github.com/limxdynamics/tron1-mujoco-sim) 中验证效果，再上真机。ROS / ROS 2 部署请参考 [tron1-rl-deploy-ros](https://github.com/limxdynamics/tron1-rl-deploy-ros) / [tron1-rl-deploy-ros2](https://github.com/limxdynamics/tron1-rl-deploy-ros2) 的 README。

## 代码结构

- 每个环境由一个环境文件和一个配置文件定义，例如 `pointfoot_flat.py` 和 `pointfoot_flat_config.py`。配置文件包含环境参数（`BipedCfgPF`）和训练参数（`BipedCfgPPOPF`）两个类，均使用继承。
- 配置中每个非零的奖励系数，都会把同名的奖励函数加入总奖励。
- 任务通过 `task_registry.register(name, EnvClass, EnvConfig, TrainConfig)` 注册，位置在 `legged_gym/envs/__init__.py`，也可以在仓库外部注册。

## 已知问题

在 GPU 上用三角网格地形仿真时，`net_contact_force_tensor` 返回的接触力不可靠。基于力传感器的解决办法见 [legged_gym 的 Known Issues](https://github.com/leggedrobotics/legged_gym#known-issues)。

## 致谢

本项目基于苏黎世联邦理工学院 Robotic Systems Lab 的 [legged_gym](https://github.com/leggedrobotics/legged_gym) 和 [rsl_rl](https://github.com/leggedrobotics/rsl_rl)，以其 `LeggedRobot` 实现作为环境的基础。

## 有问题？

欢迎 [提交 Issue](https://github.com/limxdynamics/tron1-rl-isaacgym/issues)。如果这个项目对你有帮助，点个 ⭐ 能让更多人看到它。
