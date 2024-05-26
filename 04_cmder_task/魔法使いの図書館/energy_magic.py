# extended_sample1.py

# このプログラムは魔法の杖を通じてエネルギーの波動を測るものです。

def measure_wand_energy(level):
    # 杖のエネルギーレベルを測定します。
    if level < 5:
        print("杖のエネルギーが足りません！")
    elif level == 5:
        print("杖のエネルギーが平均です。")
    else:
        print("杖のエネルギーが溢れています！")

# TODO: エネルギーレベルを時間経過で変化させるシミュレーションを追加する
energy_level = 7
measure_wand_energy(energy_level)

# 現状では単純にエネルギーレベルを表示しているだけですが、
# シミュレーション機能を追加することでよりリアルな挙動を確認できるようにする予定です。