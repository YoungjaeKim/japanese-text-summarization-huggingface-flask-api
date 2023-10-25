# japanese-text-summarization-huggingface-flask-api

This repo gives an example of text summarization to use Japanese Bart model.

The request and response are as below;

```
http://127.0.0.1:5000/summarize
```

and Post sample UTF-8 text file with key `file` as below
```text
痛い思いをして抜いてもまた伸びる鼻毛。抜いた後にくしゃみが止まらなくなる鼻毛。こんな思いはもう二度としなくて済む。本当に手軽に処理出来ます。ひげ剃りみたいな感覚で鼻の穴に突っ込んで若干動かすだけで処理出来ます。かと言って剃り過ぎる事も無さそう。何より鼻呼吸がし易くなりました。想像以上に鼻毛は鼻呼吸の抵抗になっている事が実感として分かった。あると無いとで生活上の快適さが変わる、★５に値する商品。ありがとう。
いままではドンキでたしか500円で売っていた乾電池式の鼻毛カッターを使っていた。これが出来が悪くて、すぐに回らなくなる。今回もいろいろ迷ったけど、軽く回るしなかなかいい感じだ。そんなにたくさん使わないしこれで十分
以前、使ってたパナソニック製と遜色ない切り味です。何より充電式なのが、安心です。電池式だと減ってきたときのモーター音が、いつ止まるかと恐怖でしたが、毎回充電することで、安心できます。
持ち運びに便利なラウンド形状のペンスタイルでバッグに入れていても邪魔にならないです。USB充電なのでPCにつないで充電してます。勝手にスイッチが入らないためかもしれませんが、ON/OFFのスイッチが固いため操作がしづらいです。
```
The test is from one of [Amazon reviews](https://www.amazon.co.jp/-/en/Replacement-Washable-Rechargeable-Electric-Portable/product-reviews/B0C2Y71YXV/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2).
