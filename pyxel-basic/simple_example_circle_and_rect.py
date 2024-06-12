"""
pyxelの基本を学ぶためのサンプルコード
このコードではclassは利用しません。

円と四角形を描画し、別々に動かします。
- 矢印キーで円を移動させます。
- WASDキーで四角形を移動させます。
"""
import pyxel

#ここでは初期化を行っています.
pyxel.init(160, 120, title="Hello Pyxel") #画面のサイズを160x120に設定、タイトルを設定

# 円のx座標とy座標の初期値（画面の右側)
circle_x = 100
circle_y = 60

# 四角形のx座標とy座標の初期値（画面の左側) rectはrectangle(四角形)の略です。
rect_x = 60
rect_y = 60

# 更新関数 ここに書いた処理がゲームの中で毎フレーム実行されることになります。
def update():
    # グローバル変数を関数の中で更新するために必要です。
    global circle_x, circle_y  
    global rect_x, rect_y

    #矢印キーで円の座標を移動させます
    if pyxel.btn(pyxel.KEY_UP):
        circle_y -= 2
    if pyxel.btn(pyxel.KEY_DOWN):
        circle_y += 2
    if pyxel.btn(pyxel.KEY_LEFT):
        circle_x -= 2
    if pyxel.btn(pyxel.KEY_RIGHT):
        circle_x += 2

    #WASDキーで四角形の座標を移動させます
    if pyxel.btn(pyxel.KEY_W):
        rect_y -= 2
    if pyxel.btn(pyxel.KEY_S):
        rect_y += 2
    if pyxel.btn(pyxel.KEY_A):
        rect_x -= 2
    if pyxel.btn(pyxel.KEY_D):
        rect_x += 2

# 描画関数 ここに書いた処理によって画面が描画されます。
def draw():
    pyxel.cls(0)  # 画面を黒でクリア
    pyxel.circ(circle_x, circle_y, 10, 7)  # (x, y)座標に半径10, 色7（赤色）の円を描画
    pyxel.rect(rect_x, rect_y, 20, 20, 8)  # (x, y)座標に幅20, 高さ20, 色8（水色）の四角形を描画
    
# 更新関数と描画関数をpyxel.run()に渡すことで、ゲームが開始されます。
pyxel.run(update, draw)