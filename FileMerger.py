# coding: UTF-8
#統合元のデータファイルを開く(パスで指定)
f_x = open('./dataStressChainNew/pvx00479.dat', 'r')
f_y = open('./dataStressChainNew/pvy00479.dat', 'r')
f_z = open('./dataStressChainNew/pvz00479.dat', 'r')
#統合先(書き込み先)のファイルを開く
f = open('./dataStressChainNew/pv00479.dat', 'w')

#データ読み込み
data_x = f_x.readlines()
data_y = f_y.readlines()
data_z = f_z.readlines()

#読み込んだファイルがすべて同じデータ数かをファイルの行数で判断する
if(len(data_x)==len(data_y)==len(data_z)):
   num=int(data_x[0])
   f.write(str(num) +'\n')

   for i in range(1,len(data_x)):

     toks_x = data_x[i].split()  # 第i行を半角スペースで分割する
     toks_y = data_y[i].split()
     toks_z = data_z[i].split()

     for k in range(len(toks_x)):  # 読み込んだ行のk番目の数値を書き込む
          #print(toks_x[k])
          num_x=float(toks_x[k])
          num_y=float(toks_y[k])
          num_z=float(toks_z[k])
          f.write(str(num_x)+' '+str(num_y)+' '+str(num_z)+'\n') #ファイルに書き込み
          
#ファイルを閉じる
f_x.close()
f_y.close()
f_z.close()
f.close()
