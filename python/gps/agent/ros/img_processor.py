import rospy
import roslib
from sensor_msgs.msg import Image
from ddp_controller_pkg.msg import ImgFeatures

class Image_Processor():
    def __init__(self, hyperparams, network, event):
        self._hyperparams = hyperparams
        self._network = network
        self._event = event
        self.publisher = rospy.Publisher(self.hyperparams["publish_topic"], ImgFeatures)

    def process_images():
        rospy.init_node('img_processor', anonymous=True)
        rospy.Subscriber(self._hyperparams["subscribe_topic"], Image, process)

    def process(image):
    	if self._event.isSet():
      	 rospy.signal_shutdown()

        image_data = np.fromstring(image.data, np.uint8).reshape(image.height, image.width, 3)[::-1, :, ::-1]
        image_data = image_data[self._hyperparams["vertical_crop"]:image.height - self._hyperparams["vertical_crop"],
    	                        self._hyperparams["horizontal_crop"]:image.height - self._hyperparams["horizontal_crop"]]

        # Put data through the nueral network
        self._network.blobs[self.net.blobs.keys()[0]].data[:] = image_data
        features = self._network.forward().values()[0][0]
        features = self._network(image_data)
        self.publisher.publish(features)

