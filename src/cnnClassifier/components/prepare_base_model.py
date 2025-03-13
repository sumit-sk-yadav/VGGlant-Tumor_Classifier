from pathlib import Path
import tensorflow as tf
from cnnClassifier.entity.config_entity import BaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: 'BaseModelConfig'):
        self.config = config
    
    def get_base_model(self):
        # Load the base model (e.g., VGG16)
        self.model = tf.keras.applications.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )
        # Save the base model
        self.save_model(path=self.config.base_model_path, model=self.model)
    
    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        # Freeze the layers as needed
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif freeze_till is not None and freeze_till > 0:
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        # Add the custom classification layers
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation='softmax'
        )(flatten_in)

        # Create the final model
        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        # Recreate and assign the optimizer after modifying the model
        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
        )
        
        # Print the summary of the model
        full_model.summary()
        
        return full_model
    
    def update_base_model(self):
        # Prepare the full model by modifying the base model
        self.full_model = self.prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
        
        # Save the updated model
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        # Save the model to the given path
        model.save(path)
