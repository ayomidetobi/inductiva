"""Sample usage of DualSPHysics simulation via the API."""
from absl import logging
from absl import flags
from absl import app

import inductiva

FLAGS = flags.FLAGS

flags.DEFINE_string("api_url", "http://api.inductiva.ai",
                    "Base URL of the Inductiva API.")
flags.DEFINE_string("sim_dir",
                    None,
                    "Directory with the simulation inputs.",
                    required=True)
flags.DEFINE_string("input_filename",
                    None,
                    "Name of the input file.",
                    required=True)
flags.DEFINE_string("output_dir",
                    None,
                    "Directory where the outputs will be stored.",
                    required=True)
flags.DEFINE_string("device", "gpu",
                    "Device in which device the simulation will run.")


def main(_):
    """Run a DualSPHysics simulation using user-provided input files."""

    inductiva.api_url = FLAGS.api_url

    sph_sim = inductiva.fluids.simulators.DualSPHysics(
        sim_dir=FLAGS.sim_dir, input_filename=FLAGS.input_filename)

    output_path = sph_sim.simulate(output_dir=FLAGS.output_dir,
                                   device=FLAGS.device)

    logging.info("Outputs stored in %s", output_path)


if __name__ == "__main__":
    app.run(main)
