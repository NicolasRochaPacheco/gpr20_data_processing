
import os
import json

class DataStorage(object):
    """ Class to store data using the JSON format.

    The class main objective is to provide the means to store samples in a
    persistent storage with a consistent format. The class also provides
    methods to manage the folders in order to prevent errors from happening.
    """

    @staticmethod
    def store_data(
        survey_dir,
        x_coord,
        y_coord,
        z_coord,
        antennae_height,
        timestamp,
        survey_id,
        sample_id,
        vna_freq,
        vna_trace_re,
        vna_trace_im
    ):
        """ Store the robot data for a sample in the required format.
        
        Args:

            survey_id ()
        
        """
        # Create the data list
        data_list = []

        # Formats the data list
        for indx in range(len(vna_freq)):

            # Create the dictionary for a data element
            data_dict = {
                "freq_value": vna_freq[indx],
                "real_value": vna_trace_re[indx],
                "imaginary_value": vna_trace_im[indx]
            }

            # Append the dictionary to the data list
            data_list.append(data_dict)

        # Create the file dictionary
        file_dict = {
            "x_coord": x_coord,
            "y_coord": y_coord,
            "z_coord": z_coord,
            "antennae_height": antennae_height,
            "timestamp": timestamp,
            "survey_id": survey_id,
            "sample_id": sample_id,
            "data": data_list
        }

        # Convert the file dictionary into JSON string
        json_str = json.dumps(file_dict, indent=4)

        # Create the file name
        fname = "X{:06.2f}_Y{:06.2f}_Z{:06.2f}.json".format(x_coord, y_coord, z_coord)

        # Check that main folder exists
        main_dir = DataStorage.__check_main_folder()

        # Creates the survey folder path
        survey_path = main_dir + '/' + survey_dir

        # Check that survey folder exists
        DataStorage.__check_survey_folder(survey_path)

        # Open the file to write JSON string
        with open(survey_path + '/' + fname, 'w') as json_file:
            
            # Save the JSON string into file
            json_file.write(json_str)

    @staticmethod
    def __check_main_folder():
        """ Check the main folder for storing GPR-20 surveys data.
        
        Returns:
            str: path to survey main folder.
        
        """
        # Get the home directory path
        home_path = os.path.expanduser('~')

        # Define the main folder path
        main_folder = home_path + "/gpr20_data/"

        # Check if main directory exists
        main_dir_exists = os.path.exists(main_folder)

        # Create the directory if it does not exists
        if not main_dir_exists:

            # Create the main directory for storing surveys
            os.mkdir(main_folder)

        # Return the main folder full path
        return main_folder

    @staticmethod
    def __check_survey_folder(path):
        
        # Check if main directory exists
        survey_dir_exists = os.path.exists(path)

        # Create the directory if it does not exists
        if not survey_dir_exists:

            # Create the main directory for storing surveys
            os.mkdir(path)
