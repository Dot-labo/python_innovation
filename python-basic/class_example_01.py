"""
 pythonのclassの作り方を説明するためのサンプルコード
 "Wizard" というクラス(設計図)を名前だけ定義していますが、まだなんの役にも立っていません。
"""

# Wizardクラスを定義
# classを定義する時は、class クラス名: というコードブロックを作成します。
class Wizard:
    pass

# "Wizard"クラスのインスタンス "wizard1" を生成
# クラスからインスタンス(実体)を作る時は、インスタンスの名前 = クラス名() というふうに書きます。
wizard_1 = Wizard()

# インスタンス「wizard_1」にメンバ変数を追加
wizard_1.name = 'マーリン'
wizard_1.hp = 14
wizard_1.mp = 27
wizard_1.magic_list = ['Fireball', 'Ice Storm', 'Lightning Bolt']

# インスタンス「wizard」のメンバ変数を表示
# メンバ変数を表示する際には、「インスタンス名.メンバ変数名」と書く
print("私は", wizard_1.name)
print("HPは", wizard_1.hp)
print("MPは", wizard_1.mp)
print("覚えている魔法は", wizard_1.magic_list)
