
import rospy
from gpr20_data_processing.data_processing import DataProcessing
from gpr20_msgs.srv import ProcessingStoreData, ProcessingStoreDataResponse

class DataNode(object):

    def __init__(self):

        rospy.init_node("data_processing", anonymous=False)

        rospy.Service(
            "processing_store_data",
            ProcessingStoreData,
            self.__store_data_handler
        )

        rospy.spin()

    def __store_data_handler(self, srv):
        """Hanlde the request to store data of GPR-20.
        
        Args:
            srv (gpr20_msgs.srv.ProcessingStoreData): service message request
                to store sample data.

        Returns:
            gpr20_msgs.srv.ProcessingStoreDataResponse: empty response to
                indicate that process has finished.
        """
        # Call the method to store data in file
        DataProcessing.process_data(
            srv.survey_dir,
            srv.x_coord,
            srv.y_coord,
            srv.z_coord,
            srv.antennae_height,
            srv.timestamp,
            srv.survey_id,
            srv.sample_id,
            srv.vna_freq,
            srv.vna_trace
        )

        # Return the request response
        return ProcessingStoreDataResponse()        
