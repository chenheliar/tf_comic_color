from build_generator import *
import datetime
import sys

from test_model import *
# import requests




def fit(train_ds, epochs):
    # test_log_dir = 'logs/gradient_tape/' + current_time + '/test'
    current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    train_log_dir = 'logs/gradient_tape/' + current_time + '/train'
    train_summary_writer = tf.summary.create_file_writer(train_log_dir)
    # test_summary_writer = tf.summary.create_file_writer(test_log_dir)
    global step_time
    global epoch_time
    global file_num
    

    for epoch in range(epoch_time, epochs):
        start = time.time()
        count = 0

        # Train
        for input_image, target in train_ds:
            evtime = time.time()

            gloss, dloss = train_step(input_image, target)
            step_time = step_time + 1


            # print(tf.constant(gloss).numpy())
            # getconfig.writestep(step_time, "step")
            # getconfig.writestep(step_time // file_num, "epoch")
            count = count + 1
            # print('第{}轮第{}张，耗时{:.3f}s, G_loss:{:.3f}, D_loss:{:.3f}\n'.format(epoch, count, time.time() - evtime,
            #                                                                   tf.constant(gloss).numpy(),
            #                                                                   tf.constant(dloss).numpy()))
            sys.stdout.write('\r第{}轮第{}张/{}，耗时{:.3f}s, G_loss:{:.3f}, D_loss:{:.3f}'.format(epoch, count,file_num, time.time() - evtime,
                                                                              tf.constant(gloss).numpy(),
                                                                              tf.constant(dloss).numpy()))                                                                              
            if (count + 1) % 2000 == 0:
                with train_summary_writer.as_default():

                    # tensorboard
                    tf.summary.scalar("G_loss", gloss, step=step_time)
                    tf.summary.scalar("D_loss", dloss, step=step_time)
                # checkpoint.save(file_prefix=checkpoint_prefix)
                
                # load_testpic(str(epoch)+str(count))
                # print('模型保存第{}轮第{}张，耗时{}\n'.format(epoch, count, time.time() - start))
                manager.save()
                print('\n模型保存第{}轮第{}张，耗时{}\n'.format(epoch, count, evtime - start))

                # load_testpic(str(epoch)+str(count))
        getconfig.writestep(step_time, "step")
        # saving (checkpoint) the model every 20 epochs
        # if (epoch + 1) % 1 == 0:
        #     checkpoint.save(file_prefix=checkpoint_prefix)
        # 微信提醒训练进度
        # requests.get(
        #     'https://sc.ftqq.com/SCU30568T9cc1a21bc95bea7726d00432f1b385ca5b6ef4031bfef.send?text=训练进度提醒&desp=Time_taken_for_epoch_{}_is_{}_sec'.format(
        #         epoch + 1, time.time() - start))

        # checkpoint.save(file_prefix=checkpoint_prefix)
        # print('Time taken for epoch {} is {} sec\n'.format(epoch + 1, time.time() - start))
        # manager.save()


print("train start")

# checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))




if epoch_time < EPOCHS:
    fit(train_dataset, EPOCHS)
else:
    print("训练已结束")
