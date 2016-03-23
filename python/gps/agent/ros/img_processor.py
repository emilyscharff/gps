import rospy
import roslib
from sensor_msgs.msg import Image
from ddp_controller_pkg.msg import ImgFeatures

def process_image(hyperparams, network, event):
	global hyperparams = hyperparams
	global network
	rospy.init_node('img_processor', anonymous=True)
  	rospy.Subscriber(hyperparams["subscribe_topic"], Image, process)

def process(image):
	if event.isSet():
  		rospy.signal_shutdown()

	image_data = np.fromstring(image.data, np.uint8).reshape(image.height, image.width, 3)[::-1, :, ::-1]
	image_data = image_data[hyperparams["vertical_crop"]:image.height - hyperparams["vertical_crop"],
	                        hyperparams["horizontal_crop"]:image.height - hyperparams["horizontal_crop"]]

    # Put data through the nueral network
	features = network(image_data)
	publisher = rospy.Publisher(hyperparams["publish_topic"], ImgFeatures)
	pub.publish(features)

