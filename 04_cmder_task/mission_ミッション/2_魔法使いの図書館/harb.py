# このプログラムは、魔法の薬草園で育つ植物を管理するためのものです。

class MagicalHerbGarden:
    def __init__(self):
        self.herb_list = []

    # 薬草を追加するメソッド
    def plant_herb(self, herb_name):
        self.herb_list.append(herb_name)
        print(f"{herb_name}を植えました。")

    # 薬草園の全ての植物を表示するメソッド
    def display_herbs(self):
        print("薬草園にある植物たち:")
        for herb in self.herb_list:
            print(f"- {herb}")

garden = MagicalHerbGarden()
garden.plant_herb("マンドレイク")
garden.plant_herb("ヴァーベナ")

# TODO: 薬草に季節ごとの成長サイクルを追加する
# 今のところ、植物は一度植えると成長せずにそのままですが、
# 季節に合わせて成長するようにしたいと考えています。

garden.display_herbs()