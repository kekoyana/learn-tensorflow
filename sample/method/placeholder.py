# 参考: https://qiita.com/rindai87/items/4b6f985c0583772a2e21
import tensorflow as tf

# 定数の定義
x = tf.constant(1, name="x")
# プレースホルダーという箱を用意する
y = tf.placeholder(tf.int32, name="y")

# x+yの演算を定義
add_op = tf.add(x, y)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # プレースホルダーには、feed_dictという仕組みを通じて値を外挿できる
    print(sess.run(add_op, feed_dict={y:1}))
    print(sess.run(add_op, feed_dict={y:3}))
