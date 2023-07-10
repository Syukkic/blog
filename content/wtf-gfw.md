+++
date = 2019-06-03T15:17:05+08:00
title = "中國互聯網維護日前後記"
+++

兒童節當天早上，個人的 VPS 如常順利連接。快到中午時分，電腦狀態欄的 Dropbox 圖標出現異常，開始以爲是正常的丟包所導致連接失敗，重啓網絡後仍不能恢復正常，於是停止
[Shadowsocks](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjx9qvRltHiAhWHZ1AKHdJsAx4QFjAAegQIBBAB&url=https%3A%2F%2Fshadowsocks.org%2F&usg=AOvVaw1ufD84XQhIpu7cVnkQh9Sg) 轉用 [V2Ray](https://www.v2ray.com/index.html)，重新連接，一切正常。午睡醒來後，事情變得很不正常了。V2Ray 無法建立正常連接，打算 SSH 到服務器查看並重啓，發現無法建立連接。見到這情況後，我明白了，IP
又一次被 TCP 阻斷了。

搶險一個多小時後，總算重新聯網了。

到 Telegram 一看，數個羣組的在線人數明顯比平時要少，但信息數量依舊很多。有趣的是，各個羣組都是由不同的話題而建起的，可能中間用戶有交集，但在每個羣組討論的話題都是圍繞無法正常訪問互聯網而展開——「我的 SS 倒了」，「全倒了」，「V2Ray + ws + tls 最堅挺」，「套個 CDN 吧」等等。《一天世界》博客的 Telegram Channel 也發起了[投票](https://t.me/yitianshijie/511)來進行簡單調查。這期間觀察到至少四點：

1. 能投票的說明 TA 們仍能訪問互聯網，這裡頭顯然有[倖存者偏差](https://zh.wikipedia.org/zh-hant/%E5%80%96%E5%AD%98%E8%80%85%E5%81%8F%E5%B7%AE)，當然啦，投票的題目是「二零一九年五月底六月初，妳覺得 VPN、Shadowsocks 或類似工具在中國變得更難用了嗎？」
2. 在 Telegram 的相關技術交流羣裡，面對突然的國家力量來襲，網友們除了抱怨，剩下可能只有不斷換 IP。問題在與這些是「術」層面，我並非要站在 XX 最高點要求使用者都要去到「道」層面。問題延伸開去，可以去到更根本，如果關注「道」的人少了，日後會有迭代出新技術嗎？（沒有了[一鍵安裝腳本](https://teddysun.com/548.html)，自己是否可以一步步搭建起來？）
3. 與長輩們相信微信公衆號文章「吃 XXX 會致癌」和「喝 XXX 能延壽」爲真的情況類似，「美國的 IP 都不行了」、「『V2Ray 會不會好些？』『我的 V2Ray 剛被封了，用 SS 吧』」抑或「『我的 SS 全倒了』『SS 不行了，用 V2Ray 啦』」。恐懼和無知（無貶義）往往讓我失去應有的理性思考。
4. 我想國家這麼大動作，不是適得其反嗎？細想下其實自己也是陷入了認知偏誤。我畢竟長期能夠連接道互聯網，而長期在局域網內人不會查覺到，即使察覺異常，可能也被自己的「[認知失調](https://en.wikipedia.org/wiki/Cognitive_dissonance)」機制調整回來。但局域網的人真的是這樣子嗎？

說回自己，如「觀察二」談到，我之前也是「拿來就用」，但此次「搶險」中，Shadowsocks 的連接全失敗了，也迫使自己仔細看了 V2Ray 的官方文檔。兩年前就聽說過 V2Ray，但惰性遲遲阻礙去瞭解它。人，還是不能停止學習。

寫這篇後記的同時，我其中一個 IP 又被封了。