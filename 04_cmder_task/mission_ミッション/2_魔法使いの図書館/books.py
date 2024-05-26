# このプログラムは魔法図書館の本棚管理システムです。

class MagicLibraryBookshelf:
    def __init__(self):
        self.books = []

    # 本を本棚に追加するメソッド
    def add_book(self, book_title, author):
        self.books.append({"title": book_title, "author": author})
        print(f"新しい本「{book_title}」が追加されました。")

    # 本棚の全ての本をリストするメソッド
    def list_books(self):
        print("本棚にある本:")
        for book in self.books:
            print(f"- {book['title']} by {book['author']}")

bookshelf = MagicLibraryBookshelf()
bookshelf.add_book("魔法界の歴史", "マーリン")
bookshelf.add_book("薬草とポーション", "ポンデリーナ")

# TODO: 本をカテゴリで分類する機能を追加する
# 現在は単純に本のリストを表示していますが、
# より使いやすくするためにカテゴリ別に分類した表示ができるように改良を計画しています。

bookshelf.list_books()