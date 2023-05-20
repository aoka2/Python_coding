import tkinter


class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root,
            width=380,height=280,
            borderwidth=4,relief='groove')
        
        self.root=root
        self.pack()#位置を指定
        self.pack_propagate(0)#サイズを調整
        self.create_widges()
     # 閉じるボタン

    def create_widges(self):
        quit_btn=tkinter.Button(self) #Buttonクラスをquit_btnに変数に代入
        quit_btn['text']='閉じる' #textに表示したい文字を代入
        quit_btn['command']= self.root.destroy #土台のアプリを終了する
        quit_btn.pack(side='bottom') #一番下という意味のbottomをsideに代入
    
    #テキストボックス
        self.text_box = tkinter.Entry(self)
        self.text_box['width'] = 10
        self.text_box.pack()

    #テキストを読み込む実行ボタン
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = '実行'
        submit_btn['command'] = self.input_handler
        submit_btn.pack()
    #メッセージ出力
        self.message = tkinter.Message(self)
        self.message.pack()

    def input_handler(self):
        
        text = self.text_box.get()
        self.message['text'] = text + '!!' #get()したtextに！！を追記している

root = tkinter.Tk()
root.title('サプーアプリ')
root.geometry('400x300')
app = Application(root=root)
root.mainloop() #アプリの実行