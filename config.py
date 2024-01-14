rabbitmq_config = dict(
    adress='rabbitmq',
    port='5672',
    queue_input='image_to_process',
    queue_output='image_result'
)

tensorflow_config = dict(
    class_names=['Agate', 'Amethyst', 'Azurite', 'Calcite', 'Chrysocolla', 'Citrine', 'Emerald', 'Gypsum',
                 'Labradorite', 'Malachite', 'Opal', 'Pyrite', 'Quartz', 'Ruby', 'Smoky quartz', 'Topaz', 'Tourmaline',
                 'Turquoise', 'Wulfenite'],
    image_shape=(299, 299),
    num_classes=19,
    model_path="/app/model_ai/model"
)
