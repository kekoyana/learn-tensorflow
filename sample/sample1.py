import tensorflow as tf
import numpy as np

# データ作る(x_data: 学習データ, y_data: 正しい結果(tensorflowはしらない))
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# 計算式の予測をつくる(これを何度も実行して予測する)
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

## 誤差関数
loss = tf.reduce_mean(tf.square(y - y_data))
## 勾配降下法
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初期化
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))
