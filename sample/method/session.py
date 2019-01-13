# 参考: https://qiita.com/rindai87/items/4b6f985c0583772a2e21
import tensorflow as tf

cnt = tf.Variable(0, name="cnt")
inc = tf.constant(1, name="inc")

add_op = tf.add(cnt, inc)
up_op = tf.assign(cnt, add_op)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(3):
      print(sess.run(up_op))

# 別セッションなので結果がリセットされる
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(3):
      print(sess.run(up_op))
