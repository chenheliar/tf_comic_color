from build_generator import *
import matplotlib.pyplot as plt

# def generate_images(model, test_input, name):
#     prediction = model(test_input, training=True)
#     basepath = os.path.dirname(__file__)
#     downloadpath = os.path.join(basepath, 'downloads', )
#     filename = "{}.png".format(name[:-4])
#     filepath = os.path.join(downloadpath, filename)
#     mp.imsave(filepath, prediction[0] * 0.5 + 0.5)
#     return filepath

def generate_images(model, test_input, tar):
  # the training=True is intentional here since
  # we want the batch statistics while running the model
  # on the test dataset. If we use training=False, we will get
  # the accumulated statistics learned from the training dataset
  # (which we don't want)
  prediction = model(test_input, training=True)
  plt.figure(figsize=(15,15))

  display_list = [test_input[0], tar[0], prediction[0]]
  title = ['Input Image', 'Ground Truth', 'Predicted Image']

  for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.title(title[i])
    # getting the pixel values between [0, 1] to plot it.
    plt.imshow(display_list[i] * 0.5 + 0.5)
    # plt.imsave("testimg/"+str(i)+".jpg",display_list[i] * 0.5 + 0.5)
    plt.axis('off')
  plt.show()

# 恢复到最后的检查点
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))

def load_uploadpic(pic, name):
    image = loadpic(pic)
    image = tf.expand_dims(image, 0)
    path = generate_images(generator, image, name)
    return path

for inp,tar in test_dataset.take(5):
    generate_images(generator, inp, tar)

# load_uploadpic("test.jpg","test")