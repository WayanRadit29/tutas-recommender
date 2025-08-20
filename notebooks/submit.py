import tensorflow_cloud as tfc

tfc.run(
    entry_point="train.py",
    requirements_txt="requirements.txt",
    docker_config=tfc.DockerConfig(parent_image="tensorflow/tensorflow:2.15.0"),
    chief_config=tfc.COMMON_MACHINE_CONFIGS["CPU"], 
    stream_logs= True
)