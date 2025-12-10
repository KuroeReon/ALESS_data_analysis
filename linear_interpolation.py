import numpy as np
from scipy.interpolate import interp1d
import math

def linear_interpolation_y(text_name: str):

    # --- テキスト読み込み ---
    data = np.loadtxt(text_name, delimiter=",")  # x,y が2列の場合
    x = data[:,0] 
    y = data[:,1]

    # --- 線形補間関数を作成 ---
    f = interp1d(x, y, kind='linear')  # 線形補間

    # --- 補間するx座標を生成、xの最小値,最大値を小数第4位で切り上げ、切り下げした範囲で0.001mごと ---
    min_x_round = math.ceil(min(x) * (10**3)) / (10**3)
    max_x_round = math.floor(max(x) * (10**3)) / (10**3)
    print(min_x_round)
    print(max_x_round)
    x_new = np.linspace(min_x_round, max_x_round, round((max_x_round - min_x_round) / 0.001 + 1))

    # --- 補間実行 ---
    y_new = f(x_new)

    # --- 最初の地点が（0，0）になるように平行移動 ---
    x_new_offset = x_new - np.full(round((max_x_round - min_x_round) / 0.001 + 1), min_x_round)
    y_new_offset = y_new - np.full(round((max_x_round - min_x_round) / 0.001 + 1), y_new[0])

    return y_new_offset


def linear_interpolation_x(text_name: str):

    # --- テキスト読み込み ---
    data = np.loadtxt(text_name, delimiter=",")  # x,y が2列の場合
    x = data[:,0] 

    # --- 補間するx座標を生成、xの最小値,最大値を小数第4位で切り上げ、切り下げした範囲で0.001mごと ---
    min_x_round = math.ceil(min(x) * (10**3)) / (10**3)
    max_x_round = math.floor(max(x) * (10**3)) / (10**3)
    print(min_x_round)
    print(max_x_round)
    x_new = np.linspace(min_x_round, max_x_round, round((max_x_round - min_x_round) / 0.001 + 1))

    # --- 最初の地点が（0，0）になるように平行移動 ---
    x_new_offset = x_new - np.full(round((max_x_round - min_x_round) / 0.001 + 1), min_x_round)

    return x_new_offset