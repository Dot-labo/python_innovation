"""
 pythonのclassの作り方を説明するためのサンプルコード
 "Wizard" というクラス(設計図)を名前だけ定義していますが、まだなんの役にも立っていません。
"""

# Wizardクラスを定義
# classを定義する時は、class クラス名: というコードブロックを作成します。
class Wizard:
    pass

# "Wizard"クラスのインスタンス "wizard" を生成
# クラスからインスタンス(実体)を作る時は、インスタンスの名前 = クラス名() というふうに書きます。
wizard = Wizard()

# インスタンス「wizard」にインスタンス変数を追加
wizard.name = 'マーリン'
wizard.hp = 14
wizard.mp = 27
wizard.magic_list = ['Fireball', 'Ice Storm', 'Lightning Bolt']

# インスタンス「wizard」のインスタンス変数を表示
# インスタンス変数を表示する際には、「インスタンス名.メンバ変数名」と書く
print("私は", wizard.name)
print("HPは", wizard.hp)
print("MPは", wizard.mp)
print("覚えている魔法は", wizard.magic_list)
