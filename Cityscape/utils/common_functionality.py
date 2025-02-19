import os
from Cityscape.logging.logger import DualLogger
from Cityscape.exception.exception import CityscapeException
import cv2
import sys
import shutil

def png_to_jpeg(input_path, output_path):
    logger = DualLogger().get_logger()
    try:
        os.makedirs(output_path, exist_ok=True)

        for city in os.listdir(input_path):
            city_path = os.path.join(input_path, city)
            output_city_path = os.path.join(output_path, city)
            os.makedirs(output_city_path, exist_ok=True)

            for file in os.listdir(city_path):
                if file.endswith(".png"):
                    input_file_path = os.path.join(city_path, file)
                    output_file_path = os.path.join(output_city_path, file.replace(".png", ".jpg"))

                    # Read the PNG image
                    img = cv2.imread(input_file_path, cv2.IMREAD_COLOR)

                    # Check if the image is corrupt
                    if img is None:
                        logger.warning(f"Skipping corrupt image: {input_file_path}")
                        continue

                    # Convert and save as JPEG with quality control
                    cv2.imwrite(output_file_path, img, [cv2.IMWRITE_JPEG_QUALITY, 95])

                    logger.info(f"Successfully converted {input_file_path} → {output_file_path}")

    except Exception as e:
        logger.error(f"Error occurred while converting PNG to JPEG: {str(e)}", exc_info=True)
        raise CityscapeException(e, sys)

def annotations_to_Dataset(input_path,output_path):
    logger = DualLogger().get_logger()
    try:
        os.makedirs(output_path, exist_ok=True)

        for city in os.listdir(input_path):
            city_path = os.path.join(input_path, city)
            output_city_path = os.path.join(output_path, city)
            os.makedirs(output_city_path, exist_ok=True)


            for file in os.listdir(city_path):
                if file.endswith("_gtfine_color.png"):
                    input_file_path = os.path.join(city_path, file)
                    output_file_path = os.path.join(output_city_path, file)


                    shutil.copy(input_file_path, output_file_path)
                    logger.info(f"Successfully copied {input_file_path} → {output_file_path}")
    
    
    
    except Exception as e:
        logger.error(f"Error occurred while transferring data: {str(e)}", exc_info=True)
        raise CityscapeException(e, sys)          

if __name__ == '__main__':
    logger= DualLogger().get_logger()
    input_path=r"D:/MLops project/MLops-cityscape1/Raw Dataset/annotations/gtFine/val"
    output_path=r"D:/MLops project/MLops-cityscape1/Dataset/annotations/gtFine/val"
    annotations_to_Dataset(input_path, output_path)
    logger.info("Data transferred successfully")