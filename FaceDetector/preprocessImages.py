import tensorflow as tf
import os

def preprocess_image(image):
    """
    Preprocesses a single image.

    Parameters:
    - image (Tensor): The raw image data as a Tensor.

    Returns:
    - Tensor: The preprocessed image data as a Tensor.
    """
    # Convert the image data to float32
    image = tf.image.convert_image_dtype(image, tf.float32)

    # Resize the image to (64, 64)
    image = tf.image.resize(image, (64, 64))

    # Normalize the pixel values
    image = (image - 127.5) / 127.5

    return image

def preprocess_images(data_dir):
    """
    Preprocesses images of people and saves the preprocessed images to a new directory.

    Parameters:
    - data_dir (str): The path to the directory containing the raw images.

    Returns:
    - None
    """
    # Create a directory to store the preprocessed images
    preprocessed_data_dir = os.path.join(data_dir, 'preprocessed')
    if not os.path.exists(preprocessed_data_dir):
        os.makedirs(preprocessed_data_dir)

    # Loop over the images in the data directory
    for filename in os.listdir(data_dir):
        # Load the image
        image = tf.io.read_file(os.path.join(data_dir, filename))
        image = tf.image.decode_jpeg(image)

        # Preprocess the image
        preprocessed_image = preprocess_image(image)

        # Save the preprocessed image
        preprocessed_filename = os.path.join(preprocessed_data_dir, filename)
        tf.io.write_file(preprocessed_filename, tf.image.encode_jpeg(preprocessed_image))

# Example usage
data_dir = r"C:\\Users\\sean2\\OneDrive\\Desktop\\Python Projects\\images"
preprocess_images(data_dir)

