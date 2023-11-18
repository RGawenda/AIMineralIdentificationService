rabbitmq_config = dict(
    adress='localhost',
    port='',
    queue_input='image_to_process',
    queue_output='image_result'
)

tensorflow_config = dict(
    class_names=['agate', 'amethyst', 'azurite', 'calcite', 'chrysocolla', 'citrine', 'emerald', 'gypsum',
                 'labradorite', 'malachite', 'opal', 'pyrite', 'quartz', 'ruby', 'smoky quartz', 'topaz', 'tourmaline',
                 'turquoise', 'wulfenite'],
    image_shape=(720,720),
    num_classes=19,
    model_path="model_50",
)
