
from gpr20_data_processing.data_parsing import DataParsing
from gpr20_data_processing.data_storage import DataStorage

class DataProcessing(object):

    @staticmethod
    def process_data(
        survey_dir,
        x_coord,
        y_coord,
        z_coord,
        antennae_height,
        timestamp,
        survey_id,
        sample_id,
        vna_freq,
        vna_trace
    ):

        # Parse the frequency response
        vna_freq = DataParsing.parse_vna_frequency(vna_freq)

        # Parse the trace response
        vna_trace_re, vna_trace_im = DataParsing.parse_vna_trace(
            vna_trace
        )

        # Store the data in the corresponding JSON file
        DataStorage.store_data(
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
        )
