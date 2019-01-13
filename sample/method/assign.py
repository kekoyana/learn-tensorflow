# 参考: https://qiita.com/rindai87/items/4b6f985c0583772a2e21
import tensorflow as tf

# cntという変数（カウンター）の定義
cnt = tf.Variable(0, name="cnt")
inc = tf.constant(1, name="inc")

# カウントアップ
add_op = tf.add(cnt, inc)

# cntの値を更新
up_op = tf.assign(cnt, add_op)

with tf.Session() as sess:
    # 変数を使う場合はまず初期化が必要
    sess.run(tf.global_variables_initializer())

    # カウントアップを計3回実行
    for step in range(3):
      print(sess.run(up_op))
