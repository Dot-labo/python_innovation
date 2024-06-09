"""
pyxelの基本を学ぶためのサンプルコード

矢印キーで円を動かすだけの簡単なプログラムですが、pyxelの基本的な使い方がわかります。
classを使わないで、関数だけでゲームを作成しています。

pyxelの初期化の後、、更新関数、描画関数を定義しています。
最後にpyxel.run()に更新関数と描画関数を渡すとゲームが開始されます。
"""
import pyxel

#ここでは初期化を行っています.
pyxel.init(160, 120, title="Hello Pyxel") #画面のサイズを160x120に設定、タイトルを設定
# 円のx座標とy座標の初期値（画面の中心）
x = 80
y = 60

# 更新関数 ここに書いた処理がゲームの中で毎フレーム実行されることになります。
def update():
    global x, y  # グローバル変数として座標を更新

    if pyxel.btn(pyxel.KEY_UP):
        y -= 2  # 上矢印キーで上に移動 (なぜマイナスすると上に移動するかというと、画面の一番上がy = 0, 一番下がy = 120だからです。)
    if pyxel.btn(pyxel.KEY_DOWN):
        y += 2  # 下矢印キーで下に移動 
    if pyxel.btn(pyxel.KEY_LEFT):
        x -= 2  # 左矢印キーで左に移動
    if pyxel.btn(pyxel.KEY_RIGHT):
        x += 2  # 右矢印キーで右に移動

# 描画関数 ここに書いた処理によって画面が描画されます。
def draw():
    pyxel.cls(0)  # 画面を黒でクリア
    pyxel.circ(x, y, 10, 7)  # (x, y)座標に半径10, 色7（赤色）の円を描画
    
# 更新関数と描画関数をpyxel.run()に渡すことで、ゲームが開始されます。
pyxel.run(update, draw)