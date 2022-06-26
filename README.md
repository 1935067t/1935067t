# FileMerger.ipynbについて

x座標を示すファイル、y座標を示すファイル、z座標を示すファイルの３つファイルを１つのファイルにまとめるためのプログラムです。
このプログラムを使用する際はgoogle driveに読み込むファイルとこのプログラムを置き、google colaboratoryで実行してください。

## 読み込むファイル

３つのファイルがそれぞれ同じデータの並び方をしていることを想定しています（例えば、x座標が並ぶファイルが１行あたり５個のデータで１０００行あるとすると、yのファイルzのファイルも１行５個のデータで１０００行ある）

## 出力するファイル

それぞれの行にx,y,zの順に座標が並びます（つまり、点の数が５０００点あるならば５０００行３列のファイルが出力されます）

## 変更が必要な場所

1.  ４行目の/'My Drive'/以降は読み込むファイルがある場所を指定してください
```
from google.colab import drive
drive.mount('/content/drive')
# 作業フォルダへ移動（データのある場所を指定する）
%cd /content/drive/'My Drive'/研究室関連/dataStressChainNew/
# 現在のフォルダの中身を表示
%ls
```
2.  読み込むファイルと書き込むファイルはここで指定します
```
#統合元のデータファイルを開く
f_x = open('pvx00479.dat', 'r')
f_y = open('pvy00479.dat', 'r')
f_z = open('pvz00479.dat', 'r')
#統合先(書き込み先)のファイルを開く
f = open('pv00479.dat', 'w')
```
# FileMerger.pyについて

ターミナルやコマンドプロンプトで実行するにはこちらのプログラムを使用してください。
google colabo版と違いはファイルを開くときにパスも指定する必要があります。
```
#統合元のデータファイルを開く(パスで指定)
f_x = open('./dataStressChainNew/pvx00479.dat', 'r')
f_y = open('./dataStressChainNew/pvy00479.dat', 'r')
f_z = open('./dataStressChainNew/pvz00479.dat', 'r')
```