"""
__init__関数の説明

__init__関数は、クラスの初期化処理を行う関数です。
クラスを定義する際に、__init__関数を定義しておくと、そのクラスのインスタンスを生成する際に、 * 自動的に * __init__関数が呼び出されます。
__init__関数は、インスタンスを生成する際に、そのインスタンスが持つべきメンバ変数を初期化するために使用します。
"""
class Pet:
    #特別なメソッドである__init__関数を定義
    def __init__(self, animal_type): #selfは、インスタンス自身を指します
        self.animal_type = animal_type

# "Pet"クラスのインスタンス「p1」を生成 
# インスタンスを生成した瞬間に、そのインスタンス(p1)の持つ__init__関数が呼び出される
# その際に、引数として指定した値が、self.animal_type に代入される
# このように、インスタンスを生成する際に、初期化処理を行うことができる
p1 = Pet( animal_type='イヌ' )

print("私は", p1.animal_type, "を飼っています。")
