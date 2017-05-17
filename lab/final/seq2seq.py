import numpy as np
import tensorflow as tf

learning_rate = 0.001
batch_size = 10
n_steps = 100
hidden_size = 300
input_size = 13
training_epochs = 1000
mfcc_size = 13
display_step = 50

mfcc_mat = np.load('final/mfcc_mat.npy') # [word_unit][time_step][value]
mfcc_mat = mfcc_mat[:len(mfcc_mat) / batch_size * batch_size]

x = tf.placeholder(tf.float32, [batch_size, n_steps, input_size])
y = tf.placeholder(tf.float32, [batch_size, n_steps, input_size])

encoder_inputs = tf.unstack(x, axis=1)
decoder_inputs = tf.unstack(y, axis=1)

encode_lstm = tf.contrib.rnn.BasicLSTMCell(hidden_size, forget_bias=1.0)
decode_lstm = tf.contrib.rnn.BasicLSTMCell(hidden_size, forget_bias=1.0)
decode_lstm = tf.contrib.rnn.OutputProjectionWrapper(decode_lstm, mfcc_size)
_, embedding = tf.contrib.rnn.static_rnn(encode_lstm, encoder_inputs, dtype=tf.float32)
decoder_outputs, _ = tf.contrib.legacy_seq2seq.rnn_decoder(decoder_inputs, embedding, decode_lstm)

true = [tf.reshape(encoder_input, [-1]) for encoder_input in encoder_inputs]
pred = [tf.reshape(decoder_output, [-1]) for decoder_output in decoder_outputs]
loss = 0
for i in range(len(true)):
    loss += tf.reduce_sum(tf.square(tf.subtract(pred[i], true[i])))
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(loss)

output = open('seqout', 'w')
init = tf.global_variables_initializer()
with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    sess.run(init)
    saver = tf.train.Saver()
    batch_num = 0
    for epoch in range(training_epochs):
	i = 0
	while i < len(mfcc_mat):
	    cur_in = mfcc_mat[i:i+batch_size]
	    cur_ans = mfcc_mat[i:i+batch_size]
	    for i in range(len(cur_ans)):
		cur_ans[i] = np.append([np.zeros(mfcc_size)], cur_ans[i][:-1], axis=0)
	    _, cost = sess.run([optimizer, loss], feed_dict={x:cur_in, y:cur_ans})
	    if i % display_step == 0:
                out.write('Batch: %s\n' %(batch_num))
		out.write('Loss: %s\n' %(cost))
		saver.save(sess, 'seq2seq')
	    batch_num += display_step
	    i += batch_size

