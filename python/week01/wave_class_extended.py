# ============================================================
# Week 1 Day 5 - 扩展功能的Wave类
# ============================================================
# 在基本Wave类基础上添加：
# 1. shift_phase(delta_phi): 相位移动
# 2. add_wave(other_wave): 波形叠加
# 3. sample(t_array): 多点采样
# ============================================================

import numpy as np
import matplotlib.pyplot as plt


class WaveExtended:
    """
    扩展功能的波形类
    
    新增方法：
    - shift_phase(delta_phi): 相位移动
    - add_wave(other_wave): 波形叠加
    - sample(t_array): 多点采样
    """
    
    def __init__(self, amplitude, frequency, phase=0):
        """构造方法"""
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.omega = 2 * np.pi * frequency
    
    def evaluate(self, t):
        """计算波在时间t的值"""
        return self.amplitude * np.sin(self.omega * t + self.phase)
    
    def shift_phase(self, delta_phi):
        """
        相位移动方法
        
        参数：
        - delta_phi: 相位变化量（单位rad）
        
        功能：
        - 直接修改对象的phase属性
        - 返回None（修改器方法）
        """
        self.phase += delta_phi
        print(f"相位已移动 {delta_phi:.2f} rad，新相位: {self.phase:.2f} rad")
    
    def add_wave(self, other_wave):
        """
        波形叠加方法
        
        参数：
        - other_wave: 另一个WaveExtended对象
        
        返回：
        - 新的WaveExtended对象（振幅相加，频率和相位取第一个波的值）
        """
        new_amplitude = self.amplitude + other_wave.amplitude
        # 频率和相位取第一个波的值
        new_wave = WaveExtended(new_amplitude, self.frequency, self.phase)
        print(f"波形叠加: {self.amplitude} + {other_wave.amplitude} = {new_amplitude}")
        return new_wave
    
    def sample(self, t_array):
        """
        多点采样方法
        
        参数：
        - t_array: 时间点数组（numpy数组）
        
        返回：
        - numpy数组，包含波在各时间点的值
        """
        return np.array([self.evaluate(t) for t in t_array])
    
    def info(self):
        """打印波的基本信息"""
        print(f"Wave information:")
        print(f"  amplitude: {self.amplitude}")
        print(f"  frequency: {self.frequency} Hz")
        print(f"  phase: {self.phase:.2f} rad")


# ============================================================
# 测试代码
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("测试扩展功能的Wave类")
    print("=" * 60)
    
    # 创建波形对象
    wave1 = WaveExtended(amplitude=2.0, frequency=50.0)
    wave2 = WaveExtended(amplitude=1.5, frequency=100.0, phase=np.pi/4)
    
    # 打印初始信息
    print("\n初始状态:")
    print("Wave1:")
    wave1.info()
    print("\nWave2:")
    wave2.info()
    
    # 测试相位移动
    print("\n" + "-" * 40)
    print("测试相位移动:")
    wave1.shift_phase(np.pi / 2)  # 移动90度
    
    # 测试波形叠加
    print("\n" + "-" * 40)
    print("测试波形叠加:")
    wave3 = wave1.add_wave(wave2)
    print("叠加后的波形:")
    wave3.info()
    
    # 测试多点采样
    print("\n" + "-" * 40)
    print("测试多点采样:")
    t_points = np.array([0, 0.005, 0.01, 0.015, 0.02])
    samples = wave1.sample(t_points)
    print(f"时间点: {t_points}")
    print(f"采样值: {samples}")
    
    # 绘制叠加后的波形
    print("\n正在绘制叠加后的波形...")
    period = 1.0 / wave3.frequency
    t = np.linspace(0, period, 1000)
    y = wave3.evaluate(t)
    
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, y)
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.title(f'Superposed Wave: A={wave3.amplitude}, f={wave3.frequency} Hz')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()