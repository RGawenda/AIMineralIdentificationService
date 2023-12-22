rabbitmq_config = dict(
    adress='localhost',
    port='',
    queue_input='image_to_process',
    queue_output='image_result'
)

tensorflow_config = dict(
    class_names=['Agate', 'Amethyst', 'Azurite', 'Calcite', 'Chrysocolla', 'Citrine', 'Emerald', 'Gypsum',
                 'Labradorite', 'Malachite', 'Opal', 'Pyrite', 'Quartz', 'Ruby', 'Smoky quartz', 'Topaz', 'Tourmaline',
                 'Turquoise', 'Wulfenite'],
    image_shape=(256, 256),
    num_classes=19,
    model_path="C:\\Users\\Roman\\jup\\inz_model\\model_transfer_xception_block"
)
