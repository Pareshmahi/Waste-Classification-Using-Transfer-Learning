import os
import shutil
import random

# Define main project path
project_path = r"C:\Coding and Career\Projects\Machine Learning Projects\College Minor Project - New\Waste Classification using Transfer Learning"

# Define dataset paths
dataset_path = os.path.join(project_path, "TrashBox")      # Original dataset
train_path = os.path.join(project_path, "Dataset")         # 90% data
val_path = os.path.join(project_path, "Data Validation")   # 10% data

# Ensure the directories exist
os.makedirs(train_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)

# Define class names
classes = ["paper", "plastic", "cardboard", "metal", "glass", "e-waste", "medical"]

# Define split ratio
split_ratio = 0.1  # 10% for validation, 90% for training

# Loop through each class and split data
for class_name in classes:
    class_dir = os.path.join(dataset_path, class_name)
    train_class_dir = os.path.join(train_path, class_name)
    val_class_dir = os.path.join(val_path, class_name)

    # Create class directories if they don't exist
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(val_class_dir, exist_ok=True)

    # List all files in the class folder
    files = [f for f in os.listdir(class_dir) if os.path.isfile(os.path.join(class_dir, f))]

    # Shuffle files to ensure randomness
    random.shuffle(files)

    # Compute number of files for validation
    val_size = int(len(files) * split_ratio)

    # Move files
    for i, file in enumerate(files):
        src_path = os.path.join(class_dir, file)
        if i < val_size:
            dst_path = os.path.join(val_class_dir, file)
        else:
            dst_path = os.path.join(train_class_dir, file)
        shutil.move(src_path, dst_path)

    print(f"Class {class_name}: {val_size} files moved to validation, {len(files) - val_size} files moved to dataset.")

print("✅ Splitting done successfully!")