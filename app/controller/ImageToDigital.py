# encoding=utf-8
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image, ImageFilter
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


def imageprepare(argv):
    im = Image.open(argv).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    if width > 28:
        img = im.resize((28, 28), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        tv = list(img.getdata())  # get pixel values
    elif width < 28:
        img = im.resize((28, 28), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        tv = list(img.getdata())  # get pixel values
    else:
        tv = list(im.getdata())
        return tv  # get pixel values
    return tv


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def recognize(picturePath):
    myGraph = tf.Graph()
    with myGraph.as_default():
        with tf.name_scope('inputsAndLabels'):
            x_raw = tf.placeholder(tf.float32, shape=[None, 784], name="x")
        with tf.name_scope('hidden1'):
            x = tf.reshape(x_raw, shape=[-1, 28, 28, 1])
            W_conv1 = weight_variable([5, 5, 1, 32])
            b_conv1 = bias_variable([32])
            l_conv1 = tf.nn.relu(tf.nn.conv2d(x, W_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1)
            l_pool1 = tf.nn.max_pool(l_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        with tf.name_scope('hidden2'):
            W_conv2 = weight_variable([5, 5, 32, 64])
            b_conv2 = bias_variable([64])
            l_conv2 = tf.nn.relu(tf.nn.conv2d(l_pool1, W_conv2, strides=[1, 1, 1, 1], padding='SAME') + b_conv2)
            l_pool2 = tf.nn.max_pool(l_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        with tf.name_scope('fc1'):
            W_fc1 = weight_variable([64 * 7 * 7, 1024])
            b_fc1 = bias_variable([1024])
            l_pool2_flat = tf.reshape(l_pool2, [-1, 64 * 7 * 7])
            l_fc1 = tf.nn.relu(tf.matmul(l_pool2_flat, W_fc1) + b_fc1)
            keep_prob = tf.placeholder(tf.float32)
            l_fc1_drop = tf.nn.dropout(l_fc1, keep_prob)
        with tf.name_scope('fc2'):
            W_fc2 = weight_variable([1024, 10])
            b_fc2 = bias_variable([10])
            y_conv = tf.matmul(l_fc1_drop, W_fc2) + b_fc2

    with tf.Session(graph=myGraph) as sess:
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.restore(sess, 'app/model/model.ckpt-1')
        array = imageprepare(picturePath)
        prediction = tf.argmax(y_conv, 1)  # 计算一行的最大值，返回的是一个最大值的坐标
        prediction = prediction.eval(feed_dict={x_raw: [array], keep_prob: 1},
                                     session=sess)  # 对".eval"对值进行评估，这里我们前面定义了多少个占位符，在session.run()的时候就要喂多少个数据,可以不用在意这句话，这句话的含义相等于session.run

        #writer = tf.summary.FileWriter("/home/hytera/log")

        x = sess.run(tf.cast(tf.nn.softmax(y_conv), tf.float32),
                     feed_dict={x_raw: [array], keep_prob: 1})  # 输出概率,输出的为*100的数
        return x[0]
        #print(x[0])
        #writer.add_graph(sess.graph)
        #print('The digits in this image is:%d' % prediction)
